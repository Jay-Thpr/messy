import tkinter as tk


def create_button(parent, text, command):
    b = tk.Button(parent, text=text, command=command)
    b.pack(side=tk.LEFT, padx=2)
    return b

class ButtonFactory:  # same class name, different module
    pass
