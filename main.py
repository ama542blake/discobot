# the absolute basics of discordpy: https://discordpy.readthedocs.io/en/stable/intro.html#basic-concepts
import os
import discord
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from spotify_utils import SCOPE_MODIFY_PRIVATE_PLAYLIST, SCOPE_MODIFY_PUBLIC_PLAYLIST, SPOTIFY_BASE_URL, resource_is_song

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# set up discord API
intents = discord.Intents.default()
intents.message_content = True
discord_client = discord.Client(intents=intents)

# SpotifyClientCredentials() automatically reads the SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET environment variables
auth_manager = spotipy.SpotifyOAuth(scope=[SCOPE_MODIFY_PUBLIC_PLAYLIST, SCOPE_MODIFY_PRIVATE_PLAYLIST], open_browser=True)
spotify_client = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(), auth_manager=auth_manager)
print(spotify_client.current_user())

TEST_PLAYLIST_URL = os.getenv("TEST_PLAYLIST_URL")

@discord_client.event
async def on_ready():
    print(f'Logged in as {discord_client.user}')


@discord_client.event
async def on_message(message: discord.Message):
    # ignore messages sent from this bot
    if message.author == discord_client.user:
        return

    if SPOTIFY_BASE_URL in message.content:
        # filter out parts of the message that aren't spotify
        song_urls = filter(lambda word: word.startswith(SPOTIFY_BASE_URL) and resource_is_song(word), message.content.split(' '))
        test_playlist_id = spotify_client.playlist(TEST_PLAYLIST_URL)['id']
        # TODO: https://www.newline.co/@bchiang7/breaking-down-oauth-with-spotify--90463996
        spotify_client.playlist_add_items(test_playlist_id, song_urls)
        print(f'\n\n{len(song_urls)} songs added')
        for song_url in song_urls:
            # https://developer.spotify.com/documentation/web-api/reference/#/operations/get-track
            track = spotify_client.track(song_url)
            await message.channel.send(f'You added the track {track["name"]} by {track["artists"][0]["name"]} with URI {track["uri"]}')

        return


# creates the client connection to the Discord API
discord_client.run(DISCORD_TOKEN)