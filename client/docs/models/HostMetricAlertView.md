# atlas.model.host_metric_alert_view.HostMetricAlertView

Host Metric Alert notifies about changes of measurements or metrics for mongod host.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Host Metric Alert notifies about changes of measurements or metrics for mongod host. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[RawMetricAlertView](RawMetricAlertView.md) | [**RawMetricAlertView**](RawMetricAlertView.md) | [**RawMetricAlertView**](RawMetricAlertView.md) |  | 
[TimeMetricAlertView](TimeMetricAlertView.md) | [**TimeMetricAlertView**](TimeMetricAlertView.md) | [**TimeMetricAlertView**](TimeMetricAlertView.md) |  | 
[DataMetricAlertView](DataMetricAlertView.md) | [**DataMetricAlertView**](DataMetricAlertView.md) | [**DataMetricAlertView**](DataMetricAlertView.md) |  | 
[NumberMetricAlertView](NumberMetricAlertView.md) | [**NumberMetricAlertView**](NumberMetricAlertView.md) | [**NumberMetricAlertView**](NumberMetricAlertView.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

