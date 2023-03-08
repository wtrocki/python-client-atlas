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
from pydantic import BaseModel, Field, StrictBool, StrictInt, constr, validator
from atlas.models.link import Link

class Group(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    cluster_count: StrictInt = Field(..., alias="clusterCount", description="Quantity of MongoDB Cloud clusters deployed in this project.")
    created: datetime = Field(..., description="Date and time when MongoDB Cloud created this project. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, description="Unique 24-hexadecimal digit string that identifies the MongoDB Cloud project.")
    links: Optional[List[Link]] = Field(None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    name: constr(strict=True, max_length=64, min_length=1) = Field(..., description="Human-readable label that identifies the project included in the MongoDB Cloud organization.")
    org_id: constr(strict=True, max_length=24, min_length=24) = Field(..., alias="orgId", description="Unique 24-hexadecimal digit string that identifies the MongoDB Cloud organization to which the project belongs.")
    with_default_alerts_settings: Optional[StrictBool] = Field(None, alias="withDefaultAlertsSettings", description="Flag that indicates whether to create the project with default alert settings.")
    __properties = ["clusterCount", "created", "id", "links", "name", "orgId", "withDefaultAlertsSettings"]

    @validator('id')
    def id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('name')
    def name_validate_regular_expression(cls, v):
        if not re.match(r"^[\p{L}\p{N}\-_.(),:&@+\']{1,64}$", v):
            raise ValueError(r"must validate the regular expression /^[\p{L}\p{N}\-_.(),:&@+']{1,64}$/")
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
    def from_json(cls, json_str: str) -> Group:
        """Create an instance of Group from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "cluster_count",
                            "created",
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
    def from_dict(cls, obj: dict) -> Group:
        """Create an instance of Group from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Group.parse_obj(obj)

        _obj = Group.parse_obj({
            "cluster_count": obj.get("clusterCount"),
            "created": obj.get("created"),
            "id": obj.get("id"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None,
            "name": obj.get("name"),
            "org_id": obj.get("orgId"),
            "with_default_alerts_settings": obj.get("withDefaultAlertsSettings")
        })
        return _obj

