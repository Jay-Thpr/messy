# Handler version 6 - use this one!!! (also use v7)
from src.globals.GLOBALS import app_state

def handle_click_6(event=None):
  app_state["click_count"] = app_state.get("click_count", 0) + 6
  print("handled v6")

def handle_click(event=None):
  return handle_click_6(event)
