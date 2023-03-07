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


class AzurePrivateEndpoint(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Group of Private Endpoint settings.
    """


    class MetaOapg:
        
        class properties:
            deleteRequested = schemas.BoolSchema
            errorMessage = schemas.StrSchema
            
            
            class privateEndpointConnectionName(
                schemas.StrSchema
            ):
                pass
            
            
            class privateEndpointIPAddress(
                schemas.StrSchema
            ):
                pass
            privateEndpointResourceId = schemas.StrSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def INITIATING(cls):
                    return cls("INITIATING")
                
                @schemas.classproperty
                def AVAILABLE(cls):
                    return cls("AVAILABLE")
                
                @schemas.classproperty
                def FAILED(cls):
                    return cls("FAILED")
                
                @schemas.classproperty
                def DELETING(cls):
                    return cls("DELETING")
            __annotations__ = {
                "deleteRequested": deleteRequested,
                "errorMessage": errorMessage,
                "privateEndpointConnectionName": privateEndpointConnectionName,
                "privateEndpointIPAddress": privateEndpointIPAddress,
                "privateEndpointResourceId": privateEndpointResourceId,
                "status": status,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deleteRequested"]) -> MetaOapg.properties.deleteRequested: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errorMessage"]) -> MetaOapg.properties.errorMessage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["privateEndpointConnectionName"]) -> MetaOapg.properties.privateEndpointConnectionName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["privateEndpointIPAddress"]) -> MetaOapg.properties.privateEndpointIPAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["privateEndpointResourceId"]) -> MetaOapg.properties.privateEndpointResourceId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["deleteRequested", "errorMessage", "privateEndpointConnectionName", "privateEndpointIPAddress", "privateEndpointResourceId", "status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deleteRequested"]) -> typing.Union[MetaOapg.properties.deleteRequested, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errorMessage"]) -> typing.Union[MetaOapg.properties.errorMessage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["privateEndpointConnectionName"]) -> typing.Union[MetaOapg.properties.privateEndpointConnectionName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["privateEndpointIPAddress"]) -> typing.Union[MetaOapg.properties.privateEndpointIPAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["privateEndpointResourceId"]) -> typing.Union[MetaOapg.properties.privateEndpointResourceId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["deleteRequested", "errorMessage", "privateEndpointConnectionName", "privateEndpointIPAddress", "privateEndpointResourceId", "status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        deleteRequested: typing.Union[MetaOapg.properties.deleteRequested, bool, schemas.Unset] = schemas.unset,
        errorMessage: typing.Union[MetaOapg.properties.errorMessage, str, schemas.Unset] = schemas.unset,
        privateEndpointConnectionName: typing.Union[MetaOapg.properties.privateEndpointConnectionName, str, schemas.Unset] = schemas.unset,
        privateEndpointIPAddress: typing.Union[MetaOapg.properties.privateEndpointIPAddress, str, schemas.Unset] = schemas.unset,
        privateEndpointResourceId: typing.Union[MetaOapg.properties.privateEndpointResourceId, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AzurePrivateEndpoint':
        return super().__new__(
            cls,
            *_args,
            deleteRequested=deleteRequested,
            errorMessage=errorMessage,
            privateEndpointConnectionName=privateEndpointConnectionName,
            privateEndpointIPAddress=privateEndpointIPAddress,
            privateEndpointResourceId=privateEndpointResourceId,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )