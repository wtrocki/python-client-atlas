# atlas.model.azure_private_link_connection.AzurePrivateLinkConnection

Group of Private Endpoint Service settings.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Group of Private Endpoint Service settings. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**errorMessage** | str,  | str,  | Error message returned when requesting private connection resource. The resource returns &#x60;null&#x60; if the request succeeded. | [optional] 
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the Private Endpoint Service. | [optional] 
**[privateEndpoints](#privateEndpoints)** | list, tuple,  | tuple,  | List of private endpoints assigned to this Azure Private Link Service. | [optional] 
**privateLinkServiceName** | str,  | str,  | Unique string that identifies the Azure Private Link Service that MongoDB Cloud manages. | [optional] 
**privateLinkServiceResourceId** | str,  | str,  | Root-relative path that identifies of the Azure Private Link Service that MongoDB Cloud manages. Use this value to create a private endpoint connection to an Azure VNet. | [optional] 
**regionName** | str,  | str,  | Cloud provider region that manages this Private Endpoint Service. | [optional] 
**status** | str,  | str,  | State of the Private Endpoint Service connection when MongoDB Cloud received this request. | [optional] must be one of ["INITIATING", "AVAILABLE", "WAITING_FOR_USER", "FAILED", "DELETING", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# privateEndpoints

List of private endpoints assigned to this Azure Private Link Service.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of private endpoints assigned to this Azure Private Link Service. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Root-relative path to one private endpoint assigned to this Azure Private Link Service. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

