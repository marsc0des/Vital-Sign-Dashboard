import taipy.gui.builder as tgb
from components.navbar import navbar
from data.loadData import load_data, load_file, get_latest_log_file
from data.sendEmail import send_email

#Default state values
data = load_data()
content = None
data_source_label = f"Latest log: {get_latest_log_file().name}"

heart_rate_avg = round(data["HeartRate_BPM"].mean(), 2)
breath_rate_avg = round(data["BreathRate_BPM"].mean(), 2)
heart_rate_max = round(data["HeartRate_BPM"].max(), 2)
heart_rate_min = round(data["HeartRate_BPM"].min(), 2)
breath_rate_max = round(data["BreathRate_BPM"].max(), 2)
breath_rate_min = round(data["BreathRate_BPM"].min(), 2)

age_group = "18–39"
gender = "Male"
age_group_options = ["0–17", "18–39", "40–59", "60+"]
gender_options = ["Male", "Female", "Other / Prefer not to say"]

status_text = ""
insights = []
recommendations = []
email_status = ""
recipient_email = ""

#Health classification logic
def normal_hr_range(age_group: str) -> tuple[int, int]:
    return {"0–17": (70, 100), "18–39": (60, 100), "40–59": (60, 100), "60+": (60, 100)}.get(age_group, (60, 100))

def normal_br_range(age_group: str) -> tuple[int, int]:
    return {"0–17": (20, 30), "18–39": (12, 20), "40–59": (12, 20), "60+": (12, 20)}.get(age_group, (12, 20))

def classify_health(hr: float, br: float, age_group: str, gender: str):
    hr_low, hr_high = normal_hr_range(age_group)
    br_low, br_high = normal_br_range(age_group)

    hr_status = "normal" if hr_low <= hr <= hr_high else ("low" if hr < hr_low else "high")
    br_status = "normal" if br_low <= br <= br_high else ("low" if br < br_low else "high")

    insights_list = []
    recs_list = []
    anomaly = False

    #Insights
    if hr_status == "high":
        insights_list.append(f"Heart rate ({hr} BPM) is above the normal resting range ({hr_low}–{hr_high} BPM) for your age group.")
    elif hr_status == "low":
        insights_list.append(f"Heart rate ({hr} BPM) is below the normal resting range ({hr_low}–{hr_high} BPM) for your age group.")
    else:
        insights_list.append(f"Heart rate ({hr} BPM) is within the normal resting range for your age group.")

    if br_status == "high":
        insights_list.append(f"Breathing rate ({br} BPM) is elevated above the normal range ({br_low}–{br_high} breaths/min).")
    elif br_status == "low":
        insights_list.append(f"Breathing rate ({br} BPM) is below the normal range ({br_low}–{br_high} breaths/min).")
    else:
        insights_list.append(f"Breathing rate ({br} BPM) is within the normal range.")

    #Inferred state
    if hr_status == "high" and br_status == "high":
        insights_list.append("🔴 High HR + High BR may indicate stress, physical exertion, or anxiety.")
        recs_list += ["Sit down and rest in a quiet space.", "Practice slow, deep breathing for 2–3 minutes.", "Drink water and avoid stimulants.", "Recheck vitals in 10 minutes."]
        status = "🔴 Elevated — Possible Stress or Exertion"

    elif hr_status == "low" and br_status == "normal":
        insights_list.append("🟢 Low HR + Normal BR is often a sign of good cardiovascular fitness.")
        recs_list += ["Continue your current wellness routine.", "Ensure adequate hydration.", "Monitor if you feel lightheaded or fatigued."]
        status = "🟢 Excellent — Strong Cardiovascular Fitness"

    elif hr_status == "high" and br_status == "low":
        insights_list.append("⚠️ High HR + Low BR is an unusual combination. This may be worth monitoring closely.")
        recs_list += ["Avoid physical activity for now.", "Monitor for symptoms like dizziness or chest tightness.", "Consult a healthcare provider if this persists."]
        status = "⚠️ Unusual Pattern — Monitor Closely"
        anomaly = True

    elif hr_status == "normal" and br_status == "normal":
        insights_list.append("🟢 Both heart rate and breathing rate are within normal limits.")
        recs_list += ["Maintain your current activity levels.", "Stay hydrated and keep up healthy habits."]
        status = "🟢 Normal — All Vitals Within Range"

    elif hr_status == "high":
        insights_list.append("🟡 Moderately elevated heart rate. Could reflect recent activity or mild stress.")
        recs_list += ["Rest for 5–10 minutes.", "Drink water.", "Avoid caffeine or stimulants.", "Recheck in 5 minutes."]
        status = "🟡 Elevated — Heart Rate Above Normal"

    elif hr_status == "low":
        insights_list.append("🟡 Heart rate is lower than typical. Could be normal for athletes.")
        recs_list += ["Monitor for dizziness or fatigue.", "Ensure you are not dehydrated.", "Seek medical advice if symptoms appear."]
        status = "🟡 Low Heart Rate — Monitor"

    elif br_status == "high":
        insights_list.append("🟡 Breathing rate is elevated. Could indicate exertion or respiratory discomfort.")
        recs_list += ["Sit upright and breathe slowly.", "Avoid strenuous activity.", "Seek care if shortness of breath persists."]
        status = "🟡 Elevated Breathing Rate"

    elif br_status == "low":
        insights_list.append("🟡 Breathing rate is slower than typical. Could be normal during deep rest.")
        recs_list += ["Ensure you are fully awake and alert.", "Seek medical evaluation if you feel short of breath."]
        status = "🟡 Low Breathing Rate — Monitor"

    else:
        status = "⚪ Status Undetermined"
        recs_list.append("Please verify your data and try again.")

    #Heart rate zone
    if hr < 60:
        insights_list.append("HR Zone: Rest/Recovery — Very low intensity.")
    elif hr <= 100:
        insights_list.append("HR Zone: Resting/Light — Normal at rest.")
    elif hr <= 140:
        insights_list.append("HR Zone: Aerobic — Moderate activity level.")
    else:
        insights_list.append("HR Zone: Vigorous/Maximum — High exertion.")

    if anomaly:
        insights_list.append("Anomaly flagged: This combination of vitals is atypical and warrants attention.")

    return status, insights_list, recs_list


# Run initial classification
status_text, insights, recommendations = classify_health(heart_rate_avg, breath_rate_avg, age_group, gender)


#Taipy callbacks
def on_file_upload(state):
    load_file(state)
    _refresh_stats(state)

def on_profile_change(state, var_name, value):
    _refresh_stats(state)

def _refresh_stats(state):
    state.heart_rate_avg  = round(state.data["HeartRate_BPM"].mean(), 2)
    state.breath_rate_avg = round(state.data["BreathRate_BPM"].mean(), 2)
    state.heart_rate_max  = round(state.data["HeartRate_BPM"].max(), 2)
    state.heart_rate_min  = round(state.data["HeartRate_BPM"].min(), 2)
    state.breath_rate_max = round(state.data["BreathRate_BPM"].max(), 2)
    state.breath_rate_min = round(state.data["BreathRate_BPM"].min(), 2)
    state.status_text, state.insights, state.recommendations = classify_health(
        state.heart_rate_avg, state.breath_rate_avg, state.age_group, state.gender
    )


#Page layout
with tgb.Page() as dashboard:
    navbar()

    with tgb.part(class_name="page-header"):
        tgb.text("Vital Sign Dashboard", class_name="title")

    #Data Source
    with tgb.part(class_name="card"):
        tgb.text("Data Source", class_name="card-title")
        tgb.text("Upload a CSV file, or the latest log will be used automatically.", class_name="card-subtitle")
        tgb.file_selector(
            "{content}",
            label="Upload CSV / XLSX",
            on_action=on_file_upload,
            extensions=".csv,.xlsx",
            drop_message="Drop your vital signs file here"
        )
        tgb.text("Source: {data_source_label}", class_name="source-label")

    #Stats Row
    with tgb.part(class_name="stats-row"):
        with tgb.layout("1 1 1 1 1 1"):
            with tgb.part(class_name="stat-card"):
                tgb.text("Avg Heart Rate", class_name="stat-label")
                tgb.text("{heart_rate_avg} BPM", class_name="stat-value")
            with tgb.part(class_name="stat-card"):
                tgb.text("Max Heart Rate", class_name="stat-label")
                tgb.text("{heart_rate_max} BPM", class_name="stat-value")
            with tgb.part(class_name="stat-card"):
                tgb.text("Min Heart Rate", class_name="stat-label")
                tgb.text("{heart_rate_min} BPM", class_name="stat-value")
            with tgb.part(class_name="stat-card"):
                tgb.text("Avg Breath Rate", class_name="stat-label")
                tgb.text("{breath_rate_avg} BPM", class_name="stat-value")
            with tgb.part(class_name="stat-card"):
                tgb.text("Max Breath Rate", class_name="stat-label")
                tgb.text("{breath_rate_max} BPM", class_name="stat-value")
            with tgb.part(class_name="stat-card"):
                tgb.text("Min Breath Rate", class_name="stat-label")
                tgb.text("{breath_rate_min} BPM", class_name="stat-value")

    #Charts
    with tgb.part(class_name="card"):
        tgb.text("Vital Sign Trends", class_name="card-title")
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

    #Profile Selector
    with tgb.part(class_name="card"):
        tgb.text("Your Profile", class_name="card-title")
        tgb.text("Select your age group and gender to personalise health insights.", class_name="card-subtitle")
        with tgb.layout("1 1"):
            with tgb.part(class_name="selector-group"):
                tgb.text("Age Group", class_name="selector-label")
                tgb.selector(
                    "{age_group}",
                    lov="{age_group_options}",
                    on_change=on_profile_change,
                    dropdown=True
                )
            with tgb.part(class_name="selector-group"):
                tgb.text("Gender", class_name="selector-label")
                tgb.selector(
                    "{gender}",
                    lov="{gender_options}",
                    on_change=on_profile_change,
                    dropdown=True
                )

    #Health Status Panel
    with tgb.part(class_name="card status-panel"):
        tgb.text("Health Status & Insights", class_name="card-title")
        tgb.text("{status_text}", class_name="status-badge")
        tgb.text("Insights:", class_name="insights-heading")
        tgb.text("{'• ' + '\\n• '.join(insights)}", class_name="insights-list")
        tgb.text("Recommendations:", class_name="insights-heading")
        tgb.text("{'• ' + '\\n• '.join(recommendations)}", class_name="insights-list")
        with tgb.part(class_name="disclaimer-bar"):
            tgb.text(
                "This tool is for informational purposes only and not medical advice. "
                "Consult a qualified healthcare professional for any health concerns.",
                class_name="disclaimer-text"
            )

    #Email Report
    with tgb.part(class_name="card"):
        tgb.text("Email Report", class_name="card-title")
        tgb.text("Enter your email address to receive a full report with charts and recommendations.", class_name="card-subtitle")
        tgb.input("{recipient_email}", label="Recipient Email Address", class_name="email-input")
        tgb.button("Send Report", on_action=send_email, class_name="btn-primary")
        tgb.text("{email_status}", class_name="email-status")