# atlas.model.threshold_view_integer.ThresholdViewInteger

A Limit that triggers an alert when  exceeded. The resource returns this parameter when **eventTypeName** has not been set to `OUTSIDE_METRIC_THRESHOLD`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A Limit that triggers an alert when  exceeded. The resource returns this parameter when **eventTypeName** has not been set to &#x60;OUTSIDE_METRIC_THRESHOLD&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**operator** | [**Operator**](Operator.md) | [**Operator**](Operator.md) |  | [optional] 
**threshold** | decimal.Decimal, int,  | decimal.Decimal,  | Value of metric that, when exceeded, triggers an alert. | [optional] value must be a 32 bit integer
**units** | str,  | str,  | Element used to express the quantity. This can be an element of time, storage capacity, and the like. | [optional] must be one of ["bits", "Kbits", "Mbits", "Gbits", "bytes", "KB", "MB", "GB", "TB", "PB", "nsec", "msec", "sec", "min", "hours", "million minutes", "days", "requests", "1000 requests", "GB seconds", "GB hours", "GB days", "RPU", "thousand RPU", "million RPU", "WPU", "thousand WPU", "million WPU", "count", "thousand", "million", "billion", "", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

