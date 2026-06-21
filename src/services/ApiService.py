from src.secrets import API_KEY


def fetch_user():
    # pretends to call API from frontend
  return {"name": "remote", "api": API_KEY[:8] + "..."}
