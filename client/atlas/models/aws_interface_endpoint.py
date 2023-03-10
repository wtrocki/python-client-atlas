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
from pydantic import BaseModel, Field, StrictBool, StrictStr, constr, validator

class AWSInterfaceEndpoint(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    connection_status: Optional[StrictStr] = Field(None, alias="connectionStatus", description="State of the Amazon Web Service PrivateLink connection when MongoDB Cloud received this request.")
    delete_requested: Optional[StrictBool] = Field(None, alias="deleteRequested", description="Flag that indicates whether MongoDB Cloud received a request to remove the specified private endpoint from the private endpoint service.")
    error_message: Optional[StrictStr] = Field(None, alias="errorMessage", description="Error message returned when requesting private connection resource. The resource returns `null` if the request succeeded.")
    interface_endpoint_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="interfaceEndpointId", description="Unique 24-hexadecimal digit string that identifies the interface endpoint.")
    __properties = ["connectionStatus", "deleteRequested", "errorMessage", "interfaceEndpointId"]

    @validator('connection_status')
    def connection_status_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('PENDING_ACCEPTANCE', 'PENDING', 'AVAILABLE', 'REJECTED', 'DELETING'):
            raise ValueError("must validate the enum values ('PENDING_ACCEPTANCE', 'PENDING', 'AVAILABLE', 'REJECTED', 'DELETING')")
        return v

    @validator('interface_endpoint_id')
    def interface_endpoint_id_validate_regular_expression(cls, v):
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
    def from_json(cls, json_str: str) -> AWSInterfaceEndpoint:
        """Create an instance of AWSInterfaceEndpoint from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "connection_status",
                            "delete_requested",
                            "error_message",
                            "interface_endpoint_id",
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> AWSInterfaceEndpoint:
        """Create an instance of AWSInterfaceEndpoint from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return AWSInterfaceEndpoint.parse_obj(obj)

        _obj = AWSInterfaceEndpoint.parse_obj({
            "connection_status": obj.get("connectionStatus"),
            "delete_requested": obj.get("deleteRequested"),
            "error_message": obj.get("errorMessage"),
            "interface_endpoint_id": obj.get("interfaceEndpointId")
        })
        return _obj

