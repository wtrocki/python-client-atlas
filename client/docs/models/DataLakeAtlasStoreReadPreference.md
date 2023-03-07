# atlas.model.data_lake_atlas_store_read_preference.DataLakeAtlasStoreReadPreference

MongoDB Cloud cluster read preference, which describes how to route read requests to the cluster.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | MongoDB Cloud cluster read preference, which describes how to route read requests to the cluster. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**maxStalenessSeconds** | decimal.Decimal, int,  | decimal.Decimal,  | Maximum replication lag, or **staleness**, for reads from secondaries. | [optional] value must be a 32 bit integer
**mode** | str,  | str,  | [Read preference mode](https://docs.mongodb.com/manual/core/read-preference/#read-preference-modes) that specifies to which replica set member to route the read requests. | [optional] must be one of ["primary", "primaryPreferred", "secondary", "secondaryPreferred", "nearest", ] 
**[tagSets](#tagSets)** | list, tuple,  | tuple,  | List that contains [tag sets](https://docs.mongodb.com/manual/core/read-preference-tags/) or tag specification documents. If specified, Atlas Data Lake routes read requests to replica set member or members that are associated with the specified tags. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tagSets

List that contains [tag sets](https://docs.mongodb.com/manual/core/read-preference-tags/) or tag specification documents. If specified, Atlas Data Lake routes read requests to replica set member or members that are associated with the specified tags.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains [tag sets](https://docs.mongodb.com/manual/core/read-preference-tags/) or tag specification documents. If specified, Atlas Data Lake routes read requests to replica set member or members that are associated with the specified tags. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | list, tuple,  | tuple,  | List that contains [tag sets](https://docs.mongodb.com/manual/core/read-preference-tags/) or tag specification documents. If specified, Atlas Data Lake routes read requests to replica set member or members that are associated with the specified tags. | 

# items

List that contains [tag sets](https://docs.mongodb.com/manual/core/read-preference-tags/) or tag specification documents. If specified, Atlas Data Lake routes read requests to replica set member or members that are associated with the specified tags.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains [tag sets](https://docs.mongodb.com/manual/core/read-preference-tags/) or tag specification documents. If specified, Atlas Data Lake routes read requests to replica set member or members that are associated with the specified tags. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DataLakeAtlasStoreReadPreferenceTag**](DataLakeAtlasStoreReadPreferenceTag.md) | [**DataLakeAtlasStoreReadPreferenceTag**](DataLakeAtlasStoreReadPreferenceTag.md) | [**DataLakeAtlasStoreReadPreferenceTag**](DataLakeAtlasStoreReadPreferenceTag.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

