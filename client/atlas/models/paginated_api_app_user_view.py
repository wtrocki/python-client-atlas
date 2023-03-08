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
from pydantic import BaseModel, Field, conint
from atlas.models.api_app_user_view import ApiAppUserView
from atlas.models.link import Link

class PaginatedApiAppUserView(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    links: Optional[List[Link]] = Field(None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    results: Optional[List[ApiAppUserView]] = Field(None, description="List of returned documents that MongoDB Cloud providers when completing this request.")
    total_count: Optional[conint(strict=True, ge=0)] = Field(None, alias="totalCount", description="Number of documents returned in this response.")
    __properties = ["links", "results", "totalCount"]

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
    def from_json(cls, json_str: str) -> PaginatedApiAppUserView:
        """Create an instance of PaginatedApiAppUserView from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "links",
                            "results",
                            "total_count",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item in self.results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['results'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PaginatedApiAppUserView:
        """Create an instance of PaginatedApiAppUserView from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PaginatedApiAppUserView.parse_obj(obj)

        _obj = PaginatedApiAppUserView.parse_obj({
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None,
            "results": [ApiAppUserView.from_dict(_item) for _item in obj.get("results")] if obj.get("results") is not None else None,
            "total_count": obj.get("totalCount")
        })
        return _obj

