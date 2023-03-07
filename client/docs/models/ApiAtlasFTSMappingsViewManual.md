# atlas.model.api_atlas_fts_mappings_view_manual.ApiAtlasFTSMappingsViewManual

Index specifications for the collection's fields.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Index specifications for the collection&#x27;s fields. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dynamic** | bool,  | BoolClass,  | Flag that indicates whether the index uses dynamic or static mappings. Required if **mappings.fields** is omitted. | [optional] if omitted the server will use the default value of False
**[fields](#fields)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | One or more field specifications for the Atlas Search index. Required if **mappings.dynamic** is omitted or set to **false**. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# fields

One or more field specifications for the Atlas Search index. Required if **mappings.dynamic** is omitted or set to **false**.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | One or more field specifications for the Atlas Search index. Required if **mappings.dynamic** is omitted or set to **false**. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[any_string_name](#any_string_name)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | any string name can be used but the value must be the correct type | [optional] 

# any_string_name

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

