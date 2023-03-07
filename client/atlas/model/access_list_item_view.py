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


class AccessListItemView(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "ipAddress",
        }
        
        class properties:
            
            
            class ipAddress(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)(\.(?!$)|$)){4}|([0-9a-f]{1,4}\:){7}[0-9a-f]{1,4}$',  # noqa: E501
                    }]
            
            
            class cidrBlock(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^((([0-9]{1,3}\.){3}[0-9]{1,3})|([\:]{0,2}([0-9a-f]{1,4}\:){0,7}[0-9a-f]{1,4}[\:]{0,2}))((%2[fF]|\/)[0-9]{1,3})+$',  # noqa: E501
                    }]
            __annotations__ = {
                "ipAddress": ipAddress,
                "cidrBlock": cidrBlock,
            }
    
    ipAddress: MetaOapg.properties.ipAddress
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipAddress"]) -> MetaOapg.properties.ipAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cidrBlock"]) -> MetaOapg.properties.cidrBlock: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["ipAddress", "cidrBlock", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipAddress"]) -> MetaOapg.properties.ipAddress: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cidrBlock"]) -> typing.Union[MetaOapg.properties.cidrBlock, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["ipAddress", "cidrBlock", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        ipAddress: typing.Union[MetaOapg.properties.ipAddress, str, ],
        cidrBlock: typing.Union[MetaOapg.properties.cidrBlock, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AccessListItemView':
        return super().__new__(
            cls,
            *_args,
            ipAddress=ipAddress,
            cidrBlock=cidrBlock,
            _configuration=_configuration,
            **kwargs,
        )
