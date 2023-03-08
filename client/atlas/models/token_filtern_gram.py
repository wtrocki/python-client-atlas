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
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator

class TokenFilternGram(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    max_gram: StrictInt = Field(..., alias="maxGram", description="Value that specifies the maximum length of generated n-grams. This value must be greater than or equal to **minGram**.")
    min_gram: StrictInt = Field(..., alias="minGram", description="Value that specifies the minimum length of generated n-grams. This value must be less than or equal to **maxGram**.")
    term_not_in_bounds: Optional[StrictStr] = Field('omit', alias="termNotInBounds", description="Value that indicates whether to index tokens shorter than **minGram** or longer than **maxGram**.")
    type: StrictStr = Field(..., description="Human-readable label that identifies this token filter type.")
    __properties = ["maxGram", "minGram", "termNotInBounds", "type"]

    @validator('term_not_in_bounds')
    def term_not_in_bounds_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('omit', 'include'):
            raise ValueError("must validate the enum values ('omit', 'include')")
        return v

    @validator('type')
    def type_validate_enum(cls, v):
        if v not in ('nGram'):
            raise ValueError("must validate the enum values ('nGram')")
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
    def from_json(cls, json_str: str) -> TokenFilternGram:
        """Create an instance of TokenFilternGram from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TokenFilternGram:
        """Create an instance of TokenFilternGram from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return TokenFilternGram.parse_obj(obj)

        _obj = TokenFilternGram.parse_obj({
            "max_gram": obj.get("maxGram"),
            "min_gram": obj.get("minGram"),
            "term_not_in_bounds": obj.get("termNotInBounds") if obj.get("termNotInBounds") is not None else 'omit',
            "type": obj.get("type")
        })
        return _obj
