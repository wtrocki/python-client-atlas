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
from typing import Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator

class DataFederationQueryLimit(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    current_usage: Optional[StrictInt] = Field(None, alias="currentUsage", description="Amount that indicates the current usage of the limit.")
    default_limit: Optional[StrictInt] = Field(None, alias="defaultLimit", description="Default value of the limit.")
    last_modified_date: Optional[datetime] = Field(None, alias="lastModifiedDate", description="Only used for Data Federation limits. Timestamp that indicates when this usage limit was last modified. This field uses the ISO 8601 timestamp format in UTC.")
    maximum_limit: Optional[StrictInt] = Field(None, alias="maximumLimit", description="Maximum value of the limit.")
    name: StrictStr = Field(..., description="Human-readable label that identifies the user-managed limit to modify.")
    overrun_policy: Optional[StrictStr] = Field(None, alias="overrunPolicy", description="Only used for Data Federation limits. Action to take when the usage limit is exceeded. If limit span is set to QUERY, this is ignored because MongoDB Cloud stops the query when it exceeds the usage limit.")
    value: StrictInt = Field(..., description="Amount to set the limit to.")
    __properties = ["currentUsage", "defaultLimit", "lastModifiedDate", "maximumLimit", "name", "overrunPolicy", "value"]

    @validator('overrun_policy')
    def overrun_policy_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('BLOCK', 'BLOCK_AND_KILL'):
            raise ValueError("must validate the enum values ('BLOCK', 'BLOCK_AND_KILL')")
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
    def from_json(cls, json_str: str) -> DataFederationQueryLimit:
        """Create an instance of DataFederationQueryLimit from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "current_usage",
                            "default_limit",
                            "last_modified_date",
                            "maximum_limit",
                            "name",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DataFederationQueryLimit:
        """Create an instance of DataFederationQueryLimit from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DataFederationQueryLimit.parse_obj(obj)

        _obj = DataFederationQueryLimit.parse_obj({
            "current_usage": obj.get("currentUsage"),
            "default_limit": obj.get("defaultLimit"),
            "last_modified_date": obj.get("lastModifiedDate"),
            "maximum_limit": obj.get("maximumLimit"),
            "name": obj.get("name"),
            "overrun_policy": obj.get("overrunPolicy"),
            "value": obj.get("value")
        })
        return _obj
