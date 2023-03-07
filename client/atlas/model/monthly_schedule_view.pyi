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


class MonthlyScheduleView(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "type",
        }
        
        class properties:
            type = schemas.StrSchema
            
            
            class dayOfMonth(
                schemas.Int32Schema
            ):
                pass
            
            
            class endHour(
                schemas.Int32Schema
            ):
                pass
            
            
            class endMinute(
                schemas.Int32Schema
            ):
                pass
            
            
            class startHour(
                schemas.Int32Schema
            ):
                pass
            
            
            class startMinute(
                schemas.Int32Schema
            ):
                pass
            __annotations__ = {
                "type": type,
                "dayOfMonth": dayOfMonth,
                "endHour": endHour,
                "endMinute": endMinute,
                "startHour": startHour,
                "startMinute": startMinute,
            }
    
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dayOfMonth"]) -> MetaOapg.properties.dayOfMonth: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endHour"]) -> MetaOapg.properties.endHour: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endMinute"]) -> MetaOapg.properties.endMinute: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startHour"]) -> MetaOapg.properties.startHour: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["startMinute"]) -> MetaOapg.properties.startMinute: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["type", "dayOfMonth", "endHour", "endMinute", "startHour", "startMinute", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dayOfMonth"]) -> typing.Union[MetaOapg.properties.dayOfMonth, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endHour"]) -> typing.Union[MetaOapg.properties.endHour, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endMinute"]) -> typing.Union[MetaOapg.properties.endMinute, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startHour"]) -> typing.Union[MetaOapg.properties.startHour, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["startMinute"]) -> typing.Union[MetaOapg.properties.startMinute, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["type", "dayOfMonth", "endHour", "endMinute", "startHour", "startMinute", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        dayOfMonth: typing.Union[MetaOapg.properties.dayOfMonth, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        endHour: typing.Union[MetaOapg.properties.endHour, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        endMinute: typing.Union[MetaOapg.properties.endMinute, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        startHour: typing.Union[MetaOapg.properties.startHour, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        startMinute: typing.Union[MetaOapg.properties.startMinute, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MonthlyScheduleView':
        return super().__new__(
            cls,
            *_args,
            type=type,
            dayOfMonth=dayOfMonth,
            endHour=endHour,
            endMinute=endMinute,
            startHour=startHour,
            startMinute=startMinute,
            _configuration=_configuration,
            **kwargs,
        )
