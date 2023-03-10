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
from pydantic import BaseModel, Field, StrictStr, constr, validator
from atlas.models.data_lake_atlas_store_read_preference import DataLakeAtlasStoreReadPreference

class DataLakeAtlasStore(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    cluster_name: Optional[StrictStr] = Field(None, alias="clusterName", description="Human-readable label of the MongoDB Cloud cluster on which the store is based.")
    project_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="projectId", description="Unique 24-hexadecimal digit string that identifies the project.")
    read_preference: Optional[DataLakeAtlasStoreReadPreference] = Field(None, alias="readPreference")
    name: Optional[StrictStr] = Field(None, description="Human-readable label that identifies the data store. The **databases.[n].collections.[n].dataSources.[n].storeName** field references this values as part of the mapping configuration. To use MongoDB Cloud as a data store, the data lake requires a serverless instance or an `M10` or higher cluster.")
    provider: StrictStr = ...
    __properties = ["clusterName", "projectId", "readPreference", "name", "provider"]

    @validator('project_id')
    def project_id_validate_regular_expression(cls, v):
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
    def from_json(cls, json_str: str) -> DataLakeAtlasStore:
        """Create an instance of DataLakeAtlasStore from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "project_id",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of read_preference
        if self.read_preference:
            _dict['readPreference'] = self.read_preference.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DataLakeAtlasStore:
        """Create an instance of DataLakeAtlasStore from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DataLakeAtlasStore.parse_obj(obj)

        _obj = DataLakeAtlasStore.parse_obj({
            "cluster_name": obj.get("clusterName"),
            "project_id": obj.get("projectId"),
            "read_preference": DataLakeAtlasStoreReadPreference.from_dict(obj.get("readPreference")) if obj.get("readPreference") is not None else None,
            "name": obj.get("name"),
            "provider": obj.get("provider")
        })
        return _obj

