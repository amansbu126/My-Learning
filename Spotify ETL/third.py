import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
from datetime import datetime

# Replace with your credentials from Spotify Developer Dashboard
client_id = 'your_client_id'
client_secret = 'your_client_secret'

# Set up Spotipy client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id='6edb5eb42f354de3b966dad07c74af26',
    client_secret='365f45c2ac2d47f783cdbacbbd50e6d3'
))

# Spotify playlist URL and ID
playlist_url = "https://open.spotify.com/playlist/6SAUxRqgv0EdwHHnjBRmoE"
playlist_id = playlist_url.split("/")[-1]

# Fetch playlist tracks
results = sp.playlist_tracks(playlist_id)
tracks = results['items']

# Extract data
track_data = []
for item in tracks:
    track = item['track']
    track_data.append({
        'track_name': track['name'],
        'artist': track['artists'][0]['name'],
        'album': track['album']['name'],
        'release_date': track['album']['release_date'],
        'track_id': track['id'],
        'track_url': track['external_urls']['spotify'],
        'popularity': track['popularity']
    })

# Create DataFrame
df = pd.DataFrame(track_data)

# Save to CSV locally
filename = f"spotify_playlist_{playlist_id}_{datetime.now().strftime('%Y%m%d%H%M%S')}.csv"
df.to_csv(filename, index=False)

print(f"✅ Saved to CSV: {filename}")
