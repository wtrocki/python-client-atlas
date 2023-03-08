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
from pydantic import BaseModel, Field, StrictInt, StrictStr, constr, validator
from atlas.models.link_atlas import LinkAtlas

class ApiHostViewAtlas(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    created: Optional[datetime] = Field(None, description="Date and time when MongoDB Cloud created this MongoDB process. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    group_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project. The project contains MongoDB processes that you want to return. The MongoDB process can be either the `mongod` or `mongos`.")
    hostname: Optional[constr(strict=True)] = Field(None, description="Hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (`mongod` or `mongos`).")
    id: Optional[constr(strict=True)] = Field(None, description="Combination of hostname and Internet Assigned Numbers Authority (IANA) port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (`mongod` or `mongos`). The port must be the IANA port on which the MongoDB process listens for requests.")
    last_ping: Optional[datetime] = Field(None, alias="lastPing", description="Date and time when MongoDB Cloud received the last ping for this MongoDB process. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    links: Optional[List[LinkAtlas]] = Field(None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    port: Optional[StrictInt] = Field(None, description="Internet Assigned Numbers Authority (IANA) port on which the MongoDB process listens for requests.")
    replica_set_name: Optional[StrictStr] = Field(None, alias="replicaSetName", description="Human-readable label that identifies the replica set that contains this process. This resource returns this parameter if this process belongs to a replica set.")
    type_name: Optional[StrictStr] = Field(None, alias="typeName", description="Type of MongoDB process that MongoDB Cloud tracks. MongoDB Cloud returns new processes as **NO_DATA** until MongoDB Cloud completes deploying the process.")
    user_alias: Optional[StrictStr] = Field(None, alias="userAlias", description="Human-readable label that identifies the cluster node. MongoDB Cloud sets this hostname usually to the standard hostname for the cluster node. It appears in the connection string for a cluster instead of the value of the hostname parameter.")
    version: Optional[constr(strict=True)] = Field(None, description="Version of MongoDB that this process runs.")
    __properties = ["created", "groupId", "hostname", "id", "lastPing", "links", "port", "replicaSetName", "typeName", "userAlias", "version"]

    @validator('group_id')
    def group_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('hostname')
    def hostname_validate_regular_expression(cls, v):
        if not re.match(r"^([0-9]{1,3}\.){3}[0-9]{1,3}|([0-9a-f]{1,4}\:){7}([0-9a-f]{1,4})|(([a-z0-9]+\.){1,10}[a-z]+)?$", v):
            raise ValueError(r"must validate the regular expression /^([0-9]{1,3}\.){3}[0-9]{1,3}|([0-9a-f]{1,4}\:){7}([0-9a-f]{1,4})|(([a-z0-9]+\.){1,10}[a-z]+)?$/")
        return v

    @validator('id')
    def id_validate_regular_expression(cls, v):
        if not re.match(r"^([0-9]{1,3}\.){3}[0-9]{1,3}|([0-9a-f]{1,4}\:){7}([0-9a-f]{1,4})|(([a-z0-9]+\.){1,10}[a-z]+)?(\:[0-9]{4,5})$", v):
            raise ValueError(r"must validate the regular expression /^([0-9]{1,3}\.){3}[0-9]{1,3}|([0-9a-f]{1,4}\:){7}([0-9a-f]{1,4})|(([a-z0-9]+\.){1,10}[a-z]+)?(\:[0-9]{4,5})$/")
        return v

    @validator('type_name')
    def type_name_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('REPLICA_PRIMARY', 'REPLICA_SECONDARY', 'RECOVERING', 'SHARD_MONGOS', 'SHARD_CONFIG', 'SHARD_STANDALONE', 'SHARD_PRIMARY', 'SHARD_SECONDARY', 'NO_DATA'):
            raise ValueError("must validate the enum values ('REPLICA_PRIMARY', 'REPLICA_SECONDARY', 'RECOVERING', 'SHARD_MONGOS', 'SHARD_CONFIG', 'SHARD_STANDALONE', 'SHARD_PRIMARY', 'SHARD_SECONDARY', 'NO_DATA')")
        return v

    @validator('version')
    def version_validate_regular_expression(cls, v):
        if not re.match(r"([\d]+\.[\d]+\.[\d]+)", v):
            raise ValueError(r"must validate the regular expression /([\d]+\.[\d]+\.[\d]+)/")
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
    def from_json(cls, json_str: str) -> ApiHostViewAtlas:
        """Create an instance of ApiHostViewAtlas from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "created",
                            "group_id",
                            "hostname",
                            "id",
                            "last_ping",
                            "links",
                            "port",
                            "replica_set_name",
                            "type_name",
                            "user_alias",
                            "version",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiHostViewAtlas:
        """Create an instance of ApiHostViewAtlas from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ApiHostViewAtlas.parse_obj(obj)

        _obj = ApiHostViewAtlas.parse_obj({
            "created": obj.get("created"),
            "group_id": obj.get("groupId"),
            "hostname": obj.get("hostname"),
            "id": obj.get("id"),
            "last_ping": obj.get("lastPing"),
            "links": [LinkAtlas.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None,
            "port": obj.get("port"),
            "replica_set_name": obj.get("replicaSetName"),
            "type_name": obj.get("typeName"),
            "user_alias": obj.get("userAlias"),
            "version": obj.get("version")
        })
        return _obj

