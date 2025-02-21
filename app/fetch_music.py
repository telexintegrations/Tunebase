import requests
from app.config import Config

def get_trending_music():
    """
    Fetch trending music from Last.fm API
    """
    url = "http://ws.audioscrobbler.com/2.0/"
    
    params = {
        "method": "chart.gettoptracks",  # Get top trending tracks
        "api_key": Config.LASTFM_API_KEY,  # API Key from .env
        "format": "json"  # Response format
    }
    
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()  # Last.fm API response

    print(f"Error fetching music: {response.text}")
    return None  # In case of request failure
