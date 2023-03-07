# atlas.model.dedicated_hardware_spec.DedicatedHardwareSpec

Hardware specifications for read-only nodes in the region. Read-only nodes can never become the primary member, but can enable local reads.If you don't specify this parameter, no read-only nodes are deployed to the region.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Hardware specifications for read-only nodes in the region. Read-only nodes can never become the primary member, but can enable local reads.If you don&#x27;t specify this parameter, no read-only nodes are deployed to the region. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**nodeCount** | decimal.Decimal, int,  | decimal.Decimal,  | Number of read-only nodes for MongoDB Cloud to deploy to the region. Read-only nodes can never become the primary, but can enable local reads. | [optional] value must be a 32 bit integer
**diskIOPS** | decimal.Decimal, int,  | decimal.Decimal,  | Target throughput desired for storage attached to your AWS-provisioned cluster. Change this parameter only if you:  - set &#x60;\&quot;replicationSpecs[n].regionConfigs[m].providerName\&quot; : \&quot;AWS\&quot;&#x60;. - set &#x60;\&quot;replicationSpecs[n].regionConfigs[m].electableSpecs.instanceSize\&quot; : \&quot;M30\&quot;&#x60; or greater not including &#x60;Mxx_NVME&#x60; tiers.  The maximum input/output operations per second (IOPS) depend on the selected **.instanceSize** and **.diskSizeGB**. This parameter defaults to the cluster tier&#x27;s standard IOPS value. Changing this value impacts cluster cost. MongoDB Cloud enforces minimum ratios of storage capacity to system memory for given cluster tiers. This keeps cluster performance consistent with large datasets.  - Instance sizes &#x60;M10&#x60; to &#x60;M40&#x60; have a ratio of disk capacity to system memory of 60:1. - Instance sizes greater than &#x60;M40&#x60; have a ratio of 120:1. | [optional] value must be a 32 bit integer
**ebsVolumeType** | str,  | str,  | Type of storage you want to attach to your AWS-provisioned cluster.  - &#x60;STANDARD&#x60; volume types can&#x27;t exceed the default input/output operations per second (IOPS) rate for the selected volume size.   - &#x60;PROVISIONED&#x60; volume types must fall within the allowable IOPS range for the selected volume size. | [optional] must be one of ["STANDARD", "PROVISIONED", ] if omitted the server will use the default value of "STANDARD"
**instanceSize** | str,  | str,  | Hardware specification for the instance sizes in this region. Each instance size has a default storage and memory capacity. The instance size you select applies to all the data-bearing hosts in your instance size. | [optional] must be one of ["M10", "M20", "M30", "M40", "M50", "M60", "M80", "M140", "M200", "M250", "M300", "M400", "R40", "R50", "R60", "R80", "R200", "R300", "R400", "R600", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

