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



from pydantic import BaseModel, Field, StrictStr, validator

class Role(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    collection_name: StrictStr = Field(..., alias="collectionName", description="Collection on which this role applies.")
    database_name: StrictStr = Field(..., alias="databaseName", description="Database against which the database user authenticates. Database users must provide both a username and authentication database to log into MongoDB.")
    role_name: StrictStr = Field(..., alias="roleName", description="Human-readable label that identifies a group of privileges assigned to a database user. This value can either be a built-in role or a custom role.")
    __properties = ["collectionName", "databaseName", "roleName"]

    @validator('role_name')
    def role_name_validate_enum(cls, v):
        if v not in ('atlasAdmin', 'backup', 'clusterMonitor', 'dbAdmin', 'dbAdminAnyDatabase', 'enableSharding', 'read', 'readAnyDatabase', 'readWrite', 'readWriteAnyDatabase', '<a custom role name>'):
            raise ValueError("must validate the enum values ('atlasAdmin', 'backup', 'clusterMonitor', 'dbAdmin', 'dbAdminAnyDatabase', 'enableSharding', 'read', 'readAnyDatabase', 'readWrite', 'readWriteAnyDatabase', '<a custom role name>')")
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
    def from_json(cls, json_str: str) -> Role:
        """Create an instance of Role from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Role:
        """Create an instance of Role from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Role.parse_obj(obj)

        _obj = Role.parse_obj({
            "collection_name": obj.get("collectionName"),
            "database_name": obj.get("databaseName"),
            "role_name": obj.get("roleName")
        })
        return _obj
