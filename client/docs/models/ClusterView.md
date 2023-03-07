# atlas.model.cluster_view.ClusterView

Settings that describe the clusters in each project that the API key is authorized to view.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Settings that describe the clusters in each project that the API key is authorized to view. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**alertCount** | decimal.Decimal, int,  | decimal.Decimal,  | Whole number that indicates the quantity of alerts open on the cluster. | [optional] value must be a 32 bit integer
**authEnabled** | bool,  | BoolClass,  | Flag that indicates whether authentication is required to access the nodes in this cluster. | [optional] 
**availability** | str,  | str,  | Term that expresses how many nodes of the cluster can be accessed when MongoDB Cloud receives this request. This parameter returns &#x60;available&#x60; when all nodes are accessible, &#x60;warning&#x60; only when some nodes in the cluster can be accessed, &#x60;unavailable&#x60; when the cluster can&#x27;t be accessed, or &#x60;dead&#x60; when the cluster has been deactivated. | [optional] must be one of ["available", "dead", "unavailable", "warning", ] 
**backupEnabled** | bool,  | BoolClass,  | Flag that indicates whether the cluster can perform backups. If set to &#x60;true&#x60;, the cluster can perform backups. You must set this value to &#x60;true&#x60; for NVMe clusters. Backup uses Cloud Backups for dedicated clusters and Shared Cluster Backups for tenant clusters. If set to &#x60;false&#x60;, the cluster doesn&#x27;t use MongoDB Cloud backups. | [optional] 
**clusterId** | str,  | str,  | Unique 24-hexadecimal character string that identifies the cluster. | [optional] 
**dataSizeBytes** | decimal.Decimal, int,  | decimal.Decimal,  | Total size of the data stored on each node in the cluster. The resource expresses this value in bytes. | [optional] value must be a 64 bit integer
**name** | str,  | str,  | Human-readable label that identifies the cluster. | [optional] 
**nodeCount** | decimal.Decimal, int,  | decimal.Decimal,  | Whole number that indicates the quantity of nodes that comprise the cluster. | [optional] value must be a 32 bit integer
**sslEnabled** | bool,  | BoolClass,  | Flag that indicates whether TLS authentication is required to access the nodes in this cluster. | [optional] 
**type** | str,  | str,  | Human-readable label that indicates the cluster type. | [optional] must be one of ["REPLICA_SET", "SHARDED_CLUSTER", ] 
**[versions](#versions)** | list, tuple,  | tuple,  | List that contains the versions of MongoDB that each node in the cluster runs. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# versions

List that contains the versions of MongoDB that each node in the cluster runs.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains the versions of MongoDB that each node in the cluster runs. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

