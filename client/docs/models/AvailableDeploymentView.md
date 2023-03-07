# atlas.model.available_deployment_view.AvailableDeploymentView

Deployments that can be migrated to MongoDB Atlas.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Deployments that can be migrated to MongoDB Atlas. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**featureCompatibilityVersion** | str,  | str,  | Version of MongoDB [features](https://docs.mongodb.com/manual/reference/command/setFeatureCompatibilityVersion) that this cluster supports. | 
**tlsEnabled** | bool,  | BoolClass,  | Flag that indicates whether someone enabled TLS for this cluster. | 
**managed** | bool,  | BoolClass,  | Flag that indicates whether Automation manages this cluster. | 
**name** | str,  | str,  | Human-readable label that identifies this cluster. | 
**sharded** | bool,  | BoolClass,  | Flag that indicates whether someone configured this cluster as a sharded cluster.  - If &#x60;true&#x60;, this cluster serves as a sharded cluster. - If &#x60;false&#x60;, this cluster serves as a replica set. | 
**mongoDBVersion** | str,  | str,  | Version of MongoDB that this cluster runs. | 
**agentVersion** | str,  | str,  | Version of MongoDB Agent that monitors/manages the cluster. | [optional] 
**clusterId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the cluster. | [optional] 
**dbSizeBytes** | decimal.Decimal, int,  | decimal.Decimal,  | Size of this database on disk at the time of the request expressed in bytes. | [optional] value must be a 64 bit integer
**oplogSizeMB** | decimal.Decimal, int,  | decimal.Decimal,  | Size of the Oplog on disk at the time of the request expressed in MB. | [optional] value must be a 32 bit integer
**shardsSize** | decimal.Decimal, int,  | decimal.Decimal,  | Number of shards that comprise this cluster. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

