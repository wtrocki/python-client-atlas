# coding: utf-8

"""
    MongoDB Atlas Administration API

    The MongoDB Atlas Administration API allows developers to manage all components in MongoDB Atlas. To learn more, review the [Administration API overview](https://www.mongodb.com/docs/atlas/api/atlas-admin-api/). This OpenAPI specification covers all of the collections with the exception of Alerts, Alert Configurations, and Events. Refer to the [legacy documentation](https://www.mongodb.com/docs/atlas/reference/api-resources/) for the specifications of these resources.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator

class AWSComputeAutoScaling(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    max_instance_size: Optional[StrictStr] = Field(None, alias="maxInstanceSize", description="Maximum instance size to which your cluster can automatically scale.")
    min_instance_size: Optional[StrictStr] = Field(None, alias="minInstanceSize", description="Minimum instance size to which your cluster can automatically scale.")
    __properties = ["maxInstanceSize", "minInstanceSize"]

    @validator('max_instance_size')
    def max_instance_size_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('M10', 'M20', 'M30', 'M40', 'M50', 'M60', 'M80', 'M100', 'M140', 'M200', 'M300', 'R40', 'R50', 'R60', 'R80', 'R200', 'R300', 'R400', 'R700', 'M40_NVME', 'M50_NVME', 'M60_NVME', 'M80_NVME', 'M200_NVME', 'M400_NVME'):
            raise ValueError("must validate the enum values ('M10', 'M20', 'M30', 'M40', 'M50', 'M60', 'M80', 'M100', 'M140', 'M200', 'M300', 'R40', 'R50', 'R60', 'R80', 'R200', 'R300', 'R400', 'R700', 'M40_NVME', 'M50_NVME', 'M60_NVME', 'M80_NVME', 'M200_NVME', 'M400_NVME')")
        return v

    @validator('min_instance_size')
    def min_instance_size_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('M10', 'M20', 'M30', 'M40', 'M50', 'M60', 'M80', 'M100', 'M140', 'M200', 'M300', 'R40', 'R50', 'R60', 'R80', 'R200', 'R300', 'R400', 'R700', 'M40_NVME', 'M50_NVME', 'M60_NVME', 'M80_NVME', 'M200_NVME', 'M400_NVME'):
            raise ValueError("must validate the enum values ('M10', 'M20', 'M30', 'M40', 'M50', 'M60', 'M80', 'M100', 'M140', 'M200', 'M300', 'R40', 'R50', 'R60', 'R80', 'R200', 'R300', 'R400', 'R700', 'M40_NVME', 'M50_NVME', 'M60_NVME', 'M80_NVME', 'M200_NVME', 'M400_NVME')")
        return v

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> AWSComputeAutoScaling:
        """Create an instance of AWSComputeAutoScaling from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AWSComputeAutoScaling:
        """Create an instance of AWSComputeAutoScaling from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AWSComputeAutoScaling.parse_obj(obj)

        _obj = AWSComputeAutoScaling.parse_obj({
            "max_instance_size": obj.get("maxInstanceSize"),
            "min_instance_size": obj.get("minInstanceSize")
        })
        return _obj

