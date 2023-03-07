# atlas.model.api_performance_advisor_index_view.ApiPerformanceAdvisorIndexView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**avgObjSize** | decimal.Decimal, int, float,  | decimal.Decimal,  | The average size of an object in the collection of this index. | [optional] value must be a 64 bit float
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies this index. | [optional] 
**[impact](#impact)** | list, tuple,  | tuple,  | List that contains unique 24-hexadecimal character string that identifies the query shapes in this response that the Performance Advisor suggests. | [optional] 
**[index](#index)** | list, tuple,  | tuple,  | List that contains documents that specify a key in the index and its sort order. | [optional] 
**namespace** | str,  | str,  | Human-readable label that identifies the namespace on the specified host. The resource expresses this parameter value as &#x60;&lt;database&gt;.&lt;collection&gt;&#x60;. | [optional] 
**weight** | decimal.Decimal, int, float,  | decimal.Decimal,  | Estimated performance improvement that the suggested index provides. This value corresponds to **Impact** in the Performance Advisor user interface. | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# impact

List that contains unique 24-hexadecimal character string that identifies the query shapes in this response that the Performance Advisor suggests.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains unique 24-hexadecimal character string that identifies the query shapes in this response that the Performance Advisor suggests. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | One unique 24-hexadecimal character string that identifies one query shape. | 

# index

List that contains documents that specify a key in the index and its sort order.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains documents that specify a key in the index and its sort order. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | One index key paired with its sort order. A value of &#x60;1&#x60; indicates an ascending sort order. A value of &#x60;-1&#x60; indicates a descending sort order. Keys in indexes with multiple keys appear in the same order that they appear in the index. | 

# items

One index key paired with its sort order. A value of `1` indicates an ascending sort order. A value of `-1` indicates a descending sort order. Keys in indexes with multiple keys appear in the same order that they appear in the index.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | One index key paired with its sort order. A value of &#x60;1&#x60; indicates an ascending sort order. A value of &#x60;-1&#x60; indicates a descending sort order. Keys in indexes with multiple keys appear in the same order that they appear in the index. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type One index key paired with its sort order. A value of &#x60;1&#x60; indicates an ascending sort order. A value of &#x60;-1&#x60; indicates a descending sort order. Keys in indexes with multiple keys appear in the same order that they appear in the index. | [optional] must be one of ["1", "1", "-1", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

