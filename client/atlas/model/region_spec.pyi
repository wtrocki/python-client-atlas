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


class RegionSpec(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Physical location where MongoDB Cloud provisions cluster nodes.
    """


    class MetaOapg:
        
        class properties:
            analyticsNodes = schemas.Int32Schema
            
            
            class electableNodes(
                schemas.EnumBase,
                schemas.Int32Schema
            ):
                
                @schemas.classproperty
                def POSITIVE_0(cls):
                    return cls(0)
                
                @schemas.classproperty
                def POSITIVE_3(cls):
                    return cls(3)
                
                @schemas.classproperty
                def POSITIVE_5(cls):
                    return cls(5)
                
                @schemas.classproperty
                def POSITIVE_7(cls):
                    return cls(7)
            
            
            class priority(
                schemas.Int32Schema
            ):
                pass
            readOnlyNodes = schemas.Int32Schema
            __annotations__ = {
                "analyticsNodes": analyticsNodes,
                "electableNodes": electableNodes,
                "priority": priority,
                "readOnlyNodes": readOnlyNodes,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["analyticsNodes"]) -> MetaOapg.properties.analyticsNodes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["electableNodes"]) -> MetaOapg.properties.electableNodes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["readOnlyNodes"]) -> MetaOapg.properties.readOnlyNodes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["analyticsNodes", "electableNodes", "priority", "readOnlyNodes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["analyticsNodes"]) -> typing.Union[MetaOapg.properties.analyticsNodes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["electableNodes"]) -> typing.Union[MetaOapg.properties.electableNodes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priority"]) -> typing.Union[MetaOapg.properties.priority, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["readOnlyNodes"]) -> typing.Union[MetaOapg.properties.readOnlyNodes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["analyticsNodes", "electableNodes", "priority", "readOnlyNodes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        analyticsNodes: typing.Union[MetaOapg.properties.analyticsNodes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        electableNodes: typing.Union[MetaOapg.properties.electableNodes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        priority: typing.Union[MetaOapg.properties.priority, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        readOnlyNodes: typing.Union[MetaOapg.properties.readOnlyNodes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RegionSpec':
        return super().__new__(
            cls,
            *_args,
            analyticsNodes=analyticsNodes,
            electableNodes=electableNodes,
            priority=priority,
            readOnlyNodes=readOnlyNodes,
            _configuration=_configuration,
            **kwargs,
        )