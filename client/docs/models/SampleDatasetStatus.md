# atlas.model.sample_dataset_status.SampleDatasetStatus

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**_id** | str,  | str,  | Unique 24-hexadecimal character string that identifies this sample dataset. | [optional] 
**clusterName** | str,  | str,  | Human-readable label that identifies the cluster into which you loaded the sample dataset. | [optional] 
**completeDate** | str, datetime,  | str,  | Date and time when the sample dataset load job completed. MongoDB Cloud represents this timestamp in ISO 8601 format in UTC. | [optional] value must conform to RFC-3339 date-time
**createDate** | str, datetime,  | str,  | Date and time when you started the sample dataset load job. MongoDB Cloud represents this timestamp in ISO 8601 format in UTC. | [optional] value must conform to RFC-3339 date-time
**errorMessage** | str,  | str,  | Details of the error returned when MongoDB Cloud loads the sample dataset. This endpoint returns null if state has a value other than FAILED. | [optional] 
**state** | str,  | str,  | Status of the sample dataset load job. | [optional] must be one of ["WORKING", "FAILED", "COMPLETED", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

