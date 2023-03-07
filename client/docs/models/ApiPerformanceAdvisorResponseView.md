# atlas.model.api_performance_advisor_response_view.ApiPerformanceAdvisorResponseView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[shapes](#shapes)** | list, tuple,  | tuple,  | List of query predicates, sorts, and projections that the Performance Advisor suggests. | [optional] 
**[suggestedIndexes](#suggestedIndexes)** | list, tuple,  | tuple,  | List that contains the documents with information about the indexes that the Performance Advisor suggests. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# shapes

List of query predicates, sorts, and projections that the Performance Advisor suggests.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of query predicates, sorts, and projections that the Performance Advisor suggests. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiPerformanceAdvisorShapeView**](ApiPerformanceAdvisorShapeView.md) | [**ApiPerformanceAdvisorShapeView**](ApiPerformanceAdvisorShapeView.md) | [**ApiPerformanceAdvisorShapeView**](ApiPerformanceAdvisorShapeView.md) |  | 

# suggestedIndexes

List that contains the documents with information about the indexes that the Performance Advisor suggests.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains the documents with information about the indexes that the Performance Advisor suggests. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiPerformanceAdvisorIndexView**](ApiPerformanceAdvisorIndexView.md) | [**ApiPerformanceAdvisorIndexView**](ApiPerformanceAdvisorIndexView.md) | [**ApiPerformanceAdvisorIndexView**](ApiPerformanceAdvisorIndexView.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

