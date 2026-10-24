# Copy this file to config.py and fill in your own values.
# config.py is gitignored, so your credentials never end up in the repo.
#
# Note: the credentials that appeared in earlier versions of spotify_genre.py
# were examples from testing and are not valid.

# From your app at https://developer.spotify.com/dashboard
CLIENT_ID     = "your_client_id"
CLIENT_SECRET = "your_client_secret"
REDIRECT_URI  = "https://open.spotify.com"

# The name of your PC as Spotify sees it. Playback on other devices is ignored.
MY_DEVICE_NAME = "YOUR-PC-NAME"

# Where the Spotify login token is cached. Leave as None to use ~/.spotify_cache
CACHE_PATH = None
