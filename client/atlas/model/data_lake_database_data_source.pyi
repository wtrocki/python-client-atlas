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


class DataLakeDatabaseDataSource(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Data store that maps to a collection for this data lake.
    """


    class MetaOapg:
        
        class properties:
            allowInsecure = schemas.BoolSchema
            collection = schemas.StrSchema
            collectionRegex = schemas.StrSchema
            database = schemas.StrSchema
            databaseRegex = schemas.StrSchema
            
            
            class defaultFormat(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def AVRO(cls):
                    return cls(".avro")
                
                @schemas.classproperty
                def AVRO_BZ2(cls):
                    return cls(".avro.bz2")
                
                @schemas.classproperty
                def AVRO_GZ(cls):
                    return cls(".avro.gz")
                
                @schemas.classproperty
                def BSON(cls):
                    return cls(".bson")
                
                @schemas.classproperty
                def BSON_BZ2(cls):
                    return cls(".bson.bz2")
                
                @schemas.classproperty
                def BSON_GZ(cls):
                    return cls(".bson.gz")
                
                @schemas.classproperty
                def BSONX(cls):
                    return cls(".bsonx")
                
                @schemas.classproperty
                def CSV(cls):
                    return cls(".csv")
                
                @schemas.classproperty
                def CSV_BZ2(cls):
                    return cls(".csv.bz2")
                
                @schemas.classproperty
                def CSV_GZ(cls):
                    return cls(".csv.gz")
                
                @schemas.classproperty
                def JSON(cls):
                    return cls(".json")
                
                @schemas.classproperty
                def JSON_BZ2(cls):
                    return cls(".json.bz2")
                
                @schemas.classproperty
                def JSON_GZ(cls):
                    return cls(".json.gz")
                
                @schemas.classproperty
                def ORC(cls):
                    return cls(".orc")
                
                @schemas.classproperty
                def PARQUET(cls):
                    return cls(".parquet")
                
                @schemas.classproperty
                def TSV(cls):
                    return cls(".tsv")
                
                @schemas.classproperty
                def TSV_BZ2(cls):
                    return cls(".tsv.bz2")
                
                @schemas.classproperty
                def TSV_GZ(cls):
                    return cls(".tsv.gz")
            path = schemas.StrSchema
            provenanceFieldName = schemas.StrSchema
            storeName = schemas.StrSchema
            
            
            class urls(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'urls':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "allowInsecure": allowInsecure,
                "collection": collection,
                "collectionRegex": collectionRegex,
                "database": database,
                "databaseRegex": databaseRegex,
                "defaultFormat": defaultFormat,
                "path": path,
                "provenanceFieldName": provenanceFieldName,
                "storeName": storeName,
                "urls": urls,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["allowInsecure"]) -> MetaOapg.properties.allowInsecure: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collection"]) -> MetaOapg.properties.collection: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collectionRegex"]) -> MetaOapg.properties.collectionRegex: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["database"]) -> MetaOapg.properties.database: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["databaseRegex"]) -> MetaOapg.properties.databaseRegex: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultFormat"]) -> MetaOapg.properties.defaultFormat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["path"]) -> MetaOapg.properties.path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["provenanceFieldName"]) -> MetaOapg.properties.provenanceFieldName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["storeName"]) -> MetaOapg.properties.storeName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["urls"]) -> MetaOapg.properties.urls: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["allowInsecure", "collection", "collectionRegex", "database", "databaseRegex", "defaultFormat", "path", "provenanceFieldName", "storeName", "urls", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["allowInsecure"]) -> typing.Union[MetaOapg.properties.allowInsecure, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collection"]) -> typing.Union[MetaOapg.properties.collection, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collectionRegex"]) -> typing.Union[MetaOapg.properties.collectionRegex, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["database"]) -> typing.Union[MetaOapg.properties.database, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["databaseRegex"]) -> typing.Union[MetaOapg.properties.databaseRegex, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultFormat"]) -> typing.Union[MetaOapg.properties.defaultFormat, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["path"]) -> typing.Union[MetaOapg.properties.path, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["provenanceFieldName"]) -> typing.Union[MetaOapg.properties.provenanceFieldName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["storeName"]) -> typing.Union[MetaOapg.properties.storeName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["urls"]) -> typing.Union[MetaOapg.properties.urls, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["allowInsecure", "collection", "collectionRegex", "database", "databaseRegex", "defaultFormat", "path", "provenanceFieldName", "storeName", "urls", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        allowInsecure: typing.Union[MetaOapg.properties.allowInsecure, bool, schemas.Unset] = schemas.unset,
        collection: typing.Union[MetaOapg.properties.collection, str, schemas.Unset] = schemas.unset,
        collectionRegex: typing.Union[MetaOapg.properties.collectionRegex, str, schemas.Unset] = schemas.unset,
        database: typing.Union[MetaOapg.properties.database, str, schemas.Unset] = schemas.unset,
        databaseRegex: typing.Union[MetaOapg.properties.databaseRegex, str, schemas.Unset] = schemas.unset,
        defaultFormat: typing.Union[MetaOapg.properties.defaultFormat, str, schemas.Unset] = schemas.unset,
        path: typing.Union[MetaOapg.properties.path, str, schemas.Unset] = schemas.unset,
        provenanceFieldName: typing.Union[MetaOapg.properties.provenanceFieldName, str, schemas.Unset] = schemas.unset,
        storeName: typing.Union[MetaOapg.properties.storeName, str, schemas.Unset] = schemas.unset,
        urls: typing.Union[MetaOapg.properties.urls, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'DataLakeDatabaseDataSource':
        return super().__new__(
            cls,
            *_args,
            allowInsecure=allowInsecure,
            collection=collection,
            collectionRegex=collectionRegex,
            database=database,
            databaseRegex=databaseRegex,
            defaultFormat=defaultFormat,
            path=path,
            provenanceFieldName=provenanceFieldName,
            storeName=storeName,
            urls=urls,
            _configuration=_configuration,
            **kwargs,
        )
