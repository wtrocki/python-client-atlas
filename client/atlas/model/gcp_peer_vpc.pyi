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


class GCPPeerVpc(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Group of Network Peering connection settings.
    """


    class MetaOapg:
        required = {
            "gcpProjectId",
            "networkName",
            "containerId",
        }
        
        class properties:
            
            
            class containerId(
                schemas.StrSchema
            ):
                pass
            
            
            class gcpProjectId(
                schemas.StrSchema
            ):
                pass
            
            
            class networkName(
                schemas.StrSchema
            ):
                pass
            errorMessage = schemas.StrSchema
            
            
            class id(
                schemas.StrSchema
            ):
                pass
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ADDING_PEER(cls):
                    return cls("ADDING_PEER")
                
                @schemas.classproperty
                def WAITING_FOR_USER(cls):
                    return cls("WAITING_FOR_USER")
                
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
                "containerId": containerId,
                "gcpProjectId": gcpProjectId,
                "networkName": networkName,
                "errorMessage": errorMessage,
                "id": id,
                "status": status,
            }
    
    gcpProjectId: MetaOapg.properties.gcpProjectId
    networkName: MetaOapg.properties.networkName
    containerId: MetaOapg.properties.containerId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["containerId"]) -> MetaOapg.properties.containerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gcpProjectId"]) -> MetaOapg.properties.gcpProjectId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["networkName"]) -> MetaOapg.properties.networkName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errorMessage"]) -> MetaOapg.properties.errorMessage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["containerId", "gcpProjectId", "networkName", "errorMessage", "id", "status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["containerId"]) -> MetaOapg.properties.containerId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gcpProjectId"]) -> MetaOapg.properties.gcpProjectId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["networkName"]) -> MetaOapg.properties.networkName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errorMessage"]) -> typing.Union[MetaOapg.properties.errorMessage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["containerId", "gcpProjectId", "networkName", "errorMessage", "id", "status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        gcpProjectId: typing.Union[MetaOapg.properties.gcpProjectId, str, ],
        networkName: typing.Union[MetaOapg.properties.networkName, str, ],
        containerId: typing.Union[MetaOapg.properties.containerId, str, ],
        errorMessage: typing.Union[MetaOapg.properties.errorMessage, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GCPPeerVpc':
        return super().__new__(
            cls,
            *_args,
            gcpProjectId=gcpProjectId,
            networkName=networkName,
            containerId=containerId,
            errorMessage=errorMessage,
            id=id,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )
