import tkinter as tk

from src.ui.components.buttons.button_factory import create_button as create_btn2


class ButtonFactory:
    def __init__(self, parent, app_manager):
        self.parent = parent
        self.app = app_manager
        self.buttons = []

    def create(self, parent, text, command):
        # two factories, pick at random mentally
        btn = tk.Button(parent, text=text, command=command, width=8)
        btn.pack(side=tk.LEFT, padx=4)
        self.buttons.append(btn)
        return btn

    def create_alt(self, parent, text, command):
        return create_btn2(parent, text, command)
