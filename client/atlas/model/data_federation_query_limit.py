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


class DataFederationQueryLimit(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Details of a query limit for Data Federation. Query limit is the limit on the amount of usage during a time period based on cost.
    """


    class MetaOapg:
        required = {
            "name",
            "value",
        }
        
        class properties:
            name = schemas.StrSchema
            value = schemas.Int64Schema
            currentUsage = schemas.Int64Schema
            defaultLimit = schemas.Int64Schema
            lastModifiedDate = schemas.DateTimeSchema
            maximumLimit = schemas.Int64Schema
            
            
            class overrunPolicy(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "BLOCK": "BLOCK",
                        "BLOCK_AND_KILL": "BLOCK_AND_KILL",
                    }
                
                @schemas.classproperty
                def BLOCK(cls):
                    return cls("BLOCK")
                
                @schemas.classproperty
                def BLOCK_AND_KILL(cls):
                    return cls("BLOCK_AND_KILL")
            __annotations__ = {
                "name": name,
                "value": value,
                "currentUsage": currentUsage,
                "defaultLimit": defaultLimit,
                "lastModifiedDate": lastModifiedDate,
                "maximumLimit": maximumLimit,
                "overrunPolicy": overrunPolicy,
            }
    
    name: MetaOapg.properties.name
    value: MetaOapg.properties.value
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currentUsage"]) -> MetaOapg.properties.currentUsage: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultLimit"]) -> MetaOapg.properties.defaultLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastModifiedDate"]) -> MetaOapg.properties.lastModifiedDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maximumLimit"]) -> MetaOapg.properties.maximumLimit: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["overrunPolicy"]) -> MetaOapg.properties.overrunPolicy: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "value", "currentUsage", "defaultLimit", "lastModifiedDate", "maximumLimit", "overrunPolicy", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currentUsage"]) -> typing.Union[MetaOapg.properties.currentUsage, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultLimit"]) -> typing.Union[MetaOapg.properties.defaultLimit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastModifiedDate"]) -> typing.Union[MetaOapg.properties.lastModifiedDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maximumLimit"]) -> typing.Union[MetaOapg.properties.maximumLimit, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["overrunPolicy"]) -> typing.Union[MetaOapg.properties.overrunPolicy, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "value", "currentUsage", "defaultLimit", "lastModifiedDate", "maximumLimit", "overrunPolicy", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        value: typing.Union[MetaOapg.properties.value, decimal.Decimal, int, ],
        currentUsage: typing.Union[MetaOapg.properties.currentUsage, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        defaultLimit: typing.Union[MetaOapg.properties.defaultLimit, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        lastModifiedDate: typing.Union[MetaOapg.properties.lastModifiedDate, str, datetime, schemas.Unset] = schemas.unset,
        maximumLimit: typing.Union[MetaOapg.properties.maximumLimit, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        overrunPolicy: typing.Union[MetaOapg.properties.overrunPolicy, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DataFederationQueryLimit':
        return super().__new__(
            cls,
            *_args,
            name=name,
            value=value,
            currentUsage=currentUsage,
            defaultLimit=defaultLimit,
            lastModifiedDate=lastModifiedDate,
            maximumLimit=maximumLimit,
            overrunPolicy=overrunPolicy,
            _configuration=_configuration,
            **kwargs,
        )
