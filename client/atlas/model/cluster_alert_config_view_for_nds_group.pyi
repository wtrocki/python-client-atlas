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


class ClusterAlertConfigViewForNdsGroup(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Cluster alert configuration allows to select which conditions of mongod cluster which trigger alerts and how users are notified.
    """


    class MetaOapg:
        required = {
            "eventTypeName",
        }
        
        class properties:
        
            @staticmethod
            def eventTypeName() -> typing.Type['ClusterEventTypeViewAlertable']:
                return ClusterEventTypeViewAlertable
            created = schemas.DateTimeSchema
            enabled = schemas.BoolSchema
            
            
            class groupId(
                schemas.StrSchema
            ):
                pass
            
            
            class id(
                schemas.StrSchema
            ):
                pass
            
            
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
            
            
            class matchers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ClusterMatcherView']:
                        return ClusterMatcherView
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ClusterMatcherView'], typing.List['ClusterMatcherView']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'matchers':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ClusterMatcherView':
                    return super().__getitem__(i)
            
            
            class notifications(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['NotificationViewForNdsGroup']:
                        return NotificationViewForNdsGroup
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['NotificationViewForNdsGroup'], typing.List['NotificationViewForNdsGroup']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'notifications':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'NotificationViewForNdsGroup':
                    return super().__getitem__(i)
            updated = schemas.DateTimeSchema
            __annotations__ = {
                "eventTypeName": eventTypeName,
                "created": created,
                "enabled": enabled,
                "groupId": groupId,
                "id": id,
                "links": links,
                "matchers": matchers,
                "notifications": notifications,
                "updated": updated,
            }
    
    eventTypeName: 'ClusterEventTypeViewAlertable'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["eventTypeName"]) -> 'ClusterEventTypeViewAlertable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupId"]) -> MetaOapg.properties.groupId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> MetaOapg.properties.links: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["matchers"]) -> MetaOapg.properties.matchers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notifications"]) -> MetaOapg.properties.notifications: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated"]) -> MetaOapg.properties.updated: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["eventTypeName", "created", "enabled", "groupId", "id", "links", "matchers", "notifications", "updated", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["eventTypeName"]) -> 'ClusterEventTypeViewAlertable': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> typing.Union[MetaOapg.properties.created, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabled"]) -> typing.Union[MetaOapg.properties.enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupId"]) -> typing.Union[MetaOapg.properties.groupId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union[MetaOapg.properties.links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["matchers"]) -> typing.Union[MetaOapg.properties.matchers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notifications"]) -> typing.Union[MetaOapg.properties.notifications, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated"]) -> typing.Union[MetaOapg.properties.updated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["eventTypeName", "created", "enabled", "groupId", "id", "links", "matchers", "notifications", "updated", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        eventTypeName: 'ClusterEventTypeViewAlertable',
        created: typing.Union[MetaOapg.properties.created, str, datetime, schemas.Unset] = schemas.unset,
        enabled: typing.Union[MetaOapg.properties.enabled, bool, schemas.Unset] = schemas.unset,
        groupId: typing.Union[MetaOapg.properties.groupId, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        links: typing.Union[MetaOapg.properties.links, list, tuple, schemas.Unset] = schemas.unset,
        matchers: typing.Union[MetaOapg.properties.matchers, list, tuple, schemas.Unset] = schemas.unset,
        notifications: typing.Union[MetaOapg.properties.notifications, list, tuple, schemas.Unset] = schemas.unset,
        updated: typing.Union[MetaOapg.properties.updated, str, datetime, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ClusterAlertConfigViewForNdsGroup':
        return super().__new__(
            cls,
            *_args,
            eventTypeName=eventTypeName,
            created=created,
            enabled=enabled,
            groupId=groupId,
            id=id,
            links=links,
            matchers=matchers,
            notifications=notifications,
            updated=updated,
            _configuration=_configuration,
            **kwargs,
        )

from atlas.model.cluster_event_type_view_alertable import ClusterEventTypeViewAlertable
from atlas.model.cluster_matcher_view import ClusterMatcherView
from atlas.model.link import Link
from atlas.model.notification_view_for_nds_group import NotificationViewForNdsGroup
