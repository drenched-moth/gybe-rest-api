import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.setlist import Setlist  # noqa: E501
from openapi_server import util


def delete_setlist(concert_id):  # noqa: E501
    """Delete an existing setlist

    Delete an existing setlist # noqa: E501

    :param concert_id: ID of the concert
    :type concert_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_songs_by_concert_id(concert_id):  # noqa: E501
    """Get played songs at a specific concert

    Get played songs at a specific concert # noqa: E501

    :param concert_id: 
    :type concert_id: int

    :rtype: Union[Setlist, Tuple[Setlist, int], Tuple[Setlist, int, Dict[str, str]]
    """
    return 'do some magic!'


def insert_setlist(concert_id, setlist):  # noqa: E501
    """Create a setlist for a concert

    Create a setlist for a concert # noqa: E501

    :param concert_id: ID of the concert
    :type concert_id: int
    :param setlist: setlist object
    :type setlist: dict | bytes

    :rtype: Union[Setlist, Tuple[Setlist, int], Tuple[Setlist, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        setlist = Setlist.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_setlist(concert_id, setlist):  # noqa: E501
    """Update a setlist for a concert

    Update a setlist for a concert # noqa: E501

    :param concert_id: ID of the concert
    :type concert_id: int
    :param setlist: Updated setlist object
    :type setlist: dict | bytes

    :rtype: Union[Setlist, Tuple[Setlist, int], Tuple[Setlist, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        setlist = Setlist.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
