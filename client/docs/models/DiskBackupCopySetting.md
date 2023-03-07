# atlas.model.disk_backup_copy_setting.DiskBackupCopySetting

Copy setting item in the desired backup policy.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Copy setting item in the desired backup policy. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cloudProvider** | str,  | str,  | Human-readable label that identifies the cloud provider that stores the snapshot copy. | [optional] must be one of ["AWS", "AZURE", "GCP", ] 
**[frequencies](#frequencies)** | list, tuple,  | tuple,  | List that describes which types of snapshots to copy. | [optional] 
**regionName** | str,  | str,  | Target region to copy snapshots belonging to replicationSpecId to. Please supply the &#x27;Atlas Region&#x27; which can be found under [Cloud Providers](https://www.mongodb.com/docs/atlas/reference/cloud-providers/) &#x27;regions&#x27; link. | [optional] 
**replicationSpecId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the replication object for a zone in a cluster. For global clusters, there can be multiple zones to choose from. For sharded clusters and replica set clusters, there is only one zone in the cluster. To find the Replication Spec Id, do a GET request to Return One Cluster in One Project and consult the replicationSpecs array [Return One Cluster in One Project](#operation/getLegacyCluster). | [optional] 
**shouldCopyOplogs** | bool,  | BoolClass,  | Flag that indicates whether to copy the oplogs to the target region. You can use the oplogs to perform point-in-time restores. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# frequencies

List that describes which types of snapshots to copy.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that describes which types of snapshots to copy. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["HOURLY", "DAILY", "WEEKLY", "MONTHLY", "ON_DEMAND", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

