# atlas.model.api_snapshot_view.ApiSnapshotView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**clusterId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the cluster with the snapshots you want to return. | [optional] 
**complete** | bool,  | BoolClass,  | Flag that indicates whether the snapshot exists. This flag returns &#x60;false&#x60; while MongoDB Cloud creates the snapshot. | [optional] 
**created** | [**ApiBSONTimestampView**](ApiBSONTimestampView.md) | [**ApiBSONTimestampView**](ApiBSONTimestampView.md) |  | [optional] 
**doNotDelete** | bool,  | BoolClass,  | Flag that indicates whether someone can delete this snapshot. You can&#x27;t set &#x60;\&quot;doNotDelete\&quot; : true&#x60; and set a timestamp for **expires** in the same request. | [optional] 
**expires** | str, datetime,  | str,  | Date and time when MongoDB Cloud deletes the snapshot. If &#x60;\&quot;doNotDelete\&quot; : true&#x60;, MongoDB Cloud removes any value set for this parameter. | [optional] value must conform to RFC-3339 date-time
**groupId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the project that owns the snapshots. | [optional] 
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the snapshot. | [optional] 
**lastOplogAppliedTimestamp** | [**ApiBSONTimestampView**](ApiBSONTimestampView.md) | [**ApiBSONTimestampView**](ApiBSONTimestampView.md) |  | [optional] 
**[links](#links)** | list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | [optional] 
**[parts](#parts)** | list, tuple,  | tuple,  | Metadata that describes the complete snapshot.  - For a replica set, this array contains a single document. - For a sharded cluster, this array contains one document for each shard plus one document for the config host. | [optional] 
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

# parts

Metadata that describes the complete snapshot.  - For a replica set, this array contains a single document. - For a sharded cluster, this array contains one document for each shard plus one document for the config host.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Metadata that describes the complete snapshot.  - For a replica set, this array contains a single document. - For a sharded cluster, this array contains one document for each shard plus one document for the config host. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiSnapshotPartView**](ApiSnapshotPartView.md) | [**ApiSnapshotPartView**](ApiSnapshotPartView.md) | [**ApiSnapshotPartView**](ApiSnapshotPartView.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

