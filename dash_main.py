from pathlib import Path
import pandas as pd
from taipy.gui import Gui
import taipy.gui.builder as tgb
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import smtplib
from email.message import EmailMessage

#Load Data
this_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
wb_file_path = this_dir / 'vital_log_2026-03-13_21-20-51.csv'
data = pd.read_csv(wb_file_path)

# Clean columns 
data = data[["Timestamp", "HeartRate_BPM", "BreathRate_BPM"]]

# Convert timestamp
data["Timestamp"] = pd.to_datetime(data["Timestamp"])

start_time = data["Timestamp"].min()
data = data[data["Timestamp"] >= start_time + pd.Timedelta(seconds=30)]

heart_rate_avg = round(data["HeartRate_BPM"].mean(), 2)
breath_rate_avg = round(data["BreathRate_BPM"].mean(), 2)

#Send graphs to email
def save_graphs():
    # Heart Rate Graph
    plt.figure()
    plt.plot(data["Timestamp"], data["HeartRate_BPM"])
    plt.title("Heart Rate Over Time")
    plt.xlabel("Time")
    plt.ylabel("BPM")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("heart_rate.png")
    plt.close()

    # Breath Rate Graph
    plt.figure()
    plt.plot(data["Timestamp"], data["BreathRate_BPM"])
    plt.title("Breath Rate Over Time")
    plt.xlabel("Time")
    plt.ylabel("BPM")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("breath_rate.png")
    plt.close()

#Email Function
def send_email(state):
    save_graphs()

    msg = EmailMessage()
    msg["Subject"] = "Vital Sign Report"
    msg["From"] = "VI.Waveinc@gmail.com"
    msg["To"] = "kjraw01@gmail.com"
    msg.set_content("Attached are your vital sign graphs.")

    for file in ["heart_rate.png", "breath_rate.png"]:
        with open(file, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="image",
                subtype="png",
                filename=file
            )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login("VI.Waveinc@gmail.com", "jcamaxdrfjijejwn")
        smtp.send_message(msg)


#create web page
with tgb.Page() as page:
    tgb.text("Vital Sign Dashboard", class_name="h1") #header

    with tgb.layout("1 1"): 
        with tgb.part():
            tgb.text("## Average Heart Rate: ", mode="md")
            tgb.text(f"{heart_rate_avg} BPM", class_name="h4")

        with tgb.part():
            tgb.text("## Average Breath Rate: ", mode="md")
            tgb.text(f"{breath_rate_avg} BPM", class_name="h4")

    with tgb.layout("1 1"):
        tgb.chart(
            "{data}",
            x="Timestamp",
            y="HeartRate_BPM",
            type="line",
            title="Heart Rate Over Time"
        )
        tgb.chart(
            "{data}",
            x="Timestamp",
            y="BreathRate_BPM",
            type="line",
            title="Breath Rate Over Time"
        )
    tgb.button("Send Report Email", on_action=send_email)

if __name__ == "__main__":
    Gui(page).run(
    title="Vital Sign Dashboard",
    css_file="styles.css",
    use_reloader=True,
    debug=True,
    
)
