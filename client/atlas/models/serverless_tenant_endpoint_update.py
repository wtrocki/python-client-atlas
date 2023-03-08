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
from atlas.models.serverless_aws_tenant_endpoint_update import ServerlessAWSTenantEndpointUpdate
from atlas.models.serverless_azure_tenant_endpoint_update import ServerlessAzureTenantEndpointUpdate
from typing import Any, List
from pydantic import StrictStr, Field

SERVERLESSTENANTENDPOINTUPDATE_ONE_OF_SCHEMAS = ["ServerlessAWSTenantEndpointUpdate", "ServerlessAzureTenantEndpointUpdate"]

class ServerlessTenantEndpointUpdate(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    # data type: ServerlessAWSTenantEndpointUpdate
    oneof_schema_1_validator: Optional[ServerlessAWSTenantEndpointUpdate] = None
    # data type: ServerlessAzureTenantEndpointUpdate
    oneof_schema_2_validator: Optional[ServerlessAzureTenantEndpointUpdate] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(SERVERLESSTENANTENDPOINTUPDATE_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    discriminator_value_class_map = {
    }

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = cls()
        error_messages = []
        match = 0
        # validate data type: ServerlessAWSTenantEndpointUpdate
        if type(v) is not ServerlessAWSTenantEndpointUpdate:
            error_messages.append(f"Error! Input type `{type(v)}` is not `ServerlessAWSTenantEndpointUpdate`")
        else:
            match += 1

        # validate data type: ServerlessAzureTenantEndpointUpdate
        if type(v) is not ServerlessAzureTenantEndpointUpdate:
            error_messages.append(f"Error! Input type `{type(v)}` is not `ServerlessAzureTenantEndpointUpdate`")
        else:
            match += 1

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ServerlessTenantEndpointUpdate with oneOf schemas: ServerlessAWSTenantEndpointUpdate, ServerlessAzureTenantEndpointUpdate. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ServerlessTenantEndpointUpdate with oneOf schemas: ServerlessAWSTenantEndpointUpdate, ServerlessAzureTenantEndpointUpdate. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> ServerlessTenantEndpointUpdate:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> ServerlessTenantEndpointUpdate:
        """Returns the object represented by the json string"""
        instance = cls()
        error_messages = []
        match = 0

        # use oneOf discriminator to lookup the data type
        _data_type = json.loads(json_str).get("providerName")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `providerName` in the input.")

        # check if data type is `ServerlessAWSTenantEndpointUpdate`
        if _data_type == "AWS":
            instance.actual_instance = ServerlessAWSTenantEndpointUpdate.from_json(json_str)
            return instance

        # check if data type is `ServerlessAzureTenantEndpointUpdate`
        if _data_type == "AZURE":
            instance.actual_instance = ServerlessAzureTenantEndpointUpdate.from_json(json_str)
            return instance

        # check if data type is `ServerlessAWSTenantEndpointUpdate`
        if _data_type == "ServerlessAWSTenantEndpointUpdate":
            instance.actual_instance = ServerlessAWSTenantEndpointUpdate.from_json(json_str)
            return instance

        # check if data type is `ServerlessAzureTenantEndpointUpdate`
        if _data_type == "ServerlessAzureTenantEndpointUpdate":
            instance.actual_instance = ServerlessAzureTenantEndpointUpdate.from_json(json_str)
            return instance

        # deserialize data into ServerlessAWSTenantEndpointUpdate
        try:
            instance.actual_instance = ServerlessAWSTenantEndpointUpdate.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into ServerlessAzureTenantEndpointUpdate
        try:
            instance.actual_instance = ServerlessAzureTenantEndpointUpdate.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ServerlessTenantEndpointUpdate with oneOf schemas: ServerlessAWSTenantEndpointUpdate, ServerlessAzureTenantEndpointUpdate. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ServerlessTenantEndpointUpdate with oneOf schemas: ServerlessAWSTenantEndpointUpdate, ServerlessAzureTenantEndpointUpdate. Details: " + ", ".join(error_messages))
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

