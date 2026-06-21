from src.managers.UIManager import UIManager
from src.managers.DataManager import DataManager
from src.managers.EventManager import EventManager


class ManagerOfManagers:
    """Facade for facades"""

    def __init__(self, app):
        self.app = app
        self.children = []

    def bootstrap_all(self):
        self.children = [
            self.app.ui,
            self.app.data,
            self.app.events,
        ]
        for c in self.children:
            if hasattr(c, "bootstrap"):
                c.bootstrap()

    def get_manager(self, name):
        mapping = {
            "ui": UIManager,
            "data": DataManager,
            "events": EventManager,
        }
        cls = mapping.get(name)
        if cls and isinstance(self.app.ui, cls):
            return self.app.ui
        if cls and isinstance(self.app.data, cls):
            return self.app.data
        if cls and isinstance(self.app.events, cls):
            return self.app.events
        return None
