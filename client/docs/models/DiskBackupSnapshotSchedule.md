# atlas.model.disk_backup_snapshot_schedule.DiskBackupSnapshotSchedule

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**autoExportEnabled** | bool,  | BoolClass,  | Flag that indicates whether MongoDB Cloud automatically exports cloud backup snapshots to the AWS bucket. | [optional] 
**clusterId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the cluster with the snapshot you want to return. | [optional] 
**clusterName** | str,  | str,  | Human-readable label that identifies the cluster with the snapshot you want to return. | [optional] 
**[copySettings](#copySettings)** | list, tuple,  | tuple,  | List that contains a document for each copy setting item in the desired backup policy. | [optional] 
**[deleteCopiedBackups](#deleteCopiedBackups)** | list, tuple,  | tuple,  | List that contains a document for each deleted copy setting whose backup copies you want to delete. | [optional] 
**export** | [**AutoExportPolicyView**](AutoExportPolicyView.md) | [**AutoExportPolicyView**](AutoExportPolicyView.md) |  | [optional] 
**[links](#links)** | list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | [optional] 
**nextSnapshot** | str, datetime,  | str,  | Date and time when MongoDB Cloud takes the next snapshot. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**[policies](#policies)** | list, tuple,  | tuple,  | Rules set for this backup schedule. | [optional] 
**referenceHourOfDay** | decimal.Decimal, int,  | decimal.Decimal,  | Hour of day in Coordinated Universal Time (UTC) that represents when MongoDB Cloud takes the snapshot. | [optional] value must be a 32 bit integer
**referenceMinuteOfHour** | decimal.Decimal, int,  | decimal.Decimal,  | Minute of the **referenceHourOfDay** that represents when MongoDB Cloud takes the snapshot. | [optional] value must be a 32 bit integer
**restoreWindowDays** | decimal.Decimal, int,  | decimal.Decimal,  | Number of previous days that you can restore back to with Continuous Cloud Backup accuracy. You must specify a positive, non-zero integer. This parameter applies to continuous cloud backups only. | [optional] value must be a 32 bit integer
**updateSnapshots** | bool,  | BoolClass,  | Flag that indicates whether to apply the retention changes in the updated backup policy to snapshots that MongoDB Cloud took previously. | [optional] 
**useOrgAndGroupNamesInExportPrefix** | bool,  | BoolClass,  | Flag that indicates whether to use organization and project names instead of organization and project UUIDs in the path to the metadata files that MongoDB Cloud uploads to your AWS bucket. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# copySettings

List that contains a document for each copy setting item in the desired backup policy.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains a document for each copy setting item in the desired backup policy. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DiskBackupCopySetting**](DiskBackupCopySetting.md) | [**DiskBackupCopySetting**](DiskBackupCopySetting.md) | [**DiskBackupCopySetting**](DiskBackupCopySetting.md) |  | 

# deleteCopiedBackups

List that contains a document for each deleted copy setting whose backup copies you want to delete.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains a document for each deleted copy setting whose backup copies you want to delete. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiDeleteCopiedBackupsView**](ApiDeleteCopiedBackupsView.md) | [**ApiDeleteCopiedBackupsView**](ApiDeleteCopiedBackupsView.md) | [**ApiDeleteCopiedBackupsView**](ApiDeleteCopiedBackupsView.md) |  | 

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

# policies

Rules set for this backup schedule.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Rules set for this backup schedule. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiPolicyView**](ApiPolicyView.md) | [**ApiPolicyView**](ApiPolicyView.md) | [**ApiPolicyView**](ApiPolicyView.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

