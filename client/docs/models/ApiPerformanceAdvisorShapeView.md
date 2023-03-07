# atlas.model.api_performance_advisor_shape_view.ApiPerformanceAdvisorShapeView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**avgMs** | decimal.Decimal, int,  | decimal.Decimal,  | Average duration in milliseconds for the queries examined that match this shape. | [optional] value must be a 64 bit integer
**count** | decimal.Decimal, int,  | decimal.Decimal,  | Number of queries examined that match this shape. | [optional] value must be a 64 bit integer
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies this shape. This string exists only for the duration of this API request. | [optional] 
**inefficiencyScore** | decimal.Decimal, int,  | decimal.Decimal,  | Average number of documents read for every document that the query returns. | [optional] value must be a 64 bit integer
**namespace** | str,  | str,  | Human-readable label that identifies the namespace on the specified host. The resource expresses this parameter value as &#x60;&lt;database&gt;.&lt;collection&gt;&#x60;. | [optional] 
**[operations](#operations)** | list, tuple,  | tuple,  | List that contains specific about individual queries. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# operations

List that contains specific about individual queries.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains specific about individual queries. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PerformanceAdvisorOperationView**](PerformanceAdvisorOperationView.md) | [**PerformanceAdvisorOperationView**](PerformanceAdvisorOperationView.md) | [**PerformanceAdvisorOperationView**](PerformanceAdvisorOperationView.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

