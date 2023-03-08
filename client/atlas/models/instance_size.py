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





class InstanceSize(str, Enum):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    allowed enum values
    """

    M10 = 'M10'
    M20 = 'M20'
    M30 = 'M30'
    M40 = 'M40'
    M50 = 'M50'
    M60 = 'M60'
    M80 = 'M80'
    M100 = 'M100'
    M140 = 'M140'
    M200 = 'M200'
    M300 = 'M300'
    R40 = 'R40'
    R50 = 'R50'
    R60 = 'R60'
    R80 = 'R80'
    R200 = 'R200'
    R300 = 'R300'
    R400 = 'R400'
    R700 = 'R700'
    M40_NVME = 'M40_NVME'
    M50_NVME = 'M50_NVME'
    M60_NVME = 'M60_NVME'
    M80_NVME = 'M80_NVME'
    M200_NVME = 'M200_NVME'
    M400_NVME = 'M400_NVME'
    M90 = 'M90'
    M300_NVME = 'M300_NVME'
    M600_NVME = 'M600_NVME'
    M250 = 'M250'
    M400 = 'M400'
    R600 = 'R600'

