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


class ServerlessMetricUnits(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Element used to express the quantity. This can be an element of time, storage capacity, and the like.
    """


    class MetaOapg:
        enum_value_to_name = {
            "RPU": "RPU",
            "THOUSAND_RPU": "THOUSAND_RPU",
            "MILLION_RPU": "MILLION_RPU",
            "WPU": "WPU",
            "THOUSAND_WPU": "THOUSAND_WPU",
            "MILLION_WPU": "MILLION_WPU",
        }
    
    @schemas.classproperty
    def RPU(cls):
        return cls("RPU")
    
    @schemas.classproperty
    def THOUSAND_RPU(cls):
        return cls("THOUSAND_RPU")
    
    @schemas.classproperty
    def MILLION_RPU(cls):
        return cls("MILLION_RPU")
    
    @schemas.classproperty
    def WPU(cls):
        return cls("WPU")
    
    @schemas.classproperty
    def THOUSAND_WPU(cls):
        return cls("THOUSAND_WPU")
    
    @schemas.classproperty
    def MILLION_WPU(cls):
        return cls("MILLION_WPU")
