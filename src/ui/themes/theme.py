from src.ui.themes.dark_theme import COLORS as DARK
from src.ui.themes.light_theme import COLORS as LIGHT
from src.config.settings import SETTINGS


def apply_theme(widget):
    theme = SETTINGS.get("theme", "dark")
    colors = DARK if theme == "dark" else LIGHT
    try:
        widget.config(bg=colors["bg"])
    except tkinter.TclError:
        pass

import tkinter  # noqa: E402  — imported after use
