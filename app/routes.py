from flask import Blueprint, jsonify, request
from app.fetch_music import get_trending_music
from app.utils import send_to_telex
from datetime import datetime


routes = Blueprint("routes", __name__)

@routes.route("/integration.json", methods=["GET"])
def get_integration_json():
    """
    Returns integration metadata for Telex registration
    """
    base_url = request.url_root.rstrip("/")

    return jsonify({
        "data": {
            "date": {
                "created_at": "2025-02-20",
                "updated_at": "2025-02-21"
                },
            "descriptions": {
                "app_name": "Tunebase",
                "app_description": "Fetches and delivers trending songs from Last.fm daily",
                "app_url": base_url,
                "app_logo": "https://imgur.com/a/xmPqk95",
                "background_color": "#053C26"
                },
            "is_active": True,
            "integration_category": "Communication & Collaboration",
            "integration_type": "interval",
            "key_features": [
                "fetches trending songs",
                "Runs at a specified interval",
                "Delivers data to a Telex channel"
                ],
            "author": "Mukeli Kavivya",
            "settings": [
                {
                    "label": "interval",
                    "type": "text",
                    "required": True,
                    "description": "set how often Tunebase fetches trending songs. Use contrab syntax",
                    "default": "0 0 * * *"
                    },
                {
                    "label": "Number of trending songs",
                    "description": "set how many trending songs should be fetched daily",
                    "key": "limit",
                    "default": "10",
                    "min": "1",
                    "max": "33"
                    },
                {
                    "label": "Country",
                    "type": "dropdown",
                    "description": "select country for customized trending music",
                    "options": ["United States", "Kenya", "Nigeria", "Uganda", "Africa", "United Kingdom", "Global"],
                    "default": "Global"
                    },
                {
                    "label": "preferred genre",
                    "type": "multi-select",
                    "description": "select genres to filter trending music",
                    "options": ["reggae", "jazz", "pop", "rock", "hip-hop", "Afrobeats", "Amapiano", "Electronic", "gospel", "country"],
                    "default": ["afrobeats", "jazz", "pop"]
                    }
                ],
            "tick_url": f"{base_url}/tick",
            "target_url": ""
        }
    })

@routes.route("/tick", methods=["POST"])
def tick():
    """
    called by Telex at set intervals and fetches trending music,
    sends data to Telex
    """
    try:
        music_data = get_trending_music()
        if not music_data:
            return jsonify({"error": "Failed to fetch music"}), 500

        # send data to Telex channel
        response_status = send_to_telex(music_data)
        return jsonify ({"status": "accepted", "telex_response": response_status}), 202

    except Exception as e:
        return jsonify ({"error": str(e)}), 500
