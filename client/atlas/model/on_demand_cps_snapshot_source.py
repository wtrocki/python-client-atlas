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


class OnDemandCpsSnapshotSource(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    On-Demand Cloud Provider Snapshots as Source for a Data Lake Pipeline.
    """


    class MetaOapg:
        
        class properties:
            clusterName = schemas.StrSchema
            collectionName = schemas.StrSchema
            databaseName = schemas.StrSchema
            
            
            class groupId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 24
                    min_length = 24
                    regex=[{
                        'pattern': r'^([a-f0-9]{24})$',  # noqa: E501
                    }]
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "PERIODIC_CPS": "PERIODIC_CPS",
                        "ON_DEMAND_CPS": "ON_DEMAND_CPS",
                    }
                
                @schemas.classproperty
                def PERIODIC_CPS(cls):
                    return cls("PERIODIC_CPS")
                
                @schemas.classproperty
                def ON_DEMAND_CPS(cls):
                    return cls("ON_DEMAND_CPS")
            __annotations__ = {
                "clusterName": clusterName,
                "collectionName": collectionName,
                "databaseName": databaseName,
                "groupId": groupId,
                "type": type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clusterName"]) -> MetaOapg.properties.clusterName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collectionName"]) -> MetaOapg.properties.collectionName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["databaseName"]) -> MetaOapg.properties.databaseName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupId"]) -> MetaOapg.properties.groupId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["clusterName", "collectionName", "databaseName", "groupId", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clusterName"]) -> typing.Union[MetaOapg.properties.clusterName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collectionName"]) -> typing.Union[MetaOapg.properties.collectionName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["databaseName"]) -> typing.Union[MetaOapg.properties.databaseName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupId"]) -> typing.Union[MetaOapg.properties.groupId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["clusterName", "collectionName", "databaseName", "groupId", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        clusterName: typing.Union[MetaOapg.properties.clusterName, str, schemas.Unset] = schemas.unset,
        collectionName: typing.Union[MetaOapg.properties.collectionName, str, schemas.Unset] = schemas.unset,
        databaseName: typing.Union[MetaOapg.properties.databaseName, str, schemas.Unset] = schemas.unset,
        groupId: typing.Union[MetaOapg.properties.groupId, str, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OnDemandCpsSnapshotSource':
        return super().__new__(
            cls,
            *_args,
            clusterName=clusterName,
            collectionName=collectionName,
            databaseName=databaseName,
            groupId=groupId,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )
