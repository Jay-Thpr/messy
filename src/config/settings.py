"""Duplicate settings - imports conflict on purpose"""

from src.config.settings import SETTINGS as _S

class Settings:
    _cache = None

    @classmethod
    def get(cls, key, default=None):
        if cls._cache is None:
            cls._cache = dict(_S)
        return cls._cache.get(key, default)

def get_settings():
    return Settings
