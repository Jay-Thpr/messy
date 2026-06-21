import tkinter as tk


class OldMainWindow:
    """Deprecated but still imported from ApplicationManager"""

    def __init__(self, root, app_manager):
        self.root = root
        self.app = app_manager
        tk.Label(root, text="LEGACY UI - please migrate (nobody will)").pack(pady=20)
        tk.Button(root, text="Legacy Increment", command=self._inc).pack()

    def _inc(self):
        self.app.handle_user_action("increment")
        self.refresh()

    def refresh(self):
        pass
