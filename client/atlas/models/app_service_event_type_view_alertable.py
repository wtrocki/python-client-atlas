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





class AppServiceEventTypeViewAlertable(str, Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """

    URL_CONFIRMATION = 'URL_CONFIRMATION'
    SUCCESSFUL_DEPLOY = 'SUCCESSFUL_DEPLOY'
    DEPLOYMENT_FAILURE = 'DEPLOYMENT_FAILURE'
    DEPLOYMENT_MODEL_CHANGE_SUCCESS = 'DEPLOYMENT_MODEL_CHANGE_SUCCESS'
    DEPLOYMENT_MODEL_CHANGE_FAILURE = 'DEPLOYMENT_MODEL_CHANGE_FAILURE'
    REQUEST_RATE_LIMIT = 'REQUEST_RATE_LIMIT'
    LOG_FORWARDER_FAILURE = 'LOG_FORWARDER_FAILURE'
    OUTSIDE_REALM_METRIC_THRESHOLD = 'OUTSIDE_REALM_METRIC_THRESHOLD'
    SYNC_FAILURE = 'SYNC_FAILURE'
    TRIGGER_FAILURE = 'TRIGGER_FAILURE'
    TRIGGER_AUTO_RESUMED = 'TRIGGER_AUTO_RESUMED'

