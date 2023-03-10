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

class FederatedUserView(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    email_address: StrictStr = Field(..., alias="emailAddress", description="Email address of the MongoDB Cloud user linked to the federated organization.")
    federation_settings_id: constr(strict=True, max_length=24, min_length=24) = Field(..., alias="federationSettingsId", description="Unique 24-hexadecimal digit string that identifies the federation to which this MongoDB Cloud user belongs.")
    first_name: StrictStr = Field(..., alias="firstName", description="First or given name that belongs to the MongoDB Cloud user.")
    last_name: StrictStr = Field(..., alias="lastName", description="Last name, family name, or surname that belongs to the MongoDB Cloud user.")
    user_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="userId", description="Unique 24-hexadecimal digit string that identifies this user.")
    __properties = ["emailAddress", "federationSettingsId", "firstName", "lastName", "userId"]

    @validator('federation_settings_id')
    def federation_settings_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('user_id')
    def user_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
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
    def from_json(cls, json_str: str) -> FederatedUserView:
        """Create an instance of FederatedUserView from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "user_id",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FederatedUserView:
        """Create an instance of FederatedUserView from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return FederatedUserView.parse_obj(obj)

        _obj = FederatedUserView.parse_obj({
            "email_address": obj.get("emailAddress"),
            "federation_settings_id": obj.get("federationSettingsId"),
            "first_name": obj.get("firstName"),
            "last_name": obj.get("lastName"),
            "user_id": obj.get("userId")
        })
        return _obj

