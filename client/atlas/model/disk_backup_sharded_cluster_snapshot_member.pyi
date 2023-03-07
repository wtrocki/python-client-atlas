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


class DiskBackupShardedClusterSnapshotMember(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    List that includes the snapshots and the cloud provider that stores the snapshots. The resource returns this parameter when `"type" : "SHARDED_CLUSTER"`.
    """


    class MetaOapg:
        required = {
            "replicaSetName",
            "cloudProvider",
            "id",
        }
        
        class properties:
            
            
            class cloudProvider(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def AWS(cls):
                    return cls("AWS")
                
                @schemas.classproperty
                def AZURE(cls):
                    return cls("AZURE")
                
                @schemas.classproperty
                def GCP(cls):
                    return cls("GCP")
            
            
            class id(
                schemas.StrSchema
            ):
                pass
            replicaSetName = schemas.StrSchema
            __annotations__ = {
                "cloudProvider": cloudProvider,
                "id": id,
                "replicaSetName": replicaSetName,
            }
    
    replicaSetName: MetaOapg.properties.replicaSetName
    cloudProvider: MetaOapg.properties.cloudProvider
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cloudProvider"]) -> MetaOapg.properties.cloudProvider: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["replicaSetName"]) -> MetaOapg.properties.replicaSetName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cloudProvider", "id", "replicaSetName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cloudProvider"]) -> MetaOapg.properties.cloudProvider: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["replicaSetName"]) -> MetaOapg.properties.replicaSetName: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cloudProvider", "id", "replicaSetName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        replicaSetName: typing.Union[MetaOapg.properties.replicaSetName, str, ],
        cloudProvider: typing.Union[MetaOapg.properties.cloudProvider, str, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DiskBackupShardedClusterSnapshotMember':
        return super().__new__(
            cls,
            *_args,
            replicaSetName=replicaSetName,
            cloudProvider=cloudProvider,
            id=id,
            _configuration=_configuration,
            **kwargs,
        )
