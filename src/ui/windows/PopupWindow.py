import tkinter as tk
from tkinter import simpledialog


class PopupWindow:
  def __init__(self, parent, title="Popup"):
    self.top = tk.Toplevel(parent)
    self.top.title(title)
    tk.Label(self.top, text="This popup should not exist").pack(padx=20, pady=20)
    tk.Button(self.top, text="OK", command=self.top.destroy).pack()

  @staticmethod
  def ask(parent, prompt):
    return simpledialog.askstring("MessyApp", prompt, parent=parent)
