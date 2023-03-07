# atlas.model.periodic_cps_snapshot_source.PeriodicCpsSnapshotSource

Scheduled Cloud Provider Snapshot as Source for a Data Lake Pipeline.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Scheduled Cloud Provider Snapshot as Source for a Data Lake Pipeline. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**clusterName** | str,  | str,  | Human-readable name that identifies the cluster. | [optional] 
**collectionName** | str,  | str,  | Human-readable name that identifies the collection. | [optional] 
**databaseName** | str,  | str,  | Human-readable name that identifies the database. | [optional] 
**groupId** | str,  | str,  | Unique 24-hexadecimal character string that identifies the project. | [optional] 
**policyItemId** | str,  | str,  | Unique 24-hexadecimal character string that identifies a policy item. | [optional] 
**type** | str,  | str,  | Type of ingestion source of this Data Lake Pipeline. | [optional] must be one of ["PERIODIC_CPS", "ON_DEMAND_CPS", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

