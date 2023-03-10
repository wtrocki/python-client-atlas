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
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator

class DedicatedHardwareSpec(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    node_count: Optional[StrictInt] = Field(None, alias="nodeCount", description="Number of read-only nodes for MongoDB Cloud to deploy to the region. Read-only nodes can never become the primary, but can enable local reads.")
    disk_iops: Optional[StrictInt] = Field(None, alias="diskIOPS", description="Target throughput desired for storage attached to your AWS-provisioned cluster. Change this parameter only if you:  - set `\"replicationSpecs[n].regionConfigs[m].providerName\" : \"AWS\"`. - set `\"replicationSpecs[n].regionConfigs[m].electableSpecs.instanceSize\" : \"M30\"` or greater not including `Mxx_NVME` tiers.  The maximum input/output operations per second (IOPS) depend on the selected **.instanceSize** and **.diskSizeGB**. This parameter defaults to the cluster tier's standard IOPS value. Changing this value impacts cluster cost. MongoDB Cloud enforces minimum ratios of storage capacity to system memory for given cluster tiers. This keeps cluster performance consistent with large datasets.  - Instance sizes `M10` to `M40` have a ratio of disk capacity to system memory of 60:1. - Instance sizes greater than `M40` have a ratio of 120:1.")
    ebs_volume_type: Optional[StrictStr] = Field('STANDARD', alias="ebsVolumeType", description="Type of storage you want to attach to your AWS-provisioned cluster.  - `STANDARD` volume types can't exceed the default input/output operations per second (IOPS) rate for the selected volume size.   - `PROVISIONED` volume types must fall within the allowable IOPS range for the selected volume size.")
    instance_size: Optional[StrictStr] = Field(None, alias="instanceSize", description="Hardware specification for the instance sizes in this region. Each instance size has a default storage and memory capacity. The instance size you select applies to all the data-bearing hosts in your instance size.")
    __properties = ["nodeCount", "diskIOPS", "ebsVolumeType", "instanceSize"]

    @validator('ebs_volume_type')
    def ebs_volume_type_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('STANDARD', 'PROVISIONED'):
            raise ValueError("must validate the enum values ('STANDARD', 'PROVISIONED')")
        return v

    @validator('instance_size')
    def instance_size_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('M10', 'M20', 'M30', 'M40', 'M50', 'M60', 'M80', 'M140', 'M200', 'M250', 'M300', 'M400', 'R40', 'R50', 'R60', 'R80', 'R200', 'R300', 'R400', 'R600'):
            raise ValueError("must validate the enum values ('M10', 'M20', 'M30', 'M40', 'M50', 'M60', 'M80', 'M140', 'M200', 'M250', 'M300', 'M400', 'R40', 'R50', 'R60', 'R80', 'R200', 'R300', 'R400', 'R600')")
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
    def from_json(cls, json_str: str) -> DedicatedHardwareSpec:
        """Create an instance of DedicatedHardwareSpec from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DedicatedHardwareSpec:
        """Create an instance of DedicatedHardwareSpec from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DedicatedHardwareSpec.parse_obj(obj)

        _obj = DedicatedHardwareSpec.parse_obj({
            "node_count": obj.get("nodeCount"),
            "disk_iops": obj.get("diskIOPS"),
            "ebs_volume_type": obj.get("ebsVolumeType") if obj.get("ebsVolumeType") is not None else 'STANDARD',
            "instance_size": obj.get("instanceSize")
        })
        return _obj

