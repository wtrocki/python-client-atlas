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
from pydantic import BaseModel, Field, StrictStr, constr, validator

class AWSPrivateLinkConnection(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    endpoint_service_name: Optional[constr(strict=True)] = Field(None, alias="endpointServiceName", description="Unique string that identifies the Amazon Web Services (AWS) PrivateLink endpoint service. MongoDB Cloud returns null while it creates the endpoint service.")
    error_message: Optional[StrictStr] = Field(None, alias="errorMessage", description="Error message returned when requesting private connection resource. The resource returns `null` if the request succeeded.")
    id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, description="Unique 24-hexadecimal digit string that identifies the Private Endpoint Service.")
    interface_endpoints: Optional[List[constr(strict=True, max_length=24, min_length=24)]] = Field(None, alias="interfaceEndpoints", description="List of strings that identify private endpoint interfaces applied to the specified project.")
    region_name: Optional[StrictStr] = Field(None, alias="regionName", description="Cloud provider region that manages this Private Endpoint Service.")
    status: Optional[StrictStr] = Field(None, description="State of the Private Endpoint Service connection when MongoDB Cloud received this request.")
    __properties = ["endpointServiceName", "errorMessage", "id", "interfaceEndpoints", "regionName", "status"]

    @validator('endpoint_service_name')
    def endpoint_service_name_validate_regular_expression(cls, v):
        if not re.match(r"^com\.amazonaws\.vpce\.[a-z-0-9]+\.vpce-svc-[0-9a-f]{17}", v):
            raise ValueError(r"must validate the regular expression /^com\.amazonaws\.vpce\.[a-z-0-9]+\.vpce-svc-[0-9a-f]{17}/")
        return v

    @validator('id')
    def id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('status')
    def status_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('INITIATING', 'AVAILABLE', 'WAITING_FOR_USER', 'FAILED', 'DELETING'):
            raise ValueError("must validate the enum values ('INITIATING', 'AVAILABLE', 'WAITING_FOR_USER', 'FAILED', 'DELETING')")
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
    def from_json(cls, json_str: str) -> AWSPrivateLinkConnection:
        """Create an instance of AWSPrivateLinkConnection from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "endpoint_service_name",
                            "error_message",
                            "id",
                            "interface_endpoints",
                            "region_name",
                            "status",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AWSPrivateLinkConnection:
        """Create an instance of AWSPrivateLinkConnection from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AWSPrivateLinkConnection.parse_obj(obj)

        _obj = AWSPrivateLinkConnection.parse_obj({
            "endpoint_service_name": obj.get("endpointServiceName"),
            "error_message": obj.get("errorMessage"),
            "id": obj.get("id"),
            "interface_endpoints": obj.get("interfaceEndpoints"),
            "region_name": obj.get("regionName"),
            "status": obj.get("status")
        })
        return _obj

