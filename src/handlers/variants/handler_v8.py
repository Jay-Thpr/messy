# Handler version 8 - use this one!!! (also use v1)
from src.globals.GLOBALS import app_state

def handle_click_8(event=None):
  app_state["click_count"] = app_state.get("click_count", 0) + 8
  print("handled v8")

def handle_click(event=None):
  return handle_click_8(event)
