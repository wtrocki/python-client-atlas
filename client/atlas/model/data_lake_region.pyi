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


class DataLakeRegion(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Atlas Data Lake Regions.
    """
    
    @schemas.classproperty
    def SYDNEY_AUS(cls):
        return cls("SYDNEY_AUS")
    
    @schemas.classproperty
    def MUMBAI_IND(cls):
        return cls("MUMBAI_IND")
    
    @schemas.classproperty
    def FRANKFURT_DEU(cls):
        return cls("FRANKFURT_DEU")
    
    @schemas.classproperty
    def DUBLIN_IRL(cls):
        return cls("DUBLIN_IRL")
    
    @schemas.classproperty
    def LONDON_GBR(cls):
        return cls("LONDON_GBR")
    
    @schemas.classproperty
    def VIRGINIA_USA(cls):
        return cls("VIRGINIA_USA")
    
    @schemas.classproperty
    def OREGON_USA(cls):
        return cls("OREGON_USA")
    
    @schemas.classproperty
    def SAOPAULO_BRA(cls):
        return cls("SAOPAULO_BRA")
    
    @schemas.classproperty
    def SINGAPORE_SGP(cls):
        return cls("SINGAPORE_SGP")
