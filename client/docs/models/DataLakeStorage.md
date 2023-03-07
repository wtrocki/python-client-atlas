# atlas.model.data_lake_storage.DataLakeStorage

Configuration information for each data store and its mapping to MongoDB Cloud databases.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Configuration information for each data store and its mapping to MongoDB Cloud databases. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[databases](#databases)** | list, tuple,  | tuple,  | Array that contains the queryable databases and collections for this data lake. | [optional] 
**[stores](#stores)** | list, tuple,  | tuple,  | Array that contains the data stores for the data lake. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# databases

Array that contains the queryable databases and collections for this data lake.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array that contains the queryable databases and collections for this data lake. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DataLakeDatabase**](DataLakeDatabase.md) | [**DataLakeDatabase**](DataLakeDatabase.md) | [**DataLakeDatabase**](DataLakeDatabase.md) |  | 

# stores

Array that contains the data stores for the data lake.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array that contains the data stores for the data lake. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DataLakeStore**](DataLakeStore.md) | [**DataLakeStore**](DataLakeStore.md) | [**DataLakeStore**](DataLakeStore.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

