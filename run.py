"""Alternative entry - team couldn't agree on main.py"""
from main import *  # noqa

if __name__ == "__main__":
    from src.ApplicationManager import ApplicationManager
    ApplicationManager().start()
