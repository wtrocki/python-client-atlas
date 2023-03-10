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
from pydantic import BaseModel, Field, constr, validator
from atlas.models.role_assignment import RoleAssignment

class RoleMappingView(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    external_group_name: constr(strict=True, max_length=200, min_length=1) = Field(..., alias="externalGroupName", description="Unique human-readable label that identifies the identity provider group to whichthis role mapping applies.")
    id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, description="Unique 24-hexadecimal digit string that identifies this role mapping.")
    role_assignments: Optional[List[RoleAssignment]] = Field(None, alias="roleAssignments", description="Atlas roles and the unique identifiers of the groups and organizations associated with each role.", unique_items=True)
    __properties = ["externalGroupName", "id", "roleAssignments"]

    @validator('id')
    def id_validate_regular_expression(cls, v):
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
    def from_json(cls, json_str: str) -> RoleMappingView:
        """Create an instance of RoleMappingView from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in role_assignments (list)
        _items = []
        if self.role_assignments:
            for _item in self.role_assignments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['roleAssignments'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RoleMappingView:
        """Create an instance of RoleMappingView from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return RoleMappingView.parse_obj(obj)

        _obj = RoleMappingView.parse_obj({
            "external_group_name": obj.get("externalGroupName"),
            "id": obj.get("id"),
            "role_assignments": [RoleAssignment.from_dict(_item) for _item in obj.get("roleAssignments")] if obj.get("roleAssignments") is not None else None
        })
        return _obj

