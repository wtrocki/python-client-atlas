# atlas.model.performance_advisor_operation_view.PerformanceAdvisorOperationView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[predicates](#predicates)** | list, tuple,  | tuple,  | List that contains the search criteria that the query uses. To use the values in key-value pairs in these predicates requires **Project Data Access Read Only** permissions or greater. Otherwise, MongoDB Cloud redacts these values. | [optional] 
**stats** | [**PerformanceAdvisorOpStatsView**](PerformanceAdvisorOpStatsView.md) | [**PerformanceAdvisorOpStatsView**](PerformanceAdvisorOpStatsView.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# predicates

List that contains the search criteria that the query uses. To use the values in key-value pairs in these predicates requires **Project Data Access Read Only** permissions or greater. Otherwise, MongoDB Cloud redacts these values.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains the search criteria that the query uses. To use the values in key-value pairs in these predicates requires **Project Data Access Read Only** permissions or greater. Otherwise, MongoDB Cloud redacts these values. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  | List that contains the search criteria that the query uses. To use the values in key-value pairs in these predicates requires **Project Data Access Read Only** permissions or greater. Otherwise, MongoDB Cloud redacts these values. | 

# items

List that contains the search criteria that the query uses. To use the values in key-value pairs in these predicates requires **Project Data Access Read Only** permissions or greater. Otherwise, MongoDB Cloud redacts these values.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | List that contains the search criteria that the query uses. To use the values in key-value pairs in these predicates requires **Project Data Access Read Only** permissions or greater. Otherwise, MongoDB Cloud redacts these values. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

