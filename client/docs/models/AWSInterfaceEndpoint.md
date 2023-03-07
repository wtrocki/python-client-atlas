# atlas.model.aws_interface_endpoint.AWSInterfaceEndpoint

Group of Private Endpoint settings.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Group of Private Endpoint settings. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**connectionStatus** | str,  | str,  | State of the Amazon Web Service PrivateLink connection when MongoDB Cloud received this request. | [optional] must be one of ["PENDING_ACCEPTANCE", "PENDING", "AVAILABLE", "REJECTED", "DELETING", ] 
**deleteRequested** | bool,  | BoolClass,  | Flag that indicates whether MongoDB Cloud received a request to remove the specified private endpoint from the private endpoint service. | [optional] 
**errorMessage** | str,  | str,  | Error message returned when requesting private connection resource. The resource returns &#x60;null&#x60; if the request succeeded. | [optional] 
**interfaceEndpointId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the interface endpoint. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

