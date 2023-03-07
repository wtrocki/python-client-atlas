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


class UserNotificationView(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    User notification configuration for MongoDB Cloud to send information when an event triggers an alert condition.
    """


    class MetaOapg:
        required = {
            "typeName",
        }
        
        class properties:
            
            
            class typeName(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def USER(cls):
                    return cls("USER")
            delayMin = schemas.Int32Schema
            emailEnabled = schemas.BoolSchema
            
            
            class intervalMin(
                schemas.Int32Schema
            ):
                pass
            smsEnabled = schemas.BoolSchema
            username = schemas.StrSchema
            __annotations__ = {
                "typeName": typeName,
                "delayMin": delayMin,
                "emailEnabled": emailEnabled,
                "intervalMin": intervalMin,
                "smsEnabled": smsEnabled,
                "username": username,
            }
    
    typeName: MetaOapg.properties.typeName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["typeName"]) -> MetaOapg.properties.typeName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["delayMin"]) -> MetaOapg.properties.delayMin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["emailEnabled"]) -> MetaOapg.properties.emailEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["intervalMin"]) -> MetaOapg.properties.intervalMin: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["smsEnabled"]) -> MetaOapg.properties.smsEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["username"]) -> MetaOapg.properties.username: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["typeName", "delayMin", "emailEnabled", "intervalMin", "smsEnabled", "username", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["typeName"]) -> MetaOapg.properties.typeName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["delayMin"]) -> typing.Union[MetaOapg.properties.delayMin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["emailEnabled"]) -> typing.Union[MetaOapg.properties.emailEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["intervalMin"]) -> typing.Union[MetaOapg.properties.intervalMin, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["smsEnabled"]) -> typing.Union[MetaOapg.properties.smsEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["username"]) -> typing.Union[MetaOapg.properties.username, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["typeName", "delayMin", "emailEnabled", "intervalMin", "smsEnabled", "username", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        typeName: typing.Union[MetaOapg.properties.typeName, str, ],
        delayMin: typing.Union[MetaOapg.properties.delayMin, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        emailEnabled: typing.Union[MetaOapg.properties.emailEnabled, bool, schemas.Unset] = schemas.unset,
        intervalMin: typing.Union[MetaOapg.properties.intervalMin, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        smsEnabled: typing.Union[MetaOapg.properties.smsEnabled, bool, schemas.Unset] = schemas.unset,
        username: typing.Union[MetaOapg.properties.username, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserNotificationView':
        return super().__new__(
            cls,
            *_args,
            typeName=typeName,
            delayMin=delayMin,
            emailEnabled=emailEnabled,
            intervalMin=intervalMin,
            smsEnabled=smsEnabled,
            username=username,
            _configuration=_configuration,
            **kwargs,
        )
