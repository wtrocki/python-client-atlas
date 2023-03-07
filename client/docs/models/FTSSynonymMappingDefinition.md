# atlas.model.fts_synonym_mapping_definition.FTSSynonymMappingDefinition

Synonyms used for this full text index.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Synonyms used for this full text index. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**analyzer** | str,  | str,  | Specific pre-defined method chosen to apply to the synonyms to be searched. | must be one of ["lucene.standard", "lucene.simple", "lucene.whitespace", "lucene.keyword", "lucene.arabic", "lucene.armenian", "lucene.basque", "lucene.bengali", "lucene.brazilian", "lucene.bulgarian", "lucene.catalan", "lucene.chinese", "lucene.cjk", "lucene.czech", "lucene.danish", "lucene.dutch", "lucene.english", "lucene.finnish", "lucene.french", "lucene.galician", "lucene.german", "lucene.greek", "lucene.hindi", "lucene.hungarian", "lucene.indonesian", "lucene.irish", "lucene.italian", "lucene.japanese", "lucene.korean", "lucene.kuromoji", "lucene.latvian", "lucene.lithuanian", "lucene.morfologik", "lucene.nori", "lucene.norwegian", "lucene.persian", "lucene.portuguese", "lucene.romanian", "lucene.russian", "lucene.smartcn", "lucene.sorani", "lucene.spanish", "lucene.swedish", "lucene.thai", "lucene.turkish", "lucene.ukrainian", ] if omitted the server will use the default value of "lucene.standard"
**name** | str,  | str,  | Human-readable label that identifies the synonym definition. Each **synonym.name** must be unique within the same index definition. | 
**source** | [**SynonymSource**](SynonymSource.md) | [**SynonymSource**](SynonymSource.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

