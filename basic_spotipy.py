# set up auth: https://www.youtube.com/watch?v=3RGm4jALukM
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

# sets the SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET variables, which are
# automatically read when calling SpotifyClientCredentials()
load_dotenv()

lz_uri = 'spotify:artist:36QJpDe2go2KgaRleHCDTp'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_top_tracks(lz_uri)

for track in results['tracks'][:10]:
    print('track    : ' + track['name'])
    print('audio    : ' + track['preview_url'])
    print('cover art: ' + track['album']['images'][0]['url'])
    print()