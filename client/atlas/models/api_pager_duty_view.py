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

class ApiPagerDutyView(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    region: Optional[StrictStr] = Field(None, description="PagerDuty region that indicates the API Uniform Resource Locator (URL) to use.")
    service_key: StrictStr = Field(..., alias="serviceKey", description="Service key associated with your PagerDuty account.  **NOTE**: After you create a notification which requires an API or integration key, the key appears partially redacted when you:  * View or edit the alert through the Atlas UI.  * Query the alert for the notification through the Atlas Administration API.")
    type: Optional[StrictStr] = Field(None, description="Human-readable label that identifies the service to which you want to integrate with MongoDB Cloud. The value must match the third-party service integration type.")
    __properties = ["region", "serviceKey", "type"]

    @validator('region')
    def region_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('US', 'EU'):
            raise ValueError("must validate the enum values ('US', 'EU')")
        return v

    @validator('type')
    def type_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('PAGER_DUTY'):
            raise ValueError("must validate the enum values ('PAGER_DUTY')")
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
    def from_json(cls, json_str: str) -> ApiPagerDutyView:
        """Create an instance of ApiPagerDutyView from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiPagerDutyView:
        """Create an instance of ApiPagerDutyView from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ApiPagerDutyView.parse_obj(obj)

        _obj = ApiPagerDutyView.parse_obj({
            "region": obj.get("region"),
            "service_key": obj.get("serviceKey"),
            "type": obj.get("type")
        })
        return _obj

