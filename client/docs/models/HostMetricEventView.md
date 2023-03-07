# atlas.model.host_metric_event_view.HostMetricEventView

Host Metric Event reflects different measurements and metrics about mongod host.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Host Metric Event reflects different measurements and metrics about mongod host. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[RawMetricEventView](RawMetricEventView.md) | [**RawMetricEventView**](RawMetricEventView.md) | [**RawMetricEventView**](RawMetricEventView.md) |  | 
[TimeMetricEventView](TimeMetricEventView.md) | [**TimeMetricEventView**](TimeMetricEventView.md) | [**TimeMetricEventView**](TimeMetricEventView.md) |  | 
[DataMetricEventView](DataMetricEventView.md) | [**DataMetricEventView**](DataMetricEventView.md) | [**DataMetricEventView**](DataMetricEventView.md) |  | 
[NumberMetricEventView](NumberMetricEventView.md) | [**NumberMetricEventView**](NumberMetricEventView.md) | [**NumberMetricEventView**](NumberMetricEventView.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

