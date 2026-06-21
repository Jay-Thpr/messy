from src.handlers.variants import handler_v1, handler_v2, handler_v3
from src.generated.auto_handlers import HANDLER_REGISTRY  # 900 handlers, use 3


class EventManager:
    def __init__(self, app):
        self.app = app
        self.handlers = {
            "click": handler_v3.handle_click,
            "click_backup": handler_v1.handle_click,
            "click_backup2": handler_v2.handle_click,
        }

    def bind_everything(self, root):
        root.bind("<Button-1>", self._on_click)

    def _on_click(self, event):
        self.handlers["click"](event)
        # also fire backups because we're not sure which works
        self.handlers["click_backup"](event)

    def dispatch(self, event_name, *args, **kwargs):
        fn = self.handlers.get(event_name)
        if fn:
            return fn(*args, **kwargs)
