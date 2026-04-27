import os
import sys

# Persistent path for saved notes
_base = os.environ.get("APPDATA", os.path.expanduser("~")) if sys.platform == "win32" else os.path.expanduser("~/.local/share")
APP_FOLDER = os.path.join(_base, "NotasApp")
os.makedirs(APP_FOLDER, exist_ok=True)
NOTES_FILE = os.path.join(APP_FOLDER, "mis_notas.json")

# Purple palette
PURPLE_BG      = "#1a0a2e"
PURPLE_FRAME   = "#240b3a"
PURPLE_EDITOR  = "#1e0b33"
PURPLE_ACCENT  = "#7b2cbf"
PURPLE_HOVER   = "#5a189a"
PURPLE_BRIGHT  = "#9d4edd"
PURPLE_SELECT  = "#5a189a"
PURPLE_TEXT    = "#e0aaff"