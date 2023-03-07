# atlas.model.serverless_backup_restore_job.ServerlessBackupRestoreJob

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**deliveryType** | str,  | str,  | Human-readable label that categorizes the restore job to create. | must be one of ["automated", "download", "pointInTime", ] 
**targetGroupId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the target project for the specified **targetClusterName**. | 
**targetClusterName** | str,  | str,  | Human-readable label that identifies the target cluster to which the restore job restores the snapshot. The resource returns this parameter when &#x60;\&quot;deliveryType\&quot;:&#x60; &#x60;\&quot;automated\&quot;&#x60;. | 
**cancelled** | bool,  | BoolClass,  | Flag that indicates whether someone canceled this restore job. | [optional] 
**[deliveryUrl](#deliveryUrl)** | list, tuple,  | tuple,  | One or more Uniform Resource Locators (URLs) that point to the compressed snapshot files for manual download. MongoDB Cloud returns this parameter when &#x60;\&quot;deliveryType\&quot; : \&quot;download\&quot;&#x60;. | [optional] 
**desiredTimestamp** | [**ApiBSONTimestampView**](ApiBSONTimestampView.md) | [**ApiBSONTimestampView**](ApiBSONTimestampView.md) |  | [optional] 
**expired** | bool,  | BoolClass,  | Flag that indicates whether the restore job expired. | [optional] 
**expiresAt** | str, datetime,  | str,  | Date and time when the restore job expires. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**failed** | bool,  | BoolClass,  | Flag that indicates whether the restore job failed. | [optional] 
**finishedAt** | str, datetime,  | str,  | Date and time when the restore job completed. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**id** | str,  | str,  | Unique 24-hexadecimal character string that identifies the restore job. | [optional] 
**[links](#links)** | list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | [optional] 
**oplogInc** | decimal.Decimal, int,  | decimal.Decimal,  | Oplog operation number from which you want to restore this snapshot. This number represents the second part of an Oplog timestamp. The resource returns this parameter when &#x60;\&quot;deliveryType\&quot; : \&quot;pointInTime\&quot;&#x60; and **oplogTs** exceeds &#x60;0&#x60;. | [optional] value must be a 32 bit integer
**oplogTs** | decimal.Decimal, int,  | decimal.Decimal,  | Date and time from which you want to restore this snapshot. This parameter expresses this timestamp in the number of seconds that have elapsed since the UNIX epoch. This number represents the first part of an Oplog timestamp. The resource returns this parameter when &#x60;\&quot;deliveryType\&quot; : \&quot;pointInTime\&quot;&#x60; and **oplogTs** exceeds &#x60;0&#x60;. | [optional] value must be a 32 bit integer
**pointInTimeUTCSeconds** | decimal.Decimal, int,  | decimal.Decimal,  | Date and time from which MongoDB Cloud restored this snapshot. This parameter expresses this timestamp in the number of seconds that have elapsed since the UNIX epoch. The resource returns this parameter when &#x60;\&quot;deliveryType\&quot; : \&quot;pointInTime\&quot;&#x60; and **pointInTimeUTCSeconds** exceeds &#x60;0&#x60;. | [optional] value must be a 32 bit integer
**snapshotId** | str,  | str,  | Unique 24-hexadecimal character string that identifies the snapshot. | [optional] 
**timestamp** | str, datetime,  | str,  | Date and time when MongoDB Cloud took the snapshot associated with **snapshotId**. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

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

