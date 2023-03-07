# atlas.model.data_lake_atlas_store_read_preference_tag.DataLakeAtlasStoreReadPreferenceTag

List that contains [tag sets](https://docs.mongodb.com/manual/core/read-preference-tags/) or tag specification documents. If specified, Atlas Data Lake routes read requests to replica set member or members that are associated with the specified tags.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | List that contains [tag sets](https://docs.mongodb.com/manual/core/read-preference-tags/) or tag specification documents. If specified, Atlas Data Lake routes read requests to replica set member or members that are associated with the specified tags. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Human-readable label of the tag. | [optional] 
**value** | str,  | str,  | Value of the tag. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

