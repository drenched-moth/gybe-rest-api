import unittest

from flask import json

from openapi_server.models.member import Member  # noqa: E501
from openapi_server.models.new_member import NewMember  # noqa: E501
from openapi_server.test import BaseTestCase


class TestMembersController(BaseTestCase):
    """MembersController integration test stubs"""

    def test_delete_member(self):
        """Test case for delete_member

        Delete an existing member
        """
        headers = { 
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/members/{member_id}'.format(member_id=56),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_members(self):
        """Test case for get_members

        Get all members
        """
        headers = { 
            'Accept': 'application/json',
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/members',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_insert_member(self):
        """Test case for insert_member

        Add new member
        """
        new_member = {"name":"name"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/members',
            method='POST',
            headers=headers,
            data=json.dumps(new_member),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_member(self):
        """Test case for update_member

        Update an existing member
        """
        new_member = {"name":"name"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'ApiKey': 'special-key',
        }
        response = self.client.open(
            '/v1/members/{member_id}'.format(member_id=56),
            method='PUT',
            headers=headers,
            data=json.dumps(new_member),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
