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


class ApiIndexRequestView(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "collection",
            "db",
        }
        
        class properties:
            collection = schemas.StrSchema
            db = schemas.StrSchema
        
            @staticmethod
            def collation() -> typing.Type['Collation']:
                return Collation
            
            
            class keys(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    
                    class items(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            
                            class additional_properties(
                                schemas.StrSchema
                            ):
                            
                            
                                class MetaOapg:
                            max_properties = 1
                            min_properties = 1
                        
                        def __getitem__(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        def get_item_oapg(self, name: typing.Union[str, ]) -> MetaOapg.additional_properties:
                            return super().get_item_oapg(name)
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[MetaOapg.additional_properties, str, ],
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                *_args,
                                _configuration=_configuration,
                                **kwargs,
                            )
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'keys':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
        
            @staticmethod
            def options() -> typing.Type['IndexOptions']:
                return IndexOptions
            __annotations__ = {
                "collection": collection,
                "db": db,
                "collation": collation,
                "keys": keys,
                "options": options,
            }
    
    collection: MetaOapg.properties.collection
    db: MetaOapg.properties.db
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collection"]) -> MetaOapg.properties.collection: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["db"]) -> MetaOapg.properties.db: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collation"]) -> 'Collation': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["keys"]) -> MetaOapg.properties.keys: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["options"]) -> 'IndexOptions': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["collection", "db", "collation", "keys", "options", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collection"]) -> MetaOapg.properties.collection: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["db"]) -> MetaOapg.properties.db: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collation"]) -> typing.Union['Collation', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["keys"]) -> typing.Union[MetaOapg.properties.keys, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["options"]) -> typing.Union['IndexOptions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["collection", "db", "collation", "keys", "options", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        collection: typing.Union[MetaOapg.properties.collection, str, ],
        db: typing.Union[MetaOapg.properties.db, str, ],
        collation: typing.Union['Collation', schemas.Unset] = schemas.unset,
        keys: typing.Union[MetaOapg.properties.keys, list, tuple, schemas.Unset] = schemas.unset,
        options: typing.Union['IndexOptions', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ApiIndexRequestView':
        return super().__new__(
            cls,
            *_args,
            collection=collection,
            db=db,
            collation=collation,
            keys=keys,
            options=options,
            _configuration=_configuration,
            **kwargs,
        )

from atlas.model.collation import Collation
from atlas.model.index_options import IndexOptions
