# Handler version 2 - use this one!!! (also use v3)
from src.globals.GLOBALS import app_state

def handle_click_2(event=None):
  app_state["click_count"] = app_state.get("click_count", 0) + 2
  print("handled v2")

def handle_click(event=None):
  return handle_click_2(event)
