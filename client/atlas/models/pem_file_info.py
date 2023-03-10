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
from pydantic import BaseModel, Field, StrictStr
from atlas.models.x509_certificate import X509Certificate

class PemFileInfo(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    certificates: Optional[List[X509Certificate]] = None
    file_name: Optional[StrictStr] = Field(None, alias="fileName")
    __properties = ["certificates", "fileName"]

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
    def from_json(cls, json_str: str) -> PemFileInfo:
        """Create an instance of PemFileInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in certificates (list)
        _items = []
        if self.certificates:
            for _item in self.certificates:
                if _item:
                    _items.append(_item.to_dict())
            _dict['certificates'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PemFileInfo:
        """Create an instance of PemFileInfo from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return PemFileInfo.parse_obj(obj)

        _obj = PemFileInfo.parse_obj({
            "certificates": [X509Certificate.from_dict(_item) for _item in obj.get("certificates")] if obj.get("certificates") is not None else None,
            "file_name": obj.get("fileName")
        })
        return _obj

