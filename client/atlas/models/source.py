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
from pydantic import BaseModel, Field, StrictBool, StrictStr, constr, validator

class Source(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    ca_certificate_path: Optional[StrictStr] = Field(None, alias="caCertificatePath", description="Path to the CA certificate that signed SSL certificates use to authenticate to the source cluster.")
    cluster_name: StrictStr = Field(..., alias="clusterName", description="Label that identifies the source cluster name.")
    group_id: constr(strict=True, max_length=24, min_length=24) = Field(..., alias="groupId", description="Unique 24-hexadecimal digit string that identifies the source project.")
    managed_authentication: StrictBool = Field(..., alias="managedAuthentication", description="Flag that indicates whether MongoDB Automation manages authentication to the source cluster. If true, do not provide values for username and password.")
    password: Optional[StrictStr] = Field(None, description="Password that authenticates the username to the source cluster.")
    ssl: StrictBool = Field(..., description="Flag that indicates whether you have SSL enabled.")
    username: Optional[StrictStr] = Field(None, description="Label that identifies the SCRAM-SHA user that connects to the source cluster.")
    __properties = ["caCertificatePath", "clusterName", "groupId", "managedAuthentication", "password", "ssl", "username"]

    @validator('group_id')
    def group_id_validate_regular_expression(cls, v):
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
    def from_json(cls, json_str: str) -> Source:
        """Create an instance of Source from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Source:
        """Create an instance of Source from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Source.parse_obj(obj)

        _obj = Source.parse_obj({
            "ca_certificate_path": obj.get("caCertificatePath"),
            "cluster_name": obj.get("clusterName"),
            "group_id": obj.get("groupId"),
            "managed_authentication": obj.get("managedAuthentication"),
            "password": obj.get("password"),
            "ssl": obj.get("ssl"),
            "username": obj.get("username")
        })
        return _obj

