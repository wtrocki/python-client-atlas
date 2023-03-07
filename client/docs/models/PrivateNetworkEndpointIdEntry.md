# atlas.model.private_network_endpoint_id_entry.PrivateNetworkEndpointIdEntry

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**endpointId** | str,  | str,  | Unique 22-character alphanumeric string that identifies the private endpoint. | 
**comment** | str,  | str,  | Human-readable string to associate with this private endpoint. | [optional] 
**provider** | str,  | str,  | Human-readable label that identifies the cloud service provider. Atlas Data Lake supports Amazon Web Services only. | [optional] must be one of ["AWS", ] if omitted the server will use the default value of "AWS"
**type** | str,  | str,  | Human-readable label that identifies the resource type associated with this private endpoint. | [optional] must be one of ["DATA_LAKE", ] if omitted the server will use the default value of "DATA_LAKE"
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

