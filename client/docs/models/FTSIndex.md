# atlas.model.fts_index.FTSIndex

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**database** | str,  | str,  | Human-readable label that identifies the database that contains the collection with one or more Atlas Search indexes. | 
**name** | str,  | str,  | Human-readable label that identifies this index. Within each namespace, names of all indexes in the namespace must be unique. | 
**collectionName** | str,  | str,  | Human-readable label that identifies the collection that contains one or more Atlas Search indexes. | 
**analyzer** | str,  | str,  | Specific pre-defined method chosen to convert database field text into searchable words. This conversion reduces the text of fields into the smallest units of text. These units are called a **term** or **token**. This process, known as tokenization, involves a variety of changes made to the text in fields:  - extracting words - removing punctuation - removing accents - changing to lowercase - removing common words - reducing words to their root form (stemming) - changing words to their base form (lemmatization)  MongoDB Cloud uses the selected process to build the Atlas Search index. | [optional] must be one of ["lucene.standard", "lucene.simple", "lucene.whitespace", "lucene.keyword", "lucene.arabic", "lucene.armenian", "lucene.basque", "lucene.bengali", "lucene.brazilian", "lucene.bulgarian", "lucene.catalan", "lucene.chinese", "lucene.cjk", "lucene.czech", "lucene.danish", "lucene.dutch", "lucene.english", "lucene.finnish", "lucene.french", "lucene.galician", "lucene.german", "lucene.greek", "lucene.hindi", "lucene.hungarian", "lucene.indonesian", "lucene.irish", "lucene.italian", "lucene.japanese", "lucene.korean", "lucene.kuromoji", "lucene.latvian", "lucene.lithuanian", "lucene.morfologik", "lucene.nori", "lucene.norwegian", "lucene.persian", "lucene.portuguese", "lucene.romanian", "lucene.russian", "lucene.smartcn", "lucene.sorani", "lucene.spanish", "lucene.swedish", "lucene.thai", "lucene.turkish", "lucene.ukrainian", ] if omitted the server will use the default value of "lucene.standard"
**[analyzers](#analyzers)** | list, tuple,  | tuple,  | List of user-defined methods to convert database field text into searchable words. | [optional] 
**indexID** | str,  | str,  | Unique 24-hexadecimal digit string that identifies this Atlas Search index. | [optional] 
**mappings** | [**ApiAtlasFTSMappingsViewManual**](ApiAtlasFTSMappingsViewManual.md) | [**ApiAtlasFTSMappingsViewManual**](ApiAtlasFTSMappingsViewManual.md) |  | [optional] 
**searchAnalyzer** | str,  | str,  | Method applied to identify words when searching this index. | [optional] must be one of ["lucene.standard", "lucene.simple", "lucene.whitespace", "lucene.keyword", "lucene.arabic", "lucene.armenian", "lucene.basque", "lucene.bengali", "lucene.brazilian", "lucene.bulgarian", "lucene.catalan", "lucene.chinese", "lucene.cjk", "lucene.czech", "lucene.danish", "lucene.dutch", "lucene.english", "lucene.finnish", "lucene.french", "lucene.galician", "lucene.german", "lucene.greek", "lucene.hindi", "lucene.hungarian", "lucene.indonesian", "lucene.irish", "lucene.italian", "lucene.japanese", "lucene.korean", "lucene.kuromoji", "lucene.latvian", "lucene.lithuanian", "lucene.morfologik", "lucene.nori", "lucene.norwegian", "lucene.persian", "lucene.portuguese", "lucene.romanian", "lucene.russian", "lucene.smartcn", "lucene.sorani", "lucene.spanish", "lucene.swedish", "lucene.thai", "lucene.turkish", "lucene.ukrainian", ] if omitted the server will use the default value of "lucene.standard"
**status** | str,  | str,  | Condition of the search index when you made this request.  | Status | Index Condition |  |---|---|  | IN_PROGRESS | Atlas is building or re-building the index after an edit. |  | STEADY | You can use this search index. |  | FAILED | Atlas could not build the index. |  | MIGRATING | Atlas is upgrading the underlying cluster tier and migrating indexes. |  | PAUSED | The cluster is paused. |  | [optional] must be one of ["IN_PROGRESS", "STEADY", "FAILED", "MIGRATING", "STALE", "PAUSED", ] 
**[synonyms](#synonyms)** | list, tuple,  | tuple,  | Rule sets that map words to their synonyms in this index. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# analyzers

List of user-defined methods to convert database field text into searchable words.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of user-defined methods to convert database field text into searchable words. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiAtlasFTSAnalyzersViewManual**](ApiAtlasFTSAnalyzersViewManual.md) | [**ApiAtlasFTSAnalyzersViewManual**](ApiAtlasFTSAnalyzersViewManual.md) | [**ApiAtlasFTSAnalyzersViewManual**](ApiAtlasFTSAnalyzersViewManual.md) |  | 

# synonyms

Rule sets that map words to their synonyms in this index.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Rule sets that map words to their synonyms in this index. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FTSSynonymMappingDefinition**](FTSSynonymMappingDefinition.md) | [**FTSSynonymMappingDefinition**](FTSSynonymMappingDefinition.md) | [**FTSSynonymMappingDefinition**](FTSSynonymMappingDefinition.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

