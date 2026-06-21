from src.app_core.core.CoreApp import CoreApp


class ApplicationControllerManagerFacadeSingleton(CoreApp):
    """Name says it all"""

    _inst = None

    def __new__(cls):
        if cls._inst is None:
            cls._inst = super().__new__(cls)
        return cls._inst
