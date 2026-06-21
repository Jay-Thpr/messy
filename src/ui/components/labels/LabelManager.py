import tkinter as tk


class LabelManager:
    _labels = {}

    def __init__(self, parent):
        self.parent = parent

    def create(self, key, text):
        lbl = tk.Label(self.parent, text=text)
        lbl.pack(pady=2)
        LabelManager._labels[key] = lbl
        return lbl

    def update(self, key, text):
        if key in LabelManager._labels:
            LabelManager._labels[key].config(text=text)

    @classmethod
    def get_all(cls):
        return cls._labels
