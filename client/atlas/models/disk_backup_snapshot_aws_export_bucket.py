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
from pydantic import BaseModel, Field, StrictStr, constr, validator
from atlas.models.link import Link

class DiskBackupSnapshotAWSExportBucket(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="_id", description="Unique 24-hexadecimal character string that identifies the Amazon Web Services (AWS) Simple Storage Service (S3) export bucket.")
    bucket_name: Optional[StrictStr] = Field(None, alias="bucketName", description="Human-readable label that identifies the AWS bucket that the role is authorized to access.")
    cloud_provider: Optional[StrictStr] = Field(None, alias="cloudProvider", description="Human-readable label that identifies the cloud provider that stores this snapshot.")
    iam_role_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="iamRoleId", description="Unique 24-hexadecimal character string that identifies the AWS IAM role that MongoDB Cloud uses to access the AWS S3 bucket.")
    links: Optional[List[Link]] = Field(None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    __properties = ["_id", "bucketName", "cloudProvider", "iamRoleId", "links"]

    @validator('id')
    def id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('cloud_provider')
    def cloud_provider_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('AWS', 'AZURE', 'GCP'):
            raise ValueError("must validate the enum values ('AWS', 'AZURE', 'GCP')")
        return v

    @validator('iam_role_id')
    def iam_role_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
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
    def from_json(cls, json_str: str) -> DiskBackupSnapshotAWSExportBucket:
        """Create an instance of DiskBackupSnapshotAWSExportBucket from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "links",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DiskBackupSnapshotAWSExportBucket:
        """Create an instance of DiskBackupSnapshotAWSExportBucket from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DiskBackupSnapshotAWSExportBucket.parse_obj(obj)

        _obj = DiskBackupSnapshotAWSExportBucket.parse_obj({
            "id": obj.get("_id"),
            "bucket_name": obj.get("bucketName"),
            "cloud_provider": obj.get("cloudProvider"),
            "iam_role_id": obj.get("iamRoleId"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj

