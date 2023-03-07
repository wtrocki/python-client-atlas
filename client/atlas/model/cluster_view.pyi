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


class ClusterView(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Settings that describe the clusters in each project that the API key is authorized to view.
    """


    class MetaOapg:
        
        class properties:
            alertCount = schemas.Int32Schema
            authEnabled = schemas.BoolSchema
            
            
            class availability(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def AVAILABLE(cls):
                    return cls("available")
                
                @schemas.classproperty
                def DEAD(cls):
                    return cls("dead")
                
                @schemas.classproperty
                def UNAVAILABLE(cls):
                    return cls("unavailable")
                
                @schemas.classproperty
                def WARNING(cls):
                    return cls("warning")
            backupEnabled = schemas.BoolSchema
            
            
            class clusterId(
                schemas.StrSchema
            ):
                pass
            dataSizeBytes = schemas.Int64Schema
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            nodeCount = schemas.Int32Schema
            sslEnabled = schemas.BoolSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def REPLICA_SET(cls):
                    return cls("REPLICA_SET")
                
                @schemas.classproperty
                def SHARDED_CLUSTER(cls):
                    return cls("SHARDED_CLUSTER")
            
            
            class versions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'versions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "alertCount": alertCount,
                "authEnabled": authEnabled,
                "availability": availability,
                "backupEnabled": backupEnabled,
                "clusterId": clusterId,
                "dataSizeBytes": dataSizeBytes,
                "name": name,
                "nodeCount": nodeCount,
                "sslEnabled": sslEnabled,
                "type": type,
                "versions": versions,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alertCount"]) -> MetaOapg.properties.alertCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["authEnabled"]) -> MetaOapg.properties.authEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["availability"]) -> MetaOapg.properties.availability: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["backupEnabled"]) -> MetaOapg.properties.backupEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["clusterId"]) -> MetaOapg.properties.clusterId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dataSizeBytes"]) -> MetaOapg.properties.dataSizeBytes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nodeCount"]) -> MetaOapg.properties.nodeCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sslEnabled"]) -> MetaOapg.properties.sslEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["versions"]) -> MetaOapg.properties.versions: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["alertCount", "authEnabled", "availability", "backupEnabled", "clusterId", "dataSizeBytes", "name", "nodeCount", "sslEnabled", "type", "versions", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alertCount"]) -> typing.Union[MetaOapg.properties.alertCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["authEnabled"]) -> typing.Union[MetaOapg.properties.authEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["availability"]) -> typing.Union[MetaOapg.properties.availability, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["backupEnabled"]) -> typing.Union[MetaOapg.properties.backupEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["clusterId"]) -> typing.Union[MetaOapg.properties.clusterId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dataSizeBytes"]) -> typing.Union[MetaOapg.properties.dataSizeBytes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nodeCount"]) -> typing.Union[MetaOapg.properties.nodeCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sslEnabled"]) -> typing.Union[MetaOapg.properties.sslEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union[MetaOapg.properties.type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["versions"]) -> typing.Union[MetaOapg.properties.versions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["alertCount", "authEnabled", "availability", "backupEnabled", "clusterId", "dataSizeBytes", "name", "nodeCount", "sslEnabled", "type", "versions", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        alertCount: typing.Union[MetaOapg.properties.alertCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        authEnabled: typing.Union[MetaOapg.properties.authEnabled, bool, schemas.Unset] = schemas.unset,
        availability: typing.Union[MetaOapg.properties.availability, str, schemas.Unset] = schemas.unset,
        backupEnabled: typing.Union[MetaOapg.properties.backupEnabled, bool, schemas.Unset] = schemas.unset,
        clusterId: typing.Union[MetaOapg.properties.clusterId, str, schemas.Unset] = schemas.unset,
        dataSizeBytes: typing.Union[MetaOapg.properties.dataSizeBytes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        nodeCount: typing.Union[MetaOapg.properties.nodeCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        sslEnabled: typing.Union[MetaOapg.properties.sslEnabled, bool, schemas.Unset] = schemas.unset,
        type: typing.Union[MetaOapg.properties.type, str, schemas.Unset] = schemas.unset,
        versions: typing.Union[MetaOapg.properties.versions, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ClusterView':
        return super().__new__(
            cls,
            *_args,
            alertCount=alertCount,
            authEnabled=authEnabled,
            availability=availability,
            backupEnabled=backupEnabled,
            clusterId=clusterId,
            dataSizeBytes=dataSizeBytes,
            name=name,
            nodeCount=nodeCount,
            sslEnabled=sslEnabled,
            type=type,
            versions=versions,
            _configuration=_configuration,
            **kwargs,
        )
