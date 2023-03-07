# atlas.model.serverless_instance_description_connection_strings.ServerlessInstanceDescriptionConnectionStrings

Collection of Uniform Resource Locators that point to the MongoDB database.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Collection of Uniform Resource Locators that point to the MongoDB database. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[privateEndpoint](#privateEndpoint)** | list, tuple,  | tuple,  | List of private endpoint-aware connection strings that you can use to connect to this serverless instance through a private endpoint. This parameter returns only if you created a private endpoint for this serverless instance and it is AVAILABLE. | [optional] 
**standardSrv** | str,  | str,  | Public connection string that you can use to connect to this serverless instance. This connection string uses the &#x60;mongodb+srv://&#x60; protocol. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# privateEndpoint

List of private endpoint-aware connection strings that you can use to connect to this serverless instance through a private endpoint. This parameter returns only if you created a private endpoint for this serverless instance and it is AVAILABLE.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of private endpoint-aware connection strings that you can use to connect to this serverless instance through a private endpoint. This parameter returns only if you created a private endpoint for this serverless instance and it is AVAILABLE. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ServerlessInstanceDescriptionConnectionStringsPrivateEndpoint**](ServerlessInstanceDescriptionConnectionStringsPrivateEndpoint.md) | [**ServerlessInstanceDescriptionConnectionStringsPrivateEndpoint**](ServerlessInstanceDescriptionConnectionStringsPrivateEndpoint.md) | [**ServerlessInstanceDescriptionConnectionStringsPrivateEndpoint**](ServerlessInstanceDescriptionConnectionStringsPrivateEndpoint.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

