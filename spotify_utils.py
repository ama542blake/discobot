import re

SPOTIFY_BASE_URL = "https://open.spotify.com/"
# TODO:
valid_spotify_link = re.compile(r'https://[open.]?spotify.com/[track|song|playlist/artist]/')

uri_split_re = re.compile(r'/|[?]')
def get_spotify_resource(uri: str) -> tuple[str, str]:
    """
    Takes a Spotify URI and return a tuple of (resource type, resource ID).

    :param uri: The Spotify URI to be parsed
    :return: A tuple (resource type, resourceID)
    """
    split = uri_split_re.split(uri)
    return split[3], split[4]


def resource_is_song(uri: str) -> bool:
    return (get_spotify_resource(uri)[0] == 'track')
    