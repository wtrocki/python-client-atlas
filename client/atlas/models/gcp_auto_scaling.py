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
from pydantic import BaseModel
from atlas.models.gcp_compute_auto_scaling import GCPComputeAutoScaling

class GCPAutoScaling(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    compute: Optional[GCPComputeAutoScaling] = None
    __properties = ["compute"]

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
    def from_json(cls, json_str: str) -> GCPAutoScaling:
        """Create an instance of GCPAutoScaling from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of compute
        if self.compute:
            _dict['compute'] = self.compute.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GCPAutoScaling:
        """Create an instance of GCPAutoScaling from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return GCPAutoScaling.parse_obj(obj)

        _obj = GCPAutoScaling.parse_obj({
            "compute": GCPComputeAutoScaling.from_dict(obj.get("compute")) if obj.get("compute") is not None else None
        })
        return _obj

