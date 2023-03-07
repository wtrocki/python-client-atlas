# atlas.model.app_service_metric_matcher_view.AppServiceMetricMatcherView

Rules to apply when comparing an app service metric against this alert configuration.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Rules to apply when comparing an app service metric against this alert configuration. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**fieldName** | [**AppServiceMetricMatcherField**](AppServiceMetricMatcherField.md) | [**AppServiceMetricMatcherField**](AppServiceMetricMatcherField.md) |  | [optional] 
**operator** | str,  | str,  | Comparison operator to apply when checking the current metric value against **matcher[n].value**. | [optional] must be one of ["EQUALS", "CONTAINS", "STARTS_WITH", "ENDS_WITH", "NOT_EQUALS", "NOT_CONTAINS", "REGEX", ] 
**value** | str,  | str,  | Value to match or exceed using the specified **matchers.operator**. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

