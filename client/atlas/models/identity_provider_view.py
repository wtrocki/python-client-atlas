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
from atlas.models.connected_org_config_view import ConnectedOrgConfigView
from atlas.models.pem_file_info_view import PemFileInfoView

class IdentityProviderView(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    acs_url: Optional[StrictStr] = Field(None, alias="acsUrl", description="URL that points to where to send the SAML response.")
    associated_domains: Optional[List[StrictStr]] = Field(None, alias="associatedDomains", description="List that contains the domains associated with the identity provider.", unique_items=True)
    associated_orgs: Optional[List[ConnectedOrgConfigView]] = Field(None, alias="associatedOrgs", description="List that contains the connected organization configurations associated with the identity provider.", unique_items=True)
    audience_uri: Optional[StrictStr] = Field(None, alias="audienceUri", description="Unique string that identifies the intended audience of the SAML assertion.")
    display_name: Optional[StrictStr] = Field(None, alias="displayName", description="Human-readable label that identifies the identity provider.")
    issuer_uri: Optional[StrictStr] = Field(None, alias="issuerUri", description="Unique string that identifies the issuer of the SAML Assertion.")
    okta_idp_id: constr(strict=True, max_length=20, min_length=20) = Field(..., alias="oktaIdpId", description="Unique 20-hexadecimal digit string that identifies the identity provider.")
    pem_file_info: Optional[PemFileInfoView] = Field(None, alias="pemFileInfo")
    request_binding: Optional[StrictStr] = Field(None, alias="requestBinding", description="SAML Authentication Request Protocol HTTP method binding (POST or REDIRECT) that Federated Authentication uses to send the authentication request.")
    response_signature_algorithm: Optional[StrictStr] = Field(None, alias="responseSignatureAlgorithm", description="Signature algorithm that Federated Authentication uses to encrypt the identity provider signature.")
    sso_debug_enabled: Optional[StrictBool] = Field(None, alias="ssoDebugEnabled", description="Flag that indicates whether the identity provider has SSO debug enabled.")
    sso_url: Optional[StrictStr] = Field(None, alias="ssoUrl", description="URL that points to the receiver of the SAML authentication request.")
    status: Optional[StrictStr] = Field(None, description="String enum that indicates whether the identity provider is active.")
    __properties = ["acsUrl", "associatedDomains", "associatedOrgs", "audienceUri", "displayName", "issuerUri", "oktaIdpId", "pemFileInfo", "requestBinding", "responseSignatureAlgorithm", "ssoDebugEnabled", "ssoUrl", "status"]

    @validator('okta_idp_id')
    def okta_idp_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{20})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{20})$/")
        return v

    @validator('request_binding')
    def request_binding_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('HTTP-POST', 'HTTP-REDIRECT'):
            raise ValueError("must validate the enum values ('HTTP-POST', 'HTTP-REDIRECT')")
        return v

    @validator('response_signature_algorithm')
    def response_signature_algorithm_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('SHA-1', 'SHA-256'):
            raise ValueError("must validate the enum values ('SHA-1', 'SHA-256')")
        return v

    @validator('status')
    def status_validate_enum(cls, v):
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
    def from_json(cls, json_str: str) -> IdentityProviderView:
        """Create an instance of IdentityProviderView from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in associated_orgs (list)
        _items = []
        if self.associated_orgs:
            for _item in self.associated_orgs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['associatedOrgs'] = _items
        # override the default output from pydantic by calling `to_dict()` of pem_file_info
        if self.pem_file_info:
            _dict['pemFileInfo'] = self.pem_file_info.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> IdentityProviderView:
        """Create an instance of IdentityProviderView from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return IdentityProviderView.parse_obj(obj)

        _obj = IdentityProviderView.parse_obj({
            "acs_url": obj.get("acsUrl"),
            "associated_domains": obj.get("associatedDomains"),
            "associated_orgs": [ConnectedOrgConfigView.from_dict(_item) for _item in obj.get("associatedOrgs")] if obj.get("associatedOrgs") is not None else None,
            "audience_uri": obj.get("audienceUri"),
            "display_name": obj.get("displayName"),
            "issuer_uri": obj.get("issuerUri"),
            "okta_idp_id": obj.get("oktaIdpId"),
            "pem_file_info": PemFileInfoView.from_dict(obj.get("pemFileInfo")) if obj.get("pemFileInfo") is not None else None,
            "request_binding": obj.get("requestBinding"),
            "response_signature_algorithm": obj.get("responseSignatureAlgorithm"),
            "sso_debug_enabled": obj.get("ssoDebugEnabled"),
            "sso_url": obj.get("ssoUrl"),
            "status": obj.get("status")
        })
        return _obj

