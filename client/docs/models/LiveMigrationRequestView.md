# atlas.model.live_migration_request_view.LiveMigrationRequestView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dropEnabled** | bool,  | BoolClass,  | Flag that indicates whether the migration process drops all collections from the destination cluster before the migration starts. | 
**destination** | [**Destination**](Destination.md) | [**Destination**](Destination.md) |  | 
**source** | [**Source**](Source.md) | [**Source**](Source.md) |  | 
**_id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the migration request. | [optional] 
**[migrationHosts](#migrationHosts)** | list, tuple,  | tuple,  | List of migration hosts used for this migration. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# migrationHosts

List of migration hosts used for this migration.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of migration hosts used for this migration. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

