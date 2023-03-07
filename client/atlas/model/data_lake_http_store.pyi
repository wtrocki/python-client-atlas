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


class DataLakeHTTPStore(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "provider",
        }
        
        class properties:
            provider = schemas.StrSchema
            allowInsecure = schemas.BoolSchema
            defaultFormat = schemas.StrSchema
            
            
            class urls(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'urls':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            name = schemas.StrSchema
            __annotations__ = {
                "provider": provider,
                "allowInsecure": allowInsecure,
                "defaultFormat": defaultFormat,
                "urls": urls,
                "name": name,
            }
    
    provider: MetaOapg.properties.provider
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provider"]) -> MetaOapg.properties.provider: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allowInsecure"]) -> MetaOapg.properties.allowInsecure: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultFormat"]) -> MetaOapg.properties.defaultFormat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["urls"]) -> MetaOapg.properties.urls: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["provider", "allowInsecure", "defaultFormat", "urls", "name", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provider"]) -> MetaOapg.properties.provider: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allowInsecure"]) -> typing.Union[MetaOapg.properties.allowInsecure, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultFormat"]) -> typing.Union[MetaOapg.properties.defaultFormat, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["urls"]) -> typing.Union[MetaOapg.properties.urls, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["provider", "allowInsecure", "defaultFormat", "urls", "name", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        provider: typing.Union[MetaOapg.properties.provider, str, ],
        allowInsecure: typing.Union[MetaOapg.properties.allowInsecure, bool, schemas.Unset] = schemas.unset,
        defaultFormat: typing.Union[MetaOapg.properties.defaultFormat, str, schemas.Unset] = schemas.unset,
        urls: typing.Union[MetaOapg.properties.urls, list, tuple, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DataLakeHTTPStore':
        return super().__new__(
            cls,
            *_args,
            provider=provider,
            allowInsecure=allowInsecure,
            defaultFormat=defaultFormat,
            urls=urls,
            name=name,
            _configuration=_configuration,
            **kwargs,
        )
