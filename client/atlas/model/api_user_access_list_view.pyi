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


class ApiUserAccessListView(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class cidrBlock(
                schemas.StrSchema
            ):
                pass
            
            
            class count(
                schemas.Int32Schema
            ):
                pass
            created = schemas.DateTimeSchema
            
            
            class ipAddress(
                schemas.StrSchema
            ):
                pass
            lastUsed = schemas.DateTimeSchema
            
            
            class lastUsedAddress(
                schemas.StrSchema
            ):
                pass
            
            
            class links(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Link']:
                        return Link
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Link'], typing.List['Link']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'links':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Link':
                    return super().__getitem__(i)
            __annotations__ = {
                "cidrBlock": cidrBlock,
                "count": count,
                "created": created,
                "ipAddress": ipAddress,
                "lastUsed": lastUsed,
                "lastUsedAddress": lastUsedAddress,
                "links": links,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cidrBlock"]) -> MetaOapg.properties.cidrBlock: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["count"]) -> MetaOapg.properties.count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created"]) -> MetaOapg.properties.created: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ipAddress"]) -> MetaOapg.properties.ipAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastUsed"]) -> MetaOapg.properties.lastUsed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastUsedAddress"]) -> MetaOapg.properties.lastUsedAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> MetaOapg.properties.links: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["cidrBlock", "count", "created", "ipAddress", "lastUsed", "lastUsedAddress", "links", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cidrBlock"]) -> typing.Union[MetaOapg.properties.cidrBlock, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["count"]) -> typing.Union[MetaOapg.properties.count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created"]) -> typing.Union[MetaOapg.properties.created, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ipAddress"]) -> typing.Union[MetaOapg.properties.ipAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastUsed"]) -> typing.Union[MetaOapg.properties.lastUsed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastUsedAddress"]) -> typing.Union[MetaOapg.properties.lastUsedAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union[MetaOapg.properties.links, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["cidrBlock", "count", "created", "ipAddress", "lastUsed", "lastUsedAddress", "links", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        cidrBlock: typing.Union[MetaOapg.properties.cidrBlock, str, schemas.Unset] = schemas.unset,
        count: typing.Union[MetaOapg.properties.count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        created: typing.Union[MetaOapg.properties.created, str, datetime, schemas.Unset] = schemas.unset,
        ipAddress: typing.Union[MetaOapg.properties.ipAddress, str, schemas.Unset] = schemas.unset,
        lastUsed: typing.Union[MetaOapg.properties.lastUsed, str, datetime, schemas.Unset] = schemas.unset,
        lastUsedAddress: typing.Union[MetaOapg.properties.lastUsedAddress, str, schemas.Unset] = schemas.unset,
        links: typing.Union[MetaOapg.properties.links, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApiUserAccessListView':
        return super().__new__(
            cls,
            *_args,
            cidrBlock=cidrBlock,
            count=count,
            created=created,
            ipAddress=ipAddress,
            lastUsed=lastUsed,
            lastUsedAddress=lastUsedAddress,
            links=links,
            _configuration=_configuration,
            **kwargs,
        )

from atlas.model.link import Link