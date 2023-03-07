# atlas.model.api_restore_job_view.ApiRestoreJobView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**delivery** | [**ApiRestoreJobDeliveryView**](ApiRestoreJobDeliveryView.md) | [**ApiRestoreJobDeliveryView**](ApiRestoreJobDeliveryView.md) |  | 
**batchId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the batch to which this restore job belongs. This parameter exists only for a sharded cluster restore. | [optional] 
**checkpointId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the sharded cluster checkpoint. The checkpoint represents the point in time back to which you want to restore you data. This parameter applies when &#x60;\&quot;delivery.methodName\&quot; : \&quot;AUTOMATED_RESTORE\&quot;&#x60;. Use this parameter with sharded clusters only.  - If you set **checkpointId**, you can&#x27;t set **oplogInc**, **oplogTs**, **snapshotId**, or **pointInTimeUTCMillis**. - If you provide this parameter, this endpoint restores all data up to this checkpoint to the database you specify in the **delivery** object. | [optional] 
**clusterId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the cluster with the snapshot you want to return. This parameter returns for restore clusters. | [optional] 
**clusterName** | str,  | str,  | Human-readable label that identifies the cluster containing the snapshots you want to retrieve. | [optional] 
**created** | str, datetime,  | str,  | Date and time when someone requested this restore job. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**encryptionEnabled** | bool,  | BoolClass,  | Flag that indicates whether someone encrypted the data in the restored snapshot. | [optional] 
**groupId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the project that owns the snapshots. | [optional] 
**[hashes](#hashes)** | list, tuple,  | tuple,  | List that contains documents mapping each restore file to a hashed checksum. This parameter applies after you download the corresponding **delivery.url**. If &#x60;\&quot;methodName\&quot; : \&quot;HTTP\&quot;&#x60;, this list contains one object that represents the hash of the **.tar.gz** file. | [optional] 
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the restore job. | [optional] 
**[links](#links)** | list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | [optional] 
**masterKeyUUID** | str, uuid.UUID,  | str,  | Universally Unique Identifier (UUID) that identifies the Key Management Interoperability (KMIP) master key used to encrypt the snapshot data. This parameter applies only when &#x60;\&quot;encryptionEnabled\&quot; : \&quot;true\&quot;&#x60;. | [optional] value must be a uuid
**oplogInc** | decimal.Decimal, int,  | decimal.Decimal,  | Thirty-two-bit incrementing ordinal that represents operations within a given second. When paired with **oplogTs**, this represents the point in time to which MongoDB Cloud restores your data. This parameter applies when &#x60;\&quot;delivery.methodName\&quot; : \&quot;AUTOMATED_RESTORE\&quot;&#x60;.  - If you set **oplogInc**, you must set **oplogTs**, and can&#x27;t set **checkpointId**, **snapshotId**, or **pointInTimeUTCMillis**. - If you provide this parameter, this endpoint restores all data up to and including this Oplog timestamp to the database you specified in the **delivery** object. | [optional] value must be a 32 bit integer
**oplogTs** | str,  | str,  | Date and time from which you want to restore this snapshot. This parameter expresses its value in ISO 8601 format in UTC. This represents the first part of an Oplog timestamp. When paired with **oplogInc**, they represent the last database operation to which you want to restore your data. This parameter applies when &#x60;\&quot;delivery.methodName\&quot; : \&quot;AUTOMATED_RESTORE\&quot;&#x60;. Run a query against **local.oplog.rs** on your replica set to find the desired timestamp.  - If you set **oplogTs**, you must set **oplogInc**, and you can&#x27;t set **checkpointId**, **snapshotId**, or **pointInTimeUTCMillis**. - If you provide this parameter, this endpoint restores all data up to and including this Oplog timestamp to the database you specified in the **delivery** object. | [optional] 
**pointInTimeUTCMillis** | decimal.Decimal, int,  | decimal.Decimal,  | Timestamp from which you want to restore this snapshot. This parameter expresses its value in the number of milliseconds elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time). This timestamp must fall within the last 24 hours of the current time. This parameter applies when &#x60;\&quot;delivery.methodName\&quot; : \&quot;AUTOMATED_RESTORE\&quot;&#x60;.  - If you provide this parameter, this endpoint restores all data up to this point in time to the database you specified in the **delivery** object. - If you set **pointInTimeUTCMillis**, you can&#x27;t set **oplogInc**, **oplogTs**, **snapshotId**, or **checkpointId**. | [optional] value must be a 64 bit integer
**snapshotId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the snapshot to restore. If you set **snapshotId**, you can&#x27;t set **oplogInc**, **oplogTs**, **pointInTimeUTCMillis**, or **checkpointId**. | [optional] 
**statusName** | str,  | str,  | Human-readable label that identifies the status of the downloadable file at the time of the request. | [optional] must be one of ["IN_PROGRESS", "BROKEN", "KILLED", "FINISHED", ] 
**timestamp** | [**ApiBSONTimestampView**](ApiBSONTimestampView.md) | [**ApiBSONTimestampView**](ApiBSONTimestampView.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# hashes

List that contains documents mapping each restore file to a hashed checksum. This parameter applies after you download the corresponding **delivery.url**. If `\"methodName\" : \"HTTP\"`, this list contains one object that represents the hash of the **.tar.gz** file.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains documents mapping each restore file to a hashed checksum. This parameter applies after you download the corresponding **delivery.url**. If &#x60;\&quot;methodName\&quot; : \&quot;HTTP\&quot;&#x60;, this list contains one object that represents the hash of the **.tar.gz** file. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiRestoreJobFileHashView**](ApiRestoreJobFileHashView.md) | [**ApiRestoreJobFileHashView**](ApiRestoreJobFileHashView.md) | [**ApiRestoreJobFileHashView**](ApiRestoreJobFileHashView.md) |  | 

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

