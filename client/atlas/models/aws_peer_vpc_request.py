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
from pydantic import BaseModel, Field, StrictStr, constr, validator

class AWSPeerVpcRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    container_id: constr(strict=True, max_length=24, min_length=24) = Field(..., alias="containerId", description="Unique 24-hexadecimal digit string that identifies the MongoDB Cloud network container that contains the specified network peering connection.")
    provider_name: StrictStr = Field(..., alias="providerName", description="Cloud service provider that determines the needed settings to configure the network connection for a virtual private connection.")
    accepter_region_name: StrictStr = Field(..., alias="accepterRegionName", description="Amazon Web Services (AWS) region where the Virtual Peering Connection (VPC) that you peered with the MongoDB Cloud VPC resides. The resource returns `null` if your VPC and the MongoDB Cloud VPC reside in the same region.")
    aws_account_id: constr(strict=True, max_length=12, min_length=12) = Field(..., alias="awsAccountId", description="Unique twelve-digit string that identifies the Amazon Web Services (AWS) account that owns the VPC that you peered with the MongoDB Cloud VPC.")
    connection_id: Optional[StrictStr] = Field(None, alias="connectionId", description="Unique string that identifies the peering connection on AWS.")
    error_state_name: Optional[StrictStr] = Field(None, alias="errorStateName", description="Type of error that can be returned when requesting an Amazon Web Services (AWS) peering connection. The resource returns `null` if the request succeeded.")
    id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, description="Unique 24-hexadecimal digit string that identifies the network peering connection.")
    route_table_cidr_block: constr(strict=True) = Field(..., alias="routeTableCidrBlock", description="Internet Protocol (IP) addresses expressed in Classless Inter-Domain Routing (CIDR) notation of the VPC's subnet that you want to peer with the MongoDB Cloud VPC.")
    status_name: Optional[StrictStr] = Field(None, alias="statusName", description="State of the network peering connection at the time you made the request.")
    vpc_id: constr(strict=True, min_length=5) = Field(..., alias="vpcId", description="Unique string that identifies the VPC on Amazon Web Services (AWS) that you want to peer with the MongoDB Cloud VPC.")
    __properties = ["containerId", "providerName", "accepterRegionName", "awsAccountId", "connectionId", "errorStateName", "id", "routeTableCidrBlock", "statusName", "vpcId"]

    @validator('container_id')
    def container_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('provider_name')
    def provider_name_validate_enum(cls, v):
        if v not in ('AWS', 'AZURE', 'GCP'):
            raise ValueError("must validate the enum values ('AWS', 'AZURE', 'GCP')")
        return v

    @validator('aws_account_id')
    def aws_account_id_validate_regular_expression(cls, v):
        if not re.match(r"^[0-9]{12}$", v):
            raise ValueError(r"must validate the regular expression /^[0-9]{12}$/")
        return v

    @validator('error_state_name')
    def error_state_name_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('REJECTED', 'EXPIRED', 'INVALID_ARGUMENT'):
            raise ValueError("must validate the enum values ('REJECTED', 'EXPIRED', 'INVALID_ARGUMENT')")
        return v

    @validator('id')
    def id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('route_table_cidr_block')
    def route_table_cidr_block_validate_regular_expression(cls, v):
        if not re.match(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}|([0-9a-f]{1,4}\:){7}[0-9a-f]{1,4}$", v):
            raise ValueError(r"must validate the regular expression /^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}|([0-9a-f]{1,4}\:){7}[0-9a-f]{1,4}$/")
        return v

    @validator('status_name')
    def status_name_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('INITIATING', 'PENDING_ACCEPTANCE', 'FAILED', 'FINALIZING', 'AVAILABLE', 'TERMINATING'):
            raise ValueError("must validate the enum values ('INITIATING', 'PENDING_ACCEPTANCE', 'FAILED', 'FINALIZING', 'AVAILABLE', 'TERMINATING')")
        return v

    @validator('vpc_id')
    def vpc_id_validate_regular_expression(cls, v):
        if not re.match(r"^vpc-[0-9a-f]{17}$", v):
            raise ValueError(r"must validate the regular expression /^vpc-[0-9a-f]{17}$/")
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
    def from_json(cls, json_str: str) -> AWSPeerVpcRequest:
        """Create an instance of AWSPeerVpcRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "connection_id",
                            "error_state_name",
                            "id",
                            "status_name",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AWSPeerVpcRequest:
        """Create an instance of AWSPeerVpcRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AWSPeerVpcRequest.parse_obj(obj)

        _obj = AWSPeerVpcRequest.parse_obj({
            "container_id": obj.get("containerId"),
            "provider_name": obj.get("providerName"),
            "accepter_region_name": obj.get("accepterRegionName"),
            "aws_account_id": obj.get("awsAccountId"),
            "connection_id": obj.get("connectionId"),
            "error_state_name": obj.get("errorStateName"),
            "id": obj.get("id"),
            "route_table_cidr_block": obj.get("routeTableCidrBlock"),
            "status_name": obj.get("statusName"),
            "vpc_id": obj.get("vpcId")
        })
        return _obj

