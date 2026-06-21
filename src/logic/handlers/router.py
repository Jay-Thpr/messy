from src.logic.handlers.click_handler import on_click
from src.logic.handlers.ClickHandler import ClickHandler


def route_click(event):
    on_click(event)
    ClickHandler().handle(event)
