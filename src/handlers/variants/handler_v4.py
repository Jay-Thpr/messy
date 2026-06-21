# Handler version 4 - use this one!!! (also use v5)
from src.globals.GLOBALS import app_state

def handle_click_4(event=None):
  app_state["click_count"] = app_state.get("click_count", 0) + 4
  print("handled v4")

def handle_click(event=None):
  return handle_click_4(event)
