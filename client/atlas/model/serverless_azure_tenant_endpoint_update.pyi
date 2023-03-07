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


class ServerlessAzureTenantEndpointUpdate(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Updates to a serverless Azure tenant endpoint.
    """


    class MetaOapg:
        required = {
            "providerName",
        }
        
        class properties:
            providerName = schemas.StrSchema
            
            
            class cloudProviderEndpointId(
                schemas.StrSchema
            ):
                pass
            
            
            class privateEndpointIpAddress(
                schemas.StrSchema
            ):
                pass
            
            
            class comment(
                schemas.StrSchema
            ):
                pass
            __annotations__ = {
                "providerName": providerName,
                "cloudProviderEndpointId": cloudProviderEndpointId,
                "privateEndpointIpAddress": privateEndpointIpAddress,
                "comment": comment,
            }
    
    providerName: MetaOapg.properties.providerName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerName"]) -> MetaOapg.properties.providerName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cloudProviderEndpointId"]) -> MetaOapg.properties.cloudProviderEndpointId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["privateEndpointIpAddress"]) -> MetaOapg.properties.privateEndpointIpAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["providerName", "cloudProviderEndpointId", "privateEndpointIpAddress", "comment", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerName"]) -> MetaOapg.properties.providerName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cloudProviderEndpointId"]) -> typing.Union[MetaOapg.properties.cloudProviderEndpointId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["privateEndpointIpAddress"]) -> typing.Union[MetaOapg.properties.privateEndpointIpAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union[MetaOapg.properties.comment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["providerName", "cloudProviderEndpointId", "privateEndpointIpAddress", "comment", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        providerName: typing.Union[MetaOapg.properties.providerName, str, ],
        cloudProviderEndpointId: typing.Union[MetaOapg.properties.cloudProviderEndpointId, str, schemas.Unset] = schemas.unset,
        privateEndpointIpAddress: typing.Union[MetaOapg.properties.privateEndpointIpAddress, str, schemas.Unset] = schemas.unset,
        comment: typing.Union[MetaOapg.properties.comment, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ServerlessAzureTenantEndpointUpdate':
        return super().__new__(
            cls,
            *_args,
            providerName=providerName,
            cloudProviderEndpointId=cloudProviderEndpointId,
            privateEndpointIpAddress=privateEndpointIpAddress,
            comment=comment,
            _configuration=_configuration,
            **kwargs,
        )