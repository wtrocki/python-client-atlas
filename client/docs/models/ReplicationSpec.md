# atlas.model.replication_spec.ReplicationSpec

Details that explain how MongoDB Cloud replicates data on the specified MongoDB database.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Details that explain how MongoDB Cloud replicates data on the specified MongoDB database. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the replication object for a zone in a Multi-Cloud Cluster. If you include existing zones in the request, you must specify this parameter. If you add a new zone to an existing Multi-Cloud Cluster, you may specify this parameter. The request deletes any existing zones in the Multi-Cloud Cluster that you exclude from the request. | [optional] 
**numShards** | decimal.Decimal, int,  | decimal.Decimal,  | Positive integer that specifies the number of shards to deploy in each specified zone. If you set this value to &#x60;1&#x60; and **clusterType** is &#x60;SHARDED&#x60;, MongoDB Cloud deploys a single-shard sharded cluster. Don&#x27;t create a sharded cluster with a single shard for production environments. Single-shard sharded clusters don&#x27;t provide the same benefits as multi-shard configurations. | [optional] value must be a 32 bit integer
**[regionConfigs](#regionConfigs)** | list, tuple,  | tuple,  | Hardware specifications for nodes set for a given region. Each **regionConfigs** object describes the region&#x27;s priority in elections and the number and type of MongoDB nodes that MongoDB Cloud deploys to the region. Each **regionConfigs** object must have either an **analyticsSpecs** object, **electableSpecs** object, or **readOnlySpecs** object. Tenant clusters only require **electableSpecs. Dedicated** clusters can specify any of these specifications, but must have at least one **electableSpecs** object within a **replicationSpec**. Every hardware specification must use the same **instanceSize**.  **Example:**  If you set &#x60;\&quot;replicationSpecs[n].regionConfigs[m].analyticsSpecs.instanceSize\&quot; : \&quot;M30\&quot;&#x60;, set &#x60;\&quot;replicationSpecs[n].regionConfigs[m].electableSpecs.instanceSize\&quot; : &#x60;\&quot;M30\&quot;&#x60; if you have electable nodes and &#x60;\&quot;replicationSpecs[n].regionConfigs[m].readOnlySpecs.instanceSize\&quot; : &#x60;\&quot;M30\&quot;&#x60; if you have read-only nodes. | [optional] 
**zoneName** | str,  | str,  | Human-readable label that identifies the zone in a Global Cluster. Provide this value only if &#x60;\&quot;clusterType\&quot; : \&quot;GEOSHARDED\&quot;&#x60;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# regionConfigs

Hardware specifications for nodes set for a given region. Each **regionConfigs** object describes the region's priority in elections and the number and type of MongoDB nodes that MongoDB Cloud deploys to the region. Each **regionConfigs** object must have either an **analyticsSpecs** object, **electableSpecs** object, or **readOnlySpecs** object. Tenant clusters only require **electableSpecs. Dedicated** clusters can specify any of these specifications, but must have at least one **electableSpecs** object within a **replicationSpec**. Every hardware specification must use the same **instanceSize**.  **Example:**  If you set `\"replicationSpecs[n].regionConfigs[m].analyticsSpecs.instanceSize\" : \"M30\"`, set `\"replicationSpecs[n].regionConfigs[m].electableSpecs.instanceSize\" : `\"M30\"` if you have electable nodes and `\"replicationSpecs[n].regionConfigs[m].readOnlySpecs.instanceSize\" : `\"M30\"` if you have read-only nodes.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Hardware specifications for nodes set for a given region. Each **regionConfigs** object describes the region&#x27;s priority in elections and the number and type of MongoDB nodes that MongoDB Cloud deploys to the region. Each **regionConfigs** object must have either an **analyticsSpecs** object, **electableSpecs** object, or **readOnlySpecs** object. Tenant clusters only require **electableSpecs. Dedicated** clusters can specify any of these specifications, but must have at least one **electableSpecs** object within a **replicationSpec**. Every hardware specification must use the same **instanceSize**.  **Example:**  If you set &#x60;\&quot;replicationSpecs[n].regionConfigs[m].analyticsSpecs.instanceSize\&quot; : \&quot;M30\&quot;&#x60;, set &#x60;\&quot;replicationSpecs[n].regionConfigs[m].electableSpecs.instanceSize\&quot; : &#x60;\&quot;M30\&quot;&#x60; if you have electable nodes and &#x60;\&quot;replicationSpecs[n].regionConfigs[m].readOnlySpecs.instanceSize\&quot; : &#x60;\&quot;M30\&quot;&#x60; if you have read-only nodes. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RegionConfig**](RegionConfig.md) | [**RegionConfig**](RegionConfig.md) | [**RegionConfig**](RegionConfig.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

