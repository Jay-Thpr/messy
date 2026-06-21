from src.ui.windows.MainWindow import MainWindow as View
from src.logic.business.UserLogic import UserLogic as Model
from src.controllers.ApplicationControllerManagerFacadeSingleton import (
    ApplicationControllerManagerFacadeSingleton as Controller,
)


class MVCThing:
    def __init__(self):
        self.model = Model()
        self.controller = Controller()
        self.view = None

    def attach(self, root):
        self.view = View(root, self.controller)
