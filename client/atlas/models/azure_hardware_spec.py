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
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator

class AzureHardwareSpec(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    instance_size: Optional[StrictStr] = Field(None, alias="instanceSize", description="Hardware specification for the instance sizes in this region. Each instance size has a default storage and memory capacity. The instance size you select applies to all the data-bearing hosts in your instance size.")
    node_count: Optional[StrictInt] = Field(None, alias="nodeCount", description="Number of read-only nodes for MongoDB Cloud to deploy to the region. Read-only nodes can never become the primary, but can enable local reads.")
    __properties = ["instanceSize", "nodeCount"]

    @validator('instance_size')
    def instance_size_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('M10', 'M20', 'M30', 'M40', 'M50', 'M60', 'M80', 'M90', 'M200', 'R40', 'R50', 'R60', 'R80', 'R200', 'R300', 'R400', 'M60_NVME', 'M80_NVME', 'M200_NVME', 'M300_NVME', 'M400_NVME', 'M600_NVME'):
            raise ValueError("must validate the enum values ('M10', 'M20', 'M30', 'M40', 'M50', 'M60', 'M80', 'M90', 'M200', 'R40', 'R50', 'R60', 'R80', 'R200', 'R300', 'R400', 'M60_NVME', 'M80_NVME', 'M200_NVME', 'M300_NVME', 'M400_NVME', 'M600_NVME')")
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
    def from_json(cls, json_str: str) -> AzureHardwareSpec:
        """Create an instance of AzureHardwareSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AzureHardwareSpec:
        """Create an instance of AzureHardwareSpec from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AzureHardwareSpec.parse_obj(obj)

        _obj = AzureHardwareSpec.parse_obj({
            "instance_size": obj.get("instanceSize"),
            "node_count": obj.get("nodeCount")
        })
        return _obj

