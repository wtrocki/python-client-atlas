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

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class X509CertificateView(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    not_after: Optional[datetime] = Field(None, alias="notAfter", description="Latest date that the certificate is valid.")
    not_before: Optional[datetime] = Field(None, alias="notBefore", description="Earliest date that the certificate is valid.")
    __properties = ["notAfter", "notBefore"]

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
    def from_json(cls, json_str: str) -> X509CertificateView:
        """Create an instance of X509CertificateView from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> X509CertificateView:
        """Create an instance of X509CertificateView from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return X509CertificateView.parse_obj(obj)

        _obj = X509CertificateView.parse_obj({
            "not_after": obj.get("notAfter"),
            "not_before": obj.get("notBefore")
        })
        return _obj
