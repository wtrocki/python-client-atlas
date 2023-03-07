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


class AzureRegionConfig(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Details that explain how MongoDB Cloud replicates data in one region on the specified MongoDB database.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def analyticsAutoScaling() -> typing.Type['AutoScalingV15']:
                return AutoScalingV15
        
            @staticmethod
            def analyticsSpecs() -> typing.Type['DedicatedHardwareSpec']:
                return DedicatedHardwareSpec
        
            @staticmethod
            def autoScaling() -> typing.Type['AutoScalingV15']:
                return AutoScalingV15
        
            @staticmethod
            def readOnlySpecs() -> typing.Type['DedicatedHardwareSpec']:
                return DedicatedHardwareSpec
        
            @staticmethod
            def electableSpecs() -> typing.Type['HardwareSpec']:
                return HardwareSpec
            
            
            class priority(
                schemas.Int32Schema
            ):
                pass
            
            
            class providerName(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def AWS(cls):
                    return cls("AWS")
                
                @schemas.classproperty
                def AZURE(cls):
                    return cls("AZURE")
                
                @schemas.classproperty
                def GCP(cls):
                    return cls("GCP")
                
                @schemas.classproperty
                def TENANT(cls):
                    return cls("TENANT")
            
            
            class regionName(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def US_GOV_WEST_1(cls):
                    return cls("US_GOV_WEST_1")
                
                @schemas.classproperty
                def US_GOV_EAST_1(cls):
                    return cls("US_GOV_EAST_1")
                
                @schemas.classproperty
                def US_EAST_1(cls):
                    return cls("US_EAST_1")
                
                @schemas.classproperty
                def US_EAST_2(cls):
                    return cls("US_EAST_2")
                
                @schemas.classproperty
                def US_WEST_1(cls):
                    return cls("US_WEST_1")
                
                @schemas.classproperty
                def US_WEST_2(cls):
                    return cls("US_WEST_2")
                
                @schemas.classproperty
                def CA_CENTRAL_1(cls):
                    return cls("CA_CENTRAL_1")
                
                @schemas.classproperty
                def EU_NORTH_1(cls):
                    return cls("EU_NORTH_1")
                
                @schemas.classproperty
                def EU_WEST_1(cls):
                    return cls("EU_WEST_1")
                
                @schemas.classproperty
                def EU_WEST_2(cls):
                    return cls("EU_WEST_2")
                
                @schemas.classproperty
                def EU_WEST_3(cls):
                    return cls("EU_WEST_3")
                
                @schemas.classproperty
                def EU_CENTRAL_1(cls):
                    return cls("EU_CENTRAL_1")
                
                @schemas.classproperty
                def AP_EAST_1(cls):
                    return cls("AP_EAST_1")
                
                @schemas.classproperty
                def AP_NORTHEAST_1(cls):
                    return cls("AP_NORTHEAST_1")
                
                @schemas.classproperty
                def AP_NORTHEAST_2(cls):
                    return cls("AP_NORTHEAST_2")
                
                @schemas.classproperty
                def AP_NORTHEAST_3(cls):
                    return cls("AP_NORTHEAST_3")
                
                @schemas.classproperty
                def AP_SOUTHEAST_1(cls):
                    return cls("AP_SOUTHEAST_1")
                
                @schemas.classproperty
                def AP_SOUTHEAST_2(cls):
                    return cls("AP_SOUTHEAST_2")
                
                @schemas.classproperty
                def AP_SOUTHEAST_3(cls):
                    return cls("AP_SOUTHEAST_3")
                
                @schemas.classproperty
                def AP_SOUTH_1(cls):
                    return cls("AP_SOUTH_1")
                
                @schemas.classproperty
                def SA_EAST_1(cls):
                    return cls("SA_EAST_1")
                
                @schemas.classproperty
                def CN_NORTH_1(cls):
                    return cls("CN_NORTH_1")
                
                @schemas.classproperty
                def CN_NORTHWEST_1(cls):
                    return cls("CN_NORTHWEST_1")
                
                @schemas.classproperty
                def ME_SOUTH_1(cls):
                    return cls("ME_SOUTH_1")
                
                @schemas.classproperty
                def AF_SOUTH_1(cls):
                    return cls("AF_SOUTH_1")
                
                @schemas.classproperty
                def EU_SOUTH_1(cls):
                    return cls("EU_SOUTH_1")
                
                @schemas.classproperty
                def GLOBAL(cls):
                    return cls("GLOBAL")
                
                @schemas.classproperty
                def US_CENTRAL(cls):
                    return cls("US_CENTRAL")
                
                @schemas.classproperty
                def US_EAST(cls):
                    return cls("US_EAST")
                
                @schemas.classproperty
                def US_NORTH_CENTRAL(cls):
                    return cls("US_NORTH_CENTRAL")
                
                @schemas.classproperty
                def US_WEST(cls):
                    return cls("US_WEST")
                
                @schemas.classproperty
                def US_SOUTH_CENTRAL(cls):
                    return cls("US_SOUTH_CENTRAL")
                
                @schemas.classproperty
                def EUROPE_NORTH(cls):
                    return cls("EUROPE_NORTH")
                
                @schemas.classproperty
                def EUROPE_WEST(cls):
                    return cls("EUROPE_WEST")
                
                @schemas.classproperty
                def US_WEST_CENTRAL(cls):
                    return cls("US_WEST_CENTRAL")
                
                @schemas.classproperty
                def US_WEST_3(cls):
                    return cls("US_WEST_3")
                
                @schemas.classproperty
                def CANADA_EAST(cls):
                    return cls("CANADA_EAST")
                
                @schemas.classproperty
                def CANADA_CENTRAL(cls):
                    return cls("CANADA_CENTRAL")
                
                @schemas.classproperty
                def BRAZIL_SOUTH(cls):
                    return cls("BRAZIL_SOUTH")
                
                @schemas.classproperty
                def BRAZIL_SOUTHEAST(cls):
                    return cls("BRAZIL_SOUTHEAST")
                
                @schemas.classproperty
                def AUSTRALIA_CENTRAL(cls):
                    return cls("AUSTRALIA_CENTRAL")
                
                @schemas.classproperty
                def AUSTRALIA_CENTRAL_2(cls):
                    return cls("AUSTRALIA_CENTRAL_2")
                
                @schemas.classproperty
                def AUSTRALIA_EAST(cls):
                    return cls("AUSTRALIA_EAST")
                
                @schemas.classproperty
                def AUSTRALIA_SOUTH_EAST(cls):
                    return cls("AUSTRALIA_SOUTH_EAST")
                
                @schemas.classproperty
                def GERMANY_CENTRAL(cls):
                    return cls("GERMANY_CENTRAL")
                
                @schemas.classproperty
                def GERMANY_NORTH_EAST(cls):
                    return cls("GERMANY_NORTH_EAST")
                
                @schemas.classproperty
                def GERMANY_WEST_CENTRAL(cls):
                    return cls("GERMANY_WEST_CENTRAL")
                
                @schemas.classproperty
                def GERMANY_NORTH(cls):
                    return cls("GERMANY_NORTH")
                
                @schemas.classproperty
                def SWEDEN_CENTRAL(cls):
                    return cls("SWEDEN_CENTRAL")
                
                @schemas.classproperty
                def SWEDEN_SOUTH(cls):
                    return cls("SWEDEN_SOUTH")
                
                @schemas.classproperty
                def SWITZERLAND_NORTH(cls):
                    return cls("SWITZERLAND_NORTH")
                
                @schemas.classproperty
                def SWITZERLAND_WEST(cls):
                    return cls("SWITZERLAND_WEST")
                
                @schemas.classproperty
                def UK_SOUTH(cls):
                    return cls("UK_SOUTH")
                
                @schemas.classproperty
                def UK_WEST(cls):
                    return cls("UK_WEST")
                
                @schemas.classproperty
                def NORWAY_EAST(cls):
                    return cls("NORWAY_EAST")
                
                @schemas.classproperty
                def NORWAY_WEST(cls):
                    return cls("NORWAY_WEST")
                
                @schemas.classproperty
                def INDIA_CENTRAL(cls):
                    return cls("INDIA_CENTRAL")
                
                @schemas.classproperty
                def INDIA_SOUTH(cls):
                    return cls("INDIA_SOUTH")
                
                @schemas.classproperty
                def INDIA_WEST(cls):
                    return cls("INDIA_WEST")
                
                @schemas.classproperty
                def CHINA_EAST(cls):
                    return cls("CHINA_EAST")
                
                @schemas.classproperty
                def CHINA_NORTH(cls):
                    return cls("CHINA_NORTH")
                
                @schemas.classproperty
                def ASIA_EAST(cls):
                    return cls("ASIA_EAST")
                
                @schemas.classproperty
                def JAPAN_EAST(cls):
                    return cls("JAPAN_EAST")
                
                @schemas.classproperty
                def JAPAN_WEST(cls):
                    return cls("JAPAN_WEST")
                
                @schemas.classproperty
                def ASIA_SOUTH_EAST(cls):
                    return cls("ASIA_SOUTH_EAST")
                
                @schemas.classproperty
                def KOREA_CENTRAL(cls):
                    return cls("KOREA_CENTRAL")
                
                @schemas.classproperty
                def KOREA_SOUTH(cls):
                    return cls("KOREA_SOUTH")
                
                @schemas.classproperty
                def FRANCE_CENTRAL(cls):
                    return cls("FRANCE_CENTRAL")
                
                @schemas.classproperty
                def FRANCE_SOUTH(cls):
                    return cls("FRANCE_SOUTH")
                
                @schemas.classproperty
                def SOUTH_AFRICA_NORTH(cls):
                    return cls("SOUTH_AFRICA_NORTH")
                
                @schemas.classproperty
                def SOUTH_AFRICA_WEST(cls):
                    return cls("SOUTH_AFRICA_WEST")
                
                @schemas.classproperty
                def UAE_CENTRAL(cls):
                    return cls("UAE_CENTRAL")
                
                @schemas.classproperty
                def UAE_NORTH(cls):
                    return cls("UAE_NORTH")
                
                @schemas.classproperty
                def EASTERN_US(cls):
                    return cls("EASTERN_US")
                
                @schemas.classproperty
                def US_EAST_4(cls):
                    return cls("US_EAST_4")
                
                @schemas.classproperty
                def US_WEST_4(cls):
                    return cls("US_WEST_4")
                
                @schemas.classproperty
                def CENTRAL_US(cls):
                    return cls("CENTRAL_US")
                
                @schemas.classproperty
                def WESTERN_US(cls):
                    return cls("WESTERN_US")
                
                @schemas.classproperty
                def NORTH_AMERICA_NORTHEAST_1(cls):
                    return cls("NORTH_AMERICA_NORTHEAST_1")
                
                @schemas.classproperty
                def NORTH_AMERICA_NORTHEAST_2(cls):
                    return cls("NORTH_AMERICA_NORTHEAST_2")
                
                @schemas.classproperty
                def SOUTH_AMERICA_EAST_1(cls):
                    return cls("SOUTH_AMERICA_EAST_1")
                
                @schemas.classproperty
                def SOUTH_AMERICA_WEST_1(cls):
                    return cls("SOUTH_AMERICA_WEST_1")
                
                @schemas.classproperty
                def WESTERN_EUROPE(cls):
                    return cls("WESTERN_EUROPE")
                
                @schemas.classproperty
                def EUROPE_NORTH_1(cls):
                    return cls("EUROPE_NORTH_1")
                
                @schemas.classproperty
                def EUROPE_WEST_2(cls):
                    return cls("EUROPE_WEST_2")
                
                @schemas.classproperty
                def EUROPE_WEST_3(cls):
                    return cls("EUROPE_WEST_3")
                
                @schemas.classproperty
                def EUROPE_WEST_4(cls):
                    return cls("EUROPE_WEST_4")
                
                @schemas.classproperty
                def EUROPE_WEST_6(cls):
                    return cls("EUROPE_WEST_6")
                
                @schemas.classproperty
                def EUROPE_WEST_8(cls):
                    return cls("EUROPE_WEST_8")
                
                @schemas.classproperty
                def EUROPE_WEST_9(cls):
                    return cls("EUROPE_WEST_9")
                
                @schemas.classproperty
                def EUROPE_SOUTHWEST_1(cls):
                    return cls("EUROPE_SOUTHWEST_1")
                
                @schemas.classproperty
                def EUROPE_CENTRAL_2(cls):
                    return cls("EUROPE_CENTRAL_2")
                
                @schemas.classproperty
                def AUSTRALIA_SOUTHEAST_1(cls):
                    return cls("AUSTRALIA_SOUTHEAST_1")
                
                @schemas.classproperty
                def AUSTRALIA_SOUTHEAST_2(cls):
                    return cls("AUSTRALIA_SOUTHEAST_2")
                
                @schemas.classproperty
                def EASTERN_ASIA_PACIFIC(cls):
                    return cls("EASTERN_ASIA_PACIFIC")
                
                @schemas.classproperty
                def NORTHEASTERN_ASIA_PACIFIC(cls):
                    return cls("NORTHEASTERN_ASIA_PACIFIC")
                
                @schemas.classproperty
                def SOUTHEASTERN_ASIA_PACIFIC(cls):
                    return cls("SOUTHEASTERN_ASIA_PACIFIC")
                
                @schemas.classproperty
                def ASIA_EAST_2(cls):
                    return cls("ASIA_EAST_2")
                
                @schemas.classproperty
                def ASIA_NORTHEAST_2(cls):
                    return cls("ASIA_NORTHEAST_2")
                
                @schemas.classproperty
                def ASIA_NORTHEAST_3(cls):
                    return cls("ASIA_NORTHEAST_3")
                
                @schemas.classproperty
                def ASIA_SOUTH_1(cls):
                    return cls("ASIA_SOUTH_1")
                
                @schemas.classproperty
                def ASIA_SOUTH_2(cls):
                    return cls("ASIA_SOUTH_2")
                
                @schemas.classproperty
                def ASIA_SOUTHEAST_2(cls):
                    return cls("ASIA_SOUTHEAST_2")
            __annotations__ = {
                "analyticsAutoScaling": analyticsAutoScaling,
                "analyticsSpecs": analyticsSpecs,
                "autoScaling": autoScaling,
                "readOnlySpecs": readOnlySpecs,
                "electableSpecs": electableSpecs,
                "priority": priority,
                "providerName": providerName,
                "regionName": regionName,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["analyticsAutoScaling"]) -> 'AutoScalingV15': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["analyticsSpecs"]) -> 'DedicatedHardwareSpec': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["autoScaling"]) -> 'AutoScalingV15': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["readOnlySpecs"]) -> 'DedicatedHardwareSpec': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["electableSpecs"]) -> 'HardwareSpec': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["priority"]) -> MetaOapg.properties.priority: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerName"]) -> MetaOapg.properties.providerName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["regionName"]) -> MetaOapg.properties.regionName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["analyticsAutoScaling", "analyticsSpecs", "autoScaling", "readOnlySpecs", "electableSpecs", "priority", "providerName", "regionName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["analyticsAutoScaling"]) -> typing.Union['AutoScalingV15', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["analyticsSpecs"]) -> typing.Union['DedicatedHardwareSpec', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["autoScaling"]) -> typing.Union['AutoScalingV15', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["readOnlySpecs"]) -> typing.Union['DedicatedHardwareSpec', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["electableSpecs"]) -> typing.Union['HardwareSpec', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["priority"]) -> typing.Union[MetaOapg.properties.priority, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerName"]) -> typing.Union[MetaOapg.properties.providerName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["regionName"]) -> typing.Union[MetaOapg.properties.regionName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["analyticsAutoScaling", "analyticsSpecs", "autoScaling", "readOnlySpecs", "electableSpecs", "priority", "providerName", "regionName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        analyticsAutoScaling: typing.Union['AutoScalingV15', schemas.Unset] = schemas.unset,
        analyticsSpecs: typing.Union['DedicatedHardwareSpec', schemas.Unset] = schemas.unset,
        autoScaling: typing.Union['AutoScalingV15', schemas.Unset] = schemas.unset,
        readOnlySpecs: typing.Union['DedicatedHardwareSpec', schemas.Unset] = schemas.unset,
        electableSpecs: typing.Union['HardwareSpec', schemas.Unset] = schemas.unset,
        priority: typing.Union[MetaOapg.properties.priority, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        providerName: typing.Union[MetaOapg.properties.providerName, str, schemas.Unset] = schemas.unset,
        regionName: typing.Union[MetaOapg.properties.regionName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AzureRegionConfig':
        return super().__new__(
            cls,
            *_args,
            analyticsAutoScaling=analyticsAutoScaling,
            analyticsSpecs=analyticsSpecs,
            autoScaling=autoScaling,
            readOnlySpecs=readOnlySpecs,
            electableSpecs=electableSpecs,
            priority=priority,
            providerName=providerName,
            regionName=regionName,
            _configuration=_configuration,
            **kwargs,
        )

from atlas.model.auto_scaling_v15 import AutoScalingV15
from atlas.model.dedicated_hardware_spec import DedicatedHardwareSpec
from atlas.model.hardware_spec import HardwareSpec
