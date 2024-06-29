import unittest

from flask import json

from openapi_server.models.new_recording import NewRecording  # noqa: E501
from openapi_server.models.recording import Recording  # noqa: E501
from openapi_server.test import BaseTestCase


class TestRecordingsController(BaseTestCase):
    """RecordingsController integration test stubs"""

    def test_delete_recording(self):
        """Test case for delete_recording

        Delete an existing recording
        """
        headers = { 
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/recordings/{recording_id}'.format(recording_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_recordings(self):
        """Test case for get_recordings

        Get all recordings
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
            '/v1/recordings',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_recordings_by_concert_id(self):
        """Test case for get_recordings_by_concert_id

        Get recordings of a specific concert
        """
        headers = { 
            'Accept': 'application/json',
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/concerts/{concert_id}/recordings'.format(concert_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_recordings_by_id(self):
        """Test case for get_recordings_by_id

        Get a specific recording
        """
        headers = { 
            'Accept': 'application/json',
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/recordings/{recording_id}'.format(recording_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_recordings_by_song_id(self):
        """Test case for get_recordings_by_song_id

        Get recordings where specified song can be heard
        """
        headers = { 
            'Accept': 'application/json',
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/songs/{song_id}/recordings'.format(song_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_insert_recording(self):
        """Test case for insert_recording

        Create a recording for a concert
        """
        new_recording = {"duration":6,"concert_id":0,"source_info":"source_info","url":"url"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/concerts/{concert_id}/recordings'.format(concert_id=56),
            method='POST',
            headers=headers,
            data=json.dumps(new_recording),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_recording(self):
        """Test case for update_recording

        Update a recording
        """
        new_recording = {"duration":6,"concert_id":0,"source_info":"source_info","url":"url"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/recordings/{recording_id}'.format(recording_id=56),
            method='PUT',
            headers=headers,
            data=json.dumps(new_recording),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
