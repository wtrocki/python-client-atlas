# atlas.model.data_lake_data_process_region.DataLakeDataProcessRegion

Information about the cloud provider region to which the data lake routes client connections. MongoDB Cloud supports AWS only.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Information about the cloud provider region to which the data lake routes client connections. MongoDB Cloud supports AWS only. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cloudProvider** | str,  | str,  | Name of the cloud service that hosts the data lake&#x27;s data stores. | must be one of ["AWS", "GCP", "AZURE", "TENANT", "SERVERLESS", ] 
**region** | [**DataLakeRegion**](DataLakeRegion.md) | [**DataLakeRegion**](DataLakeRegion.md) |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

