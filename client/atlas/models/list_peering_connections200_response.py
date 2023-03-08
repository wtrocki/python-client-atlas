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
from atlas.models.paginated_aws_peer_vpc_view import PaginatedAWSPeerVpcView
from atlas.models.paginated_azure_peer_network_view import PaginatedAzurePeerNetworkView
from atlas.models.paginated_gcp_peer_vpc_view import PaginatedGCPPeerVpcView
from typing import Any, List
from pydantic import StrictStr, Field

LISTPEERINGCONNECTIONS200RESPONSE_ONE_OF_SCHEMAS = ["PaginatedAWSPeerVpcView", "PaginatedAzurePeerNetworkView", "PaginatedGCPPeerVpcView"]

class ListPeeringConnections200Response(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    # data type: PaginatedAWSPeerVpcView
    oneof_schema_1_validator: Optional[PaginatedAWSPeerVpcView] = None
    # data type: PaginatedAzurePeerNetworkView
    oneof_schema_2_validator: Optional[PaginatedAzurePeerNetworkView] = None
    # data type: PaginatedGCPPeerVpcView
    oneof_schema_3_validator: Optional[PaginatedGCPPeerVpcView] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(LISTPEERINGCONNECTIONS200RESPONSE_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = cls()
        error_messages = []
        match = 0
        # validate data type: PaginatedAWSPeerVpcView
        if type(v) is not PaginatedAWSPeerVpcView:
            error_messages.append(f"Error! Input type `{type(v)}` is not `PaginatedAWSPeerVpcView`")
        else:
            match += 1

        # validate data type: PaginatedAzurePeerNetworkView
        if type(v) is not PaginatedAzurePeerNetworkView:
            error_messages.append(f"Error! Input type `{type(v)}` is not `PaginatedAzurePeerNetworkView`")
        else:
            match += 1

        # validate data type: PaginatedGCPPeerVpcView
        if type(v) is not PaginatedGCPPeerVpcView:
            error_messages.append(f"Error! Input type `{type(v)}` is not `PaginatedGCPPeerVpcView`")
        else:
            match += 1

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ListPeeringConnections200Response with oneOf schemas: PaginatedAWSPeerVpcView, PaginatedAzurePeerNetworkView, PaginatedGCPPeerVpcView. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ListPeeringConnections200Response with oneOf schemas: PaginatedAWSPeerVpcView, PaginatedAzurePeerNetworkView, PaginatedGCPPeerVpcView. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> ListPeeringConnections200Response:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> ListPeeringConnections200Response:
        """Returns the object represented by the json string"""
        instance = cls()
        error_messages = []
        match = 0

        # deserialize data into PaginatedAWSPeerVpcView
        try:
            instance.actual_instance = PaginatedAWSPeerVpcView.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into PaginatedAzurePeerNetworkView
        try:
            instance.actual_instance = PaginatedAzurePeerNetworkView.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into PaginatedGCPPeerVpcView
        try:
            instance.actual_instance = PaginatedGCPPeerVpcView.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into ListPeeringConnections200Response with oneOf schemas: PaginatedAWSPeerVpcView, PaginatedAzurePeerNetworkView, PaginatedGCPPeerVpcView. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into ListPeeringConnections200Response with oneOf schemas: PaginatedAWSPeerVpcView, PaginatedAzurePeerNetworkView, PaginatedGCPPeerVpcView. Details: " + ", ".join(error_messages))
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

