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


class LiveMigrationResponseView(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class _id(
                schemas.StrSchema
            ):
                pass
            
            
            class lagTimeSeconds(
                schemas.Int64Base,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    format = 'int64'
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'lagTimeSeconds':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                    )
            
            
            class migrationHosts(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.StrSchema
                    ):
                        pass
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'migrationHosts':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            readyForCutover = schemas.BoolSchema
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def NEW(cls):
                    return cls("NEW")
                
                @schemas.classproperty
                def WORKING(cls):
                    return cls("WORKING")
                
                @schemas.classproperty
                def FAILED(cls):
                    return cls("FAILED")
                
                @schemas.classproperty
                def COMPLETE(cls):
                    return cls("COMPLETE")
                
                @schemas.classproperty
                def EXPIRED(cls):
                    return cls("EXPIRED")
            __annotations__ = {
                "_id": _id,
                "lagTimeSeconds": lagTimeSeconds,
                "migrationHosts": migrationHosts,
                "readyForCutover": readyForCutover,
                "status": status,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["_id"]) -> MetaOapg.properties._id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lagTimeSeconds"]) -> MetaOapg.properties.lagTimeSeconds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["migrationHosts"]) -> MetaOapg.properties.migrationHosts: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["readyForCutover"]) -> MetaOapg.properties.readyForCutover: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["_id", "lagTimeSeconds", "migrationHosts", "readyForCutover", "status", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["_id"]) -> typing.Union[MetaOapg.properties._id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lagTimeSeconds"]) -> typing.Union[MetaOapg.properties.lagTimeSeconds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["migrationHosts"]) -> typing.Union[MetaOapg.properties.migrationHosts, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["readyForCutover"]) -> typing.Union[MetaOapg.properties.readyForCutover, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["_id", "lagTimeSeconds", "migrationHosts", "readyForCutover", "status", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        _id: typing.Union[MetaOapg.properties._id, str, schemas.Unset] = schemas.unset,
        lagTimeSeconds: typing.Union[MetaOapg.properties.lagTimeSeconds, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        migrationHosts: typing.Union[MetaOapg.properties.migrationHosts, list, tuple, schemas.Unset] = schemas.unset,
        readyForCutover: typing.Union[MetaOapg.properties.readyForCutover, bool, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LiveMigrationResponseView':
        return super().__new__(
            cls,
            *_args,
            _id=_id,
            lagTimeSeconds=lagTimeSeconds,
            migrationHosts=migrationHosts,
            readyForCutover=readyForCutover,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )