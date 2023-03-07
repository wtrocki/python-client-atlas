# atlas.model.tenant_restore.TenantRestore

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**snapshotId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the snapshot to restore. | 
**targetDeploymentItemName** | str,  | str,  | Human-readable label that identifies the cluster on the target project to which you want to restore the snapshot. You can restore the snapshot to a cluster tier *M2* or greater. | 
**clusterName** | str,  | str,  | Human-readable label that identifies the source cluster. | [optional] 
**deliveryType** | str,  | str,  | Means by which this resource returns the snapshot to the requesting MongoDB Cloud user. | [optional] must be one of ["RESTORE", "DOWNLOAD", ] 
**expirationDate** | str, datetime,  | str,  | Date and time when the download link no longer works. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the restore job. | [optional] 
**[links](#links)** | list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | [optional] 
**projectId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the project from which the restore job originated. | [optional] 
**restoreFinishedDate** | str, datetime,  | str,  | Date and time when MongoDB Cloud completed writing this snapshot. MongoDB Cloud changes the status of the restore job to &#x60;CLOSED&#x60;. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**restoreScheduledDate** | str, datetime,  | str,  | Date and time when MongoDB Cloud will restore this snapshot. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**snapshotFinishedDate** | str, datetime,  | str,  | Date and time when MongoDB Cloud completed writing this snapshot. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**snapshotUrl** | str,  | str,  | Internet address from which you can download the compressed snapshot files. The resource returns this parameter when  &#x60;\&quot;deliveryType\&quot; : \&quot;DOWNLOAD\&quot;&#x60;. | [optional] 
**status** | str,  | str,  | Phase of the restore workflow for this job at the time this resource made this request. | [optional] must be one of ["PENDING", "QUEUED", "RUNNING", "FAILED", "COMPLETED", ] 
**targetProjectId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the project that contains the cluster to which you want to restore the snapshot. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

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

