# atlas.model.region_spec.RegionSpec

Physical location where MongoDB Cloud provisions cluster nodes.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Physical location where MongoDB Cloud provisions cluster nodes. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**analyticsNodes** | decimal.Decimal, int,  | decimal.Decimal,  | Number of analytics nodes in the region. Analytics nodes handle analytic data such as reporting queries from MongoDB Connector for Business Intelligence on MongoDB Cloud. Analytics nodes are read-only, and can never become the primary. Use **replicationSpecs[n].{region}.analyticsNodes** instead. | [optional] value must be a 32 bit integer
**electableNodes** | decimal.Decimal, int,  | decimal.Decimal,  | Number of electable nodes to deploy in the specified region. Electable nodes can become the primary and can facilitate local reads. Use **replicationSpecs[n].{region}.electableNodes** instead. | [optional] must be one of [0, 3, 5, 7, ] value must be a 32 bit integer
**priority** | decimal.Decimal, int,  | decimal.Decimal,  | Number that indicates the election priority of the region. To identify the Preferred Region of the cluster, set this parameter to &#x60;7&#x60;. The primary node runs in the **Preferred Region**. To identify a read-only region, set this parameter to &#x60;0&#x60;. | [optional] value must be a 32 bit integer
**readOnlyNodes** | decimal.Decimal, int,  | decimal.Decimal,  | Number of read-only nodes in the region. Read-only nodes can never become the primary member, but can facilitate local reads. Use **replicationSpecs[n].{region}.readOnlyNodes** instead. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

