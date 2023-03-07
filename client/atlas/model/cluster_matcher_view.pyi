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


class ClusterMatcherView(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Rules to apply when comparing an cluster against this alert configuration.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def fieldName() -> typing.Type['ClusterMatcherField']:
                return ClusterMatcherField
            
            
            class operator(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def EQUALS(cls):
                    return cls("EQUALS")
                
                @schemas.classproperty
                def CONTAINS(cls):
                    return cls("CONTAINS")
                
                @schemas.classproperty
                def STARTS_WITH(cls):
                    return cls("STARTS_WITH")
                
                @schemas.classproperty
                def ENDS_WITH(cls):
                    return cls("ENDS_WITH")
                
                @schemas.classproperty
                def NOT_EQUALS(cls):
                    return cls("NOT_EQUALS")
                
                @schemas.classproperty
                def NOT_CONTAINS(cls):
                    return cls("NOT_CONTAINS")
                
                @schemas.classproperty
                def REGEX(cls):
                    return cls("REGEX")
            value = schemas.StrSchema
            __annotations__ = {
                "fieldName": fieldName,
                "operator": operator,
                "value": value,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fieldName"]) -> 'ClusterMatcherField': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operator"]) -> MetaOapg.properties.operator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["value"]) -> MetaOapg.properties.value: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["fieldName", "operator", "value", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fieldName"]) -> typing.Union['ClusterMatcherField', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operator"]) -> typing.Union[MetaOapg.properties.operator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["value"]) -> typing.Union[MetaOapg.properties.value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["fieldName", "operator", "value", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        fieldName: typing.Union['ClusterMatcherField', schemas.Unset] = schemas.unset,
        operator: typing.Union[MetaOapg.properties.operator, str, schemas.Unset] = schemas.unset,
        value: typing.Union[MetaOapg.properties.value, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ClusterMatcherView':
        return super().__new__(
            cls,
            *_args,
            fieldName=fieldName,
            operator=operator,
            value=value,
            _configuration=_configuration,
            **kwargs,
        )

from atlas.model.cluster_matcher_field import ClusterMatcherField
