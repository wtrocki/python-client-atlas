# atlas.model.snapshot_schedule.SnapshotSchedule

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**pointInTimeWindowHours** | decimal.Decimal, int,  | decimal.Decimal,  | Number of hours before the current time from which MongoDB Cloud can create a Continuous Cloud Backup snapshot. | value must be a 32 bit integer
**snapshotRetentionDays** | decimal.Decimal, int,  | decimal.Decimal,  | Number of days that MongoDB Cloud must keep recent snapshots. | must be one of [2, 3, 4, 5, ] value must be a 32 bit integer
**dailySnapshotRetentionDays** | decimal.Decimal, int,  | decimal.Decimal,  | Quantity of time to keep daily snapshots. MongoDB Cloud expresses this value in days. Set this value to &#x60;0&#x60; to disable daily snapshot retention. | must be one of [0, 3, 4, 5, 6, 7, 15, 30, 60, 90, 120, 180, 360, ] value must be a 32 bit integer
**clusterCheckpointIntervalMin** | decimal.Decimal, int,  | decimal.Decimal,  | Quantity of time expressed in minutes between successive cluster checkpoints. This parameter applies only to sharded clusters. This number determines the granularity of continuous cloud backups for sharded clusters. | must be one of [15, 30, 60, ] value must be a 32 bit integer
**groupId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the project that contains the cluster. | 
**monthlySnapshotRetentionMonths** | decimal.Decimal, int,  | decimal.Decimal,  | Number of months that MongoDB Cloud must keep monthly snapshots. Set this value to &#x60;0&#x60; to disable monthly snapshot retention. | must be one of [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 18, 24, 36, ] value must be a 32 bit integer
**clusterId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the cluster with the snapshot you want to return. | 
**snapshotIntervalHours** | decimal.Decimal, int,  | decimal.Decimal,  | Number of hours that must elapse before taking another snapshot. | must be one of [6, 8, 12, 24, ] value must be a 32 bit integer
**weeklySnapshotRetentionWeeks** | decimal.Decimal, int,  | decimal.Decimal,  | Number of weeks that MongoDB Cloud must keep weekly snapshots. Set this value to &#x60;0&#x60; to disable weekly snapshot retention. | must be one of [0, 1, 2, 3, 4, 5, 6, 7, 8, 12, 16, 20, 24, 52, ] value must be a 32 bit integer
**[links](#links)** | list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | [optional] 
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

