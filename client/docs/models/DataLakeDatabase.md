# atlas.model.data_lake_database.DataLakeDatabase

Database associated with this data lake. Databases contain collections and views.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Database associated with this data lake. Databases contain collections and views. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[collections](#collections)** | list, tuple,  | tuple,  | Array of collections and data sources that map to a &#x60;&#x60;stores&#x60;&#x60; data store. | [optional] 
**maxWildcardCollections** | decimal.Decimal, int,  | decimal.Decimal,  | Maximum number of wildcard collections in the database. This only applies to S3 data sources. | [optional] if omitted the server will use the default value of 100value must be a 32 bit integer
**name** | str,  | str,  | Human-readable label that identifies the database to which the data lake maps data. | [optional] 
**[views](#views)** | list, tuple,  | tuple,  | Array of aggregation pipelines that apply to the collection. This only applies to S3 data sources. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# collections

Array of collections and data sources that map to a ``stores`` data store.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of collections and data sources that map to a &#x60;&#x60;stores&#x60;&#x60; data store. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DataLakeDatabaseCollection**](DataLakeDatabaseCollection.md) | [**DataLakeDatabaseCollection**](DataLakeDatabaseCollection.md) | [**DataLakeDatabaseCollection**](DataLakeDatabaseCollection.md) |  | 

# views

Array of aggregation pipelines that apply to the collection. This only applies to S3 data sources.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of aggregation pipelines that apply to the collection. This only applies to S3 data sources. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DataLakeView**](DataLakeView.md) | [**DataLakeView**](DataLakeView.md) | [**DataLakeView**](DataLakeView.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

