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


class TokenizeredgeGram(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Tokenizer that splits input from the left side, or "edge", of a text input into n-grams of given sizes. You can't use the edgeGram tokenizer in synonym or autocomplete mapping definitions.
    """


    class MetaOapg:
        required = {
            "maxGram",
            "type",
            "minGram",
        }
        
        class properties:
            maxGram = schemas.IntSchema
            minGram = schemas.IntSchema
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def EDGE_GRAM(cls):
                    return cls("edgeGram")
            __annotations__ = {
                "maxGram": maxGram,
                "minGram": minGram,
                "type": type,
            }
    
    maxGram: MetaOapg.properties.maxGram
    type: MetaOapg.properties.type
    minGram: MetaOapg.properties.minGram
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxGram"]) -> MetaOapg.properties.maxGram: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minGram"]) -> MetaOapg.properties.minGram: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["maxGram", "minGram", "type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxGram"]) -> MetaOapg.properties.maxGram: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minGram"]) -> MetaOapg.properties.minGram: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["maxGram", "minGram", "type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        maxGram: typing.Union[MetaOapg.properties.maxGram, decimal.Decimal, int, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        minGram: typing.Union[MetaOapg.properties.minGram, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TokenizeredgeGram':
        return super().__new__(
            cls,
            *_args,
            maxGram=maxGram,
            type=type,
            minGram=minGram,
            _configuration=_configuration,
            **kwargs,
        )
