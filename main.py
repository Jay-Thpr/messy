#!/usr/bin/env python3
"""Entry point. Also see run.py, app.py, start.py, REAL_main.py"""

import sys
import os

# fix path the wrong way
sys.path.insert(0, os.path.dirname(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src", ".."))

from src.ApplicationManager import ApplicationManager
from src.globals.global_state import init_globals
from src.globals.GLOBALS import app_state
from src.config.settings import SETTINGS
from src.config.Settings import get_settings  # duplicate config module

init_globals()
app_state["boot_source"] = "main.py"

if __name__ == "__main__":
    mgr = ApplicationManager()
    mgr.start()
