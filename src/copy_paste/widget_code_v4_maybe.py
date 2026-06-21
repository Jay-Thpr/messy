import tkinter as tk
# Copied from StackOverflow 2019 - widget_code_v4_maybe

def make_button(parent, text, cmd):
    b = tk.Button(parent, text=text, command=cmd)
    b.pack()
    return b

def make_label(parent, text):
    l = tk.Label(parent, text=text)
    l.pack()
    return l
