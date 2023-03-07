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


class ClusterEventViewForNdsGroup(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Cluster event identifies different activities about cluster of mongod hosts.
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
            def eventTypeName() -> typing.Type['ClusterEventTypeViewForNdsGroup']:
                return ClusterEventTypeViewForNdsGroup
            
            
            class id(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 24
                    min_length = 24
                    regex=[{
                        'pattern': r'^([a-f0-9]{24})$',  # noqa: E501
                    }]
            
            
            class groupId(
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
            
            
            class orgId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 24
                    min_length = 24
                    regex=[{
                        'pattern': r'^([a-f0-9]{24})$',  # noqa: E501
                    }]
        
            @staticmethod
            def raw() -> typing.Type['Raw']:
                return Raw
            shardName = schemas.StrSchema
            __annotations__ = {
                "created": created,
                "eventTypeName": eventTypeName,
                "id": id,
                "groupId": groupId,
                "links": links,
                "orgId": orgId,
                "raw": raw,
                "shardName": shardName,
            }
    
    created: MetaOapg.properties.created
    eventTypeName: 'ClusterEventTypeViewForNdsGroup'
    id: MetaOapg.properties.id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eventTypeName"]) -> 'ClusterEventTypeViewForNdsGroup': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupId"]) -> MetaOapg.properties.groupId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> MetaOapg.properties.links: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["orgId"]) -> MetaOapg.properties.orgId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["raw"]) -> 'Raw': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shardName"]) -> MetaOapg.properties.shardName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["created", "eventTypeName", "id", "groupId", "links", "orgId", "raw", "shardName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eventTypeName"]) -> 'ClusterEventTypeViewForNdsGroup': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupId"]) -> typing.Union[MetaOapg.properties.groupId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union[MetaOapg.properties.links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["orgId"]) -> typing.Union[MetaOapg.properties.orgId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["raw"]) -> typing.Union['Raw', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shardName"]) -> typing.Union[MetaOapg.properties.shardName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["created", "eventTypeName", "id", "groupId", "links", "orgId", "raw", "shardName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        created: typing.Union[MetaOapg.properties.created, str, datetime, ],
        eventTypeName: 'ClusterEventTypeViewForNdsGroup',
        id: typing.Union[MetaOapg.properties.id, str, ],
        groupId: typing.Union[MetaOapg.properties.groupId, str, schemas.Unset] = schemas.unset,
        links: typing.Union[MetaOapg.properties.links, list, tuple, schemas.Unset] = schemas.unset,
        orgId: typing.Union[MetaOapg.properties.orgId, str, schemas.Unset] = schemas.unset,
        raw: typing.Union['Raw', schemas.Unset] = schemas.unset,
        shardName: typing.Union[MetaOapg.properties.shardName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ClusterEventViewForNdsGroup':
        return super().__new__(
            cls,
            *_args,
            created=created,
            eventTypeName=eventTypeName,
            id=id,
            groupId=groupId,
            links=links,
            orgId=orgId,
            raw=raw,
            shardName=shardName,
            _configuration=_configuration,
            **kwargs,
        )

from atlas.model.cluster_event_type_view_for_nds_group import ClusterEventTypeViewForNdsGroup
from atlas.model.link import Link
from atlas.model.raw import Raw
