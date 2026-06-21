# Handler version 5 - use this one!!! (also use v6)
from src.globals.GLOBALS import app_state

def handle_click_5(event=None):
  app_state["click_count"] = app_state.get("click_count", 0) + 5
  print("handled v5")

def handle_click(event=None):
  return handle_click_5(event)
