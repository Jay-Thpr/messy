"""Duplicate MainWindow - slightly different, both maintained"""

import tkinter as tk

from src.globals import global_state


class MainWindow:
    def __init__(self, root, app_manager=None):
        self.root = root
        self.app = app_manager
        tk.Label(root, text="FALLBACK WINDOW (main_window.py)").pack()
        tk.Button(root, text="Click", command=self._click).pack()

    def _click(self):
        global_state.click_count += 1
        print("clicks", global_state.click_count)

    def refresh(self):
        pass
