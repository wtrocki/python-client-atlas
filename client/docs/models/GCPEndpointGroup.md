# atlas.model.gcp_endpoint_group.GCPEndpointGroup

Group of Private Endpoint settings.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Group of Private Endpoint settings. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**deleteRequested** | bool,  | BoolClass,  | Flag that indicates whether MongoDB Cloud received a request to remove the specified private endpoint from the private endpoint service. | [optional] 
**endpointGroupName** | str,  | str,  | Human-readable label that identifies a set of endpoints. | [optional] 
**[endpoints](#endpoints)** | list, tuple,  | tuple,  | List of individual private endpoints that comprise this endpoint group. | [optional] 
**errorMessage** | str,  | str,  | Error message returned when requesting private connection resource. The resource returns &#x60;null&#x60; if the request succeeded. | [optional] 
**status** | str,  | str,  | State of the Google Cloud network endpoint group when MongoDB Cloud received this request. | [optional] must be one of ["INITIATING", "VERIFIED", "AVAILABLE", "FAILED", "DELETING", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# endpoints

List of individual private endpoints that comprise this endpoint group.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of individual private endpoints that comprise this endpoint group. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**GCPConsumerForwardingRule**](GCPConsumerForwardingRule.md) | [**GCPConsumerForwardingRule**](GCPConsumerForwardingRule.md) | [**GCPConsumerForwardingRule**](GCPConsumerForwardingRule.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

