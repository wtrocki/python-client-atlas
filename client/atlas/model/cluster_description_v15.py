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


class ClusterDescriptionV15(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            backupEnabled = schemas.BoolSchema
        
            @staticmethod
            def biConnector() -> typing.Type['BiConnector']:
                return BiConnector
            
            
            class clusterType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "REPLICASET": "REPLICASET",
                        "SHARDED": "SHARDED",
                        "GEOSHARDED": "GEOSHARDED",
                    }
                
                @schemas.classproperty
                def REPLICASET(cls):
                    return cls("REPLICASET")
                
                @schemas.classproperty
                def SHARDED(cls):
                    return cls("SHARDED")
                
                @schemas.classproperty
                def GEOSHARDED(cls):
                    return cls("GEOSHARDED")
        
            @staticmethod
            def connectionStrings() -> typing.Type['ClusterDescriptionConnectionStrings']:
                return ClusterDescriptionConnectionStrings
            createDate = schemas.DateTimeSchema
            
            
            class diskSizeGB(
                schemas.Float64Schema
            ):
            
            
                class MetaOapg:
                    format = 'double'
                    inclusive_maximum = 4096
                    inclusive_minimum = 10
            
            
            class encryptionAtRestProvider(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "NONE": "NONE",
                        "AWS": "AWS",
                        "AZURE": "AZURE",
                        "GCP": "GCP",
                    }
                
                @schemas.classproperty
                def NONE(cls):
                    return cls("NONE")
                
                @schemas.classproperty
                def AWS(cls):
                    return cls("AWS")
                
                @schemas.classproperty
                def AZURE(cls):
                    return cls("AZURE")
                
                @schemas.classproperty
                def GCP(cls):
                    return cls("GCP")
            
            
            class groupId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 24
                    min_length = 24
                    regex=[{
                        'pattern': r'^([a-f0-9]{24})$',  # noqa: E501
                    }]
            
            
            class id(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 24
                    min_length = 24
                    regex=[{
                        'pattern': r'^([a-f0-9]{24})$',  # noqa: E501
                    }]
            
            
            class labels(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['NDSLabel']:
                        return NDSLabel
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['NDSLabel'], typing.List['NDSLabel']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'labels':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'NDSLabel':
                    return super().__getitem__(i)
            
            
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
            
            
            class mongoDBMajorVersion(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "4.2": "POSITIVE_4_PT_2",
                        "4.4": "POSITIVE_4_PT_4",
                        "5.0": "POSITIVE_5_PT_0",
                        "6.0": "POSITIVE_6_PT_0",
                    }
                
                @schemas.classproperty
                def POSITIVE_4_PT_2(cls):
                    return cls("4.2")
                
                @schemas.classproperty
                def POSITIVE_4_PT_4(cls):
                    return cls("4.4")
                
                @schemas.classproperty
                def POSITIVE_5_PT_0(cls):
                    return cls("5.0")
                
                @schemas.classproperty
                def POSITIVE_6_PT_0(cls):
                    return cls("6.0")
            
            
            class mongoDBVersion(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'([\d]+\.[\d]+\.[\d]+)',  # noqa: E501
                    }]
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 64
                    min_length = 1
                    regex=[{
                        'pattern': r'^([a-zA-Z0-9]([a-zA-Z0-9-]){0,21}(?<!-)([\w]{0,42}))$',  # noqa: E501
                    }]
            paused = schemas.BoolSchema
            pitEnabled = schemas.BoolSchema
            
            
            class replicationSpecs(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ReplicationSpec']:
                        return ReplicationSpec
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ReplicationSpec'], typing.List['ReplicationSpec']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'replicationSpecs':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ReplicationSpec':
                    return super().__getitem__(i)
            
            
            class rootCertType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "ISRGROOTX1": "ISRGROOTX1",
                    }
                
                @schemas.classproperty
                def ISRGROOTX1(cls):
                    return cls("ISRGROOTX1")
            
            
            class stateName(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "IDLE": "IDLE",
                        "CREATING": "CREATING",
                        "UPDATING": "UPDATING",
                        "DELETING": "DELETING",
                        "DELETED": "DELETED",
                        "REPAIRING": "REPAIRING",
                    }
                
                @schemas.classproperty
                def IDLE(cls):
                    return cls("IDLE")
                
                @schemas.classproperty
                def CREATING(cls):
                    return cls("CREATING")
                
                @schemas.classproperty
                def UPDATING(cls):
                    return cls("UPDATING")
                
                @schemas.classproperty
                def DELETING(cls):
                    return cls("DELETING")
                
                @schemas.classproperty
                def DELETED(cls):
                    return cls("DELETED")
                
                @schemas.classproperty
                def REPAIRING(cls):
                    return cls("REPAIRING")
            terminationProtectionEnabled = schemas.BoolSchema
            
            
            class versionReleaseSystem(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "LTS": "LTS",
                        "CONTINUOUS": "CONTINUOUS",
                    }
                
                @schemas.classproperty
                def LTS(cls):
                    return cls("LTS")
                
                @schemas.classproperty
                def CONTINUOUS(cls):
                    return cls("CONTINUOUS")
            __annotations__ = {
                "backupEnabled": backupEnabled,
                "biConnector": biConnector,
                "clusterType": clusterType,
                "connectionStrings": connectionStrings,
                "createDate": createDate,
                "diskSizeGB": diskSizeGB,
                "encryptionAtRestProvider": encryptionAtRestProvider,
                "groupId": groupId,
                "id": id,
                "labels": labels,
                "links": links,
                "mongoDBMajorVersion": mongoDBMajorVersion,
                "mongoDBVersion": mongoDBVersion,
                "name": name,
                "paused": paused,
                "pitEnabled": pitEnabled,
                "replicationSpecs": replicationSpecs,
                "rootCertType": rootCertType,
                "stateName": stateName,
                "terminationProtectionEnabled": terminationProtectionEnabled,
                "versionReleaseSystem": versionReleaseSystem,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["backupEnabled"]) -> MetaOapg.properties.backupEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["biConnector"]) -> 'BiConnector': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clusterType"]) -> MetaOapg.properties.clusterType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connectionStrings"]) -> 'ClusterDescriptionConnectionStrings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createDate"]) -> MetaOapg.properties.createDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["diskSizeGB"]) -> MetaOapg.properties.diskSizeGB: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["encryptionAtRestProvider"]) -> MetaOapg.properties.encryptionAtRestProvider: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupId"]) -> MetaOapg.properties.groupId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["labels"]) -> MetaOapg.properties.labels: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> MetaOapg.properties.links: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mongoDBMajorVersion"]) -> MetaOapg.properties.mongoDBMajorVersion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mongoDBVersion"]) -> MetaOapg.properties.mongoDBVersion: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["paused"]) -> MetaOapg.properties.paused: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pitEnabled"]) -> MetaOapg.properties.pitEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["replicationSpecs"]) -> MetaOapg.properties.replicationSpecs: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rootCertType"]) -> MetaOapg.properties.rootCertType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stateName"]) -> MetaOapg.properties.stateName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["terminationProtectionEnabled"]) -> MetaOapg.properties.terminationProtectionEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["versionReleaseSystem"]) -> MetaOapg.properties.versionReleaseSystem: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["backupEnabled", "biConnector", "clusterType", "connectionStrings", "createDate", "diskSizeGB", "encryptionAtRestProvider", "groupId", "id", "labels", "links", "mongoDBMajorVersion", "mongoDBVersion", "name", "paused", "pitEnabled", "replicationSpecs", "rootCertType", "stateName", "terminationProtectionEnabled", "versionReleaseSystem", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["backupEnabled"]) -> typing.Union[MetaOapg.properties.backupEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["biConnector"]) -> typing.Union['BiConnector', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clusterType"]) -> typing.Union[MetaOapg.properties.clusterType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connectionStrings"]) -> typing.Union['ClusterDescriptionConnectionStrings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createDate"]) -> typing.Union[MetaOapg.properties.createDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["diskSizeGB"]) -> typing.Union[MetaOapg.properties.diskSizeGB, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["encryptionAtRestProvider"]) -> typing.Union[MetaOapg.properties.encryptionAtRestProvider, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupId"]) -> typing.Union[MetaOapg.properties.groupId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["labels"]) -> typing.Union[MetaOapg.properties.labels, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union[MetaOapg.properties.links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mongoDBMajorVersion"]) -> typing.Union[MetaOapg.properties.mongoDBMajorVersion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mongoDBVersion"]) -> typing.Union[MetaOapg.properties.mongoDBVersion, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["paused"]) -> typing.Union[MetaOapg.properties.paused, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pitEnabled"]) -> typing.Union[MetaOapg.properties.pitEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["replicationSpecs"]) -> typing.Union[MetaOapg.properties.replicationSpecs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rootCertType"]) -> typing.Union[MetaOapg.properties.rootCertType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stateName"]) -> typing.Union[MetaOapg.properties.stateName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["terminationProtectionEnabled"]) -> typing.Union[MetaOapg.properties.terminationProtectionEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["versionReleaseSystem"]) -> typing.Union[MetaOapg.properties.versionReleaseSystem, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["backupEnabled", "biConnector", "clusterType", "connectionStrings", "createDate", "diskSizeGB", "encryptionAtRestProvider", "groupId", "id", "labels", "links", "mongoDBMajorVersion", "mongoDBVersion", "name", "paused", "pitEnabled", "replicationSpecs", "rootCertType", "stateName", "terminationProtectionEnabled", "versionReleaseSystem", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        backupEnabled: typing.Union[MetaOapg.properties.backupEnabled, bool, schemas.Unset] = schemas.unset,
        biConnector: typing.Union['BiConnector', schemas.Unset] = schemas.unset,
        clusterType: typing.Union[MetaOapg.properties.clusterType, str, schemas.Unset] = schemas.unset,
        connectionStrings: typing.Union['ClusterDescriptionConnectionStrings', schemas.Unset] = schemas.unset,
        createDate: typing.Union[MetaOapg.properties.createDate, str, datetime, schemas.Unset] = schemas.unset,
        diskSizeGB: typing.Union[MetaOapg.properties.diskSizeGB, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        encryptionAtRestProvider: typing.Union[MetaOapg.properties.encryptionAtRestProvider, str, schemas.Unset] = schemas.unset,
        groupId: typing.Union[MetaOapg.properties.groupId, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        labels: typing.Union[MetaOapg.properties.labels, list, tuple, schemas.Unset] = schemas.unset,
        links: typing.Union[MetaOapg.properties.links, list, tuple, schemas.Unset] = schemas.unset,
        mongoDBMajorVersion: typing.Union[MetaOapg.properties.mongoDBMajorVersion, str, schemas.Unset] = schemas.unset,
        mongoDBVersion: typing.Union[MetaOapg.properties.mongoDBVersion, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        paused: typing.Union[MetaOapg.properties.paused, bool, schemas.Unset] = schemas.unset,
        pitEnabled: typing.Union[MetaOapg.properties.pitEnabled, bool, schemas.Unset] = schemas.unset,
        replicationSpecs: typing.Union[MetaOapg.properties.replicationSpecs, list, tuple, schemas.Unset] = schemas.unset,
        rootCertType: typing.Union[MetaOapg.properties.rootCertType, str, schemas.Unset] = schemas.unset,
        stateName: typing.Union[MetaOapg.properties.stateName, str, schemas.Unset] = schemas.unset,
        terminationProtectionEnabled: typing.Union[MetaOapg.properties.terminationProtectionEnabled, bool, schemas.Unset] = schemas.unset,
        versionReleaseSystem: typing.Union[MetaOapg.properties.versionReleaseSystem, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ClusterDescriptionV15':
        return super().__new__(
            cls,
            *_args,
            backupEnabled=backupEnabled,
            biConnector=biConnector,
            clusterType=clusterType,
            connectionStrings=connectionStrings,
            createDate=createDate,
            diskSizeGB=diskSizeGB,
            encryptionAtRestProvider=encryptionAtRestProvider,
            groupId=groupId,
            id=id,
            labels=labels,
            links=links,
            mongoDBMajorVersion=mongoDBMajorVersion,
            mongoDBVersion=mongoDBVersion,
            name=name,
            paused=paused,
            pitEnabled=pitEnabled,
            replicationSpecs=replicationSpecs,
            rootCertType=rootCertType,
            stateName=stateName,
            terminationProtectionEnabled=terminationProtectionEnabled,
            versionReleaseSystem=versionReleaseSystem,
            _configuration=_configuration,
            **kwargs,
        )

from atlas.model.bi_connector import BiConnector
from atlas.model.cluster_description_connection_strings import ClusterDescriptionConnectionStrings
from atlas.model.link import Link
from atlas.model.nds_label import NDSLabel
from atlas.model.replication_spec import ReplicationSpec
