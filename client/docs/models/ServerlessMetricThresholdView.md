# atlas.model.serverless_metric_threshold_view.ServerlessMetricThresholdView

Threshold for the metric that, when exceeded, triggers an alert. The metric threshold pertains to event types which reflects changes of measurements and metrics about the serverless database.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Threshold for the metric that, when exceeded, triggers an alert. The metric threshold pertains to event types which reflects changes of measurements and metrics about the serverless database. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[TimeMetricThresholdView](TimeMetricThresholdView.md) | [**TimeMetricThresholdView**](TimeMetricThresholdView.md) | [**TimeMetricThresholdView**](TimeMetricThresholdView.md) |  | 
[RawMetricThresholdView](RawMetricThresholdView.md) | [**RawMetricThresholdView**](RawMetricThresholdView.md) | [**RawMetricThresholdView**](RawMetricThresholdView.md) |  | 
[DataMetricThresholdView](DataMetricThresholdView.md) | [**DataMetricThresholdView**](DataMetricThresholdView.md) | [**DataMetricThresholdView**](DataMetricThresholdView.md) |  | 
[RPUMetricThresholdView](RPUMetricThresholdView.md) | [**RPUMetricThresholdView**](RPUMetricThresholdView.md) | [**RPUMetricThresholdView**](RPUMetricThresholdView.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

