# atlas.model.less_than_days_threshold_view.LessThanDaysThresholdView

Threshold value that triggers an alert.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Threshold value that triggers an alert. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**operator** | str,  | str,  | Comparison operator to apply when checking the current metric value. | [optional] must be one of ["LESS_THAN", ] 
**threshold** | decimal.Decimal, int,  | decimal.Decimal,  | Value of metric that, when exceeded, triggers an alert. | [optional] value must be a 32 bit integer
**units** | str,  | str,  | Element used to express the quantity. This can be an element of time, storage capacity, and the like. | [optional] must be one of ["DAYS", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

