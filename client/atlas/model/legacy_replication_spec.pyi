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


class LegacyReplicationSpec(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class id(
                schemas.StrSchema
            ):
                pass
            numShards = schemas.Int32Schema
            
            
            class regionsConfig(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def additional_properties() -> typing.Type['RegionSpec']:
                        return RegionSpec
                
                def __getitem__(self, name: typing.Union[str, ]) -> 'RegionSpec':
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                def get_item_oapg(self, name: typing.Union[str, ]) -> 'RegionSpec':
                    return super().get_item_oapg(name)
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: 'RegionSpec',
                ) -> 'regionsConfig':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            zoneName = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "numShards": numShards,
                "regionsConfig": regionsConfig,
                "zoneName": zoneName,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numShards"]) -> MetaOapg.properties.numShards: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["regionsConfig"]) -> MetaOapg.properties.regionsConfig: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["zoneName"]) -> MetaOapg.properties.zoneName: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "numShards", "regionsConfig", "zoneName", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numShards"]) -> typing.Union[MetaOapg.properties.numShards, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["regionsConfig"]) -> typing.Union[MetaOapg.properties.regionsConfig, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["zoneName"]) -> typing.Union[MetaOapg.properties.zoneName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "numShards", "regionsConfig", "zoneName", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        numShards: typing.Union[MetaOapg.properties.numShards, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        regionsConfig: typing.Union[MetaOapg.properties.regionsConfig, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        zoneName: typing.Union[MetaOapg.properties.zoneName, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LegacyReplicationSpec':
        return super().__new__(
            cls,
            *_args,
            id=id,
            numShards=numShards,
            regionsConfig=regionsConfig,
            zoneName=zoneName,
            _configuration=_configuration,
            **kwargs,
        )

from atlas.model.region_spec import RegionSpec