import requests
from app.config import Config

def send_to_telex(data):
    """
    sends fetched song to telex channel webhook
    """
    payload = {
        "message": str(data), 
        "event_name": "Trending songs",
        "status": "success",
        "username": "Ultra - Music bot "
    }
    
    response = requests.post(
        Config.TELEX_CHANNEL_WEBHOOK,
        json=payload,
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
    )
    print(response.json())
    return response.status_code