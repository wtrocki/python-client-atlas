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
from pydantic import BaseModel, Field, StrictBool, StrictStr, validator

class DataLakeDatabaseDataSource(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    allow_insecure: Optional[StrictBool] = Field(False, alias="allowInsecure", description="Flag that validates the scheme in the specified URLs. If `true`, allows insecure `HTTP` scheme, doesn't verify the server's certificate chain and hostname, and accepts any certificate with any hostname presented by the server. If `false`, allows secure `HTTPS` scheme only.")
    collection: Optional[StrictStr] = Field(None, description="Human-readable label that identifies the collection in the database. For creating a wildcard (`*`) collection, you must omit this parameter.")
    collection_regex: Optional[StrictStr] = Field(None, alias="collectionRegex", description="Regex pattern to use for creating the wildcard (*) collection. To learn more about the regex syntax, see [Go programming language](https://pkg.go.dev/regexp).")
    database: Optional[StrictStr] = Field(None, description="Human-readable label that identifies the database, which contains the collection in the cluster. You must omit this parameter to generate wildcard (`*`) collections for dynamically generated databases.")
    database_regex: Optional[StrictStr] = Field(None, alias="databaseRegex", description="Regex pattern to use for creating the wildcard (*) database. To learn more about the regex syntax, see [Go programming language](https://pkg.go.dev/regexp).")
    default_format: Optional[StrictStr] = Field(None, alias="defaultFormat", description="File format that MongoDB Cloud uses if it encounters a file without a file extension while searching **storeName**.")
    path: Optional[StrictStr] = Field(None, description="File path that controls how MongoDB Cloud searches for and parses files in the **storeName** before mapping them to a collection.Specify ``/`` to capture all files and folders from the ``prefix`` path.")
    provenance_field_name: Optional[StrictStr] = Field(None, alias="provenanceFieldName", description="Name for the field that includes the provenance of the documents in the results. MongoDB Cloud returns different fields in the results for each supported provider.")
    store_name: Optional[StrictStr] = Field(None, alias="storeName", description="Human-readable label that identifies the data store that MongoDB Cloud maps to the collection.")
    urls: Optional[List[StrictStr]] = Field(None, description="URLs of the publicly accessible data files. You can't specify URLs that require authentication. Atlas Data Lake creates a partition for each URL. If empty or omitted, Data Lake uses the URLs from the store specified in the **dataSources.storeName** parameter.")
    __properties = ["allowInsecure", "collection", "collectionRegex", "database", "databaseRegex", "defaultFormat", "path", "provenanceFieldName", "storeName", "urls"]

    @validator('default_format')
    def default_format_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('.avro', '.avro.bz2', '.avro.gz', '.bson', '.bson.bz2', '.bson.gz', '.bsonx', '.csv', '.csv.bz2', '.csv.gz', '.json', '.json.bz2', '.json.gz', '.orc', '.parquet', '.tsv', '.tsv.bz2', '.tsv.gz'):
            raise ValueError("must validate the enum values ('.avro', '.avro.bz2', '.avro.gz', '.bson', '.bson.bz2', '.bson.gz', '.bsonx', '.csv', '.csv.bz2', '.csv.gz', '.json', '.json.bz2', '.json.gz', '.orc', '.parquet', '.tsv', '.tsv.bz2', '.tsv.gz')")
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
    def from_json(cls, json_str: str) -> DataLakeDatabaseDataSource:
        """Create an instance of DataLakeDatabaseDataSource from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> DataLakeDatabaseDataSource:
        """Create an instance of DataLakeDatabaseDataSource from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return DataLakeDatabaseDataSource.parse_obj(obj)

        _obj = DataLakeDatabaseDataSource.parse_obj({
            "allow_insecure": obj.get("allowInsecure") if obj.get("allowInsecure") is not None else False,
            "collection": obj.get("collection"),
            "collection_regex": obj.get("collectionRegex"),
            "database": obj.get("database"),
            "database_regex": obj.get("databaseRegex"),
            "default_format": obj.get("defaultFormat"),
            "path": obj.get("path"),
            "provenance_field_name": obj.get("provenanceFieldName"),
            "store_name": obj.get("storeName"),
            "urls": obj.get("urls")
        })
        return _obj

