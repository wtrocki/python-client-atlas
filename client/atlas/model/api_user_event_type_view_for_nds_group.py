# coding: utf-8

"""
    MongoDB Atlas Administration API

    The MongoDB Atlas Administration API allows developers to manage all components in MongoDB Atlas. To learn more, review the [Administration API overview](https://www.mongodb.com/docs/atlas/api/atlas-admin-api/). This OpenAPI specification covers all of the collections with the exception of Alerts, Alert Configurations, and Events. Refer to the [legacy documentation](https://www.mongodb.com/docs/atlas/reference/api-resources/) for the specifications of these resources.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from atlas import schemas  # noqa: F401


class ApiUserEventTypeViewForNdsGroup(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Unique identifier of event type.
    """


    class MetaOapg:
        enum_value_to_name = {
            "API_KEY_CREATED": "CREATED",
            "API_KEY_DELETED": "DELETED",
            "API_KEY_ACCESS_LIST_ENTRY_ADDED": "ACCESS_LIST_ENTRY_ADDED",
            "API_KEY_ACCESS_LIST_ENTRY_DELETED": "ACCESS_LIST_ENTRY_DELETED",
            "API_KEY_ROLES_CHANGED": "ROLES_CHANGED",
            "API_KEY_DESCRIPTION_CHANGED": "DESCRIPTION_CHANGED",
            "API_KEY_ADDED_TO_GROUP": "ADDED_TO_GROUP",
            "API_KEY_REMOVED_FROM_GROUP": "REMOVED_FROM_GROUP",
        }
    
    @schemas.classproperty
    def CREATED(cls):
        return cls("API_KEY_CREATED")
    
    @schemas.classproperty
    def DELETED(cls):
        return cls("API_KEY_DELETED")
    
    @schemas.classproperty
    def ACCESS_LIST_ENTRY_ADDED(cls):
        return cls("API_KEY_ACCESS_LIST_ENTRY_ADDED")
    
    @schemas.classproperty
    def ACCESS_LIST_ENTRY_DELETED(cls):
        return cls("API_KEY_ACCESS_LIST_ENTRY_DELETED")
    
    @schemas.classproperty
    def ROLES_CHANGED(cls):
        return cls("API_KEY_ROLES_CHANGED")
    
    @schemas.classproperty
    def DESCRIPTION_CHANGED(cls):
        return cls("API_KEY_DESCRIPTION_CHANGED")
    
    @schemas.classproperty
    def ADDED_TO_GROUP(cls):
        return cls("API_KEY_ADDED_TO_GROUP")
    
    @schemas.classproperty
    def REMOVED_FROM_GROUP(cls):
        return cls("API_KEY_REMOVED_FROM_GROUP")
