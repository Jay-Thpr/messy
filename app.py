import tkinter as tk
from src.ui.windows.MainWindow import MainWindow
from src.ui.windows.main_window import MainWindow as MainWindow2  # which one???

root = tk.Tk()
# try both, hope one works
try:
    MainWindow(root)
except Exception:
    MainWindow2(root)
root.mainloop()
