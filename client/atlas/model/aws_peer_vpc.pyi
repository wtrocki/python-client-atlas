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


class AWSPeerVpc(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Group of Network Peering connection settings.
    """


    class MetaOapg:
        required = {
            "awsAccountId",
            "accepterRegionName",
            "vpcId",
            "routeTableCidrBlock",
            "containerId",
        }
        
        class properties:
            accepterRegionName = schemas.StrSchema
            
            
            class awsAccountId(
                schemas.StrSchema
            ):
                pass
            
            
            class containerId(
                schemas.StrSchema
            ):
                pass
            
            
            class routeTableCidrBlock(
                schemas.StrSchema
            ):
                pass
            
            
            class vpcId(
                schemas.StrSchema
            ):
                pass
            connectionId = schemas.StrSchema
            
            
            class errorStateName(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def REJECTED(cls):
                    return cls("REJECTED")
                
                @schemas.classproperty
                def EXPIRED(cls):
                    return cls("EXPIRED")
                
                @schemas.classproperty
                def INVALID_ARGUMENT(cls):
                    return cls("INVALID_ARGUMENT")
            
            
            class id(
                schemas.StrSchema
            ):
                pass
            
            
            class statusName(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def INITIATING(cls):
                    return cls("INITIATING")
                
                @schemas.classproperty
                def PENDING_ACCEPTANCE(cls):
                    return cls("PENDING_ACCEPTANCE")
                
                @schemas.classproperty
                def FAILED(cls):
                    return cls("FAILED")
                
                @schemas.classproperty
                def FINALIZING(cls):
                    return cls("FINALIZING")
                
                @schemas.classproperty
                def AVAILABLE(cls):
                    return cls("AVAILABLE")
                
                @schemas.classproperty
                def TERMINATING(cls):
                    return cls("TERMINATING")
            __annotations__ = {
                "accepterRegionName": accepterRegionName,
                "awsAccountId": awsAccountId,
                "containerId": containerId,
                "routeTableCidrBlock": routeTableCidrBlock,
                "vpcId": vpcId,
                "connectionId": connectionId,
                "errorStateName": errorStateName,
                "id": id,
                "statusName": statusName,
            }
    
    awsAccountId: MetaOapg.properties.awsAccountId
    accepterRegionName: MetaOapg.properties.accepterRegionName
    vpcId: MetaOapg.properties.vpcId
    routeTableCidrBlock: MetaOapg.properties.routeTableCidrBlock
    containerId: MetaOapg.properties.containerId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accepterRegionName"]) -> MetaOapg.properties.accepterRegionName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["awsAccountId"]) -> MetaOapg.properties.awsAccountId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["containerId"]) -> MetaOapg.properties.containerId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["routeTableCidrBlock"]) -> MetaOapg.properties.routeTableCidrBlock: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vpcId"]) -> MetaOapg.properties.vpcId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connectionId"]) -> MetaOapg.properties.connectionId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["errorStateName"]) -> MetaOapg.properties.errorStateName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["statusName"]) -> MetaOapg.properties.statusName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accepterRegionName", "awsAccountId", "containerId", "routeTableCidrBlock", "vpcId", "connectionId", "errorStateName", "id", "statusName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accepterRegionName"]) -> MetaOapg.properties.accepterRegionName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["awsAccountId"]) -> MetaOapg.properties.awsAccountId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["containerId"]) -> MetaOapg.properties.containerId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["routeTableCidrBlock"]) -> MetaOapg.properties.routeTableCidrBlock: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vpcId"]) -> MetaOapg.properties.vpcId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connectionId"]) -> typing.Union[MetaOapg.properties.connectionId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["errorStateName"]) -> typing.Union[MetaOapg.properties.errorStateName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["statusName"]) -> typing.Union[MetaOapg.properties.statusName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accepterRegionName", "awsAccountId", "containerId", "routeTableCidrBlock", "vpcId", "connectionId", "errorStateName", "id", "statusName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        awsAccountId: typing.Union[MetaOapg.properties.awsAccountId, str, ],
        accepterRegionName: typing.Union[MetaOapg.properties.accepterRegionName, str, ],
        vpcId: typing.Union[MetaOapg.properties.vpcId, str, ],
        routeTableCidrBlock: typing.Union[MetaOapg.properties.routeTableCidrBlock, str, ],
        containerId: typing.Union[MetaOapg.properties.containerId, str, ],
        connectionId: typing.Union[MetaOapg.properties.connectionId, str, schemas.Unset] = schemas.unset,
        errorStateName: typing.Union[MetaOapg.properties.errorStateName, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        statusName: typing.Union[MetaOapg.properties.statusName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AWSPeerVpc':
        return super().__new__(
            cls,
            *_args,
            awsAccountId=awsAccountId,
            accepterRegionName=accepterRegionName,
            vpcId=vpcId,
            routeTableCidrBlock=routeTableCidrBlock,
            containerId=containerId,
            connectionId=connectionId,
            errorStateName=errorStateName,
            id=id,
            statusName=statusName,
            _configuration=_configuration,
            **kwargs,
        )
