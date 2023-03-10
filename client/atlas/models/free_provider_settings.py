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
from atlas.models.free_auto_scaling import FreeAutoScaling

class FreeProviderSettings(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    auto_scaling: Optional[FreeAutoScaling] = Field(None, alias="autoScaling")
    backing_provider_name: Optional[StrictStr] = Field(None, alias="backingProviderName", description="Cloud service provider on which MongoDB Cloud provisioned the multi-tenant host. The resource returns this parameter when **providerSettings.providerName** is `TENANT` and **providerSetting.instanceSizeName** is `M2` or `M5`.")
    instance_size_name: Optional[StrictStr] = Field(None, alias="instanceSizeName", description="Cluster tier, with a default storage and memory capacity, that applies to all the data-bearing hosts in your cluster. You must set **providerSettings.providerName** to `TENANT` and specify the cloud service provider in **providerSettings.backingProviderName**.")
    region_name: Optional[StrictStr] = Field(None, alias="regionName", description="Human-readable label that identifies the geographic location of your MongoDB cluster. The region you choose can affect network latency for clients accessing your databases. For a complete list of region names, see [AWS](https://docs.atlas.mongodb.com/reference/amazon-aws/#std-label-amazon-aws), [GCP](https://docs.atlas.mongodb.com/reference/google-gcp/), and [Azure](https://docs.atlas.mongodb.com/reference/microsoft-azure/). For multi-region clusters, see **replicationSpec.{region}**.")
    provider_name: StrictStr = Field(..., alias="providerName")
    __properties = ["autoScaling", "backingProviderName", "instanceSizeName", "regionName", "providerName"]

    @validator('backing_provider_name')
    def backing_provider_name_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('AWS', 'GCP', 'AZURE', 'TENANT', 'SERVERLESS'):
            raise ValueError("must validate the enum values ('AWS', 'GCP', 'AZURE', 'TENANT', 'SERVERLESS')")
        return v

    @validator('instance_size_name')
    def instance_size_name_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('M0', 'M2', 'M5'):
            raise ValueError("must validate the enum values ('M0', 'M2', 'M5')")
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
    def from_json(cls, json_str: str) -> FreeProviderSettings:
        """Create an instance of FreeProviderSettings from a JSON string"""
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
    def from_dict(cls, obj: dict) -> FreeProviderSettings:
        """Create an instance of FreeProviderSettings from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return FreeProviderSettings.parse_obj(obj)

        _obj = FreeProviderSettings.parse_obj({
            "auto_scaling": FreeAutoScaling.from_dict(obj.get("autoScaling")) if obj.get("autoScaling") is not None else None,
            "backing_provider_name": obj.get("backingProviderName"),
            "instance_size_name": obj.get("instanceSizeName"),
            "region_name": obj.get("regionName"),
            "provider_name": obj.get("providerName")
        })
        return _obj

