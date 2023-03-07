# atlas.model.pipeline_run_stats.PipelineRunStats

Runtime statistics for this Data Lake Pipeline run.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Runtime statistics for this Data Lake Pipeline run. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**bytesExported** | decimal.Decimal, int,  | decimal.Decimal,  | Total data size in bytes exported for this pipeline run. | [optional] value must be a 64 bit integer
**numDocs** | decimal.Decimal, int,  | decimal.Decimal,  | Number of docs ingested for a this pipeline run. | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

