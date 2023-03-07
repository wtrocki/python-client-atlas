# atlas.model.data_lake_database_collection.DataLakeDatabaseCollection

A collection and data sources that map to a ``stores`` data store.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A collection and data sources that map to a &#x60;&#x60;stores&#x60;&#x60; data store. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[dataSources](#dataSources)** | list, tuple,  | tuple,  | Array that contains the data stores that map to a collection for this data lake. | [optional] 
**name** | str,  | str,  | Human-readable label that identifies the collection to which MongoDB Cloud maps the data in the data stores. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# dataSources

Array that contains the data stores that map to a collection for this data lake.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array that contains the data stores that map to a collection for this data lake. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DataLakeDatabaseDataSource**](DataLakeDatabaseDataSource.md) | [**DataLakeDatabaseDataSource**](DataLakeDatabaseDataSource.md) | [**DataLakeDatabaseDataSource**](DataLakeDatabaseDataSource.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

