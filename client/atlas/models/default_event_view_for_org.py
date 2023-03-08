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
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr, constr, validator
from atlas.models.link import Link
from atlas.models.raw import Raw

class DefaultEventViewForOrg(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    api_key_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="apiKeyId", description="Unique 24-hexadecimal digit string that identifies the [API Key](https://dochub.mongodb.org/core/atlas-create-prog-api-key) that triggered the event. If this resource returns this parameter, it doesn't return the **userId** parameter.")
    created: datetime = Field(..., description="Date and time when this event occurred. This parameter expresses its value in the <a href=\"https://en.wikipedia.org/wiki/ISO_8601\" target=\"_blank\" rel=\"noopener noreferrer\">ISO 8601</a> timestamp format in UTC.")
    event_type_name: StrictStr = Field(..., alias="eventTypeName", description="Unique identifier of event type.")
    group_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project in which the event occurred. The **eventId** identifies the specific event.")
    id: constr(strict=True, max_length=24, min_length=24) = Field(..., description="Unique 24-hexadecimal digit string that identifies the event.")
    is_global_admin: Optional[StrictBool] = Field(False, alias="isGlobalAdmin", description="Flag that indicates whether a MongoDB employee triggered the specified event.")
    links: Optional[List[Link]] = Field(None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    org_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="orgId", description="Unique 24-hexadecimal digit string that identifies the organization to which these events apply.")
    public_key: Optional[StrictStr] = Field(None, alias="publicKey", description="Public part of the [API Key](https://dochub.mongodb.org/core/atlas-create-prog-api-key) that triggered the event. If this resource returns this parameter, it doesn't return the **username** parameter.")
    raw: Optional[Raw] = None
    remote_address: Optional[constr(strict=True)] = Field(None, alias="remoteAddress", description="IPv4 or IPv6 address from which the user triggered this event.")
    user_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="userId", description="Unique 24-hexadecimal digit string that identifies the console user who triggered the event. If this resource returns this parameter, it doesn't return the **apiKeyId** parameter.")
    username: Optional[StrictStr] = Field(None, description="Email address for the user who triggered this event. If this resource returns this parameter, it doesn't return the **publicApiKey** parameter.")
    __properties = ["apiKeyId", "created", "eventTypeName", "groupId", "id", "isGlobalAdmin", "links", "orgId", "publicKey", "raw", "remoteAddress", "userId", "username"]

    @validator('api_key_id')
    def api_key_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('event_type_name')
    def event_type_name_validate_enum(cls, v):
        if v not in ('FEDERATION_SETTINGS_CREATED', 'FEDERATION_SETTINGS_DELETED', 'FEDERATION_SETTINGS_UPDATED', 'IDENTITY_PROVIDER_CREATED', 'IDENTITY_PROVIDER_UPDATED', 'IDENTITY_PROVIDER_DELETED', 'IDENTITY_PROVIDER_ACTIVATED', 'IDENTITY_PROVIDER_DEACTIVATED', 'DOMAINS_ASSOCIATED', 'DOMAIN_CREATED', 'DOMAIN_DELETED', 'DOMAIN_VERIFIED', 'ORG_SETTINGS_CONFIGURED', 'ORG_SETTINGS_UPDATED', 'ORG_SETTINGS_DELETED', 'RESTRICT_ORG_MEMBERSHIP_ENABLED', 'RESTRICT_ORG_MEMBERSHIP_DISABLED', 'ROLE_MAPPING_CREATED', 'ROLE_MAPPING_UPDATED', 'ROLE_MAPPING_DELETED', 'GROUP_DELETED', 'GROUP_CREATED', 'GROUP_MOVED', 'MLAB_MIGRATION_COMPLETED', 'MLAB_MIGRATION_TARGET_CLUSTER_CREATED', 'MLAB_MIGRATION_DATABASE_USERS_IMPORTED', 'MLAB_MIGRATION_IP_WHITELIST_IMPORTED', 'MLAB_MIGRATION_TARGET_CLUSTER_SET', 'MLAB_MIGRATION_DATABASE_RENAMED', 'MLAB_MIGRATION_LIVE_IMPORT_STARTED', 'MLAB_MIGRATION_LIVE_IMPORT_READY_FOR_CUTOVER', 'MLAB_MIGRATION_LIVE_IMPORT_CUTOVER_COMPLETE', 'MLAB_MIGRATION_LIVE_IMPORT_ERROR', 'MLAB_MIGRATION_LIVE_IMPORT_CANCELLED', 'MLAB_MIGRATION_DUMP_AND_RESTORE_TEST_STARTED', 'MLAB_MIGRATION_DUMP_AND_RESTORE_TEST_SKIPPED', 'MLAB_MIGRATION_DUMP_AND_RESTORE_STARTED', 'MLAB_MIGRATION_SUPPORT_PLAN_SELECTED', 'MLAB_MIGRATION_SUPPORT_PLAN_OPTED_OUT', 'AWS_SELF_SERVE_ACCOUNT_LINKED', 'AWS_SELF_SERVE_ACCOUNT_LINK_PENDING', 'AWS_SELF_SERVE_ACCOUNT_CANCELLED', 'AWS_SELF_SERVE_ACCOUNT_LINK_FAILED', 'GCP_SELF_SERVE_ACCOUNT_LINK_PENDING', 'GCP_SELF_SERVE_ACCOUNT_LINK_FAILED', 'AZURE_SELF_SERVE_ACCOUNT_LINKED', 'AZURE_SELF_SERVE_ACCOUNT_LINK_PENDING', 'AZURE_SELF_SERVE_ACCOUNT_CANCELLED', 'AZURE_SELF_SERVE_ACCOUNT_LINK_FAILED', 'GCP_SELF_SERVE_ACCOUNT_LINKED', 'GCP_SELF_SERVE_ACCOUNT_CANCELLED', 'ORG_POLICY_CREATED', 'ORG_POLICY_DELETED', 'ORG_POLICY_EDITED', 'ORG_POLICY_CLONED', 'SUPPORT_EMAILS_SENT_SUCCESSFULLY', 'SUPPORT_EMAILS_SENT_FAILURE'):
            raise ValueError("must validate the enum values ('FEDERATION_SETTINGS_CREATED', 'FEDERATION_SETTINGS_DELETED', 'FEDERATION_SETTINGS_UPDATED', 'IDENTITY_PROVIDER_CREATED', 'IDENTITY_PROVIDER_UPDATED', 'IDENTITY_PROVIDER_DELETED', 'IDENTITY_PROVIDER_ACTIVATED', 'IDENTITY_PROVIDER_DEACTIVATED', 'DOMAINS_ASSOCIATED', 'DOMAIN_CREATED', 'DOMAIN_DELETED', 'DOMAIN_VERIFIED', 'ORG_SETTINGS_CONFIGURED', 'ORG_SETTINGS_UPDATED', 'ORG_SETTINGS_DELETED', 'RESTRICT_ORG_MEMBERSHIP_ENABLED', 'RESTRICT_ORG_MEMBERSHIP_DISABLED', 'ROLE_MAPPING_CREATED', 'ROLE_MAPPING_UPDATED', 'ROLE_MAPPING_DELETED', 'GROUP_DELETED', 'GROUP_CREATED', 'GROUP_MOVED', 'MLAB_MIGRATION_COMPLETED', 'MLAB_MIGRATION_TARGET_CLUSTER_CREATED', 'MLAB_MIGRATION_DATABASE_USERS_IMPORTED', 'MLAB_MIGRATION_IP_WHITELIST_IMPORTED', 'MLAB_MIGRATION_TARGET_CLUSTER_SET', 'MLAB_MIGRATION_DATABASE_RENAMED', 'MLAB_MIGRATION_LIVE_IMPORT_STARTED', 'MLAB_MIGRATION_LIVE_IMPORT_READY_FOR_CUTOVER', 'MLAB_MIGRATION_LIVE_IMPORT_CUTOVER_COMPLETE', 'MLAB_MIGRATION_LIVE_IMPORT_ERROR', 'MLAB_MIGRATION_LIVE_IMPORT_CANCELLED', 'MLAB_MIGRATION_DUMP_AND_RESTORE_TEST_STARTED', 'MLAB_MIGRATION_DUMP_AND_RESTORE_TEST_SKIPPED', 'MLAB_MIGRATION_DUMP_AND_RESTORE_STARTED', 'MLAB_MIGRATION_SUPPORT_PLAN_SELECTED', 'MLAB_MIGRATION_SUPPORT_PLAN_OPTED_OUT', 'AWS_SELF_SERVE_ACCOUNT_LINKED', 'AWS_SELF_SERVE_ACCOUNT_LINK_PENDING', 'AWS_SELF_SERVE_ACCOUNT_CANCELLED', 'AWS_SELF_SERVE_ACCOUNT_LINK_FAILED', 'GCP_SELF_SERVE_ACCOUNT_LINK_PENDING', 'GCP_SELF_SERVE_ACCOUNT_LINK_FAILED', 'AZURE_SELF_SERVE_ACCOUNT_LINKED', 'AZURE_SELF_SERVE_ACCOUNT_LINK_PENDING', 'AZURE_SELF_SERVE_ACCOUNT_CANCELLED', 'AZURE_SELF_SERVE_ACCOUNT_LINK_FAILED', 'GCP_SELF_SERVE_ACCOUNT_LINKED', 'GCP_SELF_SERVE_ACCOUNT_CANCELLED', 'ORG_POLICY_CREATED', 'ORG_POLICY_DELETED', 'ORG_POLICY_EDITED', 'ORG_POLICY_CLONED', 'SUPPORT_EMAILS_SENT_SUCCESSFULLY', 'SUPPORT_EMAILS_SENT_FAILURE')")
        return v

    @validator('group_id')
    def group_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('id')
    def id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('org_id')
    def org_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('remote_address')
    def remote_address_validate_regular_expression(cls, v):
        if not re.match(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}|([0-9a-f]{1,4}\:){7}[0-9a-f]{1,4}$", v):
            raise ValueError(r"must validate the regular expression /^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}|([0-9a-f]{1,4}\:){7}[0-9a-f]{1,4}$/")
        return v

    @validator('user_id')
    def user_id_validate_regular_expression(cls, v):
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
    def from_json(cls, json_str: str) -> DefaultEventViewForOrg:
        """Create an instance of DefaultEventViewForOrg from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "api_key_id",
                            "created",
                            "group_id",
                            "id",
                            "is_global_admin",
                            "links",
                            "org_id",
                            "public_key",
                            "remote_address",
                            "user_id",
                            "username",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of raw
        if self.raw:
            _dict['raw'] = self.raw.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DefaultEventViewForOrg:
        """Create an instance of DefaultEventViewForOrg from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DefaultEventViewForOrg.parse_obj(obj)

        _obj = DefaultEventViewForOrg.parse_obj({
            "api_key_id": obj.get("apiKeyId"),
            "created": obj.get("created"),
            "event_type_name": obj.get("eventTypeName"),
            "group_id": obj.get("groupId"),
            "id": obj.get("id"),
            "is_global_admin": obj.get("isGlobalAdmin") if obj.get("isGlobalAdmin") is not None else False,
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None,
            "org_id": obj.get("orgId"),
            "public_key": obj.get("publicKey"),
            "raw": Raw.from_dict(obj.get("raw")) if obj.get("raw") is not None else None,
            "remote_address": obj.get("remoteAddress"),
            "user_id": obj.get("userId"),
            "username": obj.get("username")
        })
        return _obj
