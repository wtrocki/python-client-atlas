# atlas.model.api_performance_advisor_slow_query_list_view.ApiPerformanceAdvisorSlowQueryListView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[slowQueries](#slowQueries)** | list, tuple,  | tuple,  | List of operations that the Performance Advisor detected that took longer to execute than a specified threshold. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# slowQueries

List of operations that the Performance Advisor detected that took longer to execute than a specified threshold.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of operations that the Performance Advisor detected that took longer to execute than a specified threshold. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiPerformanceAdvisorSlowQueryView**](ApiPerformanceAdvisorSlowQueryView.md) | [**ApiPerformanceAdvisorSlowQueryView**](ApiPerformanceAdvisorSlowQueryView.md) | [**ApiPerformanceAdvisorSlowQueryView**](ApiPerformanceAdvisorSlowQueryView.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

