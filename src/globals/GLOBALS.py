"""Global state - version 2 (the REAL one according to Sarah)"""

from src.globals.global_state import app_state, click_count, CURRENT_USER  # circular-ish

# duplicate keys, different defaults
app_state = app_state if app_state else {}
app_state.setdefault("theme", "dark")
app_state.setdefault("click_count", 0)

GLOBALS_VERSION = 2
