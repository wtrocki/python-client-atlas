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
from atlas.models.link import Link
from atlas.models.notification_view_for_nds_group import NotificationViewForNdsGroup
from atlas.models.replica_set_event_type_view_for_nds_group_alertable_no_threshold import ReplicaSetEventTypeViewForNdsGroupAlertableNoThreshold
from atlas.models.replica_set_matcher_view import ReplicaSetMatcherView
from atlas.models.threshold_view_integer import ThresholdViewInteger

class ReplicaSetAlertConfigViewForNdsGroup(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    created: Optional[datetime] = Field(None, description="Date and time when MongoDB Cloud created the alert configuration. This parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.")
    enabled: Optional[StrictBool] = Field(False, description="Flag that indicates whether someone enabled this alert configuration for the specified project.")
    event_type_name: ReplicaSetEventTypeViewForNdsGroupAlertableNoThreshold = Field(..., alias="eventTypeName")
    group_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project that owns this alert configuration.")
    id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, description="Unique 24-hexadecimal digit string that identifies this alert configuration.")
    links: Optional[List[Link]] = Field(None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    matchers: Optional[List[ReplicaSetMatcherView]] = Field(None, description="List of rules that determine whether MongoDB Cloud checks an object for the alert configuration. You can filter using the matchers array if the **eventTypeName** specifies an event for a host, replica set, or sharded cluster.")
    notifications: Optional[List[NotificationViewForNdsGroup]] = Field(None, description="List that contains the targets that MongoDB Cloud sends notifications.")
    threshold: Optional[ThresholdViewInteger] = None
    updated: Optional[datetime] = Field(None, description="Date and time when someone last updated this alert configuration. This parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.")
    __properties = ["created", "enabled", "eventTypeName", "groupId", "id", "links", "matchers", "notifications", "threshold", "updated"]

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
    def from_json(cls, json_str: str) -> ReplicaSetAlertConfigViewForNdsGroup:
        """Create an instance of ReplicaSetAlertConfigViewForNdsGroup from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "created",
                            "group_id",
                            "id",
                            "links",
                            "updated",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in matchers (list)
        _items = []
        if self.matchers:
            for _item in self.matchers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['matchers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in notifications (list)
        _items = []
        if self.notifications:
            for _item in self.notifications:
                if _item:
                    _items.append(_item.to_dict())
            _dict['notifications'] = _items
        # override the default output from pydantic by calling `to_dict()` of threshold
        if self.threshold:
            _dict['threshold'] = self.threshold.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ReplicaSetAlertConfigViewForNdsGroup:
        """Create an instance of ReplicaSetAlertConfigViewForNdsGroup from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ReplicaSetAlertConfigViewForNdsGroup.parse_obj(obj)

        _obj = ReplicaSetAlertConfigViewForNdsGroup.parse_obj({
            "created": obj.get("created"),
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else False,
            "event_type_name": obj.get("eventTypeName"),
            "group_id": obj.get("groupId"),
            "id": obj.get("id"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None,
            "matchers": [ReplicaSetMatcherView.from_dict(_item) for _item in obj.get("matchers")] if obj.get("matchers") is not None else None,
            "notifications": [NotificationViewForNdsGroup.from_dict(_item) for _item in obj.get("notifications")] if obj.get("notifications") is not None else None,
            "threshold": ThresholdViewInteger.from_dict(obj.get("threshold")) if obj.get("threshold") is not None else None,
            "updated": obj.get("updated")
        })
        return _obj

