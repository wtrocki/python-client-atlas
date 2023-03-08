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
from pydantic import BaseModel, Field, StrictBool, StrictStr, constr, validator

class AWSCloudProviderContainer(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    atlas_cidr_block: Optional[constr(strict=True)] = Field(None, alias="atlasCidrBlock", description="IP addresses expressed in Classless Inter-Domain Routing (CIDR) notation that MongoDB Cloud uses for the network peering containers in your project. MongoDB Cloud assigns all of the project's clusters deployed to this cloud provider an IP address from this range. MongoDB Cloud locks this value if an M10 or greater cluster or a network peering connection exists in this project.  These CIDR blocks must fall within the ranges reserved per RFC 1918. AWS and Azure further limit the block to between the `/24` and  `/21` ranges.  To modify the CIDR block, the target project cannot have:  - Any M10 or greater clusters - Any other VPC peering connections   You can also create a new project and create a network peering connection to set the desired MongoDB Cloud network peering container CIDR block for that project. MongoDB Cloud limits the number of MongoDB nodes per network peering connection based on the CIDR block and the region selected for the project.   **Example:** A project in an Amazon Web Services (AWS) region supporting three availability zones and an MongoDB CIDR network peering container block of limit of `/24` equals 27 three-node replica sets.")
    region_name: StrictStr = Field(..., alias="regionName", description="Geographic area that Amazon Web Services (AWS) defines to which MongoDB Cloud deployed this network peering container.")
    vpc_id: Optional[constr(strict=True, min_length=5)] = Field(None, alias="vpcId", description="Unique string that identifies the MongoDB Cloud VPC on AWS.")
    id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, description="Unique 24-hexadecimal digit string that identifies the network peering container.")
    provider_name: Optional[StrictStr] = Field(None, alias="providerName", description="Cloud service provider that serves the requested network peering containers.")
    provisioned: Optional[StrictBool] = Field(None, description="Flag that indicates whether MongoDB Cloud clusters exist in the specified network peering container.")
    __properties = ["atlasCidrBlock", "regionName", "vpcId", "id", "providerName", "provisioned"]

    @validator('atlas_cidr_block')
    def atlas_cidr_block_validate_regular_expression(cls, v):
        if not re.match(r"^((([0-9]{1,3}\.){3}[0-9]{1,3})|([\:]{0,2}([0-9a-f]{1,4}\:){0,7}[0-9a-f]{1,4}[\:]{0,2}))((%2[fF]|\/)[0-9]{1,3})+$", v):
            raise ValueError(r"must validate the regular expression /^((([0-9]{1,3}\.){3}[0-9]{1,3})|([\:]{0,2}([0-9a-f]{1,4}\:){0,7}[0-9a-f]{1,4}[\:]{0,2}))((%2[fF]|\/)[0-9]{1,3})+$/")
        return v

    @validator('region_name')
    def region_name_validate_enum(cls, v):
        if v not in ('US_EAST_1', 'US_EAST_2', 'US_WEST_1', 'US_WEST_2', 'CA_CENTRAL_1', 'EU_NORTH_1', 'EU_WEST_1', 'EU_WEST_2', 'EU_WEST_3', 'EU_CENTRAL_1', 'SA_EAST_1', 'AP_EAST_1', 'AP_SOUTHEAST_2', 'AP_SOUTHEAST_3', 'AP_NORTHEAST_1', 'AP_NORTHEAST_2', 'AP_NORTHEAST_3', 'AP_SOUTHEAST_1', 'AP_SOUTH_1', 'CN_NORTH_1', 'CN_NORTHWEST_1', 'ME_SOUTH_1', 'AF_SOUTH_1', 'EU_SOUTH_1', 'GLOBAL', 'US_GOV_WEST_1', 'US_GOV_EAST_1'):
            raise ValueError("must validate the enum values ('US_EAST_1', 'US_EAST_2', 'US_WEST_1', 'US_WEST_2', 'CA_CENTRAL_1', 'EU_NORTH_1', 'EU_WEST_1', 'EU_WEST_2', 'EU_WEST_3', 'EU_CENTRAL_1', 'SA_EAST_1', 'AP_EAST_1', 'AP_SOUTHEAST_2', 'AP_SOUTHEAST_3', 'AP_NORTHEAST_1', 'AP_NORTHEAST_2', 'AP_NORTHEAST_3', 'AP_SOUTHEAST_1', 'AP_SOUTH_1', 'CN_NORTH_1', 'CN_NORTHWEST_1', 'ME_SOUTH_1', 'AF_SOUTH_1', 'EU_SOUTH_1', 'GLOBAL', 'US_GOV_WEST_1', 'US_GOV_EAST_1')")
        return v

    @validator('vpc_id')
    def vpc_id_validate_regular_expression(cls, v):
        if not re.match(r"^vpc-[0-9a-f]{17}$", v):
            raise ValueError(r"must validate the regular expression /^vpc-[0-9a-f]{17}$/")
        return v

    @validator('id')
    def id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('provider_name')
    def provider_name_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('AWS', 'GCP', 'AZURE', 'TENANT', 'SERVERLESS'):
            raise ValueError("must validate the enum values ('AWS', 'GCP', 'AZURE', 'TENANT', 'SERVERLESS')")
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
    def from_json(cls, json_str: str) -> AWSCloudProviderContainer:
        """Create an instance of AWSCloudProviderContainer from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "vpc_id",
                            "id",
                            "provisioned",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AWSCloudProviderContainer:
        """Create an instance of AWSCloudProviderContainer from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AWSCloudProviderContainer.parse_obj(obj)

        _obj = AWSCloudProviderContainer.parse_obj({
            "atlas_cidr_block": obj.get("atlasCidrBlock"),
            "region_name": obj.get("regionName"),
            "vpc_id": obj.get("vpcId"),
            "id": obj.get("id"),
            "provider_name": obj.get("providerName"),
            "provisioned": obj.get("provisioned")
        })
        return _obj

