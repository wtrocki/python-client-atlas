# atlas.model.api_mongo_db_access_logs_list_view.ApiMongoDBAccessLogsListView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[accessLogs](#accessLogs)** | list, tuple,  | tuple,  | Authentication attempt, one per object, made against the cluster. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# accessLogs

Authentication attempt, one per object, made against the cluster.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Authentication attempt, one per object, made against the cluster. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiMongoDBAccessLogsView**](ApiMongoDBAccessLogsView.md) | [**ApiMongoDBAccessLogsView**](ApiMongoDBAccessLogsView.md) | [**ApiMongoDBAccessLogsView**](ApiMongoDBAccessLogsView.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

