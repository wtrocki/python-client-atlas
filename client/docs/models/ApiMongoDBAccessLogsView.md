# atlas.model.api_mongo_db_access_logs_view.ApiMongoDBAccessLogsView

Authentication attempt, one per object, made against the cluster.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Authentication attempt, one per object, made against the cluster. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**authResult** | bool,  | BoolClass,  | Flag that indicates whether the response should return successful authentication attempts only. | [optional] 
**authSource** | str,  | str,  | Database against which someone attempted to authenticate. | [optional] 
**failureReason** | str,  | str,  | Reason that the authentication failed. Null if authentication succeeded. | [optional] 
**groupId** | str,  | str,  | Unique 24-hexadecimal character string that identifies the project. | [optional] 
**hostname** | str,  | str,  | Human-readable label that identifies the hostname of the target node that received the authentication attempt. | [optional] 
**ipAddress** | str,  | str,  | Internet Protocol address that attempted to authenticate with the database. | [optional] 
**logLine** | str,  | str,  | Text of the host log concerning the authentication attempt. | [optional] 
**timestamp** | str,  | str,  | Date and time when someone made this authentication attempt. MongoDB Cloud represents this timestamp in ISO 8601 format in UTC. | [optional] 
**username** | str,  | str,  | Username used to authenticate against the database. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

