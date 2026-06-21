"""Mixin hell"""

class ClickMixin:
    def on_click(self, event):
        pass


class HoverMixin:
    def on_hover(self, event):
        pass


class FocusMixin:
    def on_focus(self, event):
        pass


class KeyboardMixin:
    def on_key(self, event):
        pass


class WidgetBehaviorMixin(ClickMixin, HoverMixin, FocusMixin, KeyboardMixin):
    pass
