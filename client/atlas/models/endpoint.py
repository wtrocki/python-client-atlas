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
from atlas.models.aws_interface_endpoint import AWSInterfaceEndpoint
from atlas.models.azure_private_endpoint import AzurePrivateEndpoint
from atlas.models.gcp_endpoint_group import GCPEndpointGroup
from typing import Any, List
from pydantic import StrictStr, Field

ENDPOINT_ONE_OF_SCHEMAS = ["AWSInterfaceEndpoint", "AzurePrivateEndpoint", "GCPEndpointGroup"]

class Endpoint(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    # data type: AWSInterfaceEndpoint
    oneof_schema_1_validator: Optional[AWSInterfaceEndpoint] = None
    # data type: AzurePrivateEndpoint
    oneof_schema_2_validator: Optional[AzurePrivateEndpoint] = None
    # data type: GCPEndpointGroup
    oneof_schema_3_validator: Optional[GCPEndpointGroup] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(ENDPOINT_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = cls()
        error_messages = []
        match = 0
        # validate data type: AWSInterfaceEndpoint
        if type(v) is not AWSInterfaceEndpoint:
            error_messages.append(f"Error! Input type `{type(v)}` is not `AWSInterfaceEndpoint`")
        else:
            match += 1

        # validate data type: AzurePrivateEndpoint
        if type(v) is not AzurePrivateEndpoint:
            error_messages.append(f"Error! Input type `{type(v)}` is not `AzurePrivateEndpoint`")
        else:
            match += 1

        # validate data type: GCPEndpointGroup
        if type(v) is not GCPEndpointGroup:
            error_messages.append(f"Error! Input type `{type(v)}` is not `GCPEndpointGroup`")
        else:
            match += 1

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into Endpoint with oneOf schemas: AWSInterfaceEndpoint, AzurePrivateEndpoint, GCPEndpointGroup. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into Endpoint with oneOf schemas: AWSInterfaceEndpoint, AzurePrivateEndpoint, GCPEndpointGroup. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Endpoint:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Endpoint:
        """Returns the object represented by the json string"""
        instance = cls()
        error_messages = []
        match = 0

        # deserialize data into AWSInterfaceEndpoint
        try:
            instance.actual_instance = AWSInterfaceEndpoint.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into AzurePrivateEndpoint
        try:
            instance.actual_instance = AzurePrivateEndpoint.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into GCPEndpointGroup
        try:
            instance.actual_instance = GCPEndpointGroup.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into Endpoint with oneOf schemas: AWSInterfaceEndpoint, AzurePrivateEndpoint, GCPEndpointGroup. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into Endpoint with oneOf schemas: AWSInterfaceEndpoint, AzurePrivateEndpoint, GCPEndpointGroup. Details: " + ", ".join(error_messages))
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

