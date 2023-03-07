# atlas.model.serverless_azure_tenant_endpoint.ServerlessAzureTenantEndpoint

View for a serverless Azure tenant endpoint.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | View for a serverless Azure tenant endpoint. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**_id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the private endpoint. | [optional] 
**cloudProviderEndpointId** | str,  | str,  | Unique string that identifies the Azure private endpoint&#x27;s network interface that someone added to this private endpoint service. | [optional] 
**comment** | str,  | str,  | Human-readable comment associated with the private endpoint. | [optional] 
**endpointServiceName** | str,  | str,  | Unique string that identifies the Azure private endpoint service. MongoDB Cloud returns null while it creates the endpoint service. | [optional] 
**errorMessage** | str,  | str,  | Human-readable error message that indicates error condition associated with establishing the private endpoint connection. | [optional] 
**privateEndpointIpAddress** | str,  | str,  | IPv4 address of the private endpoint in your Azure VNet that someone added to this private endpoint service. | [optional] 
**privateLinkServiceResourceId** | str,  | str,  | Root-relative path that identifies the Azure Private Link Service that MongoDB Cloud manages. MongoDB Cloud returns null while it creates the endpoint service. | [optional] 
**providerName** | str,  | str,  | Human-readable label that identifies the cloud service provider. | [optional] must be one of ["AZURE", ] 
**status** | str,  | str,  | Human-readable label that indicates the current operating status of the private endpoint. | [optional] must be one of ["RESERVATION_REQUESTED", "RESERVED", "INITIATING", "AVAILABLE", "FAILED", "DELETING", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

