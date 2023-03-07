# atlas.model.api_snapshot_part_view.ApiSnapshotPartView

Characteristics that identify this snapshot.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Characteristics that identify this snapshot. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**clusterId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the cluster with the snapshots you want to return. | [optional] 
**compressionSetting** | str,  | str,  | Human-readable label that identifies the method of compression for the snapshot. | [optional] must be one of ["NONE", "GZIP", ] 
**dataSizeBytes** | decimal.Decimal, int,  | decimal.Decimal,  | Total size of the data stored on each node in the cluster. This parameter expresses its value in bytes. | [optional] value must be a 64 bit integer
**encryptionEnabled** | bool,  | BoolClass,  | Flag that indicates whether someone encrypted this snapshot. | [optional] 
**fileSizeBytes** | decimal.Decimal, int,  | decimal.Decimal,  | Number that indicates the total size of the data files in bytes. | [optional] value must be a 64 bit integer
**masterKeyUUID** | str, uuid.UUID,  | str,  | Unique string that identifies the Key Management Interoperability (KMIP) master key used to encrypt the snapshot data. The resource returns this parameter when &#x60;\&quot;parts.encryptionEnabled\&quot; : true&#x60;. | [optional] value must be a uuid
**mongodVersion** | str,  | str,  | Number that indicates the version of MongoDB that the replica set primary ran when MongoDB Cloud created the snapshot. | [optional] 
**replicaSetName** | str,  | str,  | Human-readable label that identifies the replica set. | [optional] 
**storageSizeBytes** | decimal.Decimal, int,  | decimal.Decimal,  | Number that indicates the total size of space allocated for document storage. | [optional] value must be a 64 bit integer
**typeName** | str,  | str,  | Human-readable label that identifies the type of server from which MongoDB Cloud took this snapshot. | [optional] must be one of ["REPLICA_SET", "CONFIG_SERVER", "CONFIG_SERVER_REPLICA_SET", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

