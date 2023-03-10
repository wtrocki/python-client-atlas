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



from pydantic import BaseModel, Field, StrictStr, constr, validator

class InheritedRole(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    db: StrictStr = Field(..., description="Human-readable label that identifies the database on which someone grants the action to one MongoDB user.")
    role: constr(strict=True) = Field(..., description="Human-readable label that identifies the role inherited. Set this value to `admin` for every role except `read` or `readWrite`.")
    __properties = ["db", "role"]

    @validator('role')
    def role_validate_regular_expression(cls, v):
        if not re.match(r"^\b(?!xgen-)([0-9A-Za-z_\-]+)\b(?<!\atlasAdmin|read|readWrite|dbAdmin|dbOwner|userAdmin|clusterAdmin|clusterManager|clusterMonitor|hostManager|backup|restore|readAnyDatabase|readWriteAnyDatabase|userAdminAnyDatabase|dbAdminAnyDatabase|root|__system)$", v):
            raise ValueError(r"must validate the regular expression /^\b(?!xgen-)([0-9A-Za-z_\-]+)\b(?<!\atlasAdmin|read|readWrite|dbAdmin|dbOwner|userAdmin|clusterAdmin|clusterManager|clusterMonitor|hostManager|backup|restore|readAnyDatabase|readWriteAnyDatabase|userAdminAnyDatabase|dbAdminAnyDatabase|root|__system)$/")
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
    def from_json(cls, json_str: str) -> InheritedRole:
        """Create an instance of InheritedRole from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> InheritedRole:
        """Create an instance of InheritedRole from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return InheritedRole.parse_obj(obj)

        _obj = InheritedRole.parse_obj({
            "db": obj.get("db"),
            "role": obj.get("role")
        })
        return _obj

