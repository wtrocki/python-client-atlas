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

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, constr, validator
from atlas.models.api_bson_timestamp_view import ApiBSONTimestampView
from atlas.models.api_snapshot_part_view import ApiSnapshotPartView
from atlas.models.link import Link

class ApiSnapshotView(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    cluster_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="clusterId", description="Unique 24-hexadecimal digit string that identifies the cluster with the snapshots you want to return.")
    complete: Optional[StrictBool] = Field(None, description="Flag that indicates whether the snapshot exists. This flag returns `false` while MongoDB Cloud creates the snapshot.")
    created: Optional[ApiBSONTimestampView] = None
    do_not_delete: Optional[StrictBool] = Field(None, alias="doNotDelete", description="Flag that indicates whether someone can delete this snapshot. You can't set `\"doNotDelete\" : true` and set a timestamp for **expires** in the same request.")
    expires: Optional[datetime] = Field(None, description="Date and time when MongoDB Cloud deletes the snapshot. If `\"doNotDelete\" : true`, MongoDB Cloud removes any value set for this parameter.")
    group_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project that owns the snapshots.")
    id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, description="Unique 24-hexadecimal digit string that identifies the snapshot.")
    last_oplog_applied_timestamp: Optional[ApiBSONTimestampView] = Field(None, alias="lastOplogAppliedTimestamp")
    links: Optional[List[Link]] = Field(None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    parts: Optional[List[ApiSnapshotPartView]] = Field(None, description="Metadata that describes the complete snapshot.  - For a replica set, this array contains a single document. - For a sharded cluster, this array contains one document for each shard plus one document for the config host.")
    __properties = ["clusterId", "complete", "created", "doNotDelete", "expires", "groupId", "id", "lastOplogAppliedTimestamp", "links", "parts"]

    @validator('cluster_id')
    def cluster_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('group_id')
    def group_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('id')
    def id_validate_regular_expression(cls, v):
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
    def from_json(cls, json_str: str) -> ApiSnapshotView:
        """Create an instance of ApiSnapshotView from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "cluster_id",
                            "complete",
                            "group_id",
                            "id",
                            "links",
                            "parts",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of created
        if self.created:
            _dict['created'] = self.created.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_oplog_applied_timestamp
        if self.last_oplog_applied_timestamp:
            _dict['lastOplogAppliedTimestamp'] = self.last_oplog_applied_timestamp.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in parts (list)
        _items = []
        if self.parts:
            for _item in self.parts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['parts'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiSnapshotView:
        """Create an instance of ApiSnapshotView from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ApiSnapshotView.parse_obj(obj)

        _obj = ApiSnapshotView.parse_obj({
            "cluster_id": obj.get("clusterId"),
            "complete": obj.get("complete"),
            "created": ApiBSONTimestampView.from_dict(obj.get("created")) if obj.get("created") is not None else None,
            "do_not_delete": obj.get("doNotDelete"),
            "expires": obj.get("expires"),
            "group_id": obj.get("groupId"),
            "id": obj.get("id"),
            "last_oplog_applied_timestamp": ApiBSONTimestampView.from_dict(obj.get("lastOplogAppliedTimestamp")) if obj.get("lastOplogAppliedTimestamp") is not None else None,
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None,
            "parts": [ApiSnapshotPartView.from_dict(_item) for _item in obj.get("parts")] if obj.get("parts") is not None else None
        })
        return _obj

