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
from atlas.models.aws_private_link_connection import AWSPrivateLinkConnection
from atlas.models.azure_private_link_connection import AzurePrivateLinkConnection
from atlas.models.gcp_endpoint_service import GCPEndpointService
from typing import Any, List
from pydantic import StrictStr, Field

ENDPOINTSERVICE_ONE_OF_SCHEMAS = ["AWSPrivateLinkConnection", "AzurePrivateLinkConnection", "GCPEndpointService"]

class EndpointService(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    # data type: AWSPrivateLinkConnection
    oneof_schema_1_validator: Optional[AWSPrivateLinkConnection] = None
    # data type: AzurePrivateLinkConnection
    oneof_schema_2_validator: Optional[AzurePrivateLinkConnection] = None
    # data type: GCPEndpointService
    oneof_schema_3_validator: Optional[GCPEndpointService] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(ENDPOINTSERVICE_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = cls()
        error_messages = []
        match = 0
        # validate data type: AWSPrivateLinkConnection
        if type(v) is not AWSPrivateLinkConnection:
            error_messages.append(f"Error! Input type `{type(v)}` is not `AWSPrivateLinkConnection`")
        else:
            match += 1

        # validate data type: AzurePrivateLinkConnection
        if type(v) is not AzurePrivateLinkConnection:
            error_messages.append(f"Error! Input type `{type(v)}` is not `AzurePrivateLinkConnection`")
        else:
            match += 1

        # validate data type: GCPEndpointService
        if type(v) is not GCPEndpointService:
            error_messages.append(f"Error! Input type `{type(v)}` is not `GCPEndpointService`")
        else:
            match += 1

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into EndpointService with oneOf schemas: AWSPrivateLinkConnection, AzurePrivateLinkConnection, GCPEndpointService. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into EndpointService with oneOf schemas: AWSPrivateLinkConnection, AzurePrivateLinkConnection, GCPEndpointService. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> EndpointService:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> EndpointService:
        """Returns the object represented by the json string"""
        instance = cls()
        error_messages = []
        match = 0

        # deserialize data into AWSPrivateLinkConnection
        try:
            instance.actual_instance = AWSPrivateLinkConnection.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into AzurePrivateLinkConnection
        try:
            instance.actual_instance = AzurePrivateLinkConnection.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into GCPEndpointService
        try:
            instance.actual_instance = GCPEndpointService.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into EndpointService with oneOf schemas: AWSPrivateLinkConnection, AzurePrivateLinkConnection, GCPEndpointService. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into EndpointService with oneOf schemas: AWSPrivateLinkConnection, AzurePrivateLinkConnection, GCPEndpointService. Details: " + ", ".join(error_messages))
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

