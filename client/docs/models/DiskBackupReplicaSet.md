# atlas.model.disk_backup_replica_set.DiskBackupReplicaSet

Details of the replica set snapshot that MongoDB Cloud created.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Details of the replica set snapshot that MongoDB Cloud created. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cloudProvider** | str,  | str,  | Human-readable label that identifies the cloud provider that stores this snapshot. The resource returns this parameter when &#x60;\&quot;type\&quot;: \&quot;replicaSet\&quot;&#x60;. | [optional] must be one of ["AWS", "AZURE", "GCP", ] 
**[copyRegions](#copyRegions)** | list, tuple,  | tuple,  | List that identifies the regions to which MongoDB Cloud copies the snapshot. | [optional] 
**createdAt** | str, datetime,  | str,  | Date and time when MongoDB Cloud took the snapshot. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**description** | str,  | str,  | Human-readable phrase or sentence that explains the purpose of the snapshot. The resource returns this parameter when &#x60;\&quot;status\&quot;: \&quot;onDemand\&quot;&#x60;. | [optional] 
**expiresAt** | str, datetime,  | str,  | Date and time when MongoDB Cloud deletes the snapshot. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**frequencyType** | str,  | str,  | Human-readable label that identifies how often this snapshot triggers. | [optional] must be one of ["hourly", "daily", "weekly", "monthly", ] 
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the snapshot. | [optional] 
**[links](#links)** | list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | [optional] 
**masterKeyUUID** | str, uuid.UUID,  | str,  | Unique string that identifies the Amazon Web Services (AWS) Key Management Service (KMS) Customer Master Key (CMK) used to encrypt the snapshot. The resource returns this value when &#x60;\&quot;encryptionEnabled\&quot; : true&#x60;. | [optional] value must be a uuid
**mongodVersion** | str,  | str,  | Version of the MongoDB host that this snapshot backs up. | [optional] 
**[policyItems](#policyItems)** | list, tuple,  | tuple,  | List that contains unique identifiers for the policy items. | [optional] 
**replicaSetName** | str,  | str,  | Human-readable label that identifies the replica set from which MongoDB Cloud took this snapshot. The resource returns this parameter when &#x60;\&quot;type\&quot;: \&quot;replicaSet\&quot;&#x60;. | [optional] 
**snapshotType** | str,  | str,  | Human-readable label that identifies when this snapshot triggers. | [optional] must be one of ["onDemand", "scheduled", ] 
**status** | str,  | str,  | Human-readable label that indicates the stage of the backup process for this snapshot. | [optional] must be one of ["queued", "inProgress", "completed", "failed", ] 
**storageSizeBytes** | decimal.Decimal, int,  | decimal.Decimal,  | Number of bytes taken to store the backup snapshot. | [optional] value must be a 64 bit integer
**type** | str,  | str,  | Human-readable label that categorizes the cluster as a replica set or sharded cluster. | [optional] must be one of ["REPLICA_SET", "SHARDED_CLUSTER", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# copyRegions

List that identifies the regions to which MongoDB Cloud copies the snapshot.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that identifies the regions to which MongoDB Cloud copies the snapshot. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | List that identifies the regions to which MongoDB Cloud copies the snapshot. | 

# links

List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Link**](Link.md) | [**Link**](Link.md) | [**Link**](Link.md) |  | 

# policyItems

List that contains unique identifiers for the policy items.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains unique identifiers for the policy items. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Unique 24-hexadecimal digit string that identifies one policy item. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

