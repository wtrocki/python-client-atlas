# atlas.model.host_metric_value_view.HostMetricValueView

Value of the metric that triggered the alert. The resource returns this parameter for alerts of events impacting hosts.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Value of the metric that triggered the alert. The resource returns this parameter for alerts of events impacting hosts. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**number** | decimal.Decimal, int, float,  | decimal.Decimal,  | Amount of the **metricName** recorded at the time of the event. This value triggered the alert. | [optional] value must be a 64 bit float
**units** | str,  | str,  |  | [optional] must be one of ["bits", "Kbits", "Mbits", "Gbits", "bytes", "KB", "MB", "GB", "TB", "PB", "nsec", "msec", "sec", "min", "hours", "million minutes", "days", "requests", "1000 requests", "GB seconds", "GB hours", "GB days", "RPU", "thousand RPU", "million RPU", "WPU", "thousand WPU", "million WPU", "count", "thousand", "million", "billion", "", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

