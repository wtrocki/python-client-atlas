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
from atlas.models.host_matcher_field import HostMatcherField
from atlas.models.matcher_host_type import MatcherHostType

class HostMatcherView(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    field_name: Optional[HostMatcherField] = Field(None, alias="fieldName")
    operator: Optional[StrictStr] = Field(None, description="Comparison operator to apply when checking the current metric value against **matcher[n].value**.")
    value: Optional[MatcherHostType] = None
    __properties = ["fieldName", "operator", "value"]

    @validator('operator')
    def operator_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('EQUALS', 'CONTAINS', 'STARTS_WITH', 'ENDS_WITH', 'NOT_EQUALS', 'NOT_CONTAINS', 'REGEX'):
            raise ValueError("must validate the enum values ('EQUALS', 'CONTAINS', 'STARTS_WITH', 'ENDS_WITH', 'NOT_EQUALS', 'NOT_CONTAINS', 'REGEX')")
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
    def from_json(cls, json_str: str) -> HostMatcherView:
        """Create an instance of HostMatcherView from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HostMatcherView:
        """Create an instance of HostMatcherView from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return HostMatcherView.parse_obj(obj)

        _obj = HostMatcherView.parse_obj({
            "field_name": obj.get("fieldName"),
            "operator": obj.get("operator"),
            "value": obj.get("value")
        })
        return _obj

