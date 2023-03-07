# atlas.model.managed_namespace_view.ManagedNamespaceView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**collection** | str,  | str,  | Human-readable label of the collection to manage for this Global Cluster. | [optional] 
**customShardKey** | str,  | str,  | Database parameter used to divide the *collection* into shards. Global clusters require a compound shard key. This compound shard key combines the location parameter and the user-selected custom key. | [optional] 
**db** | str,  | str,  | Human-readable label of the database to manage for this Global Cluster. | [optional] 
**isCustomShardKeyHashed** | bool,  | BoolClass,  | Flag that indicates whether someone hashed the custom shard key. If this parameter returns &#x60;false&#x60;, this cluster uses ranged sharding. | [optional] if omitted the server will use the default value of False
**isShardKeyUnique** | bool,  | BoolClass,  | Flag that indicates whether the underlying index enforces unique values. | [optional] if omitted the server will use the default value of False
**numInitialChunks** | decimal.Decimal, int,  | decimal.Decimal,  | Minimum number of chunks to create initially when sharding an empty collection with a hashed shard key. | [optional] value must be a 64 bit integer
**presplitHashedZones** | bool,  | BoolClass,  | Flag that indicates whether MongoDB Cloud should create and distribute initial chunks for an empty or non-existing collection. MongoDB Cloud distributes data based on the defined zones and zone ranges for the collection. | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

