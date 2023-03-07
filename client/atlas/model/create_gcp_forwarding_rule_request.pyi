# coding: utf-8

"""
    MongoDB Atlas Administration API

    The MongoDB Atlas Administration API allows developers to manage all components in MongoDB Atlas. To learn more, review the [Administration API overview](https://www.mongodb.com/docs/atlas/api/atlas-admin-api/). This OpenAPI specification covers all of the collections with the exception of Alerts, Alert Configurations, and Events. Refer to the [legacy documentation](https://www.mongodb.com/docs/atlas/reference/api-resources/) for the specifications of these resources.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from atlas import schemas  # noqa: F401


class CreateGCPForwardingRuleRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            endpointName = schemas.StrSchema
            
            
            class ipAddress(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "endpointName": endpointName,
                "ipAddress": ipAddress,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endpointName"]) -> MetaOapg.properties.endpointName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipAddress"]) -> MetaOapg.properties.ipAddress: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["endpointName", "ipAddress", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endpointName"]) -> typing.Union[MetaOapg.properties.endpointName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipAddress"]) -> typing.Union[MetaOapg.properties.ipAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["endpointName", "ipAddress", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        endpointName: typing.Union[MetaOapg.properties.endpointName, str, schemas.Unset] = schemas.unset,
        ipAddress: typing.Union[MetaOapg.properties.ipAddress, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateGCPForwardingRuleRequest':
        return super().__new__(
            cls,
            *_args,
            endpointName=endpointName,
            ipAddress=ipAddress,
            _configuration=_configuration,
            **kwargs,
        )
