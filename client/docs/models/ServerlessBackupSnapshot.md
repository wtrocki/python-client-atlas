# atlas.model.serverless_backup_snapshot.ServerlessBackupSnapshot

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**createdAt** | str, datetime,  | str,  | Date and time when MongoDB Cloud took the snapshot. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**expiresAt** | str, datetime,  | str,  | Date and time when MongoDB Cloud deletes the snapshot. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**frequencyType** | str,  | str,  | Human-readable label that identifies how often this snapshot triggers. | [optional] must be one of ["hourly", "daily", "weekly", "monthly", ] 
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the snapshot. | [optional] 
**[links](#links)** | list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | [optional] 
**mongodVersion** | str,  | str,  | Version of the MongoDB host that this snapshot backs up. | [optional] 
**serverlessInstanceName** | str,  | str,  | Human-readable label given to the serverless instance from which MongoDB Cloud took this snapshot. | [optional] 
**snapshotType** | str,  | str,  | Human-readable label that identifies when this snapshot triggers. | [optional] must be one of ["onDemand", "scheduled", ] 
**status** | str,  | str,  | Human-readable label that indicates the stage of the backup process for this snapshot. | [optional] must be one of ["queued", "inProgress", "completed", "failed", ] 
**storageSizeBytes** | decimal.Decimal, int,  | decimal.Decimal,  | Number of bytes taken to store the backup snapshot. | [optional] value must be a 64 bit integer
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

