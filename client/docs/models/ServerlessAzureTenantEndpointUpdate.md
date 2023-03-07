# atlas.model.serverless_azure_tenant_endpoint_update.ServerlessAzureTenantEndpointUpdate

Updates to a serverless Azure tenant endpoint.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Updates to a serverless Azure tenant endpoint. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**providerName** | str,  | str,  |  | 
**cloudProviderEndpointId** | str,  | str,  | Unique string that identifies the Azure private endpoint&#x27;s network interface for this private endpoint service. | [optional] 
**privateEndpointIpAddress** | str,  | str,  | IPv4 address of the private endpoint in your Azure VNet that someone added to this private endpoint service. | [optional] 
**comment** | str,  | str,  | Human-readable comment associated with the private endpoint. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

