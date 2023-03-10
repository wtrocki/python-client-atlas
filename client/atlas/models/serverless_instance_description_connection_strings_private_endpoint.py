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
from pydantic import BaseModel, Field, StrictStr, validator
from atlas.models.serverless_instance_description_connection_strings_private_endpoint_endpoint import ServerlessInstanceDescriptionConnectionStringsPrivateEndpointEndpoint

class ServerlessInstanceDescriptionConnectionStringsPrivateEndpoint(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    endpoints: Optional[List[ServerlessInstanceDescriptionConnectionStringsPrivateEndpointEndpoint]] = Field(None, description="List that contains the private endpoints through which you connect to MongoDB Cloud when you use **connectionStrings.privateEndpoint[n].srvConnectionString**.")
    srv_connection_string: Optional[StrictStr] = Field(None, alias="srvConnectionString", description="Private endpoint-aware connection string that uses the `mongodb+srv://` protocol to connect to MongoDB Cloud through a private endpoint. The `mongodb+srv` protocol tells the driver to look up the seed list of hosts in the Domain Name System (DNS).")
    type: Optional[StrictStr] = Field(None, description="MongoDB process type to which your application connects.")
    __properties = ["endpoints", "srvConnectionString", "type"]

    @validator('type')
    def type_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('MONGOS'):
            raise ValueError("must validate the enum values ('MONGOS')")
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
    def from_json(cls, json_str: str) -> ServerlessInstanceDescriptionConnectionStringsPrivateEndpoint:
        """Create an instance of ServerlessInstanceDescriptionConnectionStringsPrivateEndpoint from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "endpoints",
                            "srv_connection_string",
                            "type",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in endpoints (list)
        _items = []
        if self.endpoints:
            for _item in self.endpoints:
                if _item:
                    _items.append(_item.to_dict())
            _dict['endpoints'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ServerlessInstanceDescriptionConnectionStringsPrivateEndpoint:
        """Create an instance of ServerlessInstanceDescriptionConnectionStringsPrivateEndpoint from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ServerlessInstanceDescriptionConnectionStringsPrivateEndpoint.parse_obj(obj)

        _obj = ServerlessInstanceDescriptionConnectionStringsPrivateEndpoint.parse_obj({
            "endpoints": [ServerlessInstanceDescriptionConnectionStringsPrivateEndpointEndpoint.from_dict(_item) for _item in obj.get("endpoints")] if obj.get("endpoints") is not None else None,
            "srv_connection_string": obj.get("srvConnectionString"),
            "type": obj.get("type")
        })
        return _obj

