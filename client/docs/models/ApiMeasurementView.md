# atlas.model.api_measurement_view.ApiMeasurementView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[dataPoints](#dataPoints)** | list, tuple,  | tuple,  | List that contains the value of, and metadata provided for, one data point generated at a particular moment in time. If no data point exists for a particular moment in time, the &#x60;value&#x60; parameter returns &#x60;null&#x60;. | [optional] 
**name** | str,  | str,  | Human-readable label of the measurement that this data point covers. | [optional] 
**units** | str,  | str,  | Element used to quantify the measurement. The resource returns units of throughput, storage, and time. | [optional] must be one of ["BYTES", "BYTES_PER_SECOND", "GIGABYTES", "GIGABYTES_PER_HOUR", "MEGABYTES_PER_SECOND", "MILLISECONDS", "PERCENT", "SCALAR", "SCALAR_PER_SECOND", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# dataPoints

List that contains the value of, and metadata provided for, one data point generated at a particular moment in time. If no data point exists for a particular moment in time, the `value` parameter returns `null`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains the value of, and metadata provided for, one data point generated at a particular moment in time. If no data point exists for a particular moment in time, the &#x60;value&#x60; parameter returns &#x60;null&#x60;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiMetricDataPointView**](ApiMetricDataPointView.md) | [**ApiMetricDataPointView**](ApiMetricDataPointView.md) | [**ApiMetricDataPointView**](ApiMetricDataPointView.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

