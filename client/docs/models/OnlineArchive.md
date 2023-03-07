# atlas.model.online_archive.OnlineArchive

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**criteria** | [**CriteriaView**](CriteriaView.md) | [**CriteriaView**](CriteriaView.md) |  | 
**_id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the online archive. | [optional] 
**clusterName** | str,  | str,  | Human-readable label that identifies the cluster that contains the collection for which you want to create an online archive. | [optional] 
**collName** | str,  | str,  | Human-readable label that identifies the collection for which you created the online archive. | [optional] 
**collectionType** | str,  | str,  | Classification of MongoDB database collection that you want to return.  If you set this parameter to &#x60;TIMESERIES&#x60;, set &#x60;\&quot;criteria.type\&quot; : \&quot;date\&quot;&#x60; and &#x60;\&quot;criteria.dateFormat\&quot; : \&quot;ISODATE\&quot;&#x60;. | [optional] must be one of ["TIMESERIES", "STANDARD", ] if omitted the server will use the default value of "STANDARD"
**dbName** | str,  | str,  | Human-readable label of the database that contains the collection that contains the online archive. | [optional] 
**groupId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the project that contains the specified cluster. The specified cluster contains the collection for which to create the online archive. | [optional] 
**[partitionFields](#partitionFields)** | list, tuple,  | tuple,  | List that contains document parameters to use to logically divide data within a collection. Partitions provide a coarse level of filtering of the underlying collection data. To divide your data, specify up to two parameters that you frequently query. Any queries that don&#x27;t use these parameters result in a full collection scan of all archived documents. This takes more time and increase your costs. | [optional] 
**schedule** | [**OnlineArchiveSchedule**](OnlineArchiveSchedule.md) | [**OnlineArchiveSchedule**](OnlineArchiveSchedule.md) |  | [optional] 
**state** | str,  | str,  | Phase of the process to create this online archive when you made this request.  | State       | Indication | |-------------|------------| | &#x60;PENDING&#x60;   | MongoDB Cloud has queued documents for archive. Archiving hasn&#x27;t started. | | &#x60;ARCHIVING&#x60; | MongoDB Cloud started archiving documents that meet the archival criteria. | | &#x60;IDLE&#x60;      | MongoDB Cloud waits to start the next archival job. | | &#x60;PAUSING&#x60;   | Someone chose to stop archiving. MongoDB Cloud finishes the running archival job then changes the state to &#x60;PAUSED&#x60; when that job completes. | | &#x60;PAUSED&#x60;    | MongoDB Cloud has stopped archiving. Archived documents can be queried. The specified archiving operation on the active cluster cannot archive additional documents. You can resume archiving for paused archives at any time. | | &#x60;ORPHANED&#x60;  | Someone has deleted the collection associated with an active or paused archive. MongoDB Cloud doesn&#x27;t delete the archived data. You must manually delete the online archives associated with the deleted collection. | | &#x60;DELETED&#x60;   | Someone has deleted the archive was deleted. When someone deletes an online archive, MongoDB Cloud removes all associated archived documents from the cloud object storage. | | [optional] must be one of ["PENDING", "ACTIVE", "PAUSING", "PAUSED", "DELETED", "ORPHANED", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# partitionFields

List that contains document parameters to use to logically divide data within a collection. Partitions provide a coarse level of filtering of the underlying collection data. To divide your data, specify up to two parameters that you frequently query. Any queries that don't use these parameters result in a full collection scan of all archived documents. This takes more time and increase your costs.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains document parameters to use to logically divide data within a collection. Partitions provide a coarse level of filtering of the underlying collection data. To divide your data, specify up to two parameters that you frequently query. Any queries that don&#x27;t use these parameters result in a full collection scan of all archived documents. This takes more time and increase your costs. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PartitionFieldView**](PartitionFieldView.md) | [**PartitionFieldView**](PartitionFieldView.md) | [**PartitionFieldView**](PartitionFieldView.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

