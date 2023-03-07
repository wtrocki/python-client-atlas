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


class ServerlessInstanceDescriptionConnectionStrings(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Collection of Uniform Resource Locators that point to the MongoDB database.
    """


    class MetaOapg:
        
        class properties:
            
            
            class privateEndpoint(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ServerlessInstanceDescriptionConnectionStringsPrivateEndpoint']:
                        return ServerlessInstanceDescriptionConnectionStringsPrivateEndpoint
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ServerlessInstanceDescriptionConnectionStringsPrivateEndpoint'], typing.List['ServerlessInstanceDescriptionConnectionStringsPrivateEndpoint']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'privateEndpoint':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ServerlessInstanceDescriptionConnectionStringsPrivateEndpoint':
                    return super().__getitem__(i)
            standardSrv = schemas.StrSchema
            __annotations__ = {
                "privateEndpoint": privateEndpoint,
                "standardSrv": standardSrv,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["privateEndpoint"]) -> MetaOapg.properties.privateEndpoint: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["standardSrv"]) -> MetaOapg.properties.standardSrv: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["privateEndpoint", "standardSrv", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["privateEndpoint"]) -> typing.Union[MetaOapg.properties.privateEndpoint, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["standardSrv"]) -> typing.Union[MetaOapg.properties.standardSrv, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["privateEndpoint", "standardSrv", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        privateEndpoint: typing.Union[MetaOapg.properties.privateEndpoint, list, tuple, schemas.Unset] = schemas.unset,
        standardSrv: typing.Union[MetaOapg.properties.standardSrv, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ServerlessInstanceDescriptionConnectionStrings':
        return super().__new__(
            cls,
            *_args,
            privateEndpoint=privateEndpoint,
            standardSrv=standardSrv,
            _configuration=_configuration,
            **kwargs,
        )

from atlas.model.serverless_instance_description_connection_strings_private_endpoint import ServerlessInstanceDescriptionConnectionStringsPrivateEndpoint
