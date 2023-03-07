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


class GreaterThanDaysThresholdView(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Threshold value that triggers an alert.
    """


    class MetaOapg:
        
        class properties:
            
            
            class operator(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "GREATER_THAN": "GREATER_THAN",
                    }
                
                @schemas.classproperty
                def GREATER_THAN(cls):
                    return cls("GREATER_THAN")
            threshold = schemas.Int32Schema
            
            
            class units(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "DAYS": "DAYS",
                    }
                
                @schemas.classproperty
                def DAYS(cls):
                    return cls("DAYS")
            __annotations__ = {
                "operator": operator,
                "threshold": threshold,
                "units": units,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["operator"]) -> MetaOapg.properties.operator: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["threshold"]) -> MetaOapg.properties.threshold: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["units"]) -> MetaOapg.properties.units: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["operator", "threshold", "units", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["operator"]) -> typing.Union[MetaOapg.properties.operator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["threshold"]) -> typing.Union[MetaOapg.properties.threshold, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["units"]) -> typing.Union[MetaOapg.properties.units, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["operator", "threshold", "units", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        operator: typing.Union[MetaOapg.properties.operator, str, schemas.Unset] = schemas.unset,
        threshold: typing.Union[MetaOapg.properties.threshold, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        units: typing.Union[MetaOapg.properties.units, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GreaterThanDaysThresholdView':
        return super().__new__(
            cls,
            *_args,
            operator=operator,
            threshold=threshold,
            units=units,
            _configuration=_configuration,
            **kwargs,
        )
