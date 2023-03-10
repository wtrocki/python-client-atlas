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
from pydantic import BaseModel, Field, StrictBool, StrictStr

class GoogleCloudKMS(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    enabled: Optional[StrictBool] = Field(None, description="Flag that indicates whether someone enabled encryption at rest for the specified  project. To disable encryption at rest using customer key management and remove the configuration details, pass only this parameter with a value of `false`.")
    key_version_resource_id: Optional[StrictStr] = Field(None, alias="keyVersionResourceID", description="Resource path that displays the key version resource ID for your Google Cloud KMS.")
    service_account_key: Optional[StrictStr] = Field(None, alias="serviceAccountKey", description="JavaScript Object Notation (JSON) object that contains the Google Cloud Key Management Service (KMS). Format the JSON as a string and not as an object.")
    valid: Optional[StrictBool] = Field(None, description="Flag that indicates whether the Google Cloud Key Management Service (KMS) encryption key can encrypt and decrypt data.")
    __properties = ["enabled", "keyVersionResourceID", "serviceAccountKey", "valid"]

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
    def from_json(cls, json_str: str) -> GoogleCloudKMS:
        """Create an instance of GoogleCloudKMS from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "valid",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GoogleCloudKMS:
        """Create an instance of GoogleCloudKMS from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return GoogleCloudKMS.parse_obj(obj)

        _obj = GoogleCloudKMS.parse_obj({
            "enabled": obj.get("enabled"),
            "key_version_resource_id": obj.get("keyVersionResourceID"),
            "service_account_key": obj.get("serviceAccountKey"),
            "valid": obj.get("valid")
        })
        return _obj

