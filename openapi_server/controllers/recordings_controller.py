import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.new_recording import NewRecording  # noqa: E501
from openapi_server.models.recording import Recording  # noqa: E501
from openapi_server import util


def delete_recording(recording_id):  # noqa: E501
    """Delete an existing recording

    Delete an existing recording # noqa: E501

    :param recording_id: ID of the recording to delete
    :type recording_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_recordings(_date=None, year=None, before_year=None, after_year=None, venue=None, city=None, state=None, country=None):  # noqa: E501
    """Get all recordings

    Get all recordings # noqa: E501

    :param _date: Get recordings at specified date
    :type _date: str
    :param year: Get recordings at specifed afterYear
    :type year: int
    :param before_year: Get recordings before specified year
    :type before_year: int
    :param after_year: Get recordings after specified year
    :type after_year: int
    :param venue: Get recordings that took place at specified venue
    :type venue: str
    :param city: Get recordings that took place at specified city
    :type city: str
    :param state: Get recordings that took place in specified state
    :type state: str
    :param country: Get recordings that took place in specified country
    :type country: str

    :rtype: Union[List[Recording], Tuple[List[Recording], int], Tuple[List[Recording], int, Dict[str, str]]
    """
    _date = util.deserialize_date(_date)
    return 'do some magic!'


def get_recordings_by_concert_id(concert_id):  # noqa: E501
    """Get recordings of a specific concert

    Get recordings of a specific concert # noqa: E501

    :param concert_id: 
    :type concert_id: int

    :rtype: Union[List[Recording], Tuple[List[Recording], int], Tuple[List[Recording], int, Dict[str, str]]
    """
    return 'do some magic!'


def get_recordings_by_id(recording_id):  # noqa: E501
    """Get a specific recording

    Get a specific recording # noqa: E501

    :param recording_id: 
    :type recording_id: int

    :rtype: Union[Recording, Tuple[Recording, int], Tuple[Recording, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_recordings_by_song_id(song_id):  # noqa: E501
    """Get recordings where specified song can be heard

    Get recordings where specified song can be heard # noqa: E501

    :param song_id: 
    :type song_id: int

    :rtype: Union[List[Recording], Tuple[List[Recording], int], Tuple[List[Recording], int, Dict[str, str]]
    """
    return 'do some magic!'


def insert_recording(concert_id, new_recording):  # noqa: E501
    """Create a recording for a concert

    Create a recording for a concert # noqa: E501

    :param concert_id: ID of the recorded concert
    :type concert_id: int
    :param new_recording: recording object
    :type new_recording: dict | bytes

    :rtype: Union[Recording, Tuple[Recording, int], Tuple[Recording, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        new_recording = NewRecording.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_recording(recording_id, new_recording):  # noqa: E501
    """Update a recording

    Update a recording # noqa: E501

    :param recording_id: ID of the recording to update
    :type recording_id: int
    :param new_recording: Updated recording object
    :type new_recording: dict | bytes

    :rtype: Union[Recording, Tuple[Recording, int], Tuple[Recording, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        new_recording = NewRecording.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
