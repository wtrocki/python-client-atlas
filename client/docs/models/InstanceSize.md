# atlas.model.instance_size.InstanceSize

Minimum instance size to which your cluster can automatically scale. MongoDB Cloud requires this parameter if `\"replicationSpecs[n].regionConfigs[m].autoScaling.compute.scaleDownEnabled\" : true`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Minimum instance size to which your cluster can automatically scale. MongoDB Cloud requires this parameter if &#x60;\&quot;replicationSpecs[n].regionConfigs[m].autoScaling.compute.scaleDownEnabled\&quot; : true&#x60;. | must be one of ["M10", "M20", "M30", "M40", "M50", "M60", "M80", "M100", "M140", "M200", "M300", "R40", "R50", "R60", "R80", "R200", "R300", "R400", "R700", "M40_NVME", "M50_NVME", "M60_NVME", "M80_NVME", "M200_NVME", "M400_NVME", "M90", "M300_NVME", "M600_NVME", "M250", "M400", "R600", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

