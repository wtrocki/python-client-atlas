# atlas.model.db_action.DBAction

Privilege action that the role grants.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Privilege action that the role grants. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**action** | str,  | str,  | Human-readable label that identifies the privilege action. | must be one of ["FIND", "INSERT", "REMOVE", "UPDATE", "BYPASS_DOCUMENT_VALIDATION", "USE_UUID", "KILL_OP", "CREATE_COLLECTION", "CREATE_INDEX", "DROP_COLLECTION", "ENABLE_PROFILER", "CHANGE_STREAM", "COLL_MOD", "COMPACT", "CONVERT_TO_CAPPED", "DROP_DATABASE", "DROP_INDEX", "RE_INDEX", "RENAME_COLLECTION_SAME_DB", "SET_USER_WRITE_BLOCK", "BYPASS_USER_WRITE_BLOCK", "LIST_SESSIONS", "KILL_ANY_SESSION", "COLL_STATS", "CONN_POOL_STATS", "DB_HASH", "DB_STATS", "GET_CMD_LINE_OPTS", "GET_LOG", "GET_PARAMETER", "GET_SHARD_MAP", "HOST_INFO", "IN_PROG", "LIST_DATABASES", "LIST_COLLECTIONS", "LIST_INDEXES", "LIST_SHARDS", "NET_STAT", "REPL_SET_GET_CONFIG", "REPL_SET_GET_STATUS", "SERVER_STATUS", "VALIDATE", "SHARDING_STATE", "TOP", "SQL_GET_SCHEMA", "SQL_SET_SCHEMA", "VIEW_ALL_HISTORY", "OUT_TO_S3", "STORAGE_GET_CONFIG", "STORAGE_SET_CONFIG", "FLUSH_ROUTER_CONFIG", ] 
**[resources](#resources)** | list, tuple,  | tuple,  | List of resources on which you grant the action. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# resources

List of resources on which you grant the action.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of resources on which you grant the action. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DBResource**](DBResource.md) | [**DBResource**](DBResource.md) | [**DBResource**](DBResource.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

