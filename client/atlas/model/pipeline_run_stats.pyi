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


class PipelineRunStats(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Runtime statistics for this Data Lake Pipeline run.
    """


    class MetaOapg:
        
        class properties:
            bytesExported = schemas.Int64Schema
            numDocs = schemas.Int64Schema
            __annotations__ = {
                "bytesExported": bytesExported,
                "numDocs": numDocs,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bytesExported"]) -> MetaOapg.properties.bytesExported: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numDocs"]) -> MetaOapg.properties.numDocs: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["bytesExported", "numDocs", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bytesExported"]) -> typing.Union[MetaOapg.properties.bytesExported, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numDocs"]) -> typing.Union[MetaOapg.properties.numDocs, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["bytesExported", "numDocs", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        bytesExported: typing.Union[MetaOapg.properties.bytesExported, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        numDocs: typing.Union[MetaOapg.properties.numDocs, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PipelineRunStats':
        return super().__new__(
            cls,
            *_args,
            bytesExported=bytesExported,
            numDocs=numDocs,
            _configuration=_configuration,
            **kwargs,
        )