import re

SPOTIFY_BASE_URL = "https://open.spotify.com/"
# TODO:
valid_spotify_link = re.compile(r'https://[open.]?spotify.com/[track|song|playlist/artist]/')

SCOPE_MODIFY_PRIVATE_PLAYLIST = 'playlist-modify-private'
SCOPE_MODIFY_PUBLIC_PLAYLIST = 'playlist-modify-public'

uri_split_re = re.compile(r'/|[?]')
def get_spotify_resource(url: str) -> tuple[str, str]:
    """
    Takes a Spotify URI and return a tuple of (resource type, resource ID).

    :param uri: The Spotify URI to be parsed
    :return: A tuple (resource type, resourceID)
    """
    split = uri_split_re.split(url)
    return split[3], split[4]


def resource_is_song(url: str) -> bool:
    return (get_spotify_resource(url)[0] == 'track')
