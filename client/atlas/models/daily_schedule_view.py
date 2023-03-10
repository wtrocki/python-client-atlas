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
from pydantic import BaseModel, Field, StrictStr, conint

class DailyScheduleView(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    end_hour: Optional[conint(strict=True, le=23, ge=0)] = Field(None, alias="endHour", description="Hour of the day when the scheduled window to run one online archive ends.")
    end_minute: Optional[conint(strict=True, le=59, ge=0)] = Field(None, alias="endMinute", description="Minute of the hour when the scheduled window to run one online archive ends.")
    start_hour: Optional[conint(strict=True, le=23, ge=0)] = Field(None, alias="startHour", description="Hour of the day when the when the scheduled window to run one online archive starts.")
    start_minute: Optional[conint(strict=True, le=59, ge=0)] = Field(None, alias="startMinute", description="Minute of the hour when the scheduled window to run one online archive starts.")
    type: StrictStr = ...
    __properties = ["endHour", "endMinute", "startHour", "startMinute", "type"]

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
    def from_json(cls, json_str: str) -> DailyScheduleView:
        """Create an instance of DailyScheduleView from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DailyScheduleView:
        """Create an instance of DailyScheduleView from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DailyScheduleView.parse_obj(obj)

        _obj = DailyScheduleView.parse_obj({
            "end_hour": obj.get("endHour"),
            "end_minute": obj.get("endMinute"),
            "start_hour": obj.get("startHour"),
            "start_minute": obj.get("startMinute"),
            "type": obj.get("type")
        })
        return _obj

