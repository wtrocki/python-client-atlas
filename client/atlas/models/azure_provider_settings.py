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
from atlas.models.azure_auto_scaling import AzureAutoScaling

class AzureProviderSettings(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    auto_scaling: Optional[AzureAutoScaling] = Field(None, alias="autoScaling")
    disk_type_name: Optional[StrictStr] = Field(None, alias="diskTypeName", description="Disk type that corresponds to the host's root volume for Azure instances. If omitted, the default disk type for the selected **providerSettings.instanceSizeName** applies.")
    instance_size_name: Optional[StrictStr] = Field(None, alias="instanceSizeName", description="Cluster tier, with a default storage and memory capacity, that applies to all the data-bearing hosts in your cluster.")
    region_name: Optional[StrictStr] = Field(None, alias="regionName", description="Microsoft Azure Regions.")
    provider_name: StrictStr = Field(..., alias="providerName")
    __properties = ["autoScaling", "diskTypeName", "instanceSizeName", "regionName", "providerName"]

    @validator('disk_type_name')
    def disk_type_name_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('P2', 'P3', 'P4', 'P6', 'P10', 'P15', 'P20', 'P30', 'P40', 'P50'):
            raise ValueError("must validate the enum values ('P2', 'P3', 'P4', 'P6', 'P10', 'P15', 'P20', 'P30', 'P40', 'P50')")
        return v

    @validator('instance_size_name')
    def instance_size_name_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('M10', 'M20', 'M30', 'M40', 'M50', 'M60', 'M80', 'M90', 'M200', 'R40', 'R50', 'R60', 'R80', 'R200', 'R300', 'R400', 'M60_NVME', 'M80_NVME', 'M200_NVME', 'M300_NVME', 'M400_NVME', 'M600_NVME'):
            raise ValueError("must validate the enum values ('M10', 'M20', 'M30', 'M40', 'M50', 'M60', 'M80', 'M90', 'M200', 'R40', 'R50', 'R60', 'R80', 'R200', 'R300', 'R400', 'M60_NVME', 'M80_NVME', 'M200_NVME', 'M300_NVME', 'M400_NVME', 'M600_NVME')")
        return v

    @validator('region_name')
    def region_name_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('US_CENTRAL', 'US_EAST', 'US_EAST_2', 'US_NORTH_CENTRAL', 'US_WEST', 'US_SOUTH_CENTRAL', 'EUROPE_NORTH', 'EUROPE_WEST', 'US_WEST_CENTRAL', 'US_WEST_2', 'US_WEST_3', 'CANADA_EAST', 'CANADA_CENTRAL', 'BRAZIL_SOUTH', 'BRAZIL_SOUTHEAST', 'AUSTRALIA_CENTRAL', 'AUSTRALIA_CENTRAL_2', 'AUSTRALIA_EAST', 'AUSTRALIA_SOUTH_EAST', 'GERMANY_CENTRAL', 'GERMANY_NORTH_EAST', 'GERMANY_WEST_CENTRAL', 'GERMANY_NORTH', 'SWEDEN_CENTRAL', 'SWEDEN_SOUTH', 'SWITZERLAND_NORTH', 'SWITZERLAND_WEST', 'UK_SOUTH', 'UK_WEST', 'NORWAY_EAST', 'NORWAY_WEST', 'INDIA_CENTRAL', 'INDIA_SOUTH', 'INDIA_WEST', 'CHINA_EAST', 'CHINA_NORTH', 'ASIA_EAST', 'JAPAN_EAST', 'JAPAN_WEST', 'ASIA_SOUTH_EAST', 'KOREA_CENTRAL', 'KOREA_SOUTH', 'FRANCE_CENTRAL', 'FRANCE_SOUTH', 'SOUTH_AFRICA_NORTH', 'SOUTH_AFRICA_WEST', 'UAE_CENTRAL', 'UAE_NORTH'):
            raise ValueError("must validate the enum values ('US_CENTRAL', 'US_EAST', 'US_EAST_2', 'US_NORTH_CENTRAL', 'US_WEST', 'US_SOUTH_CENTRAL', 'EUROPE_NORTH', 'EUROPE_WEST', 'US_WEST_CENTRAL', 'US_WEST_2', 'US_WEST_3', 'CANADA_EAST', 'CANADA_CENTRAL', 'BRAZIL_SOUTH', 'BRAZIL_SOUTHEAST', 'AUSTRALIA_CENTRAL', 'AUSTRALIA_CENTRAL_2', 'AUSTRALIA_EAST', 'AUSTRALIA_SOUTH_EAST', 'GERMANY_CENTRAL', 'GERMANY_NORTH_EAST', 'GERMANY_WEST_CENTRAL', 'GERMANY_NORTH', 'SWEDEN_CENTRAL', 'SWEDEN_SOUTH', 'SWITZERLAND_NORTH', 'SWITZERLAND_WEST', 'UK_SOUTH', 'UK_WEST', 'NORWAY_EAST', 'NORWAY_WEST', 'INDIA_CENTRAL', 'INDIA_SOUTH', 'INDIA_WEST', 'CHINA_EAST', 'CHINA_NORTH', 'ASIA_EAST', 'JAPAN_EAST', 'JAPAN_WEST', 'ASIA_SOUTH_EAST', 'KOREA_CENTRAL', 'KOREA_SOUTH', 'FRANCE_CENTRAL', 'FRANCE_SOUTH', 'SOUTH_AFRICA_NORTH', 'SOUTH_AFRICA_WEST', 'UAE_CENTRAL', 'UAE_NORTH')")
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
    def from_json(cls, json_str: str) -> AzureProviderSettings:
        """Create an instance of AzureProviderSettings from a JSON string"""
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
    def from_dict(cls, obj: dict) -> AzureProviderSettings:
        """Create an instance of AzureProviderSettings from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AzureProviderSettings.parse_obj(obj)

        _obj = AzureProviderSettings.parse_obj({
            "auto_scaling": AzureAutoScaling.from_dict(obj.get("autoScaling")) if obj.get("autoScaling") is not None else None,
            "disk_type_name": obj.get("diskTypeName"),
            "instance_size_name": obj.get("instanceSizeName"),
            "region_name": obj.get("regionName"),
            "provider_name": obj.get("providerName")
        })
        return _obj

