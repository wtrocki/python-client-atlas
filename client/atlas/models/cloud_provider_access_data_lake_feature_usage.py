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
from pydantic import BaseModel, Field, StrictStr, validator
from atlas.models.cloud_provider_access_feature_usage_data_lake_feature_id import CloudProviderAccessFeatureUsageDataLakeFeatureId

class CloudProviderAccessDataLakeFeatureUsage(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    feature_id: Optional[CloudProviderAccessFeatureUsageDataLakeFeatureId] = Field(None, alias="featureId")
    feature_type: Optional[StrictStr] = Field(None, alias="featureType", description="Human-readable label that describes one MongoDB Cloud feature linked to this Amazon Web Services (AWS) Identity and Access Management (IAM) role.")
    __properties = ["featureId", "featureType"]

    @validator('feature_type')
    def feature_type_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('ATLAS_DATA_LAKE', 'ENCRYPTION_AT_REST', 'EXPORT_SNAPSHOT'):
            raise ValueError("must validate the enum values ('ATLAS_DATA_LAKE', 'ENCRYPTION_AT_REST', 'EXPORT_SNAPSHOT')")
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
    def from_json(cls, json_str: str) -> CloudProviderAccessDataLakeFeatureUsage:
        """Create an instance of CloudProviderAccessDataLakeFeatureUsage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "feature_type",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of feature_id
        if self.feature_id:
            _dict['featureId'] = self.feature_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CloudProviderAccessDataLakeFeatureUsage:
        """Create an instance of CloudProviderAccessDataLakeFeatureUsage from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CloudProviderAccessDataLakeFeatureUsage.parse_obj(obj)

        _obj = CloudProviderAccessDataLakeFeatureUsage.parse_obj({
            "feature_id": CloudProviderAccessFeatureUsageDataLakeFeatureId.from_dict(obj.get("featureId")) if obj.get("featureId") is not None else None,
            "feature_type": obj.get("featureType")
        })
        return _obj

