# atlas.model.disk_backup_export_job.DiskBackupExportJob

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**exportBucketId** | str,  | str,  | Unique 24-hexadecimal character string that identifies the AWS bucket to which MongoDB Cloud exports the Cloud Backup snapshot. | 
**[components](#components)** | list, tuple,  | tuple,  | Information on the export job for each replica set in the sharded cluster. | [optional] 
**createdAt** | str, datetime,  | str,  | Date and time when someone created this export job. MongoDB Cloud represents this timestamp in ISO 8601 format in UTC. | [optional] value must conform to RFC-3339 date-time
**[customData](#customData)** | list, tuple,  | tuple,  | Collection of key-value pairs that represent custom data for the metadata file that MongoDB Cloud uploads to the bucket when the export job finishes. | [optional] 
**[deliveryUrl](#deliveryUrl)** | list, tuple,  | tuple,  | One or more Uniform Resource Locators (URLs) that point to the compressed snapshot files for manual download. MongoDB Cloud returns this parameter when &#x60;\&quot;deliveryType\&quot; : \&quot;download\&quot;&#x60;. | [optional] 
**exportStatus** | [**ApiExportStatusView**](ApiExportStatusView.md) | [**ApiExportStatusView**](ApiExportStatusView.md) |  | [optional] 
**finishedAt** | str, datetime,  | str,  | Date and time when this export job completed. MongoDB Cloud represents this timestamp in ISO 8601 format in UTC. | [optional] value must conform to RFC-3339 date-time
**id** | str,  | str,  | Unique 24-hexadecimal character string that identifies the restore job. | [optional] 
**[links](#links)** | list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | [optional] 
**prefix** | str,  | str,  | Full path on the cloud provider bucket to the folder where the snapshot is exported. | [optional] 
**snapshotId** | str,  | str,  | Unique 24-hexadecimal character string that identifies the snapshot. | [optional] 
**state** | str,  | str,  | State of the export job. | [optional] must be one of ["Cancelled", "Failed", "InProgress", "Queued", "Successful", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# components

Information on the export job for each replica set in the sharded cluster.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Information on the export job for each replica set in the sharded cluster. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DiskBackupBaseRestoreMember**](DiskBackupBaseRestoreMember.md) | [**DiskBackupBaseRestoreMember**](DiskBackupBaseRestoreMember.md) | [**DiskBackupBaseRestoreMember**](DiskBackupBaseRestoreMember.md) |  | 

# customData

Collection of key-value pairs that represent custom data for the metadata file that MongoDB Cloud uploads to the bucket when the export job finishes.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Collection of key-value pairs that represent custom data for the metadata file that MongoDB Cloud uploads to the bucket when the export job finishes. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Label**](Label.md) | [**Label**](Label.md) | [**Label**](Label.md) |  | 

# deliveryUrl

One or more Uniform Resource Locators (URLs) that point to the compressed snapshot files for manual download. MongoDB Cloud returns this parameter when `\"deliveryType\" : \"download\"`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | One or more Uniform Resource Locators (URLs) that point to the compressed snapshot files for manual download. MongoDB Cloud returns this parameter when &#x60;\&quot;deliveryType\&quot; : \&quot;download\&quot;&#x60;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | One Uniform Resource Locator that point to the compressed snapshot files for manual download. | 

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

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

