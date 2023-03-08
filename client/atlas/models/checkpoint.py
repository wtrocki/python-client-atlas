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
from atlas.models.api_checkpoint_part_view import ApiCheckpointPartView
from atlas.models.link import Link

class Checkpoint(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    cluster_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="clusterId", description="Unique 24-hexadecimal digit string that identifies the cluster that contains the checkpoint.")
    completed: Optional[datetime] = Field(None, description="Date and time when the checkpoint completed and the balancer restarted. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    group_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project that owns the checkpoints.")
    id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, description="Unique 24-hexadecimal digit string that identifies checkpoint.")
    links: Optional[List[Link]] = Field(None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    parts: Optional[List[ApiCheckpointPartView]] = Field(None, description="Metadata that describes the complete snapshot.  - For a replica set, this array contains a single document. - For a sharded cluster, this array contains one document for each shard plus one document for the config host.")
    restorable: Optional[StrictBool] = Field(None, description="Flag that indicates whether MongoDB Cloud can use the checkpoint for a restore.")
    started: Optional[datetime] = Field(None, description="Date and time when the balancer stopped and began the checkpoint. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    timestamp: Optional[datetime] = Field(None, description="Date and time to which the checkpoint restores. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    __properties = ["clusterId", "completed", "groupId", "id", "links", "parts", "restorable", "started", "timestamp"]

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
    def from_json(cls, json_str: str) -> Checkpoint:
        """Create an instance of Checkpoint from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "cluster_id",
                            "completed",
                            "group_id",
                            "id",
                            "links",
                            "parts",
                            "restorable",
                            "started",
                            "timestamp",
                          },
                          exclude_none=True)
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
    def from_dict(cls, obj: dict) -> Checkpoint:
        """Create an instance of Checkpoint from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Checkpoint.parse_obj(obj)

        _obj = Checkpoint.parse_obj({
            "cluster_id": obj.get("clusterId"),
            "completed": obj.get("completed"),
            "group_id": obj.get("groupId"),
            "id": obj.get("id"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None,
            "parts": [ApiCheckpointPartView.from_dict(_item) for _item in obj.get("parts")] if obj.get("parts") is not None else None,
            "restorable": obj.get("restorable"),
            "started": obj.get("started"),
            "timestamp": obj.get("timestamp")
        })
        return _obj

