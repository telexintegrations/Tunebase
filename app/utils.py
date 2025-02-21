import requests
from app.config import Config

def send_to_telex(data):
    """
    sends fetched song to telex channel webhook
    """
    url = Config.TELEX_CHANNEL_WEBHOOK
    response = requests.post(url, json=data)
    return response.status_code