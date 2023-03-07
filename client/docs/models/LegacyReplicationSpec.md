# atlas.model.legacy_replication_spec.LegacyReplicationSpec

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the replication object for a zone in a Global Cluster.  - If you include existing zones in the request, you must specify this parameter.  - If you add a new zone to an existing Global Cluster, you may specify this parameter. The request deletes any existing zones in a Global Cluster that you exclude from the request. | [optional] 
**numShards** | decimal.Decimal, int,  | decimal.Decimal,  | Positive integer that specifies the number of shards to deploy in each specified zone If you set this value to &#x60;1&#x60; and **clusterType** is &#x60;SHARDED&#x60;, MongoDB Cloud deploys a single-shard sharded cluster. Don&#x27;t create a sharded cluster with a single shard for production environments. Single-shard sharded clusters don&#x27;t provide the same benefits as multi-shard configurations. | [optional] if omitted the server will use the default value of 1value must be a 32 bit integer
**[regionsConfig](#regionsConfig)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Physical location where MongoDB Cloud provisions cluster nodes. | [optional] 
**zoneName** | str,  | str,  | Human-readable label that identifies the zone in a Global Cluster. Provide this value only if **clusterType** is &#x60;GEOSHARDED&#x60;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# regionsConfig

Physical location where MongoDB Cloud provisions cluster nodes.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Physical location where MongoDB Cloud provisions cluster nodes. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**RegionSpec**](RegionSpec.md) | [**RegionSpec**](RegionSpec.md) | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

