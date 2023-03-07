# atlas.model.time_metric_threshold_view.TimeMetricThresholdView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**metricName** | str,  | str,  | Human-readable label that identifies the metric against which MongoDB Cloud checks the configured **metricThreshold.threshold**. | [optional] 
**mode** | str,  | str,  | MongoDB Cloud computes the current metric value as an average. | [optional] must be one of ["AVERAGE", ] 
**operator** | [**Operator**](Operator.md) | [**Operator**](Operator.md) |  | [optional] 
**threshold** | decimal.Decimal, int, float,  | decimal.Decimal,  | Value of metric that, when exceeded, triggers an alert. | [optional] value must be a 64 bit float
**units** | [**TimeMetricUnits**](TimeMetricUnits.md) | [**TimeMetricUnits**](TimeMetricUnits.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

