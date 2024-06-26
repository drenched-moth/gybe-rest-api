from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class NewConcert(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, _date=None, venue=None, city=None, state=None, country=None, extra_info=None, notes=None, acknowledgments=None):  # noqa: E501
        """NewConcert - a model defined in OpenAPI

        :param _date: The _date of this NewConcert.  # noqa: E501
        :type _date: date
        :param venue: The venue of this NewConcert.  # noqa: E501
        :type venue: str
        :param city: The city of this NewConcert.  # noqa: E501
        :type city: str
        :param state: The state of this NewConcert.  # noqa: E501
        :type state: str
        :param country: The country of this NewConcert.  # noqa: E501
        :type country: str
        :param extra_info: The extra_info of this NewConcert.  # noqa: E501
        :type extra_info: str
        :param notes: The notes of this NewConcert.  # noqa: E501
        :type notes: str
        :param acknowledgments: The acknowledgments of this NewConcert.  # noqa: E501
        :type acknowledgments: str
        """
        self.openapi_types = {
            '_date': date,
            'venue': str,
            'city': str,
            'state': str,
            'country': str,
            'extra_info': str,
            'notes': str,
            'acknowledgments': str
        }

        self.attribute_map = {
            '_date': 'date',
            'venue': 'venue',
            'city': 'city',
            'state': 'state',
            'country': 'country',
            'extra_info': 'extra_info',
            'notes': 'notes',
            'acknowledgments': 'acknowledgments'
        }

        self.__date = _date
        self._venue = venue
        self._city = city
        self._state = state
        self._country = country
        self._extra_info = extra_info
        self._notes = notes
        self._acknowledgments = acknowledgments

    @classmethod
    def from_dict(cls, dikt) -> 'NewConcert':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NewConcert of this NewConcert.  # noqa: E501
        :rtype: NewConcert
        """
        return util.deserialize_model(dikt, cls)

    @property
    def _date(self) -> date:
        """Gets the _date of this NewConcert.


        :return: The _date of this NewConcert.
        :rtype: date
        """
        return self.__date

    @_date.setter
    def _date(self, _date: date):
        """Sets the _date of this NewConcert.


        :param _date: The _date of this NewConcert.
        :type _date: date
        """
        if _date is None:
            raise ValueError("Invalid value for `_date`, must not be `None`")  # noqa: E501

        self.__date = _date

    @property
    def venue(self) -> str:
        """Gets the venue of this NewConcert.


        :return: The venue of this NewConcert.
        :rtype: str
        """
        return self._venue

    @venue.setter
    def venue(self, venue: str):
        """Sets the venue of this NewConcert.


        :param venue: The venue of this NewConcert.
        :type venue: str
        """
        if venue is None:
            raise ValueError("Invalid value for `venue`, must not be `None`")  # noqa: E501

        self._venue = venue

    @property
    def city(self) -> str:
        """Gets the city of this NewConcert.


        :return: The city of this NewConcert.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city: str):
        """Sets the city of this NewConcert.


        :param city: The city of this NewConcert.
        :type city: str
        """
        if city is None:
            raise ValueError("Invalid value for `city`, must not be `None`")  # noqa: E501

        self._city = city

    @property
    def state(self) -> str:
        """Gets the state of this NewConcert.


        :return: The state of this NewConcert.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str):
        """Sets the state of this NewConcert.


        :param state: The state of this NewConcert.
        :type state: str
        """

        self._state = state

    @property
    def country(self) -> str:
        """Gets the country of this NewConcert.


        :return: The country of this NewConcert.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country: str):
        """Sets the country of this NewConcert.


        :param country: The country of this NewConcert.
        :type country: str
        """
        if country is None:
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def extra_info(self) -> str:
        """Gets the extra_info of this NewConcert.


        :return: The extra_info of this NewConcert.
        :rtype: str
        """
        return self._extra_info

    @extra_info.setter
    def extra_info(self, extra_info: str):
        """Sets the extra_info of this NewConcert.


        :param extra_info: The extra_info of this NewConcert.
        :type extra_info: str
        """

        self._extra_info = extra_info

    @property
    def notes(self) -> str:
        """Gets the notes of this NewConcert.


        :return: The notes of this NewConcert.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes: str):
        """Sets the notes of this NewConcert.


        :param notes: The notes of this NewConcert.
        :type notes: str
        """

        self._notes = notes

    @property
    def acknowledgments(self) -> str:
        """Gets the acknowledgments of this NewConcert.


        :return: The acknowledgments of this NewConcert.
        :rtype: str
        """
        return self._acknowledgments

    @acknowledgments.setter
    def acknowledgments(self, acknowledgments: str):
        """Sets the acknowledgments of this NewConcert.


        :param acknowledgments: The acknowledgments of this NewConcert.
        :type acknowledgments: str
        """

        self._acknowledgments = acknowledgments
