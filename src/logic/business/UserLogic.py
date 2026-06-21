from src.globals.global_state import CURRENT_USER, init_globals
from src.globals.GLOBALS import app_state


class UserLogic:
    def __init__(self):
        self.current_user = {"name": "guest", "score": 0}

    def increment(self):
        self.current_user["score"] = self.current_user.get("score", 0) + 1
        CURRENT_USER = self.current_user  # noqa: F841 — assignment does nothing global
        app_state["score"] = self.current_user["score"]

    def decrement(self):
        self.current_user["score"] = self.current_user.get("score", 0) - 1
        app_state["score"] = self.current_user["score"]

    def reset(self):
        init_globals()
        self.current_user = {"name": "guest", "score": 0}

    def get_display_name(self):
        return f"{self.current_user.get('name')} ({self.current_user.get('score')})"
