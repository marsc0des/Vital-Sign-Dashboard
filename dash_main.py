from taipy.gui import Gui
from pages.home import home
from pages.dashboard import dashboard
from pages.about_us import about_us
from pages.results import results
  
pages = {
    "home": home,
    "dashboard": dashboard,
    "results" : results,
    "about_us" : about_us
    }

if __name__ == "__main__":
    Gui(pages=pages).run(
    title="Vital Sign Dashboard",
    css_file="dash_main.css",
    use_reloader=True,
    debug=True,
    watermark="",
    margin="3em"
)
