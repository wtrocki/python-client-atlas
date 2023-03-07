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


class NumberMetricEventView(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "created",
            "eventTypeName",
            "id",
        }
        
        class properties:
            created = schemas.DateTimeSchema
        
            @staticmethod
            def eventTypeName() -> typing.Type['HostMetricEventTypeView']:
                return HostMetricEventTypeView
            
            
            class id(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 24
                    min_length = 24
                    regex=[{
                        'pattern': r'^([a-f0-9]{24})$',  # noqa: E501
                    }]
            
            
            class apiKeyId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 24
                    min_length = 24
                    regex=[{
                        'pattern': r'^([a-f0-9]{24})$',  # noqa: E501
                    }]
        
            @staticmethod
            def currentValue() -> typing.Type['NumberMetricValueView']:
                return NumberMetricValueView
            
            
            class groupId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 24
                    min_length = 24
                    regex=[{
                        'pattern': r'^([a-f0-9]{24})$',  # noqa: E501
                    }]
            isGlobalAdmin = schemas.BoolSchema
            
            
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
            metricName = schemas.StrSchema
            
            
            class orgId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 24
                    min_length = 24
                    regex=[{
                        'pattern': r'^([a-f0-9]{24})$',  # noqa: E501
                    }]
            port = schemas.Int32Schema
            publicKey = schemas.StrSchema
        
            @staticmethod
            def raw() -> typing.Type['Raw']:
                return Raw
            
            
            class remoteAddress(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}|([0-9a-f]{1,4}\:){7}[0-9a-f]{1,4}$',  # noqa: E501
                    }]
            replicaSetName = schemas.StrSchema
            shardName = schemas.StrSchema
            
            
            class userId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 24
                    min_length = 24
                    regex=[{
                        'pattern': r'^([a-f0-9]{24})$',  # noqa: E501
                    }]
            username = schemas.StrSchema
            __annotations__ = {
                "created": created,
                "eventTypeName": eventTypeName,
                "id": id,
                "apiKeyId": apiKeyId,
                "currentValue": currentValue,
                "groupId": groupId,
                "isGlobalAdmin": isGlobalAdmin,
                "links": links,
                "metricName": metricName,
                "orgId": orgId,
                "port": port,
                "publicKey": publicKey,
                "raw": raw,
                "remoteAddress": remoteAddress,
                "replicaSetName": replicaSetName,
                "shardName": shardName,
                "userId": userId,
                "username": username,
            }
    
    created: MetaOapg.properties.created
    eventTypeName: 'HostMetricEventTypeView'
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eventTypeName"]) -> 'HostMetricEventTypeView': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apiKeyId"]) -> MetaOapg.properties.apiKeyId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentValue"]) -> 'NumberMetricValueView': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupId"]) -> MetaOapg.properties.groupId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isGlobalAdmin"]) -> MetaOapg.properties.isGlobalAdmin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> MetaOapg.properties.links: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["metricName"]) -> MetaOapg.properties.metricName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orgId"]) -> MetaOapg.properties.orgId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["port"]) -> MetaOapg.properties.port: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publicKey"]) -> MetaOapg.properties.publicKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["raw"]) -> 'Raw': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["remoteAddress"]) -> MetaOapg.properties.remoteAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["replicaSetName"]) -> MetaOapg.properties.replicaSetName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shardName"]) -> MetaOapg.properties.shardName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userId"]) -> MetaOapg.properties.userId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["created", "eventTypeName", "id", "apiKeyId", "currentValue", "groupId", "isGlobalAdmin", "links", "metricName", "orgId", "port", "publicKey", "raw", "remoteAddress", "replicaSetName", "shardName", "userId", "username", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eventTypeName"]) -> 'HostMetricEventTypeView': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apiKeyId"]) -> typing.Union[MetaOapg.properties.apiKeyId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentValue"]) -> typing.Union['NumberMetricValueView', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupId"]) -> typing.Union[MetaOapg.properties.groupId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isGlobalAdmin"]) -> typing.Union[MetaOapg.properties.isGlobalAdmin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union[MetaOapg.properties.links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["metricName"]) -> typing.Union[MetaOapg.properties.metricName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orgId"]) -> typing.Union[MetaOapg.properties.orgId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["port"]) -> typing.Union[MetaOapg.properties.port, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publicKey"]) -> typing.Union[MetaOapg.properties.publicKey, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["raw"]) -> typing.Union['Raw', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["remoteAddress"]) -> typing.Union[MetaOapg.properties.remoteAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["replicaSetName"]) -> typing.Union[MetaOapg.properties.replicaSetName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shardName"]) -> typing.Union[MetaOapg.properties.shardName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userId"]) -> typing.Union[MetaOapg.properties.userId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> typing.Union[MetaOapg.properties.username, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["created", "eventTypeName", "id", "apiKeyId", "currentValue", "groupId", "isGlobalAdmin", "links", "metricName", "orgId", "port", "publicKey", "raw", "remoteAddress", "replicaSetName", "shardName", "userId", "username", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        created: typing.Union[MetaOapg.properties.created, str, datetime, ],
        eventTypeName: 'HostMetricEventTypeView',
        id: typing.Union[MetaOapg.properties.id, str, ],
        apiKeyId: typing.Union[MetaOapg.properties.apiKeyId, str, schemas.Unset] = schemas.unset,
        currentValue: typing.Union['NumberMetricValueView', schemas.Unset] = schemas.unset,
        groupId: typing.Union[MetaOapg.properties.groupId, str, schemas.Unset] = schemas.unset,
        isGlobalAdmin: typing.Union[MetaOapg.properties.isGlobalAdmin, bool, schemas.Unset] = schemas.unset,
        links: typing.Union[MetaOapg.properties.links, list, tuple, schemas.Unset] = schemas.unset,
        metricName: typing.Union[MetaOapg.properties.metricName, str, schemas.Unset] = schemas.unset,
        orgId: typing.Union[MetaOapg.properties.orgId, str, schemas.Unset] = schemas.unset,
        port: typing.Union[MetaOapg.properties.port, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        publicKey: typing.Union[MetaOapg.properties.publicKey, str, schemas.Unset] = schemas.unset,
        raw: typing.Union['Raw', schemas.Unset] = schemas.unset,
        remoteAddress: typing.Union[MetaOapg.properties.remoteAddress, str, schemas.Unset] = schemas.unset,
        replicaSetName: typing.Union[MetaOapg.properties.replicaSetName, str, schemas.Unset] = schemas.unset,
        shardName: typing.Union[MetaOapg.properties.shardName, str, schemas.Unset] = schemas.unset,
        userId: typing.Union[MetaOapg.properties.userId, str, schemas.Unset] = schemas.unset,
        username: typing.Union[MetaOapg.properties.username, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NumberMetricEventView':
        return super().__new__(
            cls,
            *_args,
            created=created,
            eventTypeName=eventTypeName,
            id=id,
            apiKeyId=apiKeyId,
            currentValue=currentValue,
            groupId=groupId,
            isGlobalAdmin=isGlobalAdmin,
            links=links,
            metricName=metricName,
            orgId=orgId,
            port=port,
            publicKey=publicKey,
            raw=raw,
            remoteAddress=remoteAddress,
            replicaSetName=replicaSetName,
            shardName=shardName,
            userId=userId,
            username=username,
            _configuration=_configuration,
            **kwargs,
        )

from atlas.model.host_metric_event_type_view import HostMetricEventTypeView
from atlas.model.link import Link
from atlas.model.number_metric_value_view import NumberMetricValueView
from atlas.model.raw import Raw