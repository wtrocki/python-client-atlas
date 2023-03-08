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
from pydantic import BaseModel, Field, StrictStr, conint
from atlas.models.data_lake_database_collection import DataLakeDatabaseCollection
from atlas.models.data_lake_view import DataLakeView

class DataLakeDatabase(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    collections: Optional[List[DataLakeDatabaseCollection]] = Field(None, description="Array of collections and data sources that map to a ``stores`` data store.")
    max_wildcard_collections: Optional[conint(strict=True, le=1000, ge=1)] = Field(100, alias="maxWildcardCollections", description="Maximum number of wildcard collections in the database. This only applies to S3 data sources.")
    name: Optional[StrictStr] = Field(None, description="Human-readable label that identifies the database to which the data lake maps data.")
    views: Optional[List[DataLakeView]] = Field(None, description="Array of aggregation pipelines that apply to the collection. This only applies to S3 data sources.")
    __properties = ["collections", "maxWildcardCollections", "name", "views"]

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
    def from_json(cls, json_str: str) -> DataLakeDatabase:
        """Create an instance of DataLakeDatabase from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in collections (list)
        _items = []
        if self.collections:
            for _item in self.collections:
                if _item:
                    _items.append(_item.to_dict())
            _dict['collections'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in views (list)
        _items = []
        if self.views:
            for _item in self.views:
                if _item:
                    _items.append(_item.to_dict())
            _dict['views'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DataLakeDatabase:
        """Create an instance of DataLakeDatabase from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DataLakeDatabase.parse_obj(obj)

        _obj = DataLakeDatabase.parse_obj({
            "collections": [DataLakeDatabaseCollection.from_dict(_item) for _item in obj.get("collections")] if obj.get("collections") is not None else None,
            "max_wildcard_collections": obj.get("maxWildcardCollections") if obj.get("maxWildcardCollections") is not None else 100,
            "name": obj.get("name"),
            "views": [DataLakeView.from_dict(_item) for _item in obj.get("views")] if obj.get("views") is not None else None
        })
        return _obj
