# coding: utf-8

"""
    MongoDB Atlas Administration API

    The MongoDB Atlas Administration API allows developers to manage all components in MongoDB Atlas. To learn more, review the [Administration API overview](https://www.mongodb.com/docs/atlas/api/atlas-admin-api/). This OpenAPI specification covers all of the collections with the exception of Alerts, Alert Configurations, and Events. Refer to the [legacy documentation](https://www.mongodb.com/docs/atlas/reference/api-resources/) for the specifications of these resources.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from atlas.models.data_lake_atlas_store import DataLakeAtlasStore
from atlas.models.data_lake_http_store import DataLakeHTTPStore
from atlas.models.data_lake_online_archive_store import DataLakeOnlineArchiveStore
from atlas.models.data_lake_s3_store import DataLakeS3Store
from typing import Any, List
from pydantic import StrictStr, Field

DATALAKESTORE_ONE_OF_SCHEMAS = ["DataLakeAtlasStore", "DataLakeHTTPStore", "DataLakeOnlineArchiveStore", "DataLakeS3Store"]

class DataLakeStore(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    # data type: DataLakeS3Store
    oneof_schema_1_validator: Optional[DataLakeS3Store] = None
    # data type: DataLakeOnlineArchiveStore
    oneof_schema_2_validator: Optional[DataLakeOnlineArchiveStore] = None
    # data type: DataLakeAtlasStore
    oneof_schema_3_validator: Optional[DataLakeAtlasStore] = None
    # data type: DataLakeHTTPStore
    oneof_schema_4_validator: Optional[DataLakeHTTPStore] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(DATALAKESTORE_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    discriminator_value_class_map = {
    }

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = cls()
        error_messages = []
        match = 0
        # validate data type: DataLakeS3Store
        if type(v) is not DataLakeS3Store:
            error_messages.append(f"Error! Input type `{type(v)}` is not `DataLakeS3Store`")
        else:
            match += 1

        # validate data type: DataLakeOnlineArchiveStore
        if type(v) is not DataLakeOnlineArchiveStore:
            error_messages.append(f"Error! Input type `{type(v)}` is not `DataLakeOnlineArchiveStore`")
        else:
            match += 1

        # validate data type: DataLakeAtlasStore
        if type(v) is not DataLakeAtlasStore:
            error_messages.append(f"Error! Input type `{type(v)}` is not `DataLakeAtlasStore`")
        else:
            match += 1

        # validate data type: DataLakeHTTPStore
        if type(v) is not DataLakeHTTPStore:
            error_messages.append(f"Error! Input type `{type(v)}` is not `DataLakeHTTPStore`")
        else:
            match += 1

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into DataLakeStore with oneOf schemas: DataLakeAtlasStore, DataLakeHTTPStore, DataLakeOnlineArchiveStore, DataLakeS3Store. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into DataLakeStore with oneOf schemas: DataLakeAtlasStore, DataLakeHTTPStore, DataLakeOnlineArchiveStore, DataLakeS3Store. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> DataLakeStore:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> DataLakeStore:
        """Returns the object represented by the json string"""
        instance = cls()
        error_messages = []
        match = 0

        # use oneOf discriminator to lookup the data type
        _data_type = json.loads(json_str).get("provider")
        if not _data_type:
            raise ValueError("Failed to lookup data type from the field `provider` in the input.")

        # check if data type is `DataLakeAtlasStore`
        if _data_type == "DataLakeAtlasStore":
            instance.actual_instance = DataLakeAtlasStore.from_json(json_str)
            return instance

        # check if data type is `DataLakeHTTPStore`
        if _data_type == "DataLakeHTTPStore":
            instance.actual_instance = DataLakeHTTPStore.from_json(json_str)
            return instance

        # check if data type is `DataLakeOnlineArchiveStore`
        if _data_type == "DataLakeOnlineArchiveStore":
            instance.actual_instance = DataLakeOnlineArchiveStore.from_json(json_str)
            return instance

        # check if data type is `DataLakeS3Store`
        if _data_type == "DataLakeS3Store":
            instance.actual_instance = DataLakeS3Store.from_json(json_str)
            return instance

        # check if data type is `DataLakeAtlasStore`
        if _data_type == "atlas":
            instance.actual_instance = DataLakeAtlasStore.from_json(json_str)
            return instance

        # check if data type is `DataLakeHTTPStore`
        if _data_type == "http":
            instance.actual_instance = DataLakeHTTPStore.from_json(json_str)
            return instance

        # check if data type is `DataLakeOnlineArchiveStore`
        if _data_type == "online_archive":
            instance.actual_instance = DataLakeOnlineArchiveStore.from_json(json_str)
            return instance

        # check if data type is `DataLakeS3Store`
        if _data_type == "s3":
            instance.actual_instance = DataLakeS3Store.from_json(json_str)
            return instance

        # deserialize data into DataLakeS3Store
        try:
            instance.actual_instance = DataLakeS3Store.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into DataLakeOnlineArchiveStore
        try:
            instance.actual_instance = DataLakeOnlineArchiveStore.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into DataLakeAtlasStore
        try:
            instance.actual_instance = DataLakeAtlasStore.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))
        # deserialize data into DataLakeHTTPStore
        try:
            instance.actual_instance = DataLakeHTTPStore.from_json(json_str)
            match += 1
        except ValidationError as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into DataLakeStore with oneOf schemas: DataLakeAtlasStore, DataLakeHTTPStore, DataLakeOnlineArchiveStore, DataLakeS3Store. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into DataLakeStore with oneOf schemas: DataLakeAtlasStore, DataLakeHTTPStore, DataLakeOnlineArchiveStore, DataLakeS3Store. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_json()
        else:
            return "null"

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_dict()
        else:
            return dict()

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())

