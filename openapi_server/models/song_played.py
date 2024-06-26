from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class SongPlayed(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, song_id=None, concert_id=None, order=None):  # noqa: E501
        """SongPlayed - a model defined in OpenAPI

        :param song_id: The song_id of this SongPlayed.  # noqa: E501
        :type song_id: int
        :param concert_id: The concert_id of this SongPlayed.  # noqa: E501
        :type concert_id: int
        :param order: The order of this SongPlayed.  # noqa: E501
        :type order: int
        """
        self.openapi_types = {
            'song_id': int,
            'concert_id': int,
            'order': int
        }

        self.attribute_map = {
            'song_id': 'song_id',
            'concert_id': 'concert_id',
            'order': 'order'
        }

        self._song_id = song_id
        self._concert_id = concert_id
        self._order = order

    @classmethod
    def from_dict(cls, dikt) -> 'SongPlayed':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SongPlayed of this SongPlayed.  # noqa: E501
        :rtype: SongPlayed
        """
        return util.deserialize_model(dikt, cls)

    @property
    def song_id(self) -> int:
        """Gets the song_id of this SongPlayed.


        :return: The song_id of this SongPlayed.
        :rtype: int
        """
        return self._song_id

    @song_id.setter
    def song_id(self, song_id: int):
        """Sets the song_id of this SongPlayed.


        :param song_id: The song_id of this SongPlayed.
        :type song_id: int
        """
        if song_id is None:
            raise ValueError("Invalid value for `song_id`, must not be `None`")  # noqa: E501

        self._song_id = song_id

    @property
    def concert_id(self) -> int:
        """Gets the concert_id of this SongPlayed.


        :return: The concert_id of this SongPlayed.
        :rtype: int
        """
        return self._concert_id

    @concert_id.setter
    def concert_id(self, concert_id: int):
        """Sets the concert_id of this SongPlayed.


        :param concert_id: The concert_id of this SongPlayed.
        :type concert_id: int
        """
        if concert_id is None:
            raise ValueError("Invalid value for `concert_id`, must not be `None`")  # noqa: E501

        self._concert_id = concert_id

    @property
    def order(self) -> int:
        """Gets the order of this SongPlayed.


        :return: The order of this SongPlayed.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order: int):
        """Sets the order of this SongPlayed.


        :param order: The order of this SongPlayed.
        :type order: int
        """
        if order is None:
            raise ValueError("Invalid value for `order`, must not be `None`")  # noqa: E501

        self._order = order
