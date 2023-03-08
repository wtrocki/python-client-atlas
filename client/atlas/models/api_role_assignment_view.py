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

class ApiRoleAssignmentView(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    group_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project to which this role belongs. You can set a value for this parameter or **orgId** but not both in the same request.")
    org_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="orgId", description="Unique 24-hexadecimal digit string that identifies the organization to which this role belongs. You can set a value for this parameter or **groupId** but not both in the same request.")
    role_name: Optional[StrictStr] = Field(None, alias="roleName", description="Human-readable label that identifies the collection of privileges that MongoDB Cloud grants a specific API key, MongoDB Cloud user, or MongoDB Cloud team. These roles include organization- and project-level roles.  Organization Roles  * ORG_OWNER * ORG_MEMBER * ORG_GROUP_CREATOR * ORG_BILLING_ADMIN * ORG_READ_ONLY  Project Roles  * GROUP_CLUSTER_MANAGER * GROUP_DATA_ACCESS_ADMIN * GROUP_DATA_ACCESS_READ_ONLY * GROUP_DATA_ACCESS_READ_WRITE * GROUP_OWNER * GROUP_READ_ONLY * GROUP_SEARCH_INDEX_EDITOR  ")
    __properties = ["groupId", "orgId", "roleName"]

    @validator('group_id')
    def group_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('org_id')
    def org_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('role_name')
    def role_name_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('ORG_OWNER', 'ORG_MEMBER', 'ORG_GROUP_CREATOR', 'ORG_BILLING_ADMIN', 'ORG_READ_ONLY', 'GROUP_CLUSTER_MANAGER', 'GROUP_DATA_ACCESS_ADMIN', 'GROUP_DATA_ACCESS_READ_ONLY', 'GROUP_DATA_ACCESS_READ_WRITE', 'GROUP_OWNER', 'GROUP_READ_ONLY', 'GROUP_SEARCH_INDEX_EDITOR'):
            raise ValueError("must validate the enum values ('ORG_OWNER', 'ORG_MEMBER', 'ORG_GROUP_CREATOR', 'ORG_BILLING_ADMIN', 'ORG_READ_ONLY', 'GROUP_CLUSTER_MANAGER', 'GROUP_DATA_ACCESS_ADMIN', 'GROUP_DATA_ACCESS_READ_ONLY', 'GROUP_DATA_ACCESS_READ_WRITE', 'GROUP_OWNER', 'GROUP_READ_ONLY', 'GROUP_SEARCH_INDEX_EDITOR')")
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
    def from_json(cls, json_str: str) -> ApiRoleAssignmentView:
        """Create an instance of ApiRoleAssignmentView from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiRoleAssignmentView:
        """Create an instance of ApiRoleAssignmentView from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ApiRoleAssignmentView.parse_obj(obj)

        _obj = ApiRoleAssignmentView.parse_obj({
            "group_id": obj.get("groupId"),
            "org_id": obj.get("orgId"),
            "role_name": obj.get("roleName")
        })
        return _obj

