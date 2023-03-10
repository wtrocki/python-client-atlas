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
from atlas.models.gcp_auto_scaling import GCPAutoScaling

class GCPProviderSettings(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    auto_scaling: Optional[GCPAutoScaling] = Field(None, alias="autoScaling")
    instance_size_name: Optional[StrictStr] = Field(None, alias="instanceSizeName", description="Cluster tier, with a default storage and memory capacity, that applies to all the data-bearing hosts in your cluster.")
    region_name: Optional[StrictStr] = Field(None, alias="regionName", description="Google Compute Regions.")
    provider_name: StrictStr = Field(..., alias="providerName")
    __properties = ["autoScaling", "instanceSizeName", "regionName", "providerName"]

    @validator('instance_size_name')
    def instance_size_name_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('M10', 'M20', 'M30', 'M40', 'M50', 'M60', 'M80', 'M140', 'M200', 'M250', 'M300', 'M400', 'R40', 'R50', 'R60', 'R80', 'R200', 'R300', 'R400', 'R600'):
            raise ValueError("must validate the enum values ('M10', 'M20', 'M30', 'M40', 'M50', 'M60', 'M80', 'M140', 'M200', 'M250', 'M300', 'M400', 'R40', 'R50', 'R60', 'R80', 'R200', 'R300', 'R400', 'R600')")
        return v

    @validator('region_name')
    def region_name_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('EASTERN_US', 'US_EAST_4', 'US_WEST_2', 'US_WEST_3', 'US_WEST_4', 'CENTRAL_US', 'WESTERN_US', 'NORTH_AMERICA_NORTHEAST_1', 'NORTH_AMERICA_NORTHEAST_2', 'SOUTH_AMERICA_EAST_1', 'SOUTH_AMERICA_WEST_1', 'WESTERN_EUROPE', 'EUROPE_NORTH_1', 'EUROPE_WEST_2', 'EUROPE_WEST_3', 'EUROPE_WEST_4', 'EUROPE_WEST_6', 'EUROPE_WEST_8', 'EUROPE_WEST_9', 'EUROPE_SOUTHWEST_1', 'EUROPE_CENTRAL_2', 'AUSTRALIA_SOUTHEAST_1', 'AUSTRALIA_SOUTHEAST_2', 'EASTERN_ASIA_PACIFIC', 'NORTHEASTERN_ASIA_PACIFIC', 'SOUTHEASTERN_ASIA_PACIFIC', 'ASIA_EAST_2', 'ASIA_NORTHEAST_2', 'ASIA_NORTHEAST_3', 'ASIA_SOUTH_1', 'ASIA_SOUTH_2', 'ASIA_SOUTHEAST_2'):
            raise ValueError("must validate the enum values ('EASTERN_US', 'US_EAST_4', 'US_WEST_2', 'US_WEST_3', 'US_WEST_4', 'CENTRAL_US', 'WESTERN_US', 'NORTH_AMERICA_NORTHEAST_1', 'NORTH_AMERICA_NORTHEAST_2', 'SOUTH_AMERICA_EAST_1', 'SOUTH_AMERICA_WEST_1', 'WESTERN_EUROPE', 'EUROPE_NORTH_1', 'EUROPE_WEST_2', 'EUROPE_WEST_3', 'EUROPE_WEST_4', 'EUROPE_WEST_6', 'EUROPE_WEST_8', 'EUROPE_WEST_9', 'EUROPE_SOUTHWEST_1', 'EUROPE_CENTRAL_2', 'AUSTRALIA_SOUTHEAST_1', 'AUSTRALIA_SOUTHEAST_2', 'EASTERN_ASIA_PACIFIC', 'NORTHEASTERN_ASIA_PACIFIC', 'SOUTHEASTERN_ASIA_PACIFIC', 'ASIA_EAST_2', 'ASIA_NORTHEAST_2', 'ASIA_NORTHEAST_3', 'ASIA_SOUTH_1', 'ASIA_SOUTH_2', 'ASIA_SOUTHEAST_2')")
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
    def from_json(cls, json_str: str) -> GCPProviderSettings:
        """Create an instance of GCPProviderSettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of auto_scaling
        if self.auto_scaling:
            _dict['autoScaling'] = self.auto_scaling.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GCPProviderSettings:
        """Create an instance of GCPProviderSettings from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return GCPProviderSettings.parse_obj(obj)

        _obj = GCPProviderSettings.parse_obj({
            "auto_scaling": GCPAutoScaling.from_dict(obj.get("autoScaling")) if obj.get("autoScaling") is not None else None,
            "instance_size_name": obj.get("instanceSizeName"),
            "region_name": obj.get("regionName"),
            "provider_name": obj.get("providerName")
        })
        return _obj

