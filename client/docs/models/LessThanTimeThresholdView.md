# atlas.model.less_than_time_threshold_view.LessThanTimeThresholdView

A Limit that triggers an alert when less than a time period.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A Limit that triggers an alert when less than a time period. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**operator** | str,  | str,  | Comparison operator to apply when checking the current metric value. | [optional] must be one of ["LESS_THAN", ] 
**threshold** | decimal.Decimal, int,  | decimal.Decimal,  | Value of metric that, when exceeded, triggers an alert. | [optional] value must be a 32 bit integer
**units** | [**TimeMetricUnits**](TimeMetricUnits.md) | [**TimeMetricUnits**](TimeMetricUnits.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
