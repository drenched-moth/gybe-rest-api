import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.concert import Concert  # noqa: E501
from openapi_server.models.new_concert import NewConcert  # noqa: E501
from openapi_server import util


def create_concert(new_concert):  # noqa: E501
    """Create a new concert

    Create a new concert # noqa: E501

    :param new_concert: A new concert object
    :type new_concert: dict | bytes

    :rtype: Union[Concert, Tuple[Concert, int], Tuple[Concert, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        new_concert = NewConcert.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_concert(concert_id):  # noqa: E501
    """Delete an existing concert

    Delete an existing concert # noqa: E501

    :param concert_id: ID of the concert to delete
    :type concert_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_concert_by_id(concert_id):  # noqa: E501
    """Get a specific concert

    Get a specific concert # noqa: E501

    :param concert_id: 
    :type concert_id: int

    :rtype: Union[Concert, Tuple[Concert, int], Tuple[Concert, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_concerts(_date=None, year=None, before_year=None, after_year=None, venue=None, city=None, state=None, country=None):  # noqa: E501
    """Get concerts

    Get concerts # noqa: E501

    :param _date: The specific date of the concert (YYYY-MM-DD)
    :type _date: str
    :param year: Get concerts in the specified year
    :type year: int
    :param before_year: Get concerts before specified year
    :type before_year: int
    :param after_year: Get concerts after specified year
    :type after_year: int
    :param venue: Get concerts that took place at specified venue
    :type venue: str
    :param city: Get concerts that took place at specified city
    :type city: str
    :param state: Get concerts that took place in specified state
    :type state: str
    :param country: Get concerts that took place in specified country
    :type country: str

    :rtype: Union[List[Concert], Tuple[List[Concert], int], Tuple[List[Concert], int, Dict[str, str]]
    """
    _date = util.deserialize_date(_date)
    return 'do some magic!'


def update_concert(concert_id, new_concert):  # noqa: E501
    """Update an existing concert

    Update an existing concert # noqa: E501

    :param concert_id: ID of  the concert to update
    :type concert_id: int
    :param new_concert: Updated concert object
    :type new_concert: dict | bytes

    :rtype: Union[Concert, Tuple[Concert, int], Tuple[Concert, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        new_concert = NewConcert.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
