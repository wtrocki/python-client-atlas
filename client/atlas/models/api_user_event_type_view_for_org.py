# coding: utf-8

"""
    MongoDB Atlas Administration API

    The MongoDB Atlas Administration API allows developers to manage all components in MongoDB Atlas. To learn more, review the [Administration API overview](https://www.mongodb.com/docs/atlas/api/atlas-admin-api/). This OpenAPI specification covers all of the collections with the exception of Alerts, Alert Configurations, and Events. Refer to the [legacy documentation](https://www.mongodb.com/docs/atlas/reference/api-resources/) for the specifications of these resources.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


from inspect import getfullargspec
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class ApiUserEventTypeViewForOrg(str, Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """

    CREATED = 'API_KEY_CREATED'
    DELETED = 'API_KEY_DELETED'
    ACCESS_LIST_ENTRY_ADDED = 'API_KEY_ACCESS_LIST_ENTRY_ADDED'
    ACCESS_LIST_ENTRY_DELETED = 'API_KEY_ACCESS_LIST_ENTRY_DELETED'
    ROLES_CHANGED = 'API_KEY_ROLES_CHANGED'
    DESCRIPTION_CHANGED = 'API_KEY_DESCRIPTION_CHANGED'
    ADDED_TO_GROUP = 'API_KEY_ADDED_TO_GROUP'
    REMOVED_FROM_GROUP = 'API_KEY_REMOVED_FROM_GROUP'

