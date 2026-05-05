import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import smtplib
import tempfile
import os
from email.message import EmailMessage


SENDER_EMAIL = "VI.Waveinc@gmail.com"
SENDER_PASSWORD = "jcamaxdrfjijejwn"


def save_graphs(data) -> list[str]:
    """Generate chart PNGs into temp files and return their paths."""
    paths = []

    # Heart Rate Graph
    hr_path = os.path.join(tempfile.gettempdir(), "heart_rate.png")
    plt.figure(figsize=(8, 4))
    plt.plot(data["Timestamp"], data["HeartRate_BPM"], color="#00b4a6", linewidth=2)
    plt.title("Heart Rate Over Time", fontsize=14)
    plt.xlabel("Time")
    plt.ylabel("BPM")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(hr_path)
    plt.close()
    paths.append(hr_path)

    # Breath Rate Graph
    br_path = os.path.join(tempfile.gettempdir(), "breath_rate.png")
    plt.figure(figsize=(8, 4))
    plt.plot(data["Timestamp"], data["BreathRate_BPM"], color="#6a0dad", linewidth=2)
    plt.title("Breath Rate Over Time", fontsize=14)
    plt.xlabel("Time")
    plt.ylabel("BPM")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(br_path)
    plt.close()
    paths.append(br_path)

    return paths


def build_email_body(heart_rate_avg, breath_rate_avg, age_group, gender,
                     status, insights, recommendations, data_source_label) -> str:
    """Compose the plain-text email body."""
    lines = [
        "VI-Wave Vital Sign Report",
        f"Data source: {data_source_label}",
        f"Age group: {age_group}",
        f"Gender: {gender}",
        "",
        "Averages",
        f"Heart Rate: {heart_rate_avg} BPM",
        f"Breath Rate: {breath_rate_avg} BPM",
        "",
        "Health Status",
        f"Status: {status}",
        "",
        "Insights:",
    ]
    for insight in insights:
        lines.append(f"  • {insight}")
    lines += ["", "Recommendations:"]
    for rec in recommendations:
        lines.append(f"  • {rec}")
    lines += [
        "",
        "DISCLAIMER: This tool is for informational purposes only and not medical advice.",
        "Please consult a qualified healthcare professional for any health concerns.",
    ]
    return "\n".join(lines)


def send_email(state):
    """
    Taipy callback: send the vital sign report to state.recipient_email.
    Expects state to have:
        data, recipient_email, heart_rate_avg, breath_rate_avg,
        age_group, gender, status_text, insights, recommendations,
        data_source_label
    """
    recipient = getattr(state, "recipient_email", "").strip()
    if not recipient:
        state.email_status = "Please enter a recipient email address."
        return

    try:
        graph_paths = save_graphs(state.data)

        body = build_email_body(
            heart_rate_avg=state.heart_rate_avg,
            breath_rate_avg=state.breath_rate_avg,
            age_group=state.age_group,
            gender=state.gender,
            status=state.status_text,
            insights=state.insights,
            recommendations=state.recommendations,
            data_source_label=state.data_source_label,
        )

        msg = EmailMessage()
        msg["Subject"] = "VI-Wave Vital Sign Report"
        msg["From"] = SENDER_EMAIL
        msg["To"] = recipient
        msg.set_content(body)

        for file_path in graph_paths:
            with open(file_path, "rb") as f:
                msg.add_attachment(
                    f.read(),
                    maintype="image",
                    subtype="png",
                    filename=os.path.basename(file_path),
                )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
            smtp.send_message(msg)

        state.email_status = f"✅ Report sent to {recipient}"

    except Exception as e:
        state.email_status = f"❌ Failed to send email: {str(e)}"