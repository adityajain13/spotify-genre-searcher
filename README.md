# spotify-genre-searcher

A lightweight Windows background tool that detects when a liked song is playing on Spotify and automatically opens a Google search for its genre.

## What it does

- Runs silently in the system tray
- Polls Spotify every 30 seconds
- When a song in your Liked Songs plays on your PC, opens `SONG ARTIST genre` in Google
- Ignores playback from other devices (phone, car, etc.) — triggers on your PC only, regardless of what playlist or album you're playing from

## Requirements

- Windows
- Python 3.x
- A Spotify account

## Setup

### 1. Install dependencies

```
pip install spotipy pystray pillow
```

### 2. Create a Spotify app

1. Go to [developer.spotify.com/dashboard](https://developer.spotify.com/dashboard) and log in
2. Click **Create app**
3. Set the redirect URI to `https://open.spotify.com`
4. Copy your **Client ID** and **Client Secret**

### 3. Configure the script

Open `spotify_genre.py` and fill in your credentials at the top:

```python
CLIENT_ID     = "your_client_id"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI  = "https://open.spotify.com"
MY_DEVICE_NAME = "YOUR-PC-NAME"
```

To find your device name, run the script once with `MY_DEVICE_NAME = None` — it will print the device name in the terminal.

Update the cache path to match your username:

```python
cache_path=r"C:\Users\YOURNAME\Documents\.spotify_cache"
```

### 4. Authorize

Run the script once as `.py`. A browser window will open asking you to authorize — log in and paste the redirect URL back into the terminal. This only happens once.

### 5. Run in the background

Rename the file to `spotify_genre.pyw` and double-click it. A green tray icon will appear in the system tray. Right-click to quit.

### Auto-start with Windows

Place a shortcut to `spotify_genre.pyw` in your Startup folder:

1. Press `Win + R`
2. Type `shell:startup` and hit Enter
3. Drop the shortcut in there

## Notes

- The Spotify API has rate limits — polling every 30 seconds stays well within them
- The tool triggers whenever a liked song plays on your specific PC — it doesn't matter which playlist or album you're playing from
