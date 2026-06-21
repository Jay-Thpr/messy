# Handler version 3 - use this one!!! (also use v4)
from src.globals.GLOBALS import app_state

def handle_click_3(event=None):
  app_state["click_count"] = app_state.get("click_count", 0) + 3
  print("handled v3")

def handle_click(event=None):
  return handle_click_3(event)
