# atlas.model.compute_auto_scaling_v15.ComputeAutoScalingV15

Options that determine how this cluster handles CPU scaling.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Options that determine how this cluster handles CPU scaling. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**enabled** | bool,  | BoolClass,  | Flag that indicates whether someone enabled instance size auto-scaling.  - Set to &#x60;true&#x60; to enable instance size auto-scaling. If enabled, you must specify a value for **replicationSpecs[n].regionConfigs[m].autoScaling.compute.maxInstanceSize**. - Set to &#x60;false&#x60; to disable instance size automatic scaling. | [optional] 
**maxInstanceSize** | [**InstanceSize**](InstanceSize.md) | [**InstanceSize**](InstanceSize.md) |  | [optional] 
**minInstanceSize** | [**InstanceSize**](InstanceSize.md) | [**InstanceSize**](InstanceSize.md) |  | [optional] 
**scaleDownEnabled** | bool,  | BoolClass,  | Flag that indicates whether the instance size may scale down. MongoDB Cloud requires this parameter if &#x60;\&quot;replicationSpecs[n].regionConfigs[m].autoScaling.compute.enabled\&quot; : true&#x60;. If you enable this option, specify a value for **replicationSpecs[n].regionConfigs[m].autoScaling.compute.minInstanceSize**. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

