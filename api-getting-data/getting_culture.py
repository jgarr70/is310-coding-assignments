import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# 1. Load the secrets from your .env file
load_dotenv()



import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

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
    print(f"❤️ {track['name']} - {track['artists'][0]['name']}")


# # 2. Setup the credentials
# auth_manager = SpotifyClientCredentials(
#     client_id=os.getenv("SPOTIPY_CLIENT_ID"),
#     client_secret=os.getenv("SPOTIPY_CLIENT_SECRET")
# )

# # 3. Initialize the Spotify object
# sp = spotipy.Spotify(auth_manager=auth_manager)

# # 4. Test it out! (Search for a Rick Riordan related playlist?)
# results = sp.search(q='Don Toliver', limit=5)
# for track in results['tracks']['items']:
#     print(f"Found track: {track['name']} by {track['artists'][0]['name']}")


# with open('spotify_data.csv', 'w') as file:
#     writer = csv.writer(file)
    # Write the headers
    # writer.writerow(['name', 'link', 'quote'])
    # for character in pj_characters:
    #     writer.writerow([character['name'], character['link'], character['quote']])
