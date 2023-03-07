# atlas.model.ingestion_pipeline_run.IngestionPipelineRun

Run details of a Data Lake Pipeline.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Run details of a Data Lake Pipeline. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**_id** | str,  | str,  | Unique 24-hexadecimal character string that identifies a Data Lake Pipeline run. | [optional] 
**backupFrequencyType** | str,  | str,  | Backup schedule interval of the Data Lake Pipeline. | [optional] must be one of ["HOURLY", "DAILY", "WEEKLY", "MONTHLY", "ON_DEMAND", ] 
**createdDate** | str, datetime,  | str,  | Timestamp that indicates when the pipeline run was created. | [optional] value must conform to RFC-3339 date-time
**datasetName** | str,  | str,  | Human-readable label that identifies the dataset that Atlas generates during this pipeline run. You can use this dataset as a &#x60;dataSource&#x60; in a Federated Database collection. | [optional] 
**groupId** | str,  | str,  | Unique 24-hexadecimal character string that identifies the project. | [optional] 
**lastUpdatedDate** | str, datetime,  | str,  | Timestamp that indicates the last time that the pipeline run was updated. | [optional] value must conform to RFC-3339 date-time
**phase** | str,  | str,  | Processing phase of the Data Lake Pipeline. | [optional] must be one of ["SNAPSHOT", "EXPORT", "INGESTION", ] 
**pipelineId** | str,  | str,  | Unique 24-hexadecimal character string that identifies a Data Lake Pipeline. | [optional] 
**snapshotId** | str,  | str,  | Unique 24-hexadecimal character string that identifies the snapshot of a cluster. | [optional] 
**state** | str,  | str,  | State of the pipeline run. | [optional] must be one of ["PENDING", "IN_PROGRESS", "DONE", "FAILED", "DATASET_DELETED", ] 
**stats** | [**PipelineRunStats**](PipelineRunStats.md) | [**PipelineRunStats**](PipelineRunStats.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

