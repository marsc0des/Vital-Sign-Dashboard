import taipy.gui.builder as tgb
from taipy.gui import navigate
from components.navbar import navbar

with tgb.Page() as home:
    navbar()

    #Hero Section
    with tgb.part(class_name="hero-section"):
        with tgb.part(class_name="hero-content"):
            tgb.text("VI-Wave", class_name="hero-title")
            tgb.text("Non-Contact Vital Sign Monitoring", class_name="hero-subtitle")
            tgb.text(
                "Leveraging millimeter wave radar technology and the Doppler effect "
                "to wirelessly capture heart rate and respiratory rate",
                class_name="hero-description"
            )
            with tgb.part(class_name="hero-cta-row"):
                tgb.button("Get Started →", on_action=lambda s: navigate(s, to="dashboard"), class_name="btn-primary")
                tgb.button("Learn More",    on_action=lambda s: navigate(s, to="about_us"),  class_name="btn-secondary")

    #Features Strip 
    with tgb.part(class_name="features-section"):
        tgb.text("What VI-Wave Offers", class_name="section-title")
        with tgb.layout("1 1 1"):
            with tgb.part(class_name="feature-card"):
                tgb.text("Wireless Sensing", class_name="feature-heading")
                tgb.text(
                    "Millimeter wave radar captures vital signs without any physical contact, "
                    "making monitoring safe and effortless.",
                    class_name="feature-text"
                )
            with tgb.part(class_name="feature-card"):
                tgb.text("Real-Time Analytics", class_name="feature-heading")
                tgb.text(
                    "Visualize heart rate and breathing rate trends over time, "
                    "with instant health status classification and insights.",
                    class_name="feature-text"
                )
            with tgb.part(class_name="feature-card"):
                tgb.text("Personalized Insights", class_name="feature-heading")
                tgb.text(
                    "Age and gender-aware recommendations help you understand "
                    "what your data means and what to do next.",
                    class_name="feature-text"
                )

    #How It Works 
    with tgb.part(class_name="how-section"):
        tgb.text("How It Works", class_name="section-title")
        with tgb.layout("1 1 1 1"):
            with tgb.part(class_name="step-card"):
                tgb.text("01", class_name="step-number")
                tgb.text("Collect Data", class_name="step-title")
                tgb.text("Run a VI-Wave radar session to capture your vital signs.", class_name="step-text")
            with tgb.part(class_name="step-card"):
                tgb.text("02", class_name="step-number")
                tgb.text("Upload or Auto-Load", class_name="step-title")
                tgb.text("Upload your CSV log or let VI-Wave pick the latest session automatically.", class_name="step-text")
            with tgb.part(class_name="step-card"):
                tgb.text("03", class_name="step-number")
                tgb.text("Review Results", class_name="step-title")
                tgb.text("View interactive charts and personalized health status insights.", class_name="step-text")
            with tgb.part(class_name="step-card"):
                tgb.text("04", class_name="step-number")
                tgb.text("Share Report", class_name="step-title")
                tgb.text("Email your full report including charts and recommendations.", class_name="step-text")

    #CTA Banner
    with tgb.part(class_name="cta-banner"):
        tgb.text("Ready to explore your vital signs?", class_name="cta-title")
        tgb.button("Open Dashboard →", on_action=lambda s: navigate(s, to="dashboard"), class_name="btn-primary")

    #Disclaimer
    with tgb.part(class_name="disclaimer-bar"):
        tgb.text(
            "This tool is for informational purposes only and not medical advice. "
            "Consult a qualified healthcare professional for any health concerns.",
            class_name="disclaimer-text"
        )