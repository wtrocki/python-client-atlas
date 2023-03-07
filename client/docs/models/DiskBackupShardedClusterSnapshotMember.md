# atlas.model.disk_backup_sharded_cluster_snapshot_member.DiskBackupShardedClusterSnapshotMember

List that includes the snapshots and the cloud provider that stores the snapshots. The resource returns this parameter when `\"type\" : \"SHARDED_CLUSTER\"`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | List that includes the snapshots and the cloud provider that stores the snapshots. The resource returns this parameter when &#x60;\&quot;type\&quot; : \&quot;SHARDED_CLUSTER\&quot;&#x60;. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**replicaSetName** | str,  | str,  | Human-readable label that identifies the shard or config host from which MongoDB Cloud took this snapshot. | 
**cloudProvider** | str,  | str,  | Human-readable label that identifies the cloud provider that stores this snapshot. The resource returns this parameter when &#x60;\&quot;type\&quot;: \&quot;replicaSet\&quot;&#x60;. | must be one of ["AWS", "AZURE", "GCP", ] 
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the snapshot. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

