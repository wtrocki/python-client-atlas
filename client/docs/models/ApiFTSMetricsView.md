# atlas.model.api_fts_metrics_view.ApiFTSMetricsView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**processId** | str,  | str,  | Hostname and port that identifies the process. | 
**groupId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the project. | 
**[hardwareMetrics](#hardwareMetrics)** | list, tuple,  | tuple,  | List that contains all host compute, memory, and storage utilization dedicated to Atlas Search when MongoDB Atlas received this request. | [optional] 
**[indexMetrics](#indexMetrics)** | list, tuple,  | tuple,  | List that contains all performance and utilization measurements that Atlas Search index performed by the time MongoDB Atlas received this request. | [optional] 
**[links](#links)** | list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | [optional] 
**[statusMetrics](#statusMetrics)** | list, tuple,  | tuple,  | List that contains all available Atlas Search status metrics when MongoDB Atlas received this request. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# hardwareMetrics

List that contains all host compute, memory, and storage utilization dedicated to Atlas Search when MongoDB Atlas received this request.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains all host compute, memory, and storage utilization dedicated to Atlas Search when MongoDB Atlas received this request. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiFTSMetricView**](ApiFTSMetricView.md) | [**ApiFTSMetricView**](ApiFTSMetricView.md) | [**ApiFTSMetricView**](ApiFTSMetricView.md) |  | 

# indexMetrics

List that contains all performance and utilization measurements that Atlas Search index performed by the time MongoDB Atlas received this request.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains all performance and utilization measurements that Atlas Search index performed by the time MongoDB Atlas received this request. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiFTSMetricView**](ApiFTSMetricView.md) | [**ApiFTSMetricView**](ApiFTSMetricView.md) | [**ApiFTSMetricView**](ApiFTSMetricView.md) |  | 

# links

List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Link**](Link.md) | [**Link**](Link.md) | [**Link**](Link.md) |  | 

# statusMetrics

List that contains all available Atlas Search status metrics when MongoDB Atlas received this request.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains all available Atlas Search status metrics when MongoDB Atlas received this request. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiFTSMetricView**](ApiFTSMetricView.md) | [**ApiFTSMetricView**](ApiFTSMetricView.md) | [**ApiFTSMetricView**](ApiFTSMetricView.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

