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


class ReplicaSetEventTypeViewForNdsGroup(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Unique identifier of event type.
    """
    
    @schemas.classproperty
    def PRIMARY_ELECTED(cls):
        return cls("PRIMARY_ELECTED")
    
    @schemas.classproperty
    def REPLICATION_OPLOG_WINDOW_HEALTHY(cls):
        return cls("REPLICATION_OPLOG_WINDOW_HEALTHY")
    
    @schemas.classproperty
    def REPLICATION_OPLOG_WINDOW_RUNNING_OUT(cls):
        return cls("REPLICATION_OPLOG_WINDOW_RUNNING_OUT")
    
    @schemas.classproperty
    def ONE_PRIMARY(cls):
        return cls("ONE_PRIMARY")
    
    @schemas.classproperty
    def NO_PRIMARY(cls):
        return cls("NO_PRIMARY")
    
    @schemas.classproperty
    def TOO_MANY_ELECTIONS(cls):
        return cls("TOO_MANY_ELECTIONS")
