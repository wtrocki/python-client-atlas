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
from atlas.models.api_performance_advisor_slow_query_view import ApiPerformanceAdvisorSlowQueryView

class ApiPerformanceAdvisorSlowQueryListView(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    slow_queries: Optional[List[ApiPerformanceAdvisorSlowQueryView]] = Field(None, alias="slowQueries", description="List of operations that the Performance Advisor detected that took longer to execute than a specified threshold.")
    __properties = ["slowQueries"]

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
    def from_json(cls, json_str: str) -> ApiPerformanceAdvisorSlowQueryListView:
        """Create an instance of ApiPerformanceAdvisorSlowQueryListView from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "slow_queries",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in slow_queries (list)
        _items = []
        if self.slow_queries:
            for _item in self.slow_queries:
                if _item:
                    _items.append(_item.to_dict())
            _dict['slowQueries'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiPerformanceAdvisorSlowQueryListView:
        """Create an instance of ApiPerformanceAdvisorSlowQueryListView from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ApiPerformanceAdvisorSlowQueryListView.parse_obj(obj)

        _obj = ApiPerformanceAdvisorSlowQueryListView.parse_obj({
            "slow_queries": [ApiPerformanceAdvisorSlowQueryView.from_dict(_item) for _item in obj.get("slowQueries")] if obj.get("slowQueries") is not None else None
        })
        return _obj
