from src.globals.GLOBALS import app_state


def on_click(event=None):
    app_state["click_count"] = app_state.get("click_count", 0) + 1
