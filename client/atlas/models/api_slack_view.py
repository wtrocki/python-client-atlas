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
from pydantic import BaseModel, Field, StrictStr, constr, validator

class ApiSlackView(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    api_token: StrictStr = Field(..., alias="apiToken", description="Key that allows MongoDB Cloud to access your Slack account.  **NOTE**: After you create a notification which requires an API or integration key, the key appears partially redacted when you:  * View or edit the alert through the Atlas UI.  * Query the alert for the notification through the Atlas Administration API.  **IMPORTANT**: Slack integrations now use the OAuth2 verification method and must  be initially configured, or updated from a legacy integration, through the Atlas  third-party service integrations page. Legacy tokens will soon no longer be  supported.")
    channel_name: Optional[constr(strict=True, max_length=80, min_length=1)] = Field(..., alias="channelName", description="Name of the Slack channel to which MongoDB Cloud sends alert notifications.")
    team_name: Optional[StrictStr] = Field(None, alias="teamName", description="Human-readable label that identifies your Slack team. Set this parameter when you configure a legacy Slack integration.")
    type: Optional[StrictStr] = Field(None, description="Human-readable label that identifies the service to which you want to integrate with MongoDB Cloud. The value must match the third-party service integration type.")
    __properties = ["apiToken", "channelName", "teamName", "type"]

    @validator('type')
    def type_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('SLACK'):
            raise ValueError("must validate the enum values ('SLACK')")
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
    def from_json(cls, json_str: str) -> ApiSlackView:
        """Create an instance of ApiSlackView from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if channel_name (nullable) is None
        if self.channel_name is None:
            _dict['channelName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiSlackView:
        """Create an instance of ApiSlackView from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ApiSlackView.parse_obj(obj)

        _obj = ApiSlackView.parse_obj({
            "api_token": obj.get("apiToken"),
            "channel_name": obj.get("channelName"),
            "team_name": obj.get("teamName"),
            "type": obj.get("type")
        })
        return _obj

