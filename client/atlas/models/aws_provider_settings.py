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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, validator
from atlas.models.aws_auto_scaling import AWSAutoScaling

class AWSProviderSettings(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    auto_scaling: Optional[AWSAutoScaling] = Field(None, alias="autoScaling")
    disk_iops: Optional[StrictInt] = Field(None, alias="diskIOPS", description="Maximum Disk Input/Output Operations per Second (IOPS) that the database host can perform.")
    encrypt_ebs_volume: Optional[StrictBool] = Field(True, alias="encryptEBSVolume", description="Flag that indicates whether the Amazon Elastic Block Store (EBS) encryption feature encrypts the host's root volume for both data at rest within the volume and for data moving between the volume and the cluster. Clusters always have this setting enabled.")
    instance_size_name: Optional[StrictStr] = Field(None, alias="instanceSizeName", description="Cluster tier, with a default storage and memory capacity, that applies to all the data-bearing hosts in your cluster.")
    region_name: Optional[StrictStr] = Field(None, alias="regionName", description=" Physical location where MongoDB Cloud deploys your AWS-hosted MongoDB cluster nodes. The region you choose can affect network latency for clients accessing your databases. When MongoDB Cloud deploys a dedicated cluster, it checks if a VPC or VPC connection exists for that provider and region. If not, MongoDB Cloud creates them as part of the deployment. MongoDB Cloud assigns the VPC a CIDR block. To limit a new VPC peering connection to one CIDR block and region, create the connection first. Deploy the cluster after the connection starts.")
    volume_type: Optional[StrictStr] = Field(None, alias="volumeType", description="Disk Input/Output Operations per Second (IOPS) setting for Amazon Web Services (AWS) storage that you configure only for abbr title=\"Amazon Web Services\">AWS</abbr>. Specify whether Disk Input/Output Operations per Second (IOPS) must not exceed the default Input/Output Operations per Second (IOPS) rate for the selected volume size (`STANDARD`), or must fall within the allowable Input/Output Operations per Second (IOPS) range for the selected volume size (`PROVISIONED`).")
    provider_name: StrictStr = Field(..., alias="providerName")
    __properties = ["autoScaling", "diskIOPS", "encryptEBSVolume", "instanceSizeName", "regionName", "volumeType", "providerName"]

    @validator('instance_size_name')
    def instance_size_name_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('M10', 'M20', 'M30', 'M40', 'M50', 'M60', 'M80', 'M100', 'M140', 'M200', 'M300', 'R40', 'R50', 'R60', 'R80', 'R200', 'R300', 'R400', 'R700', 'M40_NVME', 'M50_NVME', 'M60_NVME', 'M80_NVME', 'M200_NVME', 'M400_NVME'):
            raise ValueError("must validate the enum values ('M10', 'M20', 'M30', 'M40', 'M50', 'M60', 'M80', 'M100', 'M140', 'M200', 'M300', 'R40', 'R50', 'R60', 'R80', 'R200', 'R300', 'R400', 'R700', 'M40_NVME', 'M50_NVME', 'M60_NVME', 'M80_NVME', 'M200_NVME', 'M400_NVME')")
        return v

    @validator('region_name')
    def region_name_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('US_GOV_WEST_1', 'US_GOV_EAST_1', 'US_EAST_1', 'US_EAST_2', 'US_WEST_1', 'US_WEST_2', 'CA_CENTRAL_1', 'EU_NORTH_1', 'EU_WEST_1', 'EU_WEST_2', 'EU_WEST_3', 'EU_CENTRAL_1', 'AP_EAST_1', 'AP_NORTHEAST_1', 'AP_NORTHEAST_2', 'AP_NORTHEAST_3', 'AP_SOUTHEAST_1', 'AP_SOUTHEAST_2', 'AP_SOUTHEAST_3', 'AP_SOUTH_1', 'SA_EAST_1', 'CN_NORTH_1', 'CN_NORTHWEST_1', 'ME_SOUTH_1', 'AF_SOUTH_1', 'EU_SOUTH_1', 'GLOBAL'):
            raise ValueError("must validate the enum values ('US_GOV_WEST_1', 'US_GOV_EAST_1', 'US_EAST_1', 'US_EAST_2', 'US_WEST_1', 'US_WEST_2', 'CA_CENTRAL_1', 'EU_NORTH_1', 'EU_WEST_1', 'EU_WEST_2', 'EU_WEST_3', 'EU_CENTRAL_1', 'AP_EAST_1', 'AP_NORTHEAST_1', 'AP_NORTHEAST_2', 'AP_NORTHEAST_3', 'AP_SOUTHEAST_1', 'AP_SOUTHEAST_2', 'AP_SOUTHEAST_3', 'AP_SOUTH_1', 'SA_EAST_1', 'CN_NORTH_1', 'CN_NORTHWEST_1', 'ME_SOUTH_1', 'AF_SOUTH_1', 'EU_SOUTH_1', 'GLOBAL')")
        return v

    @validator('volume_type')
    def volume_type_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('STANDARD', 'PROVISIONED'):
            raise ValueError("must validate the enum values ('STANDARD', 'PROVISIONED')")
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
    def from_json(cls, json_str: str) -> AWSProviderSettings:
        """Create an instance of AWSProviderSettings from a JSON string"""
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
    def from_dict(cls, obj: dict) -> AWSProviderSettings:
        """Create an instance of AWSProviderSettings from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AWSProviderSettings.parse_obj(obj)

        _obj = AWSProviderSettings.parse_obj({
            "auto_scaling": AWSAutoScaling.from_dict(obj.get("autoScaling")) if obj.get("autoScaling") is not None else None,
            "disk_iops": obj.get("diskIOPS"),
            "encrypt_ebs_volume": obj.get("encryptEBSVolume") if obj.get("encryptEBSVolume") is not None else True,
            "instance_size_name": obj.get("instanceSizeName"),
            "region_name": obj.get("regionName"),
            "volume_type": obj.get("volumeType"),
            "provider_name": obj.get("providerName")
        })
        return _obj

