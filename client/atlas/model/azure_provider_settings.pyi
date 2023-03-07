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


class AzureProviderSettings(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "providerName",
        }
        
        class properties:
            providerName = schemas.StrSchema
        
            @staticmethod
            def autoScaling() -> typing.Type['AzureAutoScaling']:
                return AzureAutoScaling
            
            
            class diskTypeName(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def P2(cls):
                    return cls("P2")
                
                @schemas.classproperty
                def P3(cls):
                    return cls("P3")
                
                @schemas.classproperty
                def P4(cls):
                    return cls("P4")
                
                @schemas.classproperty
                def P6(cls):
                    return cls("P6")
                
                @schemas.classproperty
                def P10(cls):
                    return cls("P10")
                
                @schemas.classproperty
                def P15(cls):
                    return cls("P15")
                
                @schemas.classproperty
                def P20(cls):
                    return cls("P20")
                
                @schemas.classproperty
                def P30(cls):
                    return cls("P30")
                
                @schemas.classproperty
                def P40(cls):
                    return cls("P40")
                
                @schemas.classproperty
                def P50(cls):
                    return cls("P50")
            
            
            class instanceSizeName(
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
            
            
            class regionName(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def US_CENTRAL(cls):
                    return cls("US_CENTRAL")
                
                @schemas.classproperty
                def US_EAST(cls):
                    return cls("US_EAST")
                
                @schemas.classproperty
                def US_EAST_2(cls):
                    return cls("US_EAST_2")
                
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
                def US_WEST_2(cls):
                    return cls("US_WEST_2")
                
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
            __annotations__ = {
                "providerName": providerName,
                "autoScaling": autoScaling,
                "diskTypeName": diskTypeName,
                "instanceSizeName": instanceSizeName,
                "regionName": regionName,
            }
    
    providerName: MetaOapg.properties.providerName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerName"]) -> MetaOapg.properties.providerName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["autoScaling"]) -> 'AzureAutoScaling': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["diskTypeName"]) -> MetaOapg.properties.diskTypeName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["instanceSizeName"]) -> MetaOapg.properties.instanceSizeName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["regionName"]) -> MetaOapg.properties.regionName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["providerName", "autoScaling", "diskTypeName", "instanceSizeName", "regionName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerName"]) -> MetaOapg.properties.providerName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["autoScaling"]) -> typing.Union['AzureAutoScaling', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["diskTypeName"]) -> typing.Union[MetaOapg.properties.diskTypeName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["instanceSizeName"]) -> typing.Union[MetaOapg.properties.instanceSizeName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["regionName"]) -> typing.Union[MetaOapg.properties.regionName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["providerName", "autoScaling", "diskTypeName", "instanceSizeName", "regionName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        providerName: typing.Union[MetaOapg.properties.providerName, str, ],
        autoScaling: typing.Union['AzureAutoScaling', schemas.Unset] = schemas.unset,
        diskTypeName: typing.Union[MetaOapg.properties.diskTypeName, str, schemas.Unset] = schemas.unset,
        instanceSizeName: typing.Union[MetaOapg.properties.instanceSizeName, str, schemas.Unset] = schemas.unset,
        regionName: typing.Union[MetaOapg.properties.regionName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AzureProviderSettings':
        return super().__new__(
            cls,
            *_args,
            providerName=providerName,
            autoScaling=autoScaling,
            diskTypeName=diskTypeName,
            instanceSizeName=instanceSizeName,
            regionName=regionName,
            _configuration=_configuration,
            **kwargs,
        )

from atlas.model.azure_auto_scaling import AzureAutoScaling
