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

class ApiNewRelicView(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    account_id: constr(strict=True, max_length=40, min_length=40) = Field(..., alias="accountId", description="Unique 40-hexadecimal digit string that identifies your New Relic account.")
    license_key: constr(strict=True, max_length=40, min_length=40) = Field(..., alias="licenseKey", description="Unique 40-hexadecimal digit string that identifies your New Relic license.  **IMPORTANT**: Effective Wednesday, June 16th, 2021, New Relic no longer supports the plugin-based integration with MongoDB. We do not recommend that you sign up for the plugin-based integration. To learn more, see the <a href=\"https://discuss.newrelic.com/t/new-relic-plugin-eol-wednesday-june-16th-2021/127267\" target=\"_blank\">New Relic Plugin EOL Statement</a> Consider configuring an alternative monitoring integration before June 16th to maintain visibility into your MongoDB deployments.")
    read_token: StrictStr = Field(..., alias="readToken", description="Query key used to access your New Relic account.")
    type: Optional[StrictStr] = Field(None, description="Human-readable label that identifies the service to which you want to integrate with MongoDB Cloud. The value must match the third-party service integration type.")
    write_token: StrictStr = Field(..., alias="writeToken", description="Insert key associated with your New Relic account.")
    __properties = ["accountId", "licenseKey", "readToken", "type", "writeToken"]

    @validator('account_id')
    def account_id_validate_regular_expression(cls, v):
        if not re.match(r"^([0-9a-f]){40}$", v):
            raise ValueError(r"must validate the regular expression /^([0-9a-f]){40}$/")
        return v

    @validator('license_key')
    def license_key_validate_regular_expression(cls, v):
        if not re.match(r"^([0-9a-f]){40}$", v):
            raise ValueError(r"must validate the regular expression /^([0-9a-f]){40}$/")
        return v

    @validator('type')
    def type_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('NEW_RELIC'):
            raise ValueError("must validate the enum values ('NEW_RELIC')")
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
    def from_json(cls, json_str: str) -> ApiNewRelicView:
        """Create an instance of ApiNewRelicView from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiNewRelicView:
        """Create an instance of ApiNewRelicView from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ApiNewRelicView.parse_obj(obj)

        _obj = ApiNewRelicView.parse_obj({
            "account_id": obj.get("accountId"),
            "license_key": obj.get("licenseKey"),
            "read_token": obj.get("readToken"),
            "type": obj.get("type"),
            "write_token": obj.get("writeToken")
        })
        return _obj
