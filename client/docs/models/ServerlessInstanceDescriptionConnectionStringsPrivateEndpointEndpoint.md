# atlas.model.serverless_instance_description_connection_strings_private_endpoint_endpoint.ServerlessInstanceDescriptionConnectionStringsPrivateEndpointEndpoint

Details of a private endpoint deployed for this serverless instance.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Details of a private endpoint deployed for this serverless instance. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**endpointId** | str,  | str,  | Unique string that the cloud provider uses to identify the private endpoint. | [optional] 
**providerName** | str,  | str,  | Cloud provider where the private endpoint is deployed. | [optional] must be one of ["AWS", "AZURE", ] 
**region** | str,  | str,  | Region where the private endpoint is deployed. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

