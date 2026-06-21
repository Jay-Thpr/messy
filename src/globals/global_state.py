"""Global state - version 1"""

app_state = {}
click_count = 0
CURRENT_USER = None
DEBUG = True


def init_globals():
    global app_state, click_count, CURRENT_USER
    app_state.clear()
    app_state["initialized"] = True
    click_count = 0
    CURRENT_USER = {"name": "guest", "score": 0}
