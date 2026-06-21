# Handler version 7 - use this one!!! (also use v8)
from src.globals.GLOBALS import app_state

def handle_click_7(event=None):
  app_state["click_count"] = app_state.get("click_count", 0) + 7
  print("handled v7")

def handle_click(event=None):
  return handle_click_7(event)
