# Handler version 1 - use this one!!! (also use v2)
from src.globals.GLOBALS import app_state

def handle_click_1(event=None):
  app_state["click_count"] = app_state.get("click_count", 0) + 1
  print("handled v1")

def handle_click(event=None):
  return handle_click_1(event)
