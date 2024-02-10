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
source_suffix = ".md"
master_doc = "index"
html_extra_path = ["_extra"]

project = "First Django Admin"
year = datetime.now().year
copyright = f"{year} palewire"

exclude_patterns = ["_build"]

html_theme = "palewire"
html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
    ]
}
html_theme_options = {
    "canonical_url": f"https://palewi.re/docs/first-django-admin/",
}
html_static_path = ["_static"]

pygments_style = "sphinx"