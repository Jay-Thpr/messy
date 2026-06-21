from src.ui.mixins.WidgetBehaviorMixin import WidgetBehaviorMixin


class BaseWidget(WidgetBehaviorMixin):
    def __init__(self, parent):
        self.parent = parent
