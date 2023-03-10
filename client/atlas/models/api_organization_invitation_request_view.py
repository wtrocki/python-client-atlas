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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, constr, validator

class ApiOrganizationInvitationRequestView(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    roles: Optional[List[StrictStr]] = Field(None, description="One or more organization or project level roles to assign to the MongoDB Cloud user.", unique_items=True)
    team_ids: Optional[List[constr(strict=True, max_length=24, min_length=24)]] = Field(None, alias="teamIds", description="List of teams to which you want to invite the desired MongoDB Cloud user.", unique_items=True)
    username: Optional[StrictStr] = Field(None, description="Email address that belongs to the desired MongoDB Cloud user.")
    __properties = ["roles", "teamIds", "username"]

    @validator('roles')
    def roles_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('ORG_OWNER', 'ORG_MEMBER', 'ORG_GROUP_CREATOR', 'ORG_BILLING_ADMIN', 'ORG_READ_ONLY'):
            raise ValueError("must validate the enum values ('ORG_OWNER', 'ORG_MEMBER', 'ORG_GROUP_CREATOR', 'ORG_BILLING_ADMIN', 'ORG_READ_ONLY')")
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
    def from_json(cls, json_str: str) -> ApiOrganizationInvitationRequestView:
        """Create an instance of ApiOrganizationInvitationRequestView from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiOrganizationInvitationRequestView:
        """Create an instance of ApiOrganizationInvitationRequestView from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ApiOrganizationInvitationRequestView.parse_obj(obj)

        _obj = ApiOrganizationInvitationRequestView.parse_obj({
            "roles": obj.get("roles"),
            "team_ids": obj.get("teamIds"),
            "username": obj.get("username")
        })
        return _obj

