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


class ClusterDescriptionConnectionStringsPrivateEndpointEndpoint(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Details of a private endpoint deployed for this cluster.
    """


    class MetaOapg:
        
        class properties:
            endpointId = schemas.StrSchema
            
            
            class providerName(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "AWS": "AWS",
                        "AZURE": "AZURE",
                        "GCP": "GCP",
                    }
                
                @schemas.classproperty
                def AWS(cls):
                    return cls("AWS")
                
                @schemas.classproperty
                def AZURE(cls):
                    return cls("AZURE")
                
                @schemas.classproperty
                def GCP(cls):
                    return cls("GCP")
            region = schemas.StrSchema
            __annotations__ = {
                "endpointId": endpointId,
                "providerName": providerName,
                "region": region,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["endpointId"]) -> MetaOapg.properties.endpointId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerName"]) -> MetaOapg.properties.providerName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["region"]) -> MetaOapg.properties.region: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["endpointId", "providerName", "region", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["endpointId"]) -> typing.Union[MetaOapg.properties.endpointId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerName"]) -> typing.Union[MetaOapg.properties.providerName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["region"]) -> typing.Union[MetaOapg.properties.region, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["endpointId", "providerName", "region", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        endpointId: typing.Union[MetaOapg.properties.endpointId, str, schemas.Unset] = schemas.unset,
        providerName: typing.Union[MetaOapg.properties.providerName, str, schemas.Unset] = schemas.unset,
        region: typing.Union[MetaOapg.properties.region, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ClusterDescriptionConnectionStringsPrivateEndpointEndpoint':
        return super().__new__(
            cls,
            *_args,
            endpointId=endpointId,
            providerName=providerName,
            region=region,
            _configuration=_configuration,
            **kwargs,
        )
