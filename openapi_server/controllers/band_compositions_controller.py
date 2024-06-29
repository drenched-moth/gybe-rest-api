import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.band_composition import BandComposition  # noqa: E501
from openapi_server import util


def delete_band_composition(concert_id):  # noqa: E501
    """Delete an existing band composition

    Delete an existing band composition # noqa: E501

    :param concert_id: ID of the concert
    :type concert_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_members_by_concert_id(concert_id):  # noqa: E501
    """Get the band composition at a specific concert

    Get the band composition at a specific concert # noqa: E501

    :param concert_id: ID of the concert
    :type concert_id: int

    :rtype: Union[BandComposition, Tuple[BandComposition, int], Tuple[BandComposition, int, Dict[str, str]]
    """
    return 'do some magic!'


def insert_band_composition(concert_id, band_composition):  # noqa: E501
    """Create the band composition for a concert

    Create the band composition for a concert # noqa: E501

    :param concert_id: ID of the concert
    :type concert_id: int
    :param band_composition: band composition object
    :type band_composition: dict | bytes

    :rtype: Union[BandComposition, Tuple[BandComposition, int], Tuple[BandComposition, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        band_composition = BandComposition.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
