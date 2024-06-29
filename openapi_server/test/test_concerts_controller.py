import unittest

from flask import json

from openapi_server.models.concert import Concert  # noqa: E501
from openapi_server.models.new_concert import NewConcert  # noqa: E501
from openapi_server.test import BaseTestCase


class TestConcertsController(BaseTestCase):
    """ConcertsController integration test stubs"""

    def test_create_concert(self):
        """Test case for create_concert

        Create a new concert
        """
        new_concert = {"date":"2000-01-23","venue":"venue","country":"country","extra_info":"extra_info","notes":"notes","city":"city","acknowledgments":"acknowledgments","state":"state"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/concerts',
            method='POST',
            headers=headers,
            data=json.dumps(new_concert),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_concert(self):
        """Test case for delete_concert

        Delete an existing concert
        """
        headers = { 
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/concerts/{concert_id}'.format(concert_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_concert_by_id(self):
        """Test case for get_concert_by_id

        Get a specific concert
        """
        headers = { 
            'Accept': 'application/json',
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/concerts/{concert_id}'.format(concert_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_concerts(self):
        """Test case for get_concerts

        Get concerts
        """
        query_string = [('date', '2013-10-20'),
                        ('year', 56),
                        ('beforeYear', 56),
                        ('afterYear', 56),
                        ('venue', 'venue_example'),
                        ('city', 'city_example'),
                        ('state', 'state_example'),
                        ('country', 'country_example')]
        headers = { 
            'Accept': 'application/json',
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/concerts',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_concert(self):
        """Test case for update_concert

        Update an existing concert
        """
        new_concert = {"date":"2000-01-23","venue":"venue","country":"country","extra_info":"extra_info","notes":"notes","city":"city","acknowledgments":"acknowledgments","state":"state"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/concerts/{concert_id}'.format(concert_id=56),
            method='PUT',
            headers=headers,
            data=json.dumps(new_concert),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
