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


from typing import Dict, List, Optional
from pydantic import BaseModel, Field, StrictFloat, StrictStr, constr, validator

class ApiPerformanceAdvisorIndexView(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    avg_obj_size: Optional[StrictFloat] = Field(None, alias="avgObjSize", description="The average size of an object in the collection of this index.")
    id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, description="Unique 24-hexadecimal digit string that identifies this index.")
    impact: Optional[List[constr(strict=True, max_length=24, min_length=24)]] = Field(None, description="List that contains unique 24-hexadecimal character string that identifies the query shapes in this response that the Performance Advisor suggests.")
    index: Optional[List[Dict[str, StrictStr]]] = Field(None, description="List that contains documents that specify a key in the index and its sort order.")
    namespace: Optional[StrictStr] = Field(None, description="Human-readable label that identifies the namespace on the specified host. The resource expresses this parameter value as `<database>.<collection>`.")
    weight: Optional[StrictFloat] = Field(None, description="Estimated performance improvement that the suggested index provides. This value corresponds to **Impact** in the Performance Advisor user interface.")
    __properties = ["avgObjSize", "id", "impact", "index", "namespace", "weight"]

    @validator('id')
    def id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('index')
    def index_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('1', '1', '-1'):
            raise ValueError("must validate the enum values ('1', '1', '-1')")
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
    def from_json(cls, json_str: str) -> ApiPerformanceAdvisorIndexView:
        """Create an instance of ApiPerformanceAdvisorIndexView from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "avg_obj_size",
                            "id",
                            "impact",
                            "index",
                            "namespace",
                            "weight",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiPerformanceAdvisorIndexView:
        """Create an instance of ApiPerformanceAdvisorIndexView from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ApiPerformanceAdvisorIndexView.parse_obj(obj)

        _obj = ApiPerformanceAdvisorIndexView.parse_obj({
            "avg_obj_size": obj.get("avgObjSize"),
            "id": obj.get("id"),
            "impact": obj.get("impact"),
            "index": obj.get("index"),
            "namespace": obj.get("namespace"),
            "weight": obj.get("weight")
        })
        return _obj
