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
from pydantic import BaseModel, Field, StrictBool, StrictStr, constr, validator

class OrgFederationSettingsView(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    federated_domains: Optional[List[StrictStr]] = Field(None, alias="federatedDomains", description="List of domains associated with the organization's identity provider.", unique_items=True)
    has_role_mappings: Optional[StrictBool] = Field(None, alias="hasRoleMappings", description="Flag that indicates whether this organization has role mappings configured.")
    id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, description="Unique 24-hexadecimal digit string that identifies this federation.")
    identity_provider_id: Optional[constr(strict=True, max_length=20, min_length=20)] = Field(None, alias="identityProviderId", description="Unique 20-hexadecimal digit string that identifies the identity provider connected to this organization.")
    identity_provider_status: Optional[StrictStr] = Field(None, alias="identityProviderStatus", description="String enum that indicates whether the identity provider is active.")
    __properties = ["federatedDomains", "hasRoleMappings", "id", "identityProviderId", "identityProviderStatus"]

    @validator('id')
    def id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('identity_provider_id')
    def identity_provider_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{20})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{20})$/")
        return v

    @validator('identity_provider_status')
    def identity_provider_status_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('ACTIVE', 'INACTIVE'):
            raise ValueError("must validate the enum values ('ACTIVE', 'INACTIVE')")
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
    def from_json(cls, json_str: str) -> OrgFederationSettingsView:
        """Create an instance of OrgFederationSettingsView from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OrgFederationSettingsView:
        """Create an instance of OrgFederationSettingsView from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return OrgFederationSettingsView.parse_obj(obj)

        _obj = OrgFederationSettingsView.parse_obj({
            "federated_domains": obj.get("federatedDomains"),
            "has_role_mappings": obj.get("hasRoleMappings"),
            "id": obj.get("id"),
            "identity_provider_id": obj.get("identityProviderId"),
            "identity_provider_status": obj.get("identityProviderStatus")
        })
        return _obj

