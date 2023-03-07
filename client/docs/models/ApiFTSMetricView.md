# atlas.model.api_fts_metric_view.ApiFTSMetricView

Measurement of one Atlas Search status when MongoDB Atlas received this request.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Measurement of one Atlas Search status when MongoDB Atlas received this request. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**metricName** | str,  | str,  | Human-readable label that identifies this Atlas Search hardware, status, or index measurement. | must be one of ["INDEX_SIZE_ON_DISK", "NUMBER_OF_DELETES", "NUMBER_OF_ERROR_QUERIES", "NUMBER_OF_GETMORE_COMMANDS", "NUMBER_OF_INDEX_FIELDS", "NUMBER_OF_INSERTS", "NUMBER_OF_SUCCESS_QUERIES", "NUMBER_OF_UPDATES", "REPLICATION_LAG", "TOTAL_NUMBER_OF_QUERIES", "FTS_DISK_USAGE", "FTS_PROCESS_CPU_KERNEL", "FTS_PROCESS_CPU_USER", "FTS_PROCESS_NORMALIZED_CPU_KERNEL", "FTS_PROCESS_NORMALIZED_CPU_USER", "FTS_PROCESS_RESIDENT_MEMORY", "FTS_PROCESS_SHARED_MEMORY", "FTS_PROCESS_VIRTUAL_MEMORY", "JVM_CURRENT_MEMORY", "JVM_MAX_MEMORY", ] 
**units** | str,  | str,  | Unit of measurement that applies to this Atlas Search metric. | must be one of ["BYTES", "BYTES_PER_SECOND", "GIGABYTES", "GIGABYTES_PER_HOUR", "KILOBYTES", "MEGABYTES", "MEGABYTES_PER_SECOND", "MILLISECONDS", "MILLISECONDS_LOGSCALE", "PERCENT", "SCALAR", "SCALAR_PER_SECOND", "SECONDS", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

