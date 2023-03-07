# atlas.model.dls_ingestion_sink.DLSIngestionSink

Atlas Data Lake Storage as the destination for a Data Lake Pipeline.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Atlas Data Lake Storage as the destination for a Data Lake Pipeline. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**metadataProvider** | str,  | str,  | Target cloud provider for this Data Lake Pipeline. | [optional] must be one of ["AWS", ] 
**metadataRegion** | str,  | str,  | Target cloud provider region for this Data Lake Pipeline. | [optional] 
**[partitionFields](#partitionFields)** | list, tuple,  | tuple,  | Ordered fields used to physically organize data in the destination. | [optional] 
**type** | str,  | str,  | Type of ingestion destination of this Data Lake Pipeline. | [optional] must be one of ["DLS", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# partitionFields

Ordered fields used to physically organize data in the destination.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Ordered fields used to physically organize data in the destination. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PartitionField**](PartitionField.md) | [**PartitionField**](PartitionField.md) | [**PartitionField**](PartitionField.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

