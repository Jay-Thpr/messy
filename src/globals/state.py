"""Yet another state module"""

state = {}

def get_state():
    from src.globals.GLOBALS import app_state
    return app_state

def set_state(k, v):
    from src.globals.global_state import app_state
    app_state[k] = v
