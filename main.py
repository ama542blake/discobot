# the absolute basics: https://discordpy.readthedocs.io/en/stable/intro.html#basic-concepts
import os
import re
import discord
from dotenv import load_dotenv
from spotify_utils import SPOTIFY_BASE_URL, get_spotify_resource, resource_is_song

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# set up discord API
intents = discord.Intents.default()
intents.message_content = True
# creates the client connection to the Discord API
discord_client = discord.Client(intents=intents)
discord_client.run(DISCORD_TOKEN)

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
        song_resource_uris = map(lambda url: get_spotify_resource(url), song_urls)
        for song_uri in song_resource_uris:
            pass

        return
