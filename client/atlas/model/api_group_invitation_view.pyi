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


class ApiGroupInvitationView(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            createdAt = schemas.DateTimeSchema
            expiresAt = schemas.DateTimeSchema
            
            
            class groupId(
                schemas.StrSchema
            ):
                pass
            
            
            class groupName(
                schemas.StrSchema
            ):
                pass
            
            
            class id(
                schemas.StrSchema
            ):
                pass
            inviterUsername = schemas.StrSchema
            
            
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
            
            
            class roles(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def CLUSTER_MANAGER(cls):
                            return cls("GROUP_CLUSTER_MANAGER")
                        
                        @schemas.classproperty
                        def DATA_ACCESS_ADMIN(cls):
                            return cls("GROUP_DATA_ACCESS_ADMIN")
                        
                        @schemas.classproperty
                        def DATA_ACCESS_READ_ONLY(cls):
                            return cls("GROUP_DATA_ACCESS_READ_ONLY")
                        
                        @schemas.classproperty
                        def DATA_ACCESS_READ_WRITE(cls):
                            return cls("GROUP_DATA_ACCESS_READ_WRITE")
                        
                        @schemas.classproperty
                        def OWNER(cls):
                            return cls("GROUP_OWNER")
                        
                        @schemas.classproperty
                        def READ_ONLY(cls):
                            return cls("GROUP_READ_ONLY")
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'roles':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            username = schemas.StrSchema
            __annotations__ = {
                "createdAt": createdAt,
                "expiresAt": expiresAt,
                "groupId": groupId,
                "groupName": groupName,
                "id": id,
                "inviterUsername": inviterUsername,
                "links": links,
                "roles": roles,
                "username": username,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["createdAt"]) -> MetaOapg.properties.createdAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiresAt"]) -> MetaOapg.properties.expiresAt: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupId"]) -> MetaOapg.properties.groupId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["groupName"]) -> MetaOapg.properties.groupName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inviterUsername"]) -> MetaOapg.properties.inviterUsername: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> MetaOapg.properties.links: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["roles"]) -> MetaOapg.properties.roles: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["createdAt", "expiresAt", "groupId", "groupName", "id", "inviterUsername", "links", "roles", "username", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["createdAt"]) -> typing.Union[MetaOapg.properties.createdAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiresAt"]) -> typing.Union[MetaOapg.properties.expiresAt, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupId"]) -> typing.Union[MetaOapg.properties.groupId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["groupName"]) -> typing.Union[MetaOapg.properties.groupName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inviterUsername"]) -> typing.Union[MetaOapg.properties.inviterUsername, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union[MetaOapg.properties.links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["roles"]) -> typing.Union[MetaOapg.properties.roles, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> typing.Union[MetaOapg.properties.username, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["createdAt", "expiresAt", "groupId", "groupName", "id", "inviterUsername", "links", "roles", "username", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        createdAt: typing.Union[MetaOapg.properties.createdAt, str, datetime, schemas.Unset] = schemas.unset,
        expiresAt: typing.Union[MetaOapg.properties.expiresAt, str, datetime, schemas.Unset] = schemas.unset,
        groupId: typing.Union[MetaOapg.properties.groupId, str, schemas.Unset] = schemas.unset,
        groupName: typing.Union[MetaOapg.properties.groupName, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        inviterUsername: typing.Union[MetaOapg.properties.inviterUsername, str, schemas.Unset] = schemas.unset,
        links: typing.Union[MetaOapg.properties.links, list, tuple, schemas.Unset] = schemas.unset,
        roles: typing.Union[MetaOapg.properties.roles, list, tuple, schemas.Unset] = schemas.unset,
        username: typing.Union[MetaOapg.properties.username, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApiGroupInvitationView':
        return super().__new__(
            cls,
            *_args,
            createdAt=createdAt,
            expiresAt=expiresAt,
            groupId=groupId,
            groupName=groupName,
            id=id,
            inviterUsername=inviterUsername,
            links=links,
            roles=roles,
            username=username,
            _configuration=_configuration,
            **kwargs,
        )

from atlas.model.link import Link
