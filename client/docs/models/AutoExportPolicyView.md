# atlas.model.auto_export_policy_view.AutoExportPolicyView

Policy for automatically exporting cloud backup snapshots.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Policy for automatically exporting cloud backup snapshots. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**exportBucketId** | str,  | str,  | Unique 24-hexadecimal character string that identifies the AWS Bucket. | [optional] 
**frequencyType** | str,  | str,  | Human-readable label that indicates the rate at which the export policy item occurs. | [optional] must be one of ["monthly", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

