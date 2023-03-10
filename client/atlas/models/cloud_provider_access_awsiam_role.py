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
from pydantic import BaseModel, Field, StrictStr, constr, validator
from atlas.models.cloud_provider_access_feature_usage import CloudProviderAccessFeatureUsage

class CloudProviderAccessAWSIAMRole(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    atlas_aws_account_arn: Optional[constr(strict=True, max_length=2048, min_length=20)] = Field(None, alias="atlasAWSAccountArn", description="Amazon Resource Name that identifies the Amazon Web Services (AWS) user account that MongoDB Cloud uses when it assumes the Identity and Access Management (IAM) role.")
    atlas_assumed_role_external_id: Optional[StrictStr] = Field(None, alias="atlasAssumedRoleExternalId", description="Unique external ID that MongoDB Cloud uses when it assumes the IAM role in your Amazon Web Services (AWS) account.")
    authorized_date: Optional[datetime] = Field(None, alias="authorizedDate", description="Date and time when someone authorized this role for the specified cloud service provider. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    created_date: Optional[datetime] = Field(None, alias="createdDate", description="Date and time when someone created this role for the specified cloud service provider. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    feature_usages: Optional[List[CloudProviderAccessFeatureUsage]] = Field(None, alias="featureUsages", description="List that contains application features associated with this Amazon Web Services (AWS) Identity and Access Management (IAM) role.")
    iam_assumed_role_arn: Optional[constr(strict=True, max_length=2048, min_length=20)] = Field(None, alias="iamAssumedRoleArn", description="Amazon Resource Name (ARN) that identifies the Amazon Web Services (AWS) Identity and Access Management (IAM) role that MongoDB Cloud assumes when it accesses resources in your AWS account.")
    role_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="roleId", description="Unique 24-hexadecimal digit string that identifies the role.")
    provider_name: StrictStr = Field(..., alias="providerName", description="Human-readable label that identifies the cloud provider of the role.")
    __properties = ["atlasAWSAccountArn", "atlasAssumedRoleExternalId", "authorizedDate", "createdDate", "featureUsages", "iamAssumedRoleArn", "roleId", "providerName"]

    @validator('role_id')
    def role_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('provider_name')
    def provider_name_validate_enum(cls, v):
        if v not in ('AWS'):
            raise ValueError("must validate the enum values ('AWS')")
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
    def from_json(cls, json_str: str) -> CloudProviderAccessAWSIAMRole:
        """Create an instance of CloudProviderAccessAWSIAMRole from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "atlas_aws_account_arn",
                            "atlas_assumed_role_external_id",
                            "authorized_date",
                            "created_date",
                            "feature_usages",
                            "role_id",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in feature_usages (list)
        _items = []
        if self.feature_usages:
            for _item in self.feature_usages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['featureUsages'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CloudProviderAccessAWSIAMRole:
        """Create an instance of CloudProviderAccessAWSIAMRole from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CloudProviderAccessAWSIAMRole.parse_obj(obj)

        _obj = CloudProviderAccessAWSIAMRole.parse_obj({
            "atlas_aws_account_arn": obj.get("atlasAWSAccountArn"),
            "atlas_assumed_role_external_id": obj.get("atlasAssumedRoleExternalId"),
            "authorized_date": obj.get("authorizedDate"),
            "created_date": obj.get("createdDate"),
            "feature_usages": [CloudProviderAccessFeatureUsage.from_dict(_item) for _item in obj.get("featureUsages")] if obj.get("featureUsages") is not None else None,
            "iam_assumed_role_arn": obj.get("iamAssumedRoleArn"),
            "role_id": obj.get("roleId"),
            "provider_name": obj.get("providerName")
        })
        return _obj

