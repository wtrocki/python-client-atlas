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


class DedicatedHardwareSpec(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Hardware specifications for read-only nodes in the region. Read-only nodes can never become the primary member, but can enable local reads.If you don't specify this parameter, no read-only nodes are deployed to the region.
    """


    class MetaOapg:
        
        class properties:
            nodeCount = schemas.Int32Schema
            diskIOPS = schemas.Int32Schema
            
            
            class ebsVolumeType(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def STANDARD(cls):
                    return cls("STANDARD")
                
                @schemas.classproperty
                def PROVISIONED(cls):
                    return cls("PROVISIONED")
            
            
            class instanceSize(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def M10(cls):
                    return cls("M10")
                
                @schemas.classproperty
                def M20(cls):
                    return cls("M20")
                
                @schemas.classproperty
                def M30(cls):
                    return cls("M30")
                
                @schemas.classproperty
                def M40(cls):
                    return cls("M40")
                
                @schemas.classproperty
                def M50(cls):
                    return cls("M50")
                
                @schemas.classproperty
                def M60(cls):
                    return cls("M60")
                
                @schemas.classproperty
                def M80(cls):
                    return cls("M80")
                
                @schemas.classproperty
                def M140(cls):
                    return cls("M140")
                
                @schemas.classproperty
                def M200(cls):
                    return cls("M200")
                
                @schemas.classproperty
                def M250(cls):
                    return cls("M250")
                
                @schemas.classproperty
                def M300(cls):
                    return cls("M300")
                
                @schemas.classproperty
                def M400(cls):
                    return cls("M400")
                
                @schemas.classproperty
                def R40(cls):
                    return cls("R40")
                
                @schemas.classproperty
                def R50(cls):
                    return cls("R50")
                
                @schemas.classproperty
                def R60(cls):
                    return cls("R60")
                
                @schemas.classproperty
                def R80(cls):
                    return cls("R80")
                
                @schemas.classproperty
                def R200(cls):
                    return cls("R200")
                
                @schemas.classproperty
                def R300(cls):
                    return cls("R300")
                
                @schemas.classproperty
                def R400(cls):
                    return cls("R400")
                
                @schemas.classproperty
                def R600(cls):
                    return cls("R600")
            __annotations__ = {
                "nodeCount": nodeCount,
                "diskIOPS": diskIOPS,
                "ebsVolumeType": ebsVolumeType,
                "instanceSize": instanceSize,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nodeCount"]) -> MetaOapg.properties.nodeCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["diskIOPS"]) -> MetaOapg.properties.diskIOPS: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ebsVolumeType"]) -> MetaOapg.properties.ebsVolumeType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["instanceSize"]) -> MetaOapg.properties.instanceSize: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["nodeCount", "diskIOPS", "ebsVolumeType", "instanceSize", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nodeCount"]) -> typing.Union[MetaOapg.properties.nodeCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["diskIOPS"]) -> typing.Union[MetaOapg.properties.diskIOPS, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ebsVolumeType"]) -> typing.Union[MetaOapg.properties.ebsVolumeType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["instanceSize"]) -> typing.Union[MetaOapg.properties.instanceSize, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["nodeCount", "diskIOPS", "ebsVolumeType", "instanceSize", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        nodeCount: typing.Union[MetaOapg.properties.nodeCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        diskIOPS: typing.Union[MetaOapg.properties.diskIOPS, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        ebsVolumeType: typing.Union[MetaOapg.properties.ebsVolumeType, str, schemas.Unset] = schemas.unset,
        instanceSize: typing.Union[MetaOapg.properties.instanceSize, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DedicatedHardwareSpec':
        return super().__new__(
            cls,
            *_args,
            nodeCount=nodeCount,
            diskIOPS=diskIOPS,
            ebsVolumeType=ebsVolumeType,
            instanceSize=instanceSize,
            _configuration=_configuration,
            **kwargs,
        )
