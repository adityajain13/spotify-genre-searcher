import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
import time
import urllib.parse
import threading
import pystray
from PIL import Image, ImageDraw

# --- YOUR SPOTIFY APP CREDENTIALS ---
CLIENT_ID     = "9139d348adec481eb63519b7c3ebf3e4"
CLIENT_SECRET = "139356707f194c64a7fe8732e831eee8"
REDIRECT_URI  = "https://open.spotify.com"
# ------------------------------------

MY_DEVICE_NAME = "ADITYA-DESKTOP"

SCOPE = "user-read-currently-playing user-library-read user-read-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE,
    cache_path=r"C:\Users\Aditya\Documents\Misc\.spotify_cache"
))

def is_liked(track_id):
    result = sp.current_user_saved_tracks_contains([track_id])
    return result[0] if result else False

def open_genre_search(title, artist):
    query = f"{title} {artist} genre"
    url = "https://www.google.com/search?q=" + urllib.parse.quote(query)
    webbrowser.open(url)

def make_tray_icon():
    size = 64
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, size-1, size-1], radius=12, fill=(26, 26, 26))
    d.rounded_rectangle([4, 4, size-5, size-5], radius=9, fill=(30, 215, 96, 30))
    note_color = (30, 215, 96)
    d.rectangle([22, 14, 26, 38], fill=note_color)
    d.rectangle([26, 14, 36, 18], fill=note_color)
    d.rectangle([32, 18, 36, 30], fill=note_color)
    d.ellipse([14, 34, 26, 42], fill=note_color)
    d.ellipse([24, 26, 36, 34], fill=note_color)
    d.ellipse([36, 34, 50, 48], outline=(255, 255, 255), width=3)
    d.line([48, 46, 55, 53], fill=(255, 255, 255), width=3)
    return img

def monitor_spotify():
    last_track_id = None
    while True:
        try:
            current = sp.current_playback()
            if current and current.get("is_playing"):
                device_name = current.get("device", {}).get("name", "")
                if device_name != MY_DEVICE_NAME:
                    last_track_id = None
                    time.sleep(30)
                    continue
                item = current.get("item")
                if item:
                    track_id = item["id"]
                    title    = item["name"]
                    artist   = item["artists"][0]["name"]
                    if track_id != last_track_id:
                        last_track_id = track_id
                        if is_liked(track_id):
                            open_genre_search(title, artist)
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(30)

def quit_app(icon, item):
    icon.stop()

def main():
    threading.Thread(target=monitor_spotify, daemon=True).start()

    icon = pystray.Icon(
        "Spotify Genre Searcher",
        make_tray_icon(),
        "Spotify Genre Searcher",
        menu=pystray.Menu(
            pystray.MenuItem("Quit", quit_app)
        )
    )
    icon.run()

if __name__ == "__main__":
    main()
