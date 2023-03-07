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


class UpdateCustomDBRole(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class actions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DBAction']:
                        return DBAction
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['DBAction'], typing.List['DBAction']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'actions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DBAction':
                    return super().__getitem__(i)
            
            
            class inheritedRoles(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['InheritedRole']:
                        return InheritedRole
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['InheritedRole'], typing.List['InheritedRole']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'inheritedRoles':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'InheritedRole':
                    return super().__getitem__(i)
            __annotations__ = {
                "actions": actions,
                "inheritedRoles": inheritedRoles,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actions"]) -> MetaOapg.properties.actions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inheritedRoles"]) -> MetaOapg.properties.inheritedRoles: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["actions", "inheritedRoles", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actions"]) -> typing.Union[MetaOapg.properties.actions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inheritedRoles"]) -> typing.Union[MetaOapg.properties.inheritedRoles, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["actions", "inheritedRoles", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        actions: typing.Union[MetaOapg.properties.actions, list, tuple, schemas.Unset] = schemas.unset,
        inheritedRoles: typing.Union[MetaOapg.properties.inheritedRoles, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UpdateCustomDBRole':
        return super().__new__(
            cls,
            *_args,
            actions=actions,
            inheritedRoles=inheritedRoles,
            _configuration=_configuration,
            **kwargs,
        )

from atlas.model.db_action import DBAction
from atlas.model.inherited_role import InheritedRole
