import taipy.gui.builder as tgb
from components.navbar import navbar

with tgb.Page() as results:
    navbar()

    with tgb.part(class_name="page-header"):
        tgb.text("Health Insights Library", class_name="title")
        tgb.text(
            "Understand what your vital signs mean. "
            "Use this reference to help interpret the data shown on your Dashboard.",
            class_name="page-subheader"
        )

    #Heart Rate Zones 
    with tgb.part(class_name="card"):
        tgb.text("Heart Rate Zones", class_name="card-title")
        tgb.text(
            "Your heart rate (HR) reflects how hard your heart is working. "
            "At rest, a normal adult HR is 60–100 BPM. Here are the common zones:",
            class_name="card-body-text"
        )
        with tgb.layout("1 1 1"):
            with tgb.part(class_name="insight-zone-card zone-green"):
                tgb.text("🟢 Resting / Recovery", class_name="zone-title")
                tgb.text("< 60 BPM", class_name="zone-range")
                tgb.text("Common in well-trained athletes or during deep rest. Monitor for dizziness.", class_name="zone-desc")
            with tgb.part(class_name="insight-zone-card zone-teal"):
                tgb.text("🔵 Normal Resting", class_name="zone-title")
                tgb.text("60 – 100 BPM", class_name="zone-range")
                tgb.text("Healthy resting heart rate for most adults. Optimal cardiovascular function.", class_name="zone-desc")
            with tgb.part(class_name="insight-zone-card zone-yellow"):
                tgb.text("🟡 Elevated", class_name="zone-title")
                tgb.text("100 – 140 BPM", class_name="zone-range")
                tgb.text("May indicate moderate exertion, stress, caffeine, or mild illness.", class_name="zone-desc")
        with tgb.layout("1 1"):
            with tgb.part(class_name="insight-zone-card zone-orange"):
                tgb.text("🟠 High / Vigorous", class_name="zone-title")
                tgb.text("140 – 170 BPM", class_name="zone-range")
                tgb.text("Intense exercise zone. Not expected at rest — warrants attention if sedentary.", class_name="zone-desc")
            with tgb.part(class_name="insight-zone-card zone-red"):
                tgb.text("🔴 Maximum / Dangerous", class_name="zone-title")
                tgb.text("> 170 BPM", class_name="zone-range")
                tgb.text("Sustained levels at rest are a medical concern. Seek evaluation.", class_name="zone-desc")

    #Breathing Rate
    with tgb.part(class_name="card"):
        tgb.text("Breathing Rate (Respiratory Rate)", class_name="card-title")
        tgb.text(
            "Respiratory rate (RR) is the number of breaths taken per minute. "
            "Normal adult RR at rest is 12–20 breaths/min.",
            class_name="card-body-text"
        )
        with tgb.layout("1 1 1"):
            with tgb.part(class_name="insight-zone-card zone-yellow"):
                tgb.text("🟡 Low", class_name="zone-title")
                tgb.text("< 12 breaths/min", class_name="zone-range")
                tgb.text("Bradypnea. May occur during deep sleep or with certain medications.", class_name="zone-desc")
            with tgb.part(class_name="insight-zone-card zone-green"):
                tgb.text("🟢 Normal", class_name="zone-title")
                tgb.text("12 – 20 breaths/min", class_name="zone-range")
                tgb.text("Healthy resting respiratory rate for adults. Indicates relaxed breathing.", class_name="zone-desc")
            with tgb.part(class_name="insight-zone-card zone-red"):
                tgb.text("🔴 Elevated", class_name="zone-title")
                tgb.text("> 20 breaths/min", class_name="zone-range")
                tgb.text("Tachypnea. May indicate anxiety, fever, respiratory illness, or exertion.", class_name="zone-desc")

    #Combined Patterns 
    with tgb.part(class_name="card"):
        tgb.text("Combined Vital Sign Patterns", class_name="card-title")
        tgb.text(
            "Heart rate and breathing rate together can reveal more than each metric alone. "
            "Here are common combined patterns and what they may suggest:",
            class_name="card-body-text"
        )
        with tgb.layout("1 1"):
            with tgb.part(class_name="pattern-card pattern-stress"):
                tgb.text("High HR + High BR", class_name="pattern-title")
                tgb.text("Stress / Exertion", class_name="pattern-label")
                tgb.text(
                    "This combination typically signals physical exertion, acute stress, anxiety, or fever. "
                    "Rest, hydrate, and breathe slowly. Recheck after 10 minutes.",
                    class_name="pattern-desc"
                )
            with tgb.part(class_name="pattern-card pattern-fit"):
                tgb.text("Low HR + Normal BR", class_name="pattern-title")
                tgb.text("Cardiovascular Fitness", class_name="pattern-label")
                tgb.text(
                    "Often seen in athletes or highly active individuals. "
                    "The heart pumps efficiently, requiring fewer beats per minute.",
                    class_name="pattern-desc"
                )
            with tgb.part(class_name="pattern-card pattern-anomaly"):
                tgb.text("High HR + Low BR", class_name="pattern-title")
                tgb.text("Unusual — Monitor", class_name="pattern-label")
                tgb.text(
                    "This atypical pattern may indicate a data anomaly, or rarely a physiological irregularity. "
                    "Consult a healthcare provider if this persists.",
                    class_name="pattern-desc"
                )
            with tgb.part(class_name="pattern-card pattern-normal"):
                tgb.text("Normal HR + Normal BR", class_name="pattern-title")
                tgb.text("Healthy Resting State", class_name="pattern-label")
                tgb.text(
                    "Both metrics within normal range indicates a healthy resting state. "
                    "Continue maintaining good habits.",
                    class_name="pattern-desc"
                )

    #Age Group Reference
    with tgb.part(class_name="card"):
        tgb.text("Normal Ranges by Age Group", class_name="card-title")
        tgb.text(
            "Normal vital sign ranges vary by age. The VI-Wave Dashboard uses these "
            "reference values when classifying your results:",
            class_name="card-body-text"
        )
        with tgb.layout("1 1 1 1"):
            with tgb.part(class_name="age-card"):
                tgb.text("Ages 0–17", class_name="age-title")
                tgb.text("HR: 70 – 100 BPM", class_name="age-stat")
                tgb.text("RR: 20 – 30 breaths/min", class_name="age-stat")
            with tgb.part(class_name="age-card"):
                tgb.text("Ages 18–39", class_name="age-title")
                tgb.text("HR: 60 – 100 BPM", class_name="age-stat")
                tgb.text("RR: 12 – 20 breaths/min", class_name="age-stat")
            with tgb.part(class_name="age-card"):
                tgb.text("Ages 40–59", class_name="age-title")
                tgb.text("HR: 60 – 100 BPM", class_name="age-stat")
                tgb.text("RR: 12 – 20 breaths/min", class_name="age-stat")
            with tgb.part(class_name="age-card"):
                tgb.text("Ages 60+", class_name="age-title")
                tgb.text("HR: 60 – 100 BPM", class_name="age-stat")
                tgb.text("RR: 12 – 20 breaths/min", class_name="age-stat")

    # ── Disclaimer ────────────────────────────────────────────────────────────
    with tgb.part(class_name="disclaimer-bar"):
        tgb.text(
            "This tool is for informational purposes only and not medical advice. "
            "Always consult a qualified healthcare professional for diagnosis or treatment.",
            class_name="disclaimer-text"
        )