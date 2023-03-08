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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, validator

class DiskBackupCopySetting(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    cloud_provider: Optional[StrictStr] = Field(None, alias="cloudProvider", description="Human-readable label that identifies the cloud provider that stores the snapshot copy.")
    frequencies: Optional[List[StrictStr]] = Field(None, description="List that describes which types of snapshots to copy.")
    region_name: Optional[StrictStr] = Field(None, alias="regionName", description="Target region to copy snapshots belonging to replicationSpecId to. Please supply the 'Atlas Region' which can be found under [Cloud Providers](https://www.mongodb.com/docs/atlas/reference/cloud-providers/) 'regions' link.")
    replication_spec_id: Optional[StrictStr] = Field(None, alias="replicationSpecId", description="Unique 24-hexadecimal digit string that identifies the replication object for a zone in a cluster. For global clusters, there can be multiple zones to choose from. For sharded clusters and replica set clusters, there is only one zone in the cluster. To find the Replication Spec Id, do a GET request to Return One Cluster in One Project and consult the replicationSpecs array [Return One Cluster in One Project](#operation/getLegacyCluster).")
    should_copy_oplogs: Optional[StrictBool] = Field(None, alias="shouldCopyOplogs", description="Flag that indicates whether to copy the oplogs to the target region. You can use the oplogs to perform point-in-time restores.")
    __properties = ["cloudProvider", "frequencies", "regionName", "replicationSpecId", "shouldCopyOplogs"]

    @validator('cloud_provider')
    def cloud_provider_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('AWS', 'AZURE', 'GCP'):
            raise ValueError("must validate the enum values ('AWS', 'AZURE', 'GCP')")
        return v

    @validator('frequencies')
    def frequencies_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('HOURLY', 'DAILY', 'WEEKLY', 'MONTHLY', 'ON_DEMAND'):
            raise ValueError("must validate the enum values ('HOURLY', 'DAILY', 'WEEKLY', 'MONTHLY', 'ON_DEMAND')")
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
    def from_json(cls, json_str: str) -> DiskBackupCopySetting:
        """Create an instance of DiskBackupCopySetting from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DiskBackupCopySetting:
        """Create an instance of DiskBackupCopySetting from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DiskBackupCopySetting.parse_obj(obj)

        _obj = DiskBackupCopySetting.parse_obj({
            "cloud_provider": obj.get("cloudProvider"),
            "frequencies": obj.get("frequencies"),
            "region_name": obj.get("regionName"),
            "replication_spec_id": obj.get("replicationSpecId"),
            "should_copy_oplogs": obj.get("shouldCopyOplogs")
        })
        return _obj
