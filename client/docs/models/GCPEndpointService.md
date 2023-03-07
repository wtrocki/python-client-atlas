# atlas.model.gcp_endpoint_service.GCPEndpointService

Group of Private Endpoint Service settings.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Group of Private Endpoint Service settings. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[endpointGroupNames](#endpointGroupNames)** | list, tuple,  | tuple,  | List of Google Cloud network endpoint groups that corresponds to the Private Service Connect endpoint service. | [optional] 
**errorMessage** | str,  | str,  | Error message returned when requesting private connection resource. The resource returns &#x60;null&#x60; if the request succeeded. | [optional] 
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the Private Endpoint Service. | [optional] 
**regionName** | str,  | str,  | Cloud provider region that manages this Private Endpoint Service. | [optional] 
**[serviceAttachmentNames](#serviceAttachmentNames)** | list, tuple,  | tuple,  | List of Uniform Resource Locators (URLs) that identifies endpoints that MongoDB Cloud can use to access one Google Cloud Service across a Google Cloud Virtual Private Connection (VPC) network. | [optional] 
**status** | str,  | str,  | State of the Private Endpoint Service connection when MongoDB Cloud received this request. | [optional] must be one of ["INITIATING", "AVAILABLE", "WAITING_FOR_USER", "FAILED", "DELETING", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# endpointGroupNames

List of Google Cloud network endpoint groups that corresponds to the Private Service Connect endpoint service.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of Google Cloud network endpoint groups that corresponds to the Private Service Connect endpoint service. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | One Google Cloud network endpoint group that corresponds to the Private Service Connect endpoint service. | 

# serviceAttachmentNames

List of Uniform Resource Locators (URLs) that identifies endpoints that MongoDB Cloud can use to access one Google Cloud Service across a Google Cloud Virtual Private Connection (VPC) network.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of Uniform Resource Locators (URLs) that identifies endpoints that MongoDB Cloud can use to access one Google Cloud Service across a Google Cloud Virtual Private Connection (VPC) network. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Uniform Resource Locator (URL) that identifies one endpoint that MongoDB Cloud can use to access one Google Cloud Service across a Google Cloud Virtual Private Connection (VPC) network. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

