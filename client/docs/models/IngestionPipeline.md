# atlas.model.ingestion_pipeline.IngestionPipeline

Details of a Data Lake Pipeline.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Details of a Data Lake Pipeline. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**_id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the Data Lake Pipeline. | [optional] 
**createdDate** | str, datetime,  | str,  | Timestamp that indicates when the Data Lake Pipeline was created. | [optional] value must conform to RFC-3339 date-time
**groupId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the group. | [optional] 
**lastUpdatedDate** | str, datetime,  | str,  | Timestamp that indicates the last time that the Data Lake Pipeline was updated. | [optional] value must conform to RFC-3339 date-time
**name** | str,  | str,  | Name of this Data Lake Pipeline. | [optional] 
**sink** | [**IngestionSink**](IngestionSink.md) | [**IngestionSink**](IngestionSink.md) |  | [optional] 
**source** | [**IngestionSource**](IngestionSource.md) | [**IngestionSource**](IngestionSource.md) |  | [optional] 
**state** | str,  | str,  | State of this Data Lake Pipeline. | [optional] must be one of ["ACTIVE", "PAUSED", ] 
**[transformations](#transformations)** | list, tuple,  | tuple,  | Fields to be excluded for this Data Lake Pipeline. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# transformations

Fields to be excluded for this Data Lake Pipeline.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Fields to be excluded for this Data Lake Pipeline. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FieldTransformation**](FieldTransformation.md) | [**FieldTransformation**](FieldTransformation.md) | [**FieldTransformation**](FieldTransformation.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

