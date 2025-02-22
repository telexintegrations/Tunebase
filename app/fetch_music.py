import requests
from app.config import Config

# country mapping for Last.fm API
COUNTRY_MAPPING = {
    "United States": "United States",
    "Kenya": "Kenya",
    "Nigeria": "Nigeria",
    "Uganda": "Uganda",
    "Africa": "South Africa",
    "United Kingdom": "United Kingdom",
    "Global": None
}

def get_trending_music(limit=10, country="Global", preferred_genres=["afrobeats", "jazz", "pop"]):
    """
    Fetch trending music from Last.fm API and return formatted data.
    """
    url = "http://ws.audioscrobbler.com/2.0/"
    
    # select the correct API method
    method = "geo.gettoptracks" if country != "Global" else "chart.gettoptracks"
    
    # set API parameters
    track_params = {
        "method": method,
        "api_key": Config.LASTFM_API_KEY,
        "limit": str(int(limit) * 2),  # request more tracks to avoid empty results after filtering
        "format": "json"
    }

    # add country filter if applicable
    if country != "Global":
        track_params["country"] = COUNTRY_MAPPING.get(country, "Global")

    # fetch top tracks from Last.fm
    track_response = requests.get(url, params=track_params)
    
    if track_response.status_code != 200:
        print(f"Error fetching tracks: {track_response.text}")
        return None

    track_data = track_response.json()
    
    # process tracks
    trending_songs = []
    for i, track in enumerate(track_data.get("tracks", {}).get("track", [])):
        if len(trending_songs) >= int(limit):  # stop when we have enough songs
            break

        track_name = track.get("name")
        artist_name = track.get("artist", {}).get("name")
        
        # fetch track genres/tags
        tags_url = "http://ws.audioscrobbler.com/2.0/"
        tags_params = {
            "method": "track.gettoptags",
            "artist": artist_name,
            "track": track_name,
            "api_key": Config.LASTFM_API_KEY,
            "format": "json"
        }
       
        tags_response = requests.get(tags_url, params=tags_params)
        if tags_response.status_code == 200:
            tags_data = tags_response.json()
            track_genres = [tag.get("name").lower() for tag in tags_data.get("toptags", {}).get("tag", [])]

            # check if track matches any preferred genre
            if any(genre in preferred_genres for genre in track_genres):
                trending_songs.append(f"{i}. {artist_name}: {track_name}")

    # return as formatted text
    if not trending_songs:
        return "No trending songs found for the given filters."

    return "\n".join(trending_songs)  # returns formatted list without numbers