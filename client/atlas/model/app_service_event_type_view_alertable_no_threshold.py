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


class AppServiceEventTypeViewAlertableNoThreshold(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Event type that triggers an alert.
    """


    class MetaOapg:
        enum_value_to_name = {
            "URL_CONFIRMATION": "URL_CONFIRMATION",
            "SUCCESSFUL_DEPLOY": "SUCCESSFUL_DEPLOY",
            "DEPLOYMENT_FAILURE": "DEPLOYMENT_FAILURE",
            "REQUEST_RATE_LIMIT": "REQUEST_RATE_LIMIT",
            "LOG_FORWARDER_FAILURE": "LOG_FORWARDER_FAILURE",
            "SYNC_FAILURE": "SYNC_FAILURE",
            "TRIGGER_FAILURE": "TRIGGER_FAILURE",
            "TRIGGER_AUTO_RESUMED": "TRIGGER_AUTO_RESUMED",
            "DEPLOYMENT_MODEL_CHANGE_SUCCESS": "DEPLOYMENT_MODEL_CHANGE_SUCCESS",
            "DEPLOYMENT_MODEL_CHANGE_FAILURE": "DEPLOYMENT_MODEL_CHANGE_FAILURE",
        }
    
    @schemas.classproperty
    def URL_CONFIRMATION(cls):
        return cls("URL_CONFIRMATION")
    
    @schemas.classproperty
    def SUCCESSFUL_DEPLOY(cls):
        return cls("SUCCESSFUL_DEPLOY")
    
    @schemas.classproperty
    def DEPLOYMENT_FAILURE(cls):
        return cls("DEPLOYMENT_FAILURE")
    
    @schemas.classproperty
    def REQUEST_RATE_LIMIT(cls):
        return cls("REQUEST_RATE_LIMIT")
    
    @schemas.classproperty
    def LOG_FORWARDER_FAILURE(cls):
        return cls("LOG_FORWARDER_FAILURE")
    
    @schemas.classproperty
    def SYNC_FAILURE(cls):
        return cls("SYNC_FAILURE")
    
    @schemas.classproperty
    def TRIGGER_FAILURE(cls):
        return cls("TRIGGER_FAILURE")
    
    @schemas.classproperty
    def TRIGGER_AUTO_RESUMED(cls):
        return cls("TRIGGER_AUTO_RESUMED")
    
    @schemas.classproperty
    def DEPLOYMENT_MODEL_CHANGE_SUCCESS(cls):
        return cls("DEPLOYMENT_MODEL_CHANGE_SUCCESS")
    
    @schemas.classproperty
    def DEPLOYMENT_MODEL_CHANGE_FAILURE(cls):
        return cls("DEPLOYMENT_MODEL_CHANGE_FAILURE")