import os
import sys
from datetime import datetime
from pathlib import Path

THIS_DIR = Path(__file__).parent.absolute()

sys.path.insert(0, os.path.abspath(".."))
sys.path.insert(0, str(THIS_DIR.parent))

extensions = [
    "myst_parser",
]
templates_path = ["_templates"]
source_suffix = ".rst"
master_doc = "index"
html_extra_path = ["_extra"]

project = "First Django Admin"
year = datetime.now().year
copyright = f"{year} Ben Welsh"

exclude_patterns = ["_build"]

html_theme = "alabaster"
html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
        "relations.html",
        "searchbox.html",
        "donate.html",
    ]
}
html_theme_options = {
    "canonical_url": f"https://palewi.re/docs/first-django-admin/",
    "show_powered_by": False,
    "show_relbar_bottom": True,
}

html_static_path = ["_static"]
html_css_files = [
    "css/custom.css",
]
html_js_files = []

pygments_style = "sphinx"