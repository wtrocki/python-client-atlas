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


class ComputeAutoScaling(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Collection of settings that configures how a cluster might scale its cluster tier and whether the cluster can scale down. Cluster tier auto-scaling is unavailable for clusters using Low CPU or NVME storage classes.
    """


    class MetaOapg:
        
        class properties:
            enabled = schemas.BoolSchema
            scaleDownEnabled = schemas.BoolSchema
            __annotations__ = {
                "enabled": enabled,
                "scaleDownEnabled": scaleDownEnabled,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["enabled"]) -> MetaOapg.properties.enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scaleDownEnabled"]) -> MetaOapg.properties.scaleDownEnabled: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["enabled", "scaleDownEnabled", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["enabled"]) -> typing.Union[MetaOapg.properties.enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scaleDownEnabled"]) -> typing.Union[MetaOapg.properties.scaleDownEnabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["enabled", "scaleDownEnabled", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        enabled: typing.Union[MetaOapg.properties.enabled, bool, schemas.Unset] = schemas.unset,
        scaleDownEnabled: typing.Union[MetaOapg.properties.scaleDownEnabled, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ComputeAutoScaling':
        return super().__new__(
            cls,
            *_args,
            enabled=enabled,
            scaleDownEnabled=scaleDownEnabled,
            _configuration=_configuration,
            **kwargs,
        )
