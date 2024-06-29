import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.new_song import NewSong  # noqa: E501
from openapi_server.models.song import Song  # noqa: E501
from openapi_server import util


def delete_song(song_id):  # noqa: E501
    """Delete an existing song

    Delete an existing song # noqa: E501

    :param song_id: ID of the song to delete
    :type song_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_song_by_id(song_id):  # noqa: E501
    """Get names for a specific song

    Get names for a specific song # noqa: E501

    :param song_id: Song ID
    :type song_id: int

    :rtype: Union[List[Song], Tuple[List[Song], int], Tuple[List[Song], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_songs(matches=None):  # noqa: E501
    """Get songs

    Get songs # noqa: E501

    :param matches: Aliases of given song name
    :type matches: str

    :rtype: Union[List[Song], Tuple[List[Song], int], Tuple[List[Song], int, Dict[str, str]]
    """
    return 'do some magic!'


def insert_aliases(song_id, new_song):  # noqa: E501
    """Add aliases to a specific song

    Add aliases to a specific song # noqa: E501

    :param song_id: Song ID
    :type song_id: int
    :param new_song: New aliases object
    :type new_song: dict | bytes

    :rtype: Union[Song, Tuple[Song, int], Tuple[Song, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        new_song = NewSong.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def insert_song(new_song):  # noqa: E501
    """Create a new song

    Create a new song # noqa: E501

    :param new_song: A new song object
    :type new_song: dict | bytes

    :rtype: Union[Song, Tuple[Song, int], Tuple[Song, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        new_song = NewSong.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
