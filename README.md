# 🎵 Tunebase

**Tunebase** is an integration that fetches trending music from **LASTFM API** and allows data transmission to **Telex**.

---

## 🚀 Features
- Fetches **top trending music** from Lastfm.
- Supports **country-based filtering** (Kenya, Nigeria, United States, etc.).
- Allows **genre selection** (Afrobeats, Jazz, Pop, etc.).
- Configurable **song limit**.
- Integrates with **Telex** for data transmission.

---

## 🛠 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/telexintegrations/Tunebase.git
   cd tunebase
   ```

2. **Create a virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in the root directory and add:
     ```ini
     LASTFM_API_KEY=your_lastfm_api_key
     TELEX_API_KEY=your_telex_api_key
     ```

---

## 🎵 Usage

### Running the Flask API

Start the Flask server:
```bash
python3 run.py
```

### Fetch trending music

To fetch trending music, create a test.py file:
```ini
import requests
from app.fetch_music import get_trending_music

def main():
    music_data = get_trending_music(limit=10, country="Kenya", preferred_genres=["jazz"])
    print("Music Data:", music_data)

if __name__ == "__main__":
    main()

```

Run test.py:
```bash
python3 test.py
```


## ⚙️ API Reference


**Endpoint:**  
`GET /integration.json`

**Query Parameters:**

| Parameter   | Type   | Description |
|------------|--------|-------------|
| `limit`    | `int`  | Number of songs to fetch (default: 10) |
| `country`  | `str`  | Country for filtering (default: "Global") |
| `genres`   | `str`  | Comma-separated list of preferred genres |

---

## 📂 Project Structure

```
tunebase/
│── app/                     # Main application directory
│   ├── __init__.py          # Initializes Flask app
│   ├── routes.py            # Defines API endpoints
│   ├── fetch_music.py       # Fetches trending music from Spotify API
│   ├── config.py            # Configuration settings
│   ├── utils.py             # Helper functions (send data to Telex)
│── tunebase.json            # Telex Integration JSON file
│── requirements.txt         # Dependencies
│── run.py                   # Flask app entry point
│── README.md                # Project documentation
```

---

## 🤝 Contributing

- Fork the repo, create a new branch, and submit a pull request.
- Report bugs or suggest features in the Issues section.

---

## 📜 License

MIT License © 2025 Mukeli