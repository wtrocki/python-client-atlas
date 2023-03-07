# atlas.model.role.Role

Range of resources available to this database user.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Range of resources available to this database user. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**databaseName** | str,  | str,  | Database against which the database user authenticates. Database users must provide both a username and authentication database to log into MongoDB. | 
**roleName** | str,  | str,  | Human-readable label that identifies a group of privileges assigned to a database user. This value can either be a built-in role or a custom role. | must be one of ["atlasAdmin", "backup", "clusterMonitor", "dbAdmin", "dbAdminAnyDatabase", "enableSharding", "read", "readAnyDatabase", "readWrite", "readWriteAnyDatabase", "<a custom role name>", ] 
**collectionName** | str,  | str,  | Collection on which this role applies. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

