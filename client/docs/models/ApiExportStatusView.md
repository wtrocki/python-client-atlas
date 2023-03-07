# atlas.model.api_export_status_view.ApiExportStatusView

State of the export job for the collections on the replica set only.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | State of the export job for the collections on the replica set only. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**exportedCollections** | decimal.Decimal, int,  | decimal.Decimal,  | Number of collections on the replica set that MongoDB Cloud exported. | [optional] value must be a 32 bit integer
**totalCollections** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of collections on the replica set to export. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

