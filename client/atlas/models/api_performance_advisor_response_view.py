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
from pydantic import BaseModel, Field
from atlas.models.api_performance_advisor_index_view import ApiPerformanceAdvisorIndexView
from atlas.models.api_performance_advisor_shape_view import ApiPerformanceAdvisorShapeView

class ApiPerformanceAdvisorResponseView(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    shapes: Optional[List[ApiPerformanceAdvisorShapeView]] = Field(None, description="List of query predicates, sorts, and projections that the Performance Advisor suggests.")
    suggested_indexes: Optional[List[ApiPerformanceAdvisorIndexView]] = Field(None, alias="suggestedIndexes", description="List that contains the documents with information about the indexes that the Performance Advisor suggests.")
    __properties = ["shapes", "suggestedIndexes"]

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
    def from_json(cls, json_str: str) -> ApiPerformanceAdvisorResponseView:
        """Create an instance of ApiPerformanceAdvisorResponseView from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "shapes",
                            "suggested_indexes",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in shapes (list)
        _items = []
        if self.shapes:
            for _item in self.shapes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['shapes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in suggested_indexes (list)
        _items = []
        if self.suggested_indexes:
            for _item in self.suggested_indexes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['suggestedIndexes'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiPerformanceAdvisorResponseView:
        """Create an instance of ApiPerformanceAdvisorResponseView from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ApiPerformanceAdvisorResponseView.parse_obj(obj)

        _obj = ApiPerformanceAdvisorResponseView.parse_obj({
            "shapes": [ApiPerformanceAdvisorShapeView.from_dict(_item) for _item in obj.get("shapes")] if obj.get("shapes") is not None else None,
            "suggested_indexes": [ApiPerformanceAdvisorIndexView.from_dict(_item) for _item in obj.get("suggestedIndexes")] if obj.get("suggestedIndexes") is not None else None
        })
        return _obj

