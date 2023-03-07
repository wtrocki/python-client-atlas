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


class GCPCloudProviderContainer(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Collection of settings that configures the network container for a virtual private connection on Amazon Web Services.
    """


    class MetaOapg:
        required = {
            "atlasCidrBlock",
        }
        
        class properties:
            
            
            class atlasCidrBlock(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    regex=[{
                        'pattern': r'^((([0-9]{1,3}\.){3}[0-9]{1,3})|([\:]{0,2}([0-9a-f]{1,4}\:){0,7}[0-9a-f]{1,4}[\:]{0,2}))((%2[fF]|\/)[0-9]{1,3})+$',  # noqa: E501
                    }]
            
            
            class gcpProjectId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 26
                    min_length = 26
                    regex=[{
                        'pattern': r'^p-[0-9a-z]{24}$',  # noqa: E501
                    }]
            
            
            class networkName(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 36
                    min_length = 36
                    regex=[{
                        'pattern': r'^nt-[0-9a-f]{24}-[0-9a-z]{8}$',  # noqa: E501
                    }]
            
            
            class regions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                    
                    
                        class MetaOapg:
                            enum_value_to_name = {
                                "ASIA_EAST_2": "ASIA_EAST_2",
                                "ASIA_NORTHEAST_2": "ASIA_NORTHEAST_2",
                                "ASIA_NORTHEAST_3": "ASIA_NORTHEAST_3",
                                "ASIA_SOUTH_1": "ASIA_SOUTH_1",
                                "ASIA_SOUTH_2": "ASIA_SOUTH_2",
                                "ASIA_SOUTHEAST_2": "ASIA_SOUTHEAST_2",
                                "AUSTRALIA_SOUTHEAST_1": "AUSTRALIA_SOUTHEAST_1",
                                "AUSTRALIA_SOUTHEAST_2": "AUSTRALIA_SOUTHEAST_2",
                                "CENTRAL_US": "CENTRAL_US",
                                "EASTERN_ASIA_PACIFIC": "EASTERN_ASIA_PACIFIC",
                                "EASTERN_US": "EASTERN_US",
                                "EUROPE_CENTRAL_2": "EUROPE_CENTRAL_2",
                                "EUROPE_NORTH_1": "EUROPE_NORTH_1",
                                "EUROPE_WEST_2": "EUROPE_WEST_2",
                                "EUROPE_WEST_3": "EUROPE_WEST_3",
                                "EUROPE_WEST_4": "EUROPE_WEST_4",
                                "EUROPE_WEST_6": "EUROPE_WEST_6",
                                "NORTH_AMERICA_NORTHEAST_1": "NORTH_AMERICA_NORTHEAST_1",
                                "NORTH_AMERICA_NORTHEAST_2": "NORTH_AMERICA_NORTHEAST_2",
                                "NORTHEASTERN_ASIA_PACIFIC": "NORTHEASTERN_ASIA_PACIFIC",
                                "SOUTH_AMERICA_EAST_1": "SOUTH_AMERICA_EAST_1",
                                "SOUTH_AMERICA_WEST_1": "SOUTH_AMERICA_WEST_1",
                                "SOUTHEASTERN_ASIA_PACIFIC": "SOUTHEASTERN_ASIA_PACIFIC",
                                "US_EAST_4": "US_EAST_4",
                                "US_WEST_2": "US_WEST_2",
                                "US_WEST_3": "US_WEST_3",
                                "US_WEST_4": "US_WEST_4",
                                "WESTERN_EUROPE": "WESTERN_EUROPE",
                                "WESTERN_US": "WESTERN_US",
                            }
                        
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
                        
                        @schemas.classproperty
                        def AUSTRALIA_SOUTHEAST_1(cls):
                            return cls("AUSTRALIA_SOUTHEAST_1")
                        
                        @schemas.classproperty
                        def AUSTRALIA_SOUTHEAST_2(cls):
                            return cls("AUSTRALIA_SOUTHEAST_2")
                        
                        @schemas.classproperty
                        def CENTRAL_US(cls):
                            return cls("CENTRAL_US")
                        
                        @schemas.classproperty
                        def EASTERN_ASIA_PACIFIC(cls):
                            return cls("EASTERN_ASIA_PACIFIC")
                        
                        @schemas.classproperty
                        def EASTERN_US(cls):
                            return cls("EASTERN_US")
                        
                        @schemas.classproperty
                        def EUROPE_CENTRAL_2(cls):
                            return cls("EUROPE_CENTRAL_2")
                        
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
                        def NORTH_AMERICA_NORTHEAST_1(cls):
                            return cls("NORTH_AMERICA_NORTHEAST_1")
                        
                        @schemas.classproperty
                        def NORTH_AMERICA_NORTHEAST_2(cls):
                            return cls("NORTH_AMERICA_NORTHEAST_2")
                        
                        @schemas.classproperty
                        def NORTHEASTERN_ASIA_PACIFIC(cls):
                            return cls("NORTHEASTERN_ASIA_PACIFIC")
                        
                        @schemas.classproperty
                        def SOUTH_AMERICA_EAST_1(cls):
                            return cls("SOUTH_AMERICA_EAST_1")
                        
                        @schemas.classproperty
                        def SOUTH_AMERICA_WEST_1(cls):
                            return cls("SOUTH_AMERICA_WEST_1")
                        
                        @schemas.classproperty
                        def SOUTHEASTERN_ASIA_PACIFIC(cls):
                            return cls("SOUTHEASTERN_ASIA_PACIFIC")
                        
                        @schemas.classproperty
                        def US_EAST_4(cls):
                            return cls("US_EAST_4")
                        
                        @schemas.classproperty
                        def US_WEST_2(cls):
                            return cls("US_WEST_2")
                        
                        @schemas.classproperty
                        def US_WEST_3(cls):
                            return cls("US_WEST_3")
                        
                        @schemas.classproperty
                        def US_WEST_4(cls):
                            return cls("US_WEST_4")
                        
                        @schemas.classproperty
                        def WESTERN_EUROPE(cls):
                            return cls("WESTERN_EUROPE")
                        
                        @schemas.classproperty
                        def WESTERN_US(cls):
                            return cls("WESTERN_US")
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'regions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class id(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 24
                    min_length = 24
                    regex=[{
                        'pattern': r'^([a-f0-9]{24})$',  # noqa: E501
                    }]
            
            
            class providerName(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "AWS": "AWS",
                        "GCP": "GCP",
                        "AZURE": "AZURE",
                        "TENANT": "TENANT",
                        "SERVERLESS": "SERVERLESS",
                    }
                
                @schemas.classproperty
                def AWS(cls):
                    return cls("AWS")
                
                @schemas.classproperty
                def GCP(cls):
                    return cls("GCP")
                
                @schemas.classproperty
                def AZURE(cls):
                    return cls("AZURE")
                
                @schemas.classproperty
                def TENANT(cls):
                    return cls("TENANT")
                
                @schemas.classproperty
                def SERVERLESS(cls):
                    return cls("SERVERLESS")
            provisioned = schemas.BoolSchema
            __annotations__ = {
                "atlasCidrBlock": atlasCidrBlock,
                "gcpProjectId": gcpProjectId,
                "networkName": networkName,
                "regions": regions,
                "id": id,
                "providerName": providerName,
                "provisioned": provisioned,
            }
    
    atlasCidrBlock: MetaOapg.properties.atlasCidrBlock
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["atlasCidrBlock"]) -> MetaOapg.properties.atlasCidrBlock: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gcpProjectId"]) -> MetaOapg.properties.gcpProjectId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["networkName"]) -> MetaOapg.properties.networkName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["regions"]) -> MetaOapg.properties.regions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["providerName"]) -> MetaOapg.properties.providerName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provisioned"]) -> MetaOapg.properties.provisioned: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["atlasCidrBlock", "gcpProjectId", "networkName", "regions", "id", "providerName", "provisioned", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["atlasCidrBlock"]) -> MetaOapg.properties.atlasCidrBlock: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gcpProjectId"]) -> typing.Union[MetaOapg.properties.gcpProjectId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["networkName"]) -> typing.Union[MetaOapg.properties.networkName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["regions"]) -> typing.Union[MetaOapg.properties.regions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["providerName"]) -> typing.Union[MetaOapg.properties.providerName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provisioned"]) -> typing.Union[MetaOapg.properties.provisioned, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["atlasCidrBlock", "gcpProjectId", "networkName", "regions", "id", "providerName", "provisioned", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        atlasCidrBlock: typing.Union[MetaOapg.properties.atlasCidrBlock, str, ],
        gcpProjectId: typing.Union[MetaOapg.properties.gcpProjectId, str, schemas.Unset] = schemas.unset,
        networkName: typing.Union[MetaOapg.properties.networkName, str, schemas.Unset] = schemas.unset,
        regions: typing.Union[MetaOapg.properties.regions, list, tuple, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        providerName: typing.Union[MetaOapg.properties.providerName, str, schemas.Unset] = schemas.unset,
        provisioned: typing.Union[MetaOapg.properties.provisioned, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GCPCloudProviderContainer':
        return super().__new__(
            cls,
            *_args,
            atlasCidrBlock=atlasCidrBlock,
            gcpProjectId=gcpProjectId,
            networkName=networkName,
            regions=regions,
            id=id,
            providerName=providerName,
            provisioned=provisioned,
            _configuration=_configuration,
            **kwargs,
        )