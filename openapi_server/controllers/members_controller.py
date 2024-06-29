import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.member import Member  # noqa: E501
from openapi_server.models.new_member import NewMember  # noqa: E501
from openapi_server import util


def delete_member(member_id):  # noqa: E501
    """Delete an existing member

    Delete an existing member # noqa: E501

    :param member_id: ID of the member to delete
    :type member_id: int

    :rtype: Union[None, Tuple[None, int], Tuple[None, int, Dict[str, str]]
    """
    return 'do some magic!'


def get_members():  # noqa: E501
    """Get all members

    Get all members # noqa: E501


    :rtype: Union[List[Member], Tuple[List[Member], int], Tuple[List[Member], int, Dict[str, str]]
    """
    return 'do some magic!'


def insert_member(new_member):  # noqa: E501
    """Add new member

    Add new member # noqa: E501

    :param new_member: New member object
    :type new_member: dict | bytes

    :rtype: Union[Member, Tuple[Member, int], Tuple[Member, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        new_member = NewMember.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_member(member_id, new_member):  # noqa: E501
    """Update an existing member

    Update an existing member # noqa: E501

    :param member_id: ID of the member to update
    :type member_id: int
    :param new_member: Updated member object
    :type new_member: dict | bytes

    :rtype: Union[Member, Tuple[Member, int], Tuple[Member, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        new_member = NewMember.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
