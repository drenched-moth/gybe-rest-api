import unittest

from flask import json

from openapi_server.models.setlist import Setlist  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSetlistsController(BaseTestCase):
    """SetlistsController integration test stubs"""

    def test_delete_setlist(self):
        """Test case for delete_setlist

        Delete an existing setlist
        """
        headers = { 
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/concerts/{concert_id}/songs'.format(concert_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_songs_by_concert_id(self):
        """Test case for get_songs_by_concert_id

        Get played songs at a specific concert
        """
        headers = { 
            'Accept': 'application/json',
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/concerts/{concert_id}/songs'.format(concert_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_insert_setlist(self):
        """Test case for insert_setlist

        Create a setlist for a concert
        """
        setlist = {"songs":[{"song_id":0,"concert_id":6,"order":1},{"song_id":0,"concert_id":6,"order":1}]}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/concerts/{concert_id}/songs'.format(concert_id=56),
            method='POST',
            headers=headers,
            data=json.dumps(setlist),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_setlist(self):
        """Test case for update_setlist

        Update a setlist for a concert
        """
        setlist = {"songs":[{"song_id":0,"concert_id":6,"order":1},{"song_id":0,"concert_id":6,"order":1}]}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/concerts/{concert_id}/songs'.format(concert_id=56),
            method='PUT',
            headers=headers,
            data=json.dumps(setlist),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
