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
from pydantic import BaseModel, Field, StrictStr, constr, validator
from atlas.models.cluster_event_type_view_for_nds_group import ClusterEventTypeViewForNdsGroup
from atlas.models.link import Link
from atlas.models.raw import Raw

class ClusterEventViewForNdsGroup(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    created: datetime = Field(..., description="Date and time when this event occurred. This parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.")
    event_type_name: ClusterEventTypeViewForNdsGroup = Field(..., alias="eventTypeName")
    group_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project in which the event occurred. The **eventId** identifies the specific event.")
    id: constr(strict=True, max_length=24, min_length=24) = Field(..., description="Unique 24-hexadecimal digit string that identifies the event.")
    links: Optional[List[Link]] = Field(None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    org_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="orgId", description="Unique 24-hexadecimal digit string that identifies the organization to which these events apply.")
    raw: Optional[Raw] = None
    shard_name: Optional[StrictStr] = Field(None, alias="shardName", description="Human-readable label of the shard associated with the event.")
    __properties = ["created", "eventTypeName", "groupId", "id", "links", "orgId", "raw", "shardName"]

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

    @validator('org_id')
    def org_id_validate_regular_expression(cls, v):
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
    def from_json(cls, json_str: str) -> ClusterEventViewForNdsGroup:
        """Create an instance of ClusterEventViewForNdsGroup from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "created",
                            "group_id",
                            "id",
                            "links",
                            "org_id",
                            "shard_name",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of raw
        if self.raw:
            _dict['raw'] = self.raw.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClusterEventViewForNdsGroup:
        """Create an instance of ClusterEventViewForNdsGroup from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ClusterEventViewForNdsGroup.parse_obj(obj)

        _obj = ClusterEventViewForNdsGroup.parse_obj({
            "created": obj.get("created"),
            "event_type_name": obj.get("eventTypeName"),
            "group_id": obj.get("groupId"),
            "id": obj.get("id"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None,
            "org_id": obj.get("orgId"),
            "raw": Raw.from_dict(obj.get("raw")) if obj.get("raw") is not None else None,
            "shard_name": obj.get("shardName")
        })
        return _obj
