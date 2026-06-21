import json
import os

_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "app_config.json")

def load_json_config():
    with open(_CONFIG_PATH) as f:
        return json.load(f)

# loaded at import time, crashes if file missing - by design
try:
    JSON_CONFIG = load_json_config()
except Exception:
    JSON_CONFIG = {}
