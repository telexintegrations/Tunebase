import os

class Config:
    LASTFM_API_KEY = os.getenv("LASTFM_API_KEY")
    TELEX_CHANNEL_WEBHOOK = os.getenv("TELEX_CHANNEL_WEBHOOK")