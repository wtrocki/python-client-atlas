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


class FTSIndex(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "database",
            "name",
            "collectionName",
        }
        
        class properties:
            collectionName = schemas.StrSchema
            database = schemas.StrSchema
            name = schemas.StrSchema
            
            
            class analyzer(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def STANDARD(cls):
                    return cls("lucene.standard")
                
                @schemas.classproperty
                def SIMPLE(cls):
                    return cls("lucene.simple")
                
                @schemas.classproperty
                def WHITESPACE(cls):
                    return cls("lucene.whitespace")
                
                @schemas.classproperty
                def KEYWORD(cls):
                    return cls("lucene.keyword")
                
                @schemas.classproperty
                def ARABIC(cls):
                    return cls("lucene.arabic")
                
                @schemas.classproperty
                def ARMENIAN(cls):
                    return cls("lucene.armenian")
                
                @schemas.classproperty
                def BASQUE(cls):
                    return cls("lucene.basque")
                
                @schemas.classproperty
                def BENGALI(cls):
                    return cls("lucene.bengali")
                
                @schemas.classproperty
                def BRAZILIAN(cls):
                    return cls("lucene.brazilian")
                
                @schemas.classproperty
                def BULGARIAN(cls):
                    return cls("lucene.bulgarian")
                
                @schemas.classproperty
                def CATALAN(cls):
                    return cls("lucene.catalan")
                
                @schemas.classproperty
                def CHINESE(cls):
                    return cls("lucene.chinese")
                
                @schemas.classproperty
                def CJK(cls):
                    return cls("lucene.cjk")
                
                @schemas.classproperty
                def CZECH(cls):
                    return cls("lucene.czech")
                
                @schemas.classproperty
                def DANISH(cls):
                    return cls("lucene.danish")
                
                @schemas.classproperty
                def DUTCH(cls):
                    return cls("lucene.dutch")
                
                @schemas.classproperty
                def ENGLISH(cls):
                    return cls("lucene.english")
                
                @schemas.classproperty
                def FINNISH(cls):
                    return cls("lucene.finnish")
                
                @schemas.classproperty
                def FRENCH(cls):
                    return cls("lucene.french")
                
                @schemas.classproperty
                def GALICIAN(cls):
                    return cls("lucene.galician")
                
                @schemas.classproperty
                def GERMAN(cls):
                    return cls("lucene.german")
                
                @schemas.classproperty
                def GREEK(cls):
                    return cls("lucene.greek")
                
                @schemas.classproperty
                def HINDI(cls):
                    return cls("lucene.hindi")
                
                @schemas.classproperty
                def HUNGARIAN(cls):
                    return cls("lucene.hungarian")
                
                @schemas.classproperty
                def INDONESIAN(cls):
                    return cls("lucene.indonesian")
                
                @schemas.classproperty
                def IRISH(cls):
                    return cls("lucene.irish")
                
                @schemas.classproperty
                def ITALIAN(cls):
                    return cls("lucene.italian")
                
                @schemas.classproperty
                def JAPANESE(cls):
                    return cls("lucene.japanese")
                
                @schemas.classproperty
                def KOREAN(cls):
                    return cls("lucene.korean")
                
                @schemas.classproperty
                def KUROMOJI(cls):
                    return cls("lucene.kuromoji")
                
                @schemas.classproperty
                def LATVIAN(cls):
                    return cls("lucene.latvian")
                
                @schemas.classproperty
                def LITHUANIAN(cls):
                    return cls("lucene.lithuanian")
                
                @schemas.classproperty
                def MORFOLOGIK(cls):
                    return cls("lucene.morfologik")
                
                @schemas.classproperty
                def NORI(cls):
                    return cls("lucene.nori")
                
                @schemas.classproperty
                def NORWEGIAN(cls):
                    return cls("lucene.norwegian")
                
                @schemas.classproperty
                def PERSIAN(cls):
                    return cls("lucene.persian")
                
                @schemas.classproperty
                def PORTUGUESE(cls):
                    return cls("lucene.portuguese")
                
                @schemas.classproperty
                def ROMANIAN(cls):
                    return cls("lucene.romanian")
                
                @schemas.classproperty
                def RUSSIAN(cls):
                    return cls("lucene.russian")
                
                @schemas.classproperty
                def SMARTCN(cls):
                    return cls("lucene.smartcn")
                
                @schemas.classproperty
                def SORANI(cls):
                    return cls("lucene.sorani")
                
                @schemas.classproperty
                def SPANISH(cls):
                    return cls("lucene.spanish")
                
                @schemas.classproperty
                def SWEDISH(cls):
                    return cls("lucene.swedish")
                
                @schemas.classproperty
                def THAI(cls):
                    return cls("lucene.thai")
                
                @schemas.classproperty
                def TURKISH(cls):
                    return cls("lucene.turkish")
                
                @schemas.classproperty
                def UKRAINIAN(cls):
                    return cls("lucene.ukrainian")
            
            
            class analyzers(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ApiAtlasFTSAnalyzersViewManual']:
                        return ApiAtlasFTSAnalyzersViewManual
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ApiAtlasFTSAnalyzersViewManual'], typing.List['ApiAtlasFTSAnalyzersViewManual']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'analyzers':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ApiAtlasFTSAnalyzersViewManual':
                    return super().__getitem__(i)
            
            
            class indexID(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def mappings() -> typing.Type['ApiAtlasFTSMappingsViewManual']:
                return ApiAtlasFTSMappingsViewManual
            
            
            class searchAnalyzer(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def STANDARD(cls):
                    return cls("lucene.standard")
                
                @schemas.classproperty
                def SIMPLE(cls):
                    return cls("lucene.simple")
                
                @schemas.classproperty
                def WHITESPACE(cls):
                    return cls("lucene.whitespace")
                
                @schemas.classproperty
                def KEYWORD(cls):
                    return cls("lucene.keyword")
                
                @schemas.classproperty
                def ARABIC(cls):
                    return cls("lucene.arabic")
                
                @schemas.classproperty
                def ARMENIAN(cls):
                    return cls("lucene.armenian")
                
                @schemas.classproperty
                def BASQUE(cls):
                    return cls("lucene.basque")
                
                @schemas.classproperty
                def BENGALI(cls):
                    return cls("lucene.bengali")
                
                @schemas.classproperty
                def BRAZILIAN(cls):
                    return cls("lucene.brazilian")
                
                @schemas.classproperty
                def BULGARIAN(cls):
                    return cls("lucene.bulgarian")
                
                @schemas.classproperty
                def CATALAN(cls):
                    return cls("lucene.catalan")
                
                @schemas.classproperty
                def CHINESE(cls):
                    return cls("lucene.chinese")
                
                @schemas.classproperty
                def CJK(cls):
                    return cls("lucene.cjk")
                
                @schemas.classproperty
                def CZECH(cls):
                    return cls("lucene.czech")
                
                @schemas.classproperty
                def DANISH(cls):
                    return cls("lucene.danish")
                
                @schemas.classproperty
                def DUTCH(cls):
                    return cls("lucene.dutch")
                
                @schemas.classproperty
                def ENGLISH(cls):
                    return cls("lucene.english")
                
                @schemas.classproperty
                def FINNISH(cls):
                    return cls("lucene.finnish")
                
                @schemas.classproperty
                def FRENCH(cls):
                    return cls("lucene.french")
                
                @schemas.classproperty
                def GALICIAN(cls):
                    return cls("lucene.galician")
                
                @schemas.classproperty
                def GERMAN(cls):
                    return cls("lucene.german")
                
                @schemas.classproperty
                def GREEK(cls):
                    return cls("lucene.greek")
                
                @schemas.classproperty
                def HINDI(cls):
                    return cls("lucene.hindi")
                
                @schemas.classproperty
                def HUNGARIAN(cls):
                    return cls("lucene.hungarian")
                
                @schemas.classproperty
                def INDONESIAN(cls):
                    return cls("lucene.indonesian")
                
                @schemas.classproperty
                def IRISH(cls):
                    return cls("lucene.irish")
                
                @schemas.classproperty
                def ITALIAN(cls):
                    return cls("lucene.italian")
                
                @schemas.classproperty
                def JAPANESE(cls):
                    return cls("lucene.japanese")
                
                @schemas.classproperty
                def KOREAN(cls):
                    return cls("lucene.korean")
                
                @schemas.classproperty
                def KUROMOJI(cls):
                    return cls("lucene.kuromoji")
                
                @schemas.classproperty
                def LATVIAN(cls):
                    return cls("lucene.latvian")
                
                @schemas.classproperty
                def LITHUANIAN(cls):
                    return cls("lucene.lithuanian")
                
                @schemas.classproperty
                def MORFOLOGIK(cls):
                    return cls("lucene.morfologik")
                
                @schemas.classproperty
                def NORI(cls):
                    return cls("lucene.nori")
                
                @schemas.classproperty
                def NORWEGIAN(cls):
                    return cls("lucene.norwegian")
                
                @schemas.classproperty
                def PERSIAN(cls):
                    return cls("lucene.persian")
                
                @schemas.classproperty
                def PORTUGUESE(cls):
                    return cls("lucene.portuguese")
                
                @schemas.classproperty
                def ROMANIAN(cls):
                    return cls("lucene.romanian")
                
                @schemas.classproperty
                def RUSSIAN(cls):
                    return cls("lucene.russian")
                
                @schemas.classproperty
                def SMARTCN(cls):
                    return cls("lucene.smartcn")
                
                @schemas.classproperty
                def SORANI(cls):
                    return cls("lucene.sorani")
                
                @schemas.classproperty
                def SPANISH(cls):
                    return cls("lucene.spanish")
                
                @schemas.classproperty
                def SWEDISH(cls):
                    return cls("lucene.swedish")
                
                @schemas.classproperty
                def THAI(cls):
                    return cls("lucene.thai")
                
                @schemas.classproperty
                def TURKISH(cls):
                    return cls("lucene.turkish")
                
                @schemas.classproperty
                def UKRAINIAN(cls):
                    return cls("lucene.ukrainian")
            
            
            class status(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def IN_PROGRESS(cls):
                    return cls("IN_PROGRESS")
                
                @schemas.classproperty
                def STEADY(cls):
                    return cls("STEADY")
                
                @schemas.classproperty
                def FAILED(cls):
                    return cls("FAILED")
                
                @schemas.classproperty
                def MIGRATING(cls):
                    return cls("MIGRATING")
                
                @schemas.classproperty
                def STALE(cls):
                    return cls("STALE")
                
                @schemas.classproperty
                def PAUSED(cls):
                    return cls("PAUSED")
            
            
            class synonyms(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['FTSSynonymMappingDefinition']:
                        return FTSSynonymMappingDefinition
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['FTSSynonymMappingDefinition'], typing.List['FTSSynonymMappingDefinition']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'synonyms':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'FTSSynonymMappingDefinition':
                    return super().__getitem__(i)
            __annotations__ = {
                "collectionName": collectionName,
                "database": database,
                "name": name,
                "analyzer": analyzer,
                "analyzers": analyzers,
                "indexID": indexID,
                "mappings": mappings,
                "searchAnalyzer": searchAnalyzer,
                "status": status,
                "synonyms": synonyms,
            }
    
    database: MetaOapg.properties.database
    name: MetaOapg.properties.name
    collectionName: MetaOapg.properties.collectionName
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["collectionName"]) -> MetaOapg.properties.collectionName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["database"]) -> MetaOapg.properties.database: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["analyzer"]) -> MetaOapg.properties.analyzer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["analyzers"]) -> MetaOapg.properties.analyzers: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["indexID"]) -> MetaOapg.properties.indexID: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mappings"]) -> 'ApiAtlasFTSMappingsViewManual': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["searchAnalyzer"]) -> MetaOapg.properties.searchAnalyzer: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["synonyms"]) -> MetaOapg.properties.synonyms: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["collectionName", "database", "name", "analyzer", "analyzers", "indexID", "mappings", "searchAnalyzer", "status", "synonyms", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["collectionName"]) -> MetaOapg.properties.collectionName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["database"]) -> MetaOapg.properties.database: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["analyzer"]) -> typing.Union[MetaOapg.properties.analyzer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["analyzers"]) -> typing.Union[MetaOapg.properties.analyzers, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["indexID"]) -> typing.Union[MetaOapg.properties.indexID, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mappings"]) -> typing.Union['ApiAtlasFTSMappingsViewManual', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["searchAnalyzer"]) -> typing.Union[MetaOapg.properties.searchAnalyzer, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["synonyms"]) -> typing.Union[MetaOapg.properties.synonyms, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["collectionName", "database", "name", "analyzer", "analyzers", "indexID", "mappings", "searchAnalyzer", "status", "synonyms", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        database: typing.Union[MetaOapg.properties.database, str, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        collectionName: typing.Union[MetaOapg.properties.collectionName, str, ],
        analyzer: typing.Union[MetaOapg.properties.analyzer, str, schemas.Unset] = schemas.unset,
        analyzers: typing.Union[MetaOapg.properties.analyzers, list, tuple, schemas.Unset] = schemas.unset,
        indexID: typing.Union[MetaOapg.properties.indexID, str, schemas.Unset] = schemas.unset,
        mappings: typing.Union['ApiAtlasFTSMappingsViewManual', schemas.Unset] = schemas.unset,
        searchAnalyzer: typing.Union[MetaOapg.properties.searchAnalyzer, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, str, schemas.Unset] = schemas.unset,
        synonyms: typing.Union[MetaOapg.properties.synonyms, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'FTSIndex':
        return super().__new__(
            cls,
            *_args,
            database=database,
            name=name,
            collectionName=collectionName,
            analyzer=analyzer,
            analyzers=analyzers,
            indexID=indexID,
            mappings=mappings,
            searchAnalyzer=searchAnalyzer,
            status=status,
            synonyms=synonyms,
            _configuration=_configuration,
            **kwargs,
        )

from atlas.model.api_atlas_fts_analyzers_view_manual import ApiAtlasFTSAnalyzersViewManual
from atlas.model.api_atlas_fts_mappings_view_manual import ApiAtlasFTSMappingsViewManual
from atlas.model.fts_synonym_mapping_definition import FTSSynonymMappingDefinition
