# atlas.model.partition_field.PartitionField

Partition Field in the Data Lake Storage provider for a Data Lake Pipeline.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Partition Field in the Data Lake Storage provider for a Data Lake Pipeline. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**fieldName** | str,  | str,  | Human-readable label that identifies the field name used to partition data. | 
**order** | decimal.Decimal, int,  | decimal.Decimal,  | Sequence in which MongoDB Cloud slices the collection data to create partitions. The resource expresses this sequence starting with zero. | if omitted the server will use the default value of 0value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

