import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import pyeuropeana.apis as apis
from rich import print as rprint

# 1. Load the secrets from your .env file
load_dotenv()

# Simplified setup
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="user-top-read user-library-read",
    redirect_uri="http://127.0.0.1:8888/callback"
))

# Get your Top 5 Songs
print("--- YOUR ALL-TIME TOP TRACKS ---")
results = sp.current_user_top_tracks(limit=5, time_range='long_term')
for i, item in enumerate(results['items']):
    print(f"{i+1}. {item['name']} - {item['artists'][0]['name']}")

# Get your 5 most recently Liked Songs
print("\n--- RECENTLY LIKED ---")
liked = sp.current_user_saved_tracks(limit=5)
for item in liked['items']:
    track = item['track']
    print(f" {track['name']} - {track['artists'][0]['name']}")


response = apis.entity.suggest(
   text = 'The Beatles',
   type = 'agent' # Search for people/groups
)

# rprint(response['items'][:3]) # View first 3 suggestions

for item in response['items'][:3]:
    # 1. Get the main ID
    print(f"ID: {item['id']}")
    
    # 2. Get the Bulgarian name (since it's the only one in prefLabel here)
    main_name = item['prefLabel'].get('bg', 'No Name')
    print(f"Main Name: {main_name}")
    
    # 3. Get all the English nicknames and join them with a comma
    en_aliases = item['altLabel'].get('en', [])
    print(f"English Nicknames: {', '.join(en_aliases)}")
    
    # 4. Get the image URL
    image = item['isShownBy']['id']
    print(f"Image Link: {image}")

# Create a master dictionary to hold all your results
data_to_save = {
    "top_tracks": results['items'],
    "liked_songs": liked['items'],
    "europeana_beatles": response['items'][:3]
}

# Write it to a file
with open("api-getting-data/spotify_data.json", "w") as f:
    json.dump(data_to_save, f, indent=4)

print("Saved to spotify_data.json!")