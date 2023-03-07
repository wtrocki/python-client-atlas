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


class DiskBackupShardedClusterSnapshot(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Details of the sharded cluster snapshot that MongoDB Cloud created.
    """


    class MetaOapg:
        
        class properties:
            createdAt = schemas.DateTimeSchema
            description = schemas.StrSchema
            expiresAt = schemas.DateTimeSchema
            
            
            class frequencyType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "hourly": "HOURLY",
                        "daily": "DAILY",
                        "weekly": "WEEKLY",
                        "monthly": "MONTHLY",
                    }
                
                @schemas.classproperty
                def HOURLY(cls):
                    return cls("hourly")
                
                @schemas.classproperty
                def DAILY(cls):
                    return cls("daily")
                
                @schemas.classproperty
                def WEEKLY(cls):
                    return cls("weekly")
                
                @schemas.classproperty
                def MONTHLY(cls):
                    return cls("monthly")
            
            
            class id(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 24
                    min_length = 24
                    regex=[{
                        'pattern': r'^([a-f0-9]{24})$',  # noqa: E501
                    }]
            
            
            class links(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Link']:
                        return Link
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Link'], typing.List['Link']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'links':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Link':
                    return super().__getitem__(i)
            masterKeyUUID = schemas.UUIDSchema
            
            
            class members(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DiskBackupShardedClusterSnapshotMember']:
                        return DiskBackupShardedClusterSnapshotMember
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['DiskBackupShardedClusterSnapshotMember'], typing.List['DiskBackupShardedClusterSnapshotMember']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'members':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DiskBackupShardedClusterSnapshotMember':
                    return super().__getitem__(i)
            
            
            class mongodVersion(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'([\d]+\.[\d]+\.[\d]+)',  # noqa: E501
                    }]
            
            
            class policyItems(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            max_length = 24
                            min_length = 24
                            regex=[{
                                'pattern': r'^([a-f0-9]{24})$',  # noqa: E501
                            }]
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'policyItems':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class snapshotIds(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            max_length = 24
                            min_length = 24
                            regex=[{
                                'pattern': r'^([a-f0-9]{24})$',  # noqa: E501
                            }]
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'snapshotIds':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class snapshotType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "onDemand": "ON_DEMAND",
                        "scheduled": "SCHEDULED",
                    }
                
                @schemas.classproperty
                def ON_DEMAND(cls):
                    return cls("onDemand")
                
                @schemas.classproperty
                def SCHEDULED(cls):
                    return cls("scheduled")
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "queued": "QUEUED",
                        "inProgress": "IN_PROGRESS",
                        "completed": "COMPLETED",
                        "failed": "FAILED",
                    }
                
                @schemas.classproperty
                def QUEUED(cls):
                    return cls("queued")
                
                @schemas.classproperty
                def IN_PROGRESS(cls):
                    return cls("inProgress")
                
                @schemas.classproperty
                def COMPLETED(cls):
                    return cls("completed")
                
                @schemas.classproperty
                def FAILED(cls):
                    return cls("failed")
            storageSizeBytes = schemas.Int64Schema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "REPLICA_SET": "REPLICA_SET",
                        "SHARDED_CLUSTER": "SHARDED_CLUSTER",
                    }
                
                @schemas.classproperty
                def REPLICA_SET(cls):
                    return cls("REPLICA_SET")
                
                @schemas.classproperty
                def SHARDED_CLUSTER(cls):
                    return cls("SHARDED_CLUSTER")
            __annotations__ = {
                "createdAt": createdAt,
                "description": description,
                "expiresAt": expiresAt,
                "frequencyType": frequencyType,
                "id": id,
                "links": links,
                "masterKeyUUID": masterKeyUUID,
                "members": members,
                "mongodVersion": mongodVersion,
                "policyItems": policyItems,
                "snapshotIds": snapshotIds,
                "snapshotType": snapshotType,
                "status": status,
                "storageSizeBytes": storageSizeBytes,
                "type": type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiresAt"]) -> MetaOapg.properties.expiresAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["frequencyType"]) -> MetaOapg.properties.frequencyType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> MetaOapg.properties.links: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["masterKeyUUID"]) -> MetaOapg.properties.masterKeyUUID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["members"]) -> MetaOapg.properties.members: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mongodVersion"]) -> MetaOapg.properties.mongodVersion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["policyItems"]) -> MetaOapg.properties.policyItems: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["snapshotIds"]) -> MetaOapg.properties.snapshotIds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["snapshotType"]) -> MetaOapg.properties.snapshotType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["storageSizeBytes"]) -> MetaOapg.properties.storageSizeBytes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["createdAt", "description", "expiresAt", "frequencyType", "id", "links", "masterKeyUUID", "members", "mongodVersion", "policyItems", "snapshotIds", "snapshotType", "status", "storageSizeBytes", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> typing.Union[MetaOapg.properties.createdAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiresAt"]) -> typing.Union[MetaOapg.properties.expiresAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["frequencyType"]) -> typing.Union[MetaOapg.properties.frequencyType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union[MetaOapg.properties.links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["masterKeyUUID"]) -> typing.Union[MetaOapg.properties.masterKeyUUID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["members"]) -> typing.Union[MetaOapg.properties.members, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mongodVersion"]) -> typing.Union[MetaOapg.properties.mongodVersion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["policyItems"]) -> typing.Union[MetaOapg.properties.policyItems, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["snapshotIds"]) -> typing.Union[MetaOapg.properties.snapshotIds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["snapshotType"]) -> typing.Union[MetaOapg.properties.snapshotType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["storageSizeBytes"]) -> typing.Union[MetaOapg.properties.storageSizeBytes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["createdAt", "description", "expiresAt", "frequencyType", "id", "links", "masterKeyUUID", "members", "mongodVersion", "policyItems", "snapshotIds", "snapshotType", "status", "storageSizeBytes", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        createdAt: typing.Union[MetaOapg.properties.createdAt, str, datetime, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        expiresAt: typing.Union[MetaOapg.properties.expiresAt, str, datetime, schemas.Unset] = schemas.unset,
        frequencyType: typing.Union[MetaOapg.properties.frequencyType, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        links: typing.Union[MetaOapg.properties.links, list, tuple, schemas.Unset] = schemas.unset,
        masterKeyUUID: typing.Union[MetaOapg.properties.masterKeyUUID, str, uuid.UUID, schemas.Unset] = schemas.unset,
        members: typing.Union[MetaOapg.properties.members, list, tuple, schemas.Unset] = schemas.unset,
        mongodVersion: typing.Union[MetaOapg.properties.mongodVersion, str, schemas.Unset] = schemas.unset,
        policyItems: typing.Union[MetaOapg.properties.policyItems, list, tuple, schemas.Unset] = schemas.unset,
        snapshotIds: typing.Union[MetaOapg.properties.snapshotIds, list, tuple, schemas.Unset] = schemas.unset,
        snapshotType: typing.Union[MetaOapg.properties.snapshotType, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        storageSizeBytes: typing.Union[MetaOapg.properties.storageSizeBytes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DiskBackupShardedClusterSnapshot':
        return super().__new__(
            cls,
            *_args,
            createdAt=createdAt,
            description=description,
            expiresAt=expiresAt,
            frequencyType=frequencyType,
            id=id,
            links=links,
            masterKeyUUID=masterKeyUUID,
            members=members,
            mongodVersion=mongodVersion,
            policyItems=policyItems,
            snapshotIds=snapshotIds,
            snapshotType=snapshotType,
            status=status,
            storageSizeBytes=storageSizeBytes,
            type=type,
            _configuration=_configuration,
            **kwargs,
        )

from atlas.model.disk_backup_sharded_cluster_snapshot_member import DiskBackupShardedClusterSnapshotMember
from atlas.model.link import Link
