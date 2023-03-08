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
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conint, validator

class ClusterDescriptionProcessArgs(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    default_read_concern: Optional[StrictStr] = Field('available', alias="defaultReadConcern", description="[Default level of acknowledgment requested from MongoDB for read operations](https://docs.mongodb.com/manual/reference/read-concern/) set for this cluster.  MongoDB 4.4 clusters default to `available`. MongoDB 5.0 and later clusters default to `local`.")
    default_write_concern: Optional[StrictStr] = Field('1', alias="defaultWriteConcern", description="[Default level of acknowledgment requested from MongoDB for write operations](https://docs.mongodb.com/manual/reference/write-concern/) set for this cluster.  MongoDB 4.4 clusters default to `1`. MongoDB 5.0 and later clusters default to `majority`.")
    fail_index_key_too_long: Optional[StrictBool] = Field(True, alias="failIndexKeyTooLong", description="Flag that indicates whether you can insert or update documents where all indexed entries don't exceed 1024 bytes. If you set this to false, [mongod](https://docs.mongodb.com/upcoming/reference/program/mongod/#mongodb-binary-bin.mongod) writes documents that exceed this limit but doesn't index them.")
    javascript_enabled: Optional[StrictBool] = Field(True, alias="javascriptEnabled", description="Flag that indicates whether the cluster allows execution of operations that perform server-side executions of JavaScript.")
    minimum_enabled_tls_protocol: Optional[StrictStr] = Field(None, alias="minimumEnabledTlsProtocol", description="Minimum Transport Layer Security (TLS) version that the cluster accepts for incoming connections. Clusters using TLS 1.0 or 1.1 should consider setting TLS 1.2 as the minimum TLS protocol version.")
    no_table_scan: Optional[StrictBool] = Field(False, alias="noTableScan", description="Flag that indicates whether the cluster disables executing any query that requires a collection scan to return results.")
    oplog_min_retention_hours: Optional[StrictFloat] = Field(None, alias="oplogMinRetentionHours", description="Minimum retention window for cluster's oplog expressed in hours. A value of null indicates that the cluster uses the default minimum oplog window that MongoDB Cloud calculates.")
    oplog_size_mb: Optional[StrictInt] = Field(None, alias="oplogSizeMB", description="Storage limit of cluster's oplog expressed in megabytes. A value of null indicates that the cluster uses the default oplog size that MongoDB Cloud calculates.")
    sample_refresh_interval_bi_connector: Optional[conint(strict=True, ge=0)] = Field(0, alias="sampleRefreshIntervalBIConnector", description="Interval in seconds at which the mongosqld process re-samples data to create its relational schema.")
    sample_size_bi_connector: Optional[conint(strict=True, ge=0)] = Field(1000, alias="sampleSizeBIConnector", description="Number of documents per database to sample when gathering schema information.")
    __properties = ["defaultReadConcern", "defaultWriteConcern", "failIndexKeyTooLong", "javascriptEnabled", "minimumEnabledTlsProtocol", "noTableScan", "oplogMinRetentionHours", "oplogSizeMB", "sampleRefreshIntervalBIConnector", "sampleSizeBIConnector"]

    @validator('default_read_concern')
    def default_read_concern_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('local', 'available', 'majority', 'linearizable', 'snapshot'):
            raise ValueError("must validate the enum values ('local', 'available', 'majority', 'linearizable', 'snapshot')")
        return v

    @validator('minimum_enabled_tls_protocol')
    def minimum_enabled_tls_protocol_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('TLS1_0', 'TLS1_1', 'TLS1_2'):
            raise ValueError("must validate the enum values ('TLS1_0', 'TLS1_1', 'TLS1_2')")
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
    def from_json(cls, json_str: str) -> ClusterDescriptionProcessArgs:
        """Create an instance of ClusterDescriptionProcessArgs from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # set to None if oplog_min_retention_hours (nullable) is None
        if self.oplog_min_retention_hours is None:
            _dict['oplogMinRetentionHours'] = None

        # set to None if oplog_size_mb (nullable) is None
        if self.oplog_size_mb is None:
            _dict['oplogSizeMB'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ClusterDescriptionProcessArgs:
        """Create an instance of ClusterDescriptionProcessArgs from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ClusterDescriptionProcessArgs.parse_obj(obj)

        _obj = ClusterDescriptionProcessArgs.parse_obj({
            "default_read_concern": obj.get("defaultReadConcern") if obj.get("defaultReadConcern") is not None else 'available',
            "default_write_concern": obj.get("defaultWriteConcern") if obj.get("defaultWriteConcern") is not None else '1',
            "fail_index_key_too_long": obj.get("failIndexKeyTooLong") if obj.get("failIndexKeyTooLong") is not None else True,
            "javascript_enabled": obj.get("javascriptEnabled") if obj.get("javascriptEnabled") is not None else True,
            "minimum_enabled_tls_protocol": obj.get("minimumEnabledTlsProtocol"),
            "no_table_scan": obj.get("noTableScan") if obj.get("noTableScan") is not None else False,
            "oplog_min_retention_hours": obj.get("oplogMinRetentionHours"),
            "oplog_size_mb": obj.get("oplogSizeMB"),
            "sample_refresh_interval_bi_connector": obj.get("sampleRefreshIntervalBIConnector") if obj.get("sampleRefreshIntervalBIConnector") is not None else 0,
            "sample_size_bi_connector": obj.get("sampleSizeBIConnector") if obj.get("sampleSizeBIConnector") is not None else 1000
        })
        return _obj
