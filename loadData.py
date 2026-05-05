from pathlib import Path
import pandas as pd


def get_latest_log_file():
    """Return the most recent CSV file from the logs folder."""
    logs_dir = Path(__file__).parent.parent / "logs" #update to computer path
    if not logs_dir.exists():
        raise FileNotFoundError(f"Logs folder not found at: {logs_dir}")
    csv_files = sorted(logs_dir.glob("vital_log_*.csv"))
    if not csv_files:
        raise FileNotFoundError("No vital log files found in logs folder.")
    return csv_files[-1]


def process_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and process a raw vital signs DataFrame."""
    df = df[["Timestamp", "HeartRate_BPM", "BreathRate_BPM"]].copy()
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    start_time = df["Timestamp"].min()
    df = df[df["Timestamp"] >= start_time + pd.Timedelta(seconds=30)]
    return df.reset_index(drop=True)


def load_data() -> pd.DataFrame:
    """Load the latest log file from the logs folder."""
    file_path = get_latest_log_file()
    df = pd.read_csv(file_path)
    return process_data(df)


def load_file(state):
    """Taipy callback: load data from the user-uploaded file, fallback to latest log."""
    if state.content:
        try:
            df = pd.read_csv(state.content)
            state.data = process_data(df)
            state.data_source_label = f"Uploaded file"
            return
        except Exception as e:
            print(f"Error reading uploaded file: {e}")

    # Fallback to latest log
    try:
        df_fallback = load_data()
        state.data = df_fallback
        state.data_source_label = f"Latest log: {get_latest_log_file().name}"
    except FileNotFoundError as e:
        print(f"Fallback failed: {e}")
        state.data_source_label = "No data available"