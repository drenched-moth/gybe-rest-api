from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class Recording(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, recording_id=None, concert_id=None, duration=None, source_info=None, url=None):  # noqa: E501
        """Recording - a model defined in OpenAPI

        :param recording_id: The recording_id of this Recording.  # noqa: E501
        :type recording_id: int
        :param concert_id: The concert_id of this Recording.  # noqa: E501
        :type concert_id: int
        :param duration: The duration of this Recording.  # noqa: E501
        :type duration: int
        :param source_info: The source_info of this Recording.  # noqa: E501
        :type source_info: str
        :param url: The url of this Recording.  # noqa: E501
        :type url: str
        """
        self.openapi_types = {
            'recording_id': int,
            'concert_id': int,
            'duration': int,
            'source_info': str,
            'url': str
        }

        self.attribute_map = {
            'recording_id': 'recording_id',
            'concert_id': 'concert_id',
            'duration': 'duration',
            'source_info': 'source_info',
            'url': 'url'
        }

        self._recording_id = recording_id
        self._concert_id = concert_id
        self._duration = duration
        self._source_info = source_info
        self._url = url

    @classmethod
    def from_dict(cls, dikt) -> 'Recording':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Recording of this Recording.  # noqa: E501
        :rtype: Recording
        """
        return util.deserialize_model(dikt, cls)

    @property
    def recording_id(self) -> int:
        """Gets the recording_id of this Recording.


        :return: The recording_id of this Recording.
        :rtype: int
        """
        return self._recording_id

    @recording_id.setter
    def recording_id(self, recording_id: int):
        """Sets the recording_id of this Recording.


        :param recording_id: The recording_id of this Recording.
        :type recording_id: int
        """
        if recording_id is None:
            raise ValueError("Invalid value for `recording_id`, must not be `None`")  # noqa: E501

        self._recording_id = recording_id

    @property
    def concert_id(self) -> int:
        """Gets the concert_id of this Recording.


        :return: The concert_id of this Recording.
        :rtype: int
        """
        return self._concert_id

    @concert_id.setter
    def concert_id(self, concert_id: int):
        """Sets the concert_id of this Recording.


        :param concert_id: The concert_id of this Recording.
        :type concert_id: int
        """
        if concert_id is None:
            raise ValueError("Invalid value for `concert_id`, must not be `None`")  # noqa: E501

        self._concert_id = concert_id

    @property
    def duration(self) -> int:
        """Gets the duration of this Recording.


        :return: The duration of this Recording.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration: int):
        """Sets the duration of this Recording.


        :param duration: The duration of this Recording.
        :type duration: int
        """

        self._duration = duration

    @property
    def source_info(self) -> str:
        """Gets the source_info of this Recording.


        :return: The source_info of this Recording.
        :rtype: str
        """
        return self._source_info

    @source_info.setter
    def source_info(self, source_info: str):
        """Sets the source_info of this Recording.


        :param source_info: The source_info of this Recording.
        :type source_info: str
        """

        self._source_info = source_info

    @property
    def url(self) -> str:
        """Gets the url of this Recording.


        :return: The url of this Recording.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this Recording.


        :param url: The url of this Recording.
        :type url: str
        """

        self._url = url
