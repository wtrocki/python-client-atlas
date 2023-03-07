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


class ApiKeyView(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Details contained in one API key.
    """


    class MetaOapg:
        required = {
            "id",
            "publicKey",
        }
        
        class properties:
            
            
            class id(
                schemas.StrSchema
            ):
                pass
            
            
            class publicKey(
                schemas.StrSchema
            ):
                pass
            
            
            class accessList(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AccessListItemView']:
                        return AccessListItemView
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['AccessListItemView'], typing.List['AccessListItemView']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'accessList':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AccessListItemView':
                    return super().__getitem__(i)
            
            
            class roles(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ApiRoleAssignmentView']:
                        return ApiRoleAssignmentView
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ApiRoleAssignmentView'], typing.List['ApiRoleAssignmentView']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'roles':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ApiRoleAssignmentView':
                    return super().__getitem__(i)
            __annotations__ = {
                "id": id,
                "publicKey": publicKey,
                "accessList": accessList,
                "roles": roles,
            }

    
    id: MetaOapg.properties.id
    publicKey: MetaOapg.properties.publicKey
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["publicKey"]) -> MetaOapg.properties.publicKey: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accessList"]) -> MetaOapg.properties.accessList: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["roles"]) -> MetaOapg.properties.roles: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "publicKey", "accessList", "roles", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["publicKey"]) -> MetaOapg.properties.publicKey: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accessList"]) -> typing.Union[MetaOapg.properties.accessList, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["roles"]) -> typing.Union[MetaOapg.properties.roles, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "publicKey", "accessList", "roles", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, None, ],
        accessList: typing.Union[MetaOapg.properties.accessList, list, tuple, schemas.Unset] = schemas.unset,
        roles: typing.Union[MetaOapg.properties.roles, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApiKeyView':
        return super().__new__(
            cls,
            *_args,
            accessList=accessList,
            roles=roles,
            _configuration=_configuration,
            **kwargs,
        )

from atlas.model.access_list_item_view import AccessListItemView
from atlas.model.api_role_assignment_view import ApiRoleAssignmentView