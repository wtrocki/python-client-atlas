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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator

class CustomCriteriaView(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    query: StrictStr = Field(..., description="MongoDB find query that selects documents to archive. The specified query follows the syntax of the `db.collection.find(query)` command. This query can't use the empty document (`{}`) to return all documents. Set this parameter when **\"criteria.type\" : \"CUSTOM\"**.")
    type: Optional[StrictStr] = Field(None, description="Means by which MongoDB Cloud selects data to archive. Data can be chosen using the age of the data or a MongoDB query. **DATE** selects documents to archive based on a date. **CUSTOM** selects documents to archive based on a custom JSON query. MongoDB Cloud doesn't support **CUSTOM** when `\"collectionType\": \"TIMESERIES\"`.")
    __properties = ["query", "type"]

    @validator('type')
    def type_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('DATE', 'CUSTOM'):
            raise ValueError("must validate the enum values ('DATE', 'CUSTOM')")
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
    def from_json(cls, json_str: str) -> CustomCriteriaView:
        """Create an instance of CustomCriteriaView from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CustomCriteriaView:
        """Create an instance of CustomCriteriaView from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CustomCriteriaView.parse_obj(obj)

        _obj = CustomCriteriaView.parse_obj({
            "query": obj.get("query"),
            "type": obj.get("type")
        })
        return _obj

