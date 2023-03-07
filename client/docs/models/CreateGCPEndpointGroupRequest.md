# atlas.model.create_gcp_endpoint_group_request.CreateGCPEndpointGroupRequest

Group of Private Endpoint settings.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Group of Private Endpoint settings. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[CreateEndpointRequest](CreateEndpointRequest.md) | [**CreateEndpointRequest**](CreateEndpointRequest.md) | [**CreateEndpointRequest**](CreateEndpointRequest.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**endpointGroupName** | str,  | str,  | Human-readable label that identifies a set of endpoints. | [optional] 
**[endpoints](#endpoints)** | list, tuple,  | tuple,  | List of individual private endpoints that comprise this endpoint group. | [optional] 
**gcpProjectId** | str,  | str,  | Unique string that identifies the Google Cloud project in which you created the endpoints. | [optional] 
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
[**CreateGCPForwardingRuleRequest**](CreateGCPForwardingRuleRequest.md) | [**CreateGCPForwardingRuleRequest**](CreateGCPForwardingRuleRequest.md) | [**CreateGCPForwardingRuleRequest**](CreateGCPForwardingRuleRequest.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

