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
from atlas.models.api_key_view import ApiKeyView
from atlas.models.link import Link

class ApiSystemStatusView(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    api_key: Optional[ApiKeyView] = Field(..., alias="apiKey")
    app_name: StrictStr = Field(..., alias="appName", description="Human-readable label that identifies the service from which you requested this response.")
    build: StrictStr = Field(..., description="Unique 40-hexadecimal digit hash that identifies the latest git commit merged for this application.")
    links: Optional[List[Link]] = Field(None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    throttling: StrictBool = Field(..., description="Flag that indicates whether someone enabled throttling on this service.")
    __properties = ["apiKey", "appName", "build", "links", "throttling"]

    @validator('app_name')
    def app_name_validate_enum(cls, v):
        if v not in ('MongoDB Atlas'):
            raise ValueError("must validate the enum values ('MongoDB Atlas')")
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
    def from_json(cls, json_str: str) -> ApiSystemStatusView:
        """Create an instance of ApiSystemStatusView from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "app_name",
                            "build",
                            "links",
                            "throttling",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of api_key
        if self.api_key:
            _dict['apiKey'] = self.api_key.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if api_key (nullable) is None
        if self.api_key is None:
            _dict['apiKey'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiSystemStatusView:
        """Create an instance of ApiSystemStatusView from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ApiSystemStatusView.parse_obj(obj)

        _obj = ApiSystemStatusView.parse_obj({
            "api_key": ApiKeyView.from_dict(obj.get("apiKey")) if obj.get("apiKey") is not None else None,
            "app_name": obj.get("appName"),
            "build": obj.get("build"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None,
            "throttling": obj.get("throttling")
        })
        return _obj

