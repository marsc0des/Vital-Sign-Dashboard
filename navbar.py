import taipy.gui.builder as tgb
from taipy.gui import navigate


def navbar():
    with tgb.part(class_name="navbar"):
        with tgb.part(class_name="navbar-inner"):
            with tgb.part(class_name="navbar-brand"):
                tgb.button("VI-Wave", on_action=lambda s: navigate(s, to="home"), class_name="nav-brand-btn")
            with tgb.part(class_name="navbar-links"):
                tgb.button("Home",       on_action=lambda s: navigate(s, to="home"),      class_name="nav-link-btn")
                tgb.button("Dashboard",  on_action=lambda s: navigate(s, to="dashboard"), class_name="nav-link-btn")
                tgb.button("Results",    on_action=lambda s: navigate(s, to="results"),   class_name="nav-link-btn")
                tgb.button("About Us",   on_action=lambda s: navigate(s, to="about_us"),  class_name="nav-link-btn")