# atlas.model.api_index_request_view.ApiIndexRequestView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**collection** | str,  | str,  | Human-readable label of the collection for which MongoDB Cloud creates an index. | 
**db** | str,  | str,  | Human-readable label of the database that holds the collection on which MongoDB Cloud creates an index. | 
**collation** | [**Collation**](Collation.md) | [**Collation**](Collation.md) |  | [optional] 
**[keys](#keys)** | list, tuple,  | tuple,  | List that contains one or more objects that describe the parameters that you want to index. | [optional] 
**options** | [**IndexOptions**](IndexOptions.md) | [**IndexOptions**](IndexOptions.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# keys

List that contains one or more objects that describe the parameters that you want to index.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains one or more objects that describe the parameters that you want to index. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Key-value pair that sets the parameter to index as the key and the type of index as its value. To create a [multikey index](https://docs.mongodb.com/manual/core/index-multikey/), list each parameter in its own object within this array. | 

# items

Key-value pair that sets the parameter to index as the key and the type of index as its value. To create a [multikey index](https://docs.mongodb.com/manual/core/index-multikey/), list each parameter in its own object within this array.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Key-value pair that sets the parameter to index as the key and the type of index as its value. To create a [multikey index](https://docs.mongodb.com/manual/core/index-multikey/), list each parameter in its own object within this array. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type Key-value pair that sets the parameter to index as the key and the type of index as its value. To create a [multikey index](https://docs.mongodb.com/manual/core/index-multikey/), list each parameter in its own object within this array. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

