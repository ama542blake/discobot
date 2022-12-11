# the absolute basics: https://discordpy.readthedocs.io/en/stable/intro.html#basic-concepts
import discord
import os
import re
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user}')


uri_split_re = re.compile(r'/|[?]')
def get_spotify_resource(uri: str) -> tuple[str, str]:
    """
    Takes a Spotify URI and return a tuple of (resource type, resource ID)
    :param uri: The Spotify URI to be parsed
    :return: A tuple (resource type, resourceID)
    """
    split = uri_split_re.split(uri)
    return split[4], split[5]


# TODO:
valid_spotify_link = re.compile(r'https://[open.]?spotify.com/[track|song|playlist/artist]/')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if 'https://open.spotify.com/' in message.content:
        # TODO: need to test get_spotify_uri_resource_type
        # TODO: once we can retrieve the type, call the appropriate method to find the resource at the URI
        print()
        await message.channel.send(f'You included a spotify link')

        return

    if 'https://www.youtube.com/' in message.content:
        await message.channel.send(f'You included a YouTube link')
        return


# creates the client connection to the Spotify API
client.run(TOKEN)
