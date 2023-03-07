# atlas.model.api_checkpoint_part_view.ApiCheckpointPartView

Metadata contained in one document that describes the complete snapshot taken for this node.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Metadata contained in one document that describes the complete snapshot taken for this node. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**replicaSetName** | str,  | str,  | Human-readable label that identifies the replica set to which this checkpoint applies. | [optional] 
**shardName** | str,  | str,  | Human-readable label that identifies the shard to which this checkpoint applies. | [optional] 
**tokenDiscovered** | bool,  | BoolClass,  | Flag that indicates whether the token exists. | [optional] 
**tokenTimestamp** | [**ApiBSONTimestampView**](ApiBSONTimestampView.md) | [**ApiBSONTimestampView**](ApiBSONTimestampView.md) |  | [optional] 
**typeName** | str,  | str,  | Human-readable label that identifies the type of host that the part represents. | [optional] must be one of ["REPLICA_SET", "CONFIG_SERVER", "CONFIG_SERVER_REPLICA_SET", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

