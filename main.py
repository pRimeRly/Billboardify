import os
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

SPOTIFY_ID = os.environ["SPOTIFY_CLIENT-ID"]
SPOTIFY_AUTH_KEY = os.environ["SPOTIFY_CLIENT-SECRET"]
SPOTIFY_REDIRECT_URI = os.environ["SPOTIFY_REDIRECT_URI"]

scope = "playlist-modify-private playlist-read-private"

user_year_prompt = input("Which year would you like to travel to? Type the date in this format YYYY-MM-DD:")
BASE_BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
playlist_name = f"{user_year_prompt} Billboard 100"

URL = f"{BASE_BILLBOARD_URL}{user_year_prompt}"
response = requests.get(URL)
webpage = response.text

soup = BeautifulSoup(webpage, "html.parser")
song_name_span = soup.find("span", class_="chart-element__information__song")

list_items = soup.find_all("li", class_="o-chart-results-list__item")
h3_tags = [item.find("h3", class_="c-title") for item in list_items]
song_name_tag = [tag for tag in h3_tags if tag is not None]
song_name = [name_tag.get_text().strip() for name_tag in song_name_tag]

# Spotify authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        SPOTIFY_ID,
        SPOTIFY_AUTH_KEY,
        SPOTIFY_REDIRECT_URI,
        scope=scope,
        cache_path="token.txt",
        show_dialog=True
    ))

user_id = sp.current_user()["id"]
song_uris = []
year = user_year_prompt[:4]

for song in song_name:
    try:
        query = f"track: {song} year: {year}"
        result = sp.search(q=query, limit=1, type="track")
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify.")
        continue

user_playlists = sp.user_playlists(user_id)["items"]
playlist_exists = any(playlist["name"] == playlist_name for playlist in user_playlists)

for playlist in user_playlists:
    if playlist["name"] == playlist_name:
        print("Playlist exists")
        playlist_id = playlist["id"]
        sp.playlist_add_items(playlist_id, song_uris)
        break
else:
    playlist = sp.user_playlist_create(user_id, playlist_name, public=False, description=f"Top 100 Songs from {year}!!")
    playlist_id = playlist["id"]
    sp.playlist_add_items(playlist_id, song_uris)

print(playlist)
