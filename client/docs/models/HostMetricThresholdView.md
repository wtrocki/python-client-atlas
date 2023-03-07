# atlas.model.host_metric_threshold_view.HostMetricThresholdView

Threshold for the metric that, when exceeded, triggers an alert. The metric threshold pertains to event types which reflects changes of measurements and metrics about mongod host.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Threshold for the metric that, when exceeded, triggers an alert. The metric threshold pertains to event types which reflects changes of measurements and metrics about mongod host. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[RawMetricThresholdView](RawMetricThresholdView.md) | [**RawMetricThresholdView**](RawMetricThresholdView.md) | [**RawMetricThresholdView**](RawMetricThresholdView.md) |  | 
[TimeMetricThresholdView](TimeMetricThresholdView.md) | [**TimeMetricThresholdView**](TimeMetricThresholdView.md) | [**TimeMetricThresholdView**](TimeMetricThresholdView.md) |  | 
[DataMetricThresholdView](DataMetricThresholdView.md) | [**DataMetricThresholdView**](DataMetricThresholdView.md) | [**DataMetricThresholdView**](DataMetricThresholdView.md) |  | 
[NumberMetricThresholdView](NumberMetricThresholdView.md) | [**NumberMetricThresholdView**](NumberMetricThresholdView.md) | [**NumberMetricThresholdView**](NumberMetricThresholdView.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

