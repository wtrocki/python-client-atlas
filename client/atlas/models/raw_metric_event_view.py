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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, constr, validator
from atlas.models.host_metric_event_type_view import HostMetricEventTypeView
from atlas.models.link import Link
from atlas.models.raw import Raw
from atlas.models.raw_metric_value_view import RawMetricValueView

class RawMetricEventView(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    api_key_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="apiKeyId", description="Unique 24-hexadecimal digit string that identifies the [API Key](https://dochub.mongodb.org/core/atlas-create-prog-api-key) that triggered the event. If this resource returns this parameter, it doesn't return the **userId** parameter.")
    created: datetime = Field(..., description="Date and time when this event occurred. This parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.")
    current_value: Optional[RawMetricValueView] = Field(None, alias="currentValue")
    event_type_name: HostMetricEventTypeView = Field(..., alias="eventTypeName")
    group_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project in which the event occurred. The **eventId** identifies the specific event.")
    id: constr(strict=True, max_length=24, min_length=24) = Field(..., description="Unique 24-hexadecimal digit string that identifies the event.")
    is_global_admin: Optional[StrictBool] = Field(False, alias="isGlobalAdmin", description="Flag that indicates whether a MongoDB employee triggered the specified event.")
    links: Optional[List[Link]] = Field(None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    metric_name: Optional[StrictStr] = Field(None, alias="metricName", description="Human-readable label of the metric associated with the **alertId**. This field may change type of **currentValue** field.")
    org_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="orgId", description="Unique 24-hexadecimal digit string that identifies the organization to which these events apply.")
    port: Optional[StrictInt] = Field(None, description="IANA port on which the MongoDB process listens for requests.")
    public_key: Optional[StrictStr] = Field(None, alias="publicKey", description="Public part of the [API Key](https://dochub.mongodb.org/core/atlas-create-prog-api-key) that triggered the event. If this resource returns this parameter, it doesn't return the **username** parameter.")
    raw: Optional[Raw] = None
    remote_address: Optional[constr(strict=True)] = Field(None, alias="remoteAddress", description="IPv4 or IPv6 address from which the user triggered this event.")
    replica_set_name: Optional[StrictStr] = Field(None, alias="replicaSetName", description="Human-readable label of the replica set associated with the event.")
    shard_name: Optional[StrictStr] = Field(None, alias="shardName", description="Human-readable label of the shard associated with the event.")
    user_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="userId", description="Unique 24-hexadecimal digit string that identifies the console user who triggered the event. If this resource returns this parameter, it doesn't return the **apiKeyId** parameter.")
    username: Optional[StrictStr] = Field(None, description="Email address for the user who triggered this event. If this resource returns this parameter, it doesn't return the **publicApiKey** parameter.")
    __properties = ["apiKeyId", "created", "currentValue", "eventTypeName", "groupId", "id", "isGlobalAdmin", "links", "metricName", "orgId", "port", "publicKey", "raw", "remoteAddress", "replicaSetName", "shardName", "userId", "username"]

    @validator('api_key_id')
    def api_key_id_validate_regular_expression(cls, v):
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

    @validator('org_id')
    def org_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('remote_address')
    def remote_address_validate_regular_expression(cls, v):
        if not re.match(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}|([0-9a-f]{1,4}\:){7}[0-9a-f]{1,4}$", v):
            raise ValueError(r"must validate the regular expression /^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}|([0-9a-f]{1,4}\:){7}[0-9a-f]{1,4}$/")
        return v

    @validator('user_id')
    def user_id_validate_regular_expression(cls, v):
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
    def from_json(cls, json_str: str) -> RawMetricEventView:
        """Create an instance of RawMetricEventView from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "api_key_id",
                            "created",
                            "group_id",
                            "id",
                            "is_global_admin",
                            "links",
                            "metric_name",
                            "org_id",
                            "port",
                            "public_key",
                            "remote_address",
                            "replica_set_name",
                            "shard_name",
                            "user_id",
                            "username",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of current_value
        if self.current_value:
            _dict['currentValue'] = self.current_value.to_dict()
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
    def from_dict(cls, obj: dict) -> RawMetricEventView:
        """Create an instance of RawMetricEventView from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return RawMetricEventView.parse_obj(obj)

        _obj = RawMetricEventView.parse_obj({
            "api_key_id": obj.get("apiKeyId"),
            "created": obj.get("created"),
            "current_value": RawMetricValueView.from_dict(obj.get("currentValue")) if obj.get("currentValue") is not None else None,
            "event_type_name": obj.get("eventTypeName"),
            "group_id": obj.get("groupId"),
            "id": obj.get("id"),
            "is_global_admin": obj.get("isGlobalAdmin") if obj.get("isGlobalAdmin") is not None else False,
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None,
            "metric_name": obj.get("metricName"),
            "org_id": obj.get("orgId"),
            "port": obj.get("port"),
            "public_key": obj.get("publicKey"),
            "raw": Raw.from_dict(obj.get("raw")) if obj.get("raw") is not None else None,
            "remote_address": obj.get("remoteAddress"),
            "replica_set_name": obj.get("replicaSetName"),
            "shard_name": obj.get("shardName"),
            "user_id": obj.get("userId"),
            "username": obj.get("username")
        })
        return _obj

