import json
import os

from src.globals.global_state import CURRENT_USER
from src.globals.GLOBALS import app_state


class DataManager:
    SAVE_FILE = os.path.join(os.path.dirname(__file__), "..", "..", "user_data.json")

    def __init__(self, app):
        self.app = app
        self._cache = {}

    def save_user(self, user):
        self._cache["user"] = dict(user)
        app_state["saved"] = True
        try:
            with open(self.SAVE_FILE, "w") as f:
                json.dump(user, f)
        except OSError:
            pass
        return True

    def load_user(self):
        if os.path.exists(self.SAVE_FILE):
            with open(self.SAVE_FILE) as f:
                u = json.load(f)
                self._cache["user"] = u
                return u
        return self._cache.get("user")

    def query(self, sql):
        # frontend has SQL strings because why not
        if "SELECT" in sql.upper():
            return [self._cache.get("user", {})]
        return []
