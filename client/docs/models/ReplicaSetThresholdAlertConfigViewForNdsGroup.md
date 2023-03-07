# atlas.model.replica_set_threshold_alert_config_view_for_nds_group.ReplicaSetThresholdAlertConfigViewForNdsGroup

Replica Set threshold alert configuration allows to select thresholds for conditions of mongod replica set which trigger alerts and how users are notified.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Replica Set threshold alert configuration allows to select thresholds for conditions of mongod replica set which trigger alerts and how users are notified. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[LessThanTimeThresholdAlertConfigViewForNdsGroup](LessThanTimeThresholdAlertConfigViewForNdsGroup.md) | [**LessThanTimeThresholdAlertConfigViewForNdsGroup**](LessThanTimeThresholdAlertConfigViewForNdsGroup.md) | [**LessThanTimeThresholdAlertConfigViewForNdsGroup**](LessThanTimeThresholdAlertConfigViewForNdsGroup.md) |  | 
[GreaterThanRawThresholdAlertConfigViewForNdsGroup](GreaterThanRawThresholdAlertConfigViewForNdsGroup.md) | [**GreaterThanRawThresholdAlertConfigViewForNdsGroup**](GreaterThanRawThresholdAlertConfigViewForNdsGroup.md) | [**GreaterThanRawThresholdAlertConfigViewForNdsGroup**](GreaterThanRawThresholdAlertConfigViewForNdsGroup.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

