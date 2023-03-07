# atlas.model.azure_private_endpoint.AzurePrivateEndpoint

Group of Private Endpoint settings.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Group of Private Endpoint settings. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**deleteRequested** | bool,  | BoolClass,  | Flag that indicates whether MongoDB Cloud received a request to remove the specified private endpoint from the private endpoint service. | [optional] 
**errorMessage** | str,  | str,  | Error message returned when requesting private connection resource. The resource returns &#x60;null&#x60; if the request succeeded. | [optional] 
**privateEndpointConnectionName** | str,  | str,  | Human-readable label that MongoDB Cloud generates that identifies the private endpoint connection. | [optional] 
**privateEndpointIPAddress** | str,  | str,  | IPv4 address of the private endpoint in your Azure VNet that someone added to this private endpoint service. | [optional] 
**privateEndpointResourceId** | str,  | str,  | Unique string that identifies the Azure private endpoint&#x27;s network interface that someone added to this private endpoint service. | [optional] 
**status** | str,  | str,  | State of the Azure Private Link Service connection when MongoDB Cloud received this request. | [optional] must be one of ["INITIATING", "AVAILABLE", "FAILED", "DELETING", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

