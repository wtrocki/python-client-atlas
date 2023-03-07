# atlas.model.live_migration_response_view.LiveMigrationResponseView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**_id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the migration job. | [optional] 
**lagTimeSeconds** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Replication lag between the source and destination clusters. Atlas returns this setting only during an active migration, before the cutover phase. | [optional] value must be a 64 bit integer
**[migrationHosts](#migrationHosts)** | list, tuple,  | tuple,  | List of hosts running MongoDB Agents. These Agents can transfer your MongoDB data between one source and one target cluster. | [optional] 
**readyForCutover** | bool,  | BoolClass,  | Flag that indicates the migrated cluster can be cut over to MongoDB Atlas. | [optional] 
**status** | str,  | str,  | Progress made in migrating one cluster to MongoDB Atlas.  | Status   | Explanation | |----------|-------------| | NEW      | Someone scheduled a local cluster migration to MongoDB Atlas. | | FAILED   | The cluster migration to MongoDB Atlas failed.                | | COMPLETE | The cluster migration to MongoDB Atlas succeeded.             | | EXPIRED  | MongoDB Atlas prepares to begin the cut over of the migrating cluster when source and target clusters have almost synchronized. If &#x60;\&quot;readyForCutover\&quot; : true&#x60;, this synchronization starts a timer of 120 hours. You can extend this timer. If the timer expires, MongoDB Atlas returns this status. | | WORKING  | The cluster migration to MongoDB Atlas is performing one of the following tasks:&lt;ul&gt;&lt;li&gt;Preparing connections to source and target clusters&lt;/li&gt;&lt;li&gt;Replicating data from source to target&lt;/li&gt;&lt;li&gt;Verifying MongoDB Atlas connection settings&lt;/li&gt;&lt;li&gt;Stopping replication after the cut over&lt;/li&gt;&lt;/ul&gt; |  | [optional] must be one of ["NEW", "WORKING", "FAILED", "COMPLETE", "EXPIRED", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# migrationHosts

List of hosts running MongoDB Agents. These Agents can transfer your MongoDB data between one source and one target cluster.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of hosts running MongoDB Agents. These Agents can transfer your MongoDB data between one source and one target cluster. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | One host running a MongoDB Agent. This Agent can transfer your MongoDB data between one source and one target cluster. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

