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
from pydantic import BaseModel, Field, StrictBool

class OrganizationSettings(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    api_access_list_required: Optional[StrictBool] = Field(None, alias="apiAccessListRequired", description="Flag that indicates whether to require API operations to originate from an IP Address added to the API access list for the specified organization.")
    multi_factor_auth_required: Optional[StrictBool] = Field(None, alias="multiFactorAuthRequired", description="Flag that indicates whether to require users to set up Multi-Factor Authentication (MFA) before accessing the specified organization. To learn more, see: https://www.mongodb.com/docs/atlas/security-multi-factor-authentication/.")
    restrict_employee_access: Optional[StrictBool] = Field(None, alias="restrictEmployeeAccess", description="Flag that indicates whether to block MongoDB Support from accessing Atlas infrastructure for any deployment in the specified organization without explicit permission. Once this setting is turned on, you can grant MongoDB Support a 24-hour bypass access to the Atlas deployment to resolve support issues. To learn more, see: https://www.mongodb.com/docs/atlas/security-restrict-support-access/.")
    __properties = ["apiAccessListRequired", "multiFactorAuthRequired", "restrictEmployeeAccess"]

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
    def from_json(cls, json_str: str) -> OrganizationSettings:
        """Create an instance of OrganizationSettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrganizationSettings:
        """Create an instance of OrganizationSettings from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return OrganizationSettings.parse_obj(obj)

        _obj = OrganizationSettings.parse_obj({
            "api_access_list_required": obj.get("apiAccessListRequired"),
            "multi_factor_auth_required": obj.get("multiFactorAuthRequired"),
            "restrict_employee_access": obj.get("restrictEmployeeAccess")
        })
        return _obj

