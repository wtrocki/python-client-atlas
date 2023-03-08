# coding: utf-8

"""
    MongoDB Atlas Administration API

    The MongoDB Atlas Administration API allows developers to manage all components in MongoDB Atlas. To learn more, review the [Administration API overview](https://www.mongodb.com/docs/atlas/api/atlas-admin-api/). This OpenAPI specification covers all of the collections with the exception of Alerts, Alert Configurations, and Events. Refer to the [legacy documentation](https://www.mongodb.com/docs/atlas/reference/api-resources/) for the specifications of these resources.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from atlas.models.aws_region_config import AWSRegionConfig
from atlas.models.azure_region_config import AzureRegionConfig
from atlas.models.gcp_region_config import GCPRegionConfig
from atlas.models.tenant_region_config import TenantRegionConfig
from typing import Any, List
from pydantic import StrictStr, Field

REGIONCONFIG_ONE_OF_SCHEMAS = ["AWSRegionConfig", "AzureRegionConfig", "GCPRegionConfig", "TenantRegionConfig"]

class RegionConfig(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    # data type: AWSRegionConfig
    oneof_schema_1_validator: Optional[AWSRegionConfig] = None
    # data type: AzureRegionConfig
    oneof_schema_2_validator: Optional[AzureRegionConfig] = None
    # data type: GCPRegionConfig
    oneof_schema_3_validator: Optional[GCPRegionConfig] = None
    # data type: TenantRegionConfig
    oneof_schema_4_validator: Optional[TenantRegionConfig] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(REGIONCONFIG_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    discriminator_value_class_map = {
    }

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = cls()
        error_messages = []
        match = 0
        # validate data type: AWSRegionConfig
        if type(v) is not AWSRegionConfig:
            error_messages.append(f"Error! Input type `{type(v)}` is not `AWSRegionConfig`")
        else:
            match += 1

        # validate data type: AzureRegionConfig
        if type(v) is not AzureRegionConfig:
            error_messages.append(f"Error! Input type `{type(v)}` is not `AzureRegionConfig`")
        else:
            match += 1

        # validate data type: GCPRegionConfig
        if type(v) is not GCPRegionConfig:
            error_messages.append(f"Error! Input type `{type(v)}` is not `GCPRegionConfig`")
        else:
            match += 1

        # validate data type: TenantRegionConfig
        if type(v) is not TenantRegionConfig:
            error_messages.append(f"Error! Input type `{type(v)}` is not `TenantRegionConfig`")
        else:
            match += 1

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into RegionConfig with oneOf schemas: AWSRegionConfig, AzureRegionConfig, GCPRegionConfig, TenantRegionConfig. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into RegionConfig with oneOf schemas: AWSRegionConfig, AzureRegionConfig, GCPRegionConfig, TenantRegionConfig. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> RegionConfig:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> RegionConfig:
        """Returns the object represented by the json string"""
        instance = cls()
        error_messages = []
        match = 0

        # use oneOf discriminator to lookup the data type
        _data_type = json.loads(json_str).get("providerName")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `providerName` in the input.")

        # check if data type is `AWSRegionConfig`
        if _data_type == "AWS":
            instance.actual_instance = AWSRegionConfig.from_json(json_str)
            return instance

        # check if data type is `AWSRegionConfig`
        if _data_type == "AWSRegionConfig":
            instance.actual_instance = AWSRegionConfig.from_json(json_str)
            return instance

        # check if data type is `AzureRegionConfig`
        if _data_type == "AZURE":
            instance.actual_instance = AzureRegionConfig.from_json(json_str)
            return instance

        # check if data type is `AzureRegionConfig`
        if _data_type == "AzureRegionConfig":
            instance.actual_instance = AzureRegionConfig.from_json(json_str)
            return instance

        # check if data type is `GCPRegionConfig`
        if _data_type == "GCP":
            instance.actual_instance = GCPRegionConfig.from_json(json_str)
            return instance

        # check if data type is `GCPRegionConfig`
        if _data_type == "GCPRegionConfig":
            instance.actual_instance = GCPRegionConfig.from_json(json_str)
            return instance

        # check if data type is `TenantRegionConfig`
        if _data_type == "TENANT":
            instance.actual_instance = TenantRegionConfig.from_json(json_str)
            return instance

        # check if data type is `TenantRegionConfig`
        if _data_type == "TenantRegionConfig":
            instance.actual_instance = TenantRegionConfig.from_json(json_str)
            return instance

        # deserialize data into AWSRegionConfig
        try:
            instance.actual_instance = AWSRegionConfig.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into AzureRegionConfig
        try:
            instance.actual_instance = AzureRegionConfig.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into GCPRegionConfig
        try:
            instance.actual_instance = GCPRegionConfig.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into TenantRegionConfig
        try:
            instance.actual_instance = TenantRegionConfig.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into RegionConfig with oneOf schemas: AWSRegionConfig, AzureRegionConfig, GCPRegionConfig, TenantRegionConfig. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into RegionConfig with oneOf schemas: AWSRegionConfig, AzureRegionConfig, GCPRegionConfig, TenantRegionConfig. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_json()
        else:
            return "null"

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_dict()
        else:
            return dict()

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())
