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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conint, validator

class PagerDutyNotificationView(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    delay_min: Optional[StrictInt] = Field(None, alias="delayMin", description="Number of minutes that MongoDB Cloud waits after detecting an alert condition before it sends out the first notification.")
    interval_min: Optional[conint(strict=True, ge=5)] = Field(None, alias="intervalMin", description="Number of minutes to wait between successive notifications. MongoDB Cloud sends notifications until someone acknowledges the unacknowledged alert.  PagerDuty, VictorOps, and OpsGenie notifications don't return this element. Configure and manage the notification interval within each of those services.")
    region: Optional[StrictStr] = Field('US', description="PagerDuty region that indicates which API Uniform Resource Locator (URL) to use.")
    service_key: Optional[StrictStr] = Field(None, alias="serviceKey", description="PagerDuty service key that MongoDB Cloud needs to send notifications via PagerDuty. The resource requires this parameter when `\"notifications.[n].typeName\" : \"PAGER_DUTY\"`. If the key later becomes invalid, MongoDB Cloud sends an email to the project owners. If the key remains invalid, MongoDB Cloud removes it.  **NOTE**: After you create a notification which requires an API or integration key, the key appears partially redacted when you:  * View or edit the alert through the Atlas UI.  * Query the alert for the notification through the Atlas Administration API.")
    type_name: StrictStr = Field(..., alias="typeName", description="Human-readable label that displays the alert notification type.")
    __properties = ["delayMin", "intervalMin", "region", "serviceKey", "typeName"]

    @validator('region')
    def region_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('US', 'EU'):
            raise ValueError("must validate the enum values ('US', 'EU')")
        return v

    @validator('type_name')
    def type_name_validate_enum(cls, v):
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
    def from_json(cls, json_str: str) -> PagerDutyNotificationView:
        """Create an instance of PagerDutyNotificationView from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PagerDutyNotificationView:
        """Create an instance of PagerDutyNotificationView from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PagerDutyNotificationView.parse_obj(obj)

        _obj = PagerDutyNotificationView.parse_obj({
            "delay_min": obj.get("delayMin"),
            "interval_min": obj.get("intervalMin"),
            "region": obj.get("region") if obj.get("region") is not None else 'US',
            "service_key": obj.get("serviceKey"),
            "type_name": obj.get("typeName")
        })
        return _obj

