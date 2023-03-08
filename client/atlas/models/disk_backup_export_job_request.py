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
from pydantic import BaseModel, Field, constr, validator
from atlas.models.label import Label
from atlas.models.link import Link

class DiskBackupExportJobRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    custom_data: Optional[List[Label]] = Field(None, alias="customData", description="Collection of key-value pairs that represent custom data to add to the metadata file that MongoDB Cloud uploads to the bucket when the export job finishes.")
    export_bucket_id: constr(strict=True, max_length=24, min_length=24) = Field(..., alias="exportBucketId", description="Unique 24-hexadecimal character string that identifies the AWS bucket to which MongoDB Cloud exports the Cloud Backup snapshot.")
    links: Optional[List[Link]] = Field(None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    snapshot_id: constr(strict=True, max_length=24, min_length=24) = Field(..., alias="snapshotId", description="Unique 24-hexadecimal character string that identifies the Cloud Backup snasphot to export.")
    __properties = ["customData", "exportBucketId", "links", "snapshotId"]

    @validator('export_bucket_id')
    def export_bucket_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('snapshot_id')
    def snapshot_id_validate_regular_expression(cls, v):
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
    def from_json(cls, json_str: str) -> DiskBackupExportJobRequest:
        """Create an instance of DiskBackupExportJobRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "links",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in custom_data (list)
        _items = []
        if self.custom_data:
            for _item in self.custom_data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['customData'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DiskBackupExportJobRequest:
        """Create an instance of DiskBackupExportJobRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DiskBackupExportJobRequest.parse_obj(obj)

        _obj = DiskBackupExportJobRequest.parse_obj({
            "custom_data": [Label.from_dict(_item) for _item in obj.get("customData")] if obj.get("customData") is not None else None,
            "export_bucket_id": obj.get("exportBucketId"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None,
            "snapshot_id": obj.get("snapshotId")
        })
        return _obj
