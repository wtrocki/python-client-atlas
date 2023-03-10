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
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, constr, validator
from atlas.models.api_policy_item_view import ApiPolicyItemView

class DataProtectionSettings(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    copy_protection_enabled: Optional[StrictBool] = Field(None, alias="copyProtectionEnabled", description="Flag that indicates whether to enable additional backup copies for the cluster.")
    encryption_at_rest_enabled: Optional[StrictBool] = Field(None, alias="encryptionAtRestEnabled", description="Flag that indicates whether Encryption at Rest using Customer Key  Management is required for all clusters with a Data Protection Policy.")
    on_demand_policy_item: Optional[ApiPolicyItemView] = Field(None, alias="onDemandPolicyItem")
    pit_enabled: Optional[StrictBool] = Field(None, alias="pitEnabled", description="Flag that indicates whether the cluster uses Continuous Cloud Backups with a Data Protection Policy.")
    project_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="projectId", description="Unique 24-hexadecimal digit string that identifies the project for the Data Protection Policy.")
    restore_window_days: Optional[StrictInt] = Field(None, alias="restoreWindowDays", description="Number of previous days that you can restore back to with Continuous Cloud Backup with a Data Protection Policy. You must specify a positive, non-zero integer, and the maximum retention window can't exceed the hourly retention time. This parameter applies only to Continuous Cloud Backups with a Data Protection Policy.")
    scheduled_policy_items: Optional[List[ApiPolicyItemView]] = Field(None, alias="scheduledPolicyItems", description="List that contains the specifications for one scheduled policy.")
    state: Optional[StrictStr] = Field(None, description="Label that indicates the state of the Data Protection Policy settings.")
    updated_date: Optional[datetime] = Field(None, alias="updatedDate", description="ISO 8601 timestamp format in UTC that indicates when the user updated the Data Protection Policy settings.")
    updated_user: Optional[StrictStr] = Field(None, alias="updatedUser", description="Email address that identifies the user who updated the Data Protection Policy settings.")
    __properties = ["copyProtectionEnabled", "encryptionAtRestEnabled", "onDemandPolicyItem", "pitEnabled", "projectId", "restoreWindowDays", "scheduledPolicyItems", "state", "updatedDate", "updatedUser"]

    @validator('project_id')
    def project_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('state')
    def state_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('ACTIVE', 'ENABLING', 'UPDATING', 'DISABLING'):
            raise ValueError("must validate the enum values ('ACTIVE', 'ENABLING', 'UPDATING', 'DISABLING')")
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
    def from_json(cls, json_str: str) -> DataProtectionSettings:
        """Create an instance of DataProtectionSettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "state",
                            "updated_date",
                            "updated_user",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of on_demand_policy_item
        if self.on_demand_policy_item:
            _dict['onDemandPolicyItem'] = self.on_demand_policy_item.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in scheduled_policy_items (list)
        _items = []
        if self.scheduled_policy_items:
            for _item in self.scheduled_policy_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['scheduledPolicyItems'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DataProtectionSettings:
        """Create an instance of DataProtectionSettings from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DataProtectionSettings.parse_obj(obj)

        _obj = DataProtectionSettings.parse_obj({
            "copy_protection_enabled": obj.get("copyProtectionEnabled"),
            "encryption_at_rest_enabled": obj.get("encryptionAtRestEnabled"),
            "on_demand_policy_item": ApiPolicyItemView.from_dict(obj.get("onDemandPolicyItem")) if obj.get("onDemandPolicyItem") is not None else None,
            "pit_enabled": obj.get("pitEnabled"),
            "project_id": obj.get("projectId"),
            "restore_window_days": obj.get("restoreWindowDays"),
            "scheduled_policy_items": [ApiPolicyItemView.from_dict(_item) for _item in obj.get("scheduledPolicyItems")] if obj.get("scheduledPolicyItems") is not None else None,
            "state": obj.get("state"),
            "updated_date": obj.get("updatedDate"),
            "updated_user": obj.get("updatedUser")
        })
        return _obj

