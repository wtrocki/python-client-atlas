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


class AzureComputeAutoScaling(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Collection of settings that configures how a cluster might scale its cluster tier and whether the cluster can scale down. Cluster tier auto-scaling is unavailable for clusters using Low CPU or NVME storage classes.
    """


    class MetaOapg:
        
        class properties:
            
            
            class maxInstanceSize(
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
                def M90(cls):
                    return cls("M90")
                
                @schemas.classproperty
                def M200(cls):
                    return cls("M200")
                
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
                def M60_NVME(cls):
                    return cls("M60_NVME")
                
                @schemas.classproperty
                def M80_NVME(cls):
                    return cls("M80_NVME")
                
                @schemas.classproperty
                def M200_NVME(cls):
                    return cls("M200_NVME")
                
                @schemas.classproperty
                def M300_NVME(cls):
                    return cls("M300_NVME")
                
                @schemas.classproperty
                def M400_NVME(cls):
                    return cls("M400_NVME")
                
                @schemas.classproperty
                def M600_NVME(cls):
                    return cls("M600_NVME")
            
            
            class minInstanceSize(
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
                def M90(cls):
                    return cls("M90")
                
                @schemas.classproperty
                def M200(cls):
                    return cls("M200")
                
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
                def M60_NVME(cls):
                    return cls("M60_NVME")
                
                @schemas.classproperty
                def M80_NVME(cls):
                    return cls("M80_NVME")
                
                @schemas.classproperty
                def M200_NVME(cls):
                    return cls("M200_NVME")
                
                @schemas.classproperty
                def M300_NVME(cls):
                    return cls("M300_NVME")
                
                @schemas.classproperty
                def M400_NVME(cls):
                    return cls("M400_NVME")
                
                @schemas.classproperty
                def M600_NVME(cls):
                    return cls("M600_NVME")
            __annotations__ = {
                "maxInstanceSize": maxInstanceSize,
                "minInstanceSize": minInstanceSize,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maxInstanceSize"]) -> MetaOapg.properties.maxInstanceSize: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minInstanceSize"]) -> MetaOapg.properties.minInstanceSize: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["maxInstanceSize", "minInstanceSize", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maxInstanceSize"]) -> typing.Union[MetaOapg.properties.maxInstanceSize, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minInstanceSize"]) -> typing.Union[MetaOapg.properties.minInstanceSize, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["maxInstanceSize", "minInstanceSize", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        maxInstanceSize: typing.Union[MetaOapg.properties.maxInstanceSize, str, schemas.Unset] = schemas.unset,
        minInstanceSize: typing.Union[MetaOapg.properties.minInstanceSize, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AzureComputeAutoScaling':
        return super().__new__(
            cls,
            *_args,
            maxInstanceSize=maxInstanceSize,
            minInstanceSize=minInstanceSize,
            _configuration=_configuration,
            **kwargs,
        )