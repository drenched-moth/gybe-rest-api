import unittest

from flask import json

from openapi_server.models.new_song import NewSong  # noqa: E501
from openapi_server.models.song import Song  # noqa: E501
from openapi_server.test import BaseTestCase


class TestSongsController(BaseTestCase):
    """SongsController integration test stubs"""

    def test_delete_song(self):
        """Test case for delete_song

        Delete an existing song
        """
        headers = { 
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/songs/{song_id}'.format(song_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_song_by_id(self):
        """Test case for get_song_by_id

        Get names for a specific song
        """
        headers = { 
            'Accept': 'application/json',
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/songs/{song_id}'.format(song_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_songs(self):
        """Test case for get_songs

        Get songs
        """
        query_string = [('matches', 'matches_example')]
        headers = { 
            'Accept': 'application/json',
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/songs',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_insert_aliases(self):
        """Test case for insert_aliases

        Add aliases to a specific song
        """
        new_song = {"names":["names","names"]}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/songs/{song_id}'.format(song_id=56),
            method='POST',
            headers=headers,
            data=json.dumps(new_song),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_insert_song(self):
        """Test case for insert_song

        Create a new song
        """
        new_song = {"names":["names","names"]}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/songs',
            method='POST',
            headers=headers,
            data=json.dumps(new_song),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
