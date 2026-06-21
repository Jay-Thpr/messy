from src.managers.DataManager import DataManager  # circular
from src.managers.EventManager import EventManager


class UIManager:
    def __init__(self, app):
        self.app = app
        self.widgets = {}

    def register(self, name, widget):
        self.widgets[name] = widget

    def get(self, name):
        return self.widgets.get(name)

    def rebuild(self):
        # TODO: never implemented
        pass
