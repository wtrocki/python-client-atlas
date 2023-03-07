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


class ServerlessInstanceDescriptionCreate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Settings that you can specify when you create a serverless instance.
    """


    class MetaOapg:
        required = {
            "name",
            "providerSettings",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def providerSettings() -> typing.Type['ServerlessProviderSettings']:
                return ServerlessProviderSettings
        
            @staticmethod
            def serverlessBackupOptions() -> typing.Type['ServerlessBackupOptions']:
                return ServerlessBackupOptions
            
            
            class stateName(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def IDLE(cls):
                    return cls("IDLE")
                
                @schemas.classproperty
                def CREATING(cls):
                    return cls("CREATING")
                
                @schemas.classproperty
                def UPDATING(cls):
                    return cls("UPDATING")
                
                @schemas.classproperty
                def DELETING(cls):
                    return cls("DELETING")
                
                @schemas.classproperty
                def DELETED(cls):
                    return cls("DELETED")
                
                @schemas.classproperty
                def REPAIRING(cls):
                    return cls("REPAIRING")
            terminationProtectionEnabled = schemas.BoolSchema
            __annotations__ = {
                "name": name,
                "providerSettings": providerSettings,
                "serverlessBackupOptions": serverlessBackupOptions,
                "stateName": stateName,
                "terminationProtectionEnabled": terminationProtectionEnabled,
            }
    
    name: MetaOapg.properties.name
    providerSettings: 'ServerlessProviderSettings'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerSettings"]) -> 'ServerlessProviderSettings': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serverlessBackupOptions"]) -> 'ServerlessBackupOptions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stateName"]) -> MetaOapg.properties.stateName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["terminationProtectionEnabled"]) -> MetaOapg.properties.terminationProtectionEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "providerSettings", "serverlessBackupOptions", "stateName", "terminationProtectionEnabled", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerSettings"]) -> 'ServerlessProviderSettings': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serverlessBackupOptions"]) -> typing.Union['ServerlessBackupOptions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stateName"]) -> typing.Union[MetaOapg.properties.stateName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["terminationProtectionEnabled"]) -> typing.Union[MetaOapg.properties.terminationProtectionEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "providerSettings", "serverlessBackupOptions", "stateName", "terminationProtectionEnabled", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        providerSettings: 'ServerlessProviderSettings',
        serverlessBackupOptions: typing.Union['ServerlessBackupOptions', schemas.Unset] = schemas.unset,
        stateName: typing.Union[MetaOapg.properties.stateName, str, schemas.Unset] = schemas.unset,
        terminationProtectionEnabled: typing.Union[MetaOapg.properties.terminationProtectionEnabled, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ServerlessInstanceDescriptionCreate':
        return super().__new__(
            cls,
            *_args,
            name=name,
            providerSettings=providerSettings,
            serverlessBackupOptions=serverlessBackupOptions,
            stateName=stateName,
            terminationProtectionEnabled=terminationProtectionEnabled,
            _configuration=_configuration,
            **kwargs,
        )

from atlas.model.serverless_backup_options import ServerlessBackupOptions
from atlas.model.serverless_provider_settings import ServerlessProviderSettings