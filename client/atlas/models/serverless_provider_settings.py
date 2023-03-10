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

class ServerlessProviderSettings(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    backing_provider_name: StrictStr = Field(..., alias="backingProviderName", description="Cloud service provider on which MongoDB Cloud provisioned the serverless instance.")
    provider_name: Optional[StrictStr] = Field('SERVERLESS', alias="providerName", description="Human-readable label that identifies the cloud service provider.")
    region_name: StrictStr = Field(..., alias="regionName", description="Human-readable label that identifies the geographic location of your MongoDB serverless instance. The region you choose can affect network latency for clients accessing your databases. For a complete list of region names, see [AWS](https://docs.atlas.mongodb.com/reference/amazon-aws/#std-label-amazon-aws), [GCP](https://docs.atlas.mongodb.com/reference/google-gcp/), and [Azure](https://docs.atlas.mongodb.com/reference/microsoft-azure/).")
    __properties = ["backingProviderName", "providerName", "regionName"]

    @validator('backing_provider_name')
    def backing_provider_name_validate_enum(cls, v):
        if v not in ('AWS', 'AZURE', 'GCP'):
            raise ValueError("must validate the enum values ('AWS', 'AZURE', 'GCP')")
        return v

    @validator('provider_name')
    def provider_name_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('SERVERLESS'):
            raise ValueError("must validate the enum values ('SERVERLESS')")
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
    def from_json(cls, json_str: str) -> ServerlessProviderSettings:
        """Create an instance of ServerlessProviderSettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ServerlessProviderSettings:
        """Create an instance of ServerlessProviderSettings from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ServerlessProviderSettings.parse_obj(obj)

        _obj = ServerlessProviderSettings.parse_obj({
            "backing_provider_name": obj.get("backingProviderName"),
            "provider_name": obj.get("providerName") if obj.get("providerName") is not None else 'SERVERLESS',
            "region_name": obj.get("regionName")
        })
        return _obj

