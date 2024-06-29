import unittest

from flask import json

from openapi_server.models.band_composition import BandComposition  # noqa: E501
from openapi_server.test import BaseTestCase


class TestBandCompositionsController(BaseTestCase):
    """BandCompositionsController integration test stubs"""

    def test_delete_band_composition(self):
        """Test case for delete_band_composition

        Delete an existing band composition
        """
        headers = { 
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/concerts/{concert_id}/members'.format(concert_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_members_by_concert_id(self):
        """Test case for get_members_by_concert_id

        Get the band composition at a specific concert
        """
        headers = { 
            'Accept': 'application/json',
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/concerts/{concert_id}/members'.format(concert_id=56),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_insert_band_composition(self):
        """Test case for insert_band_composition

        Create the band composition for a concert
        """
        band_composition = {"members":[{"name":"name","id":0},{"name":"name","id":0}]}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/concerts/{concert_id}/members'.format(concert_id=56),
            method='POST',
            headers=headers,
            data=json.dumps(band_composition),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
