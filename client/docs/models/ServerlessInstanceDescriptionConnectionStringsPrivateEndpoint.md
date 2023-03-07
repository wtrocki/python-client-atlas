# atlas.model.serverless_instance_description_connection_strings_private_endpoint.ServerlessInstanceDescriptionConnectionStringsPrivateEndpoint

Private endpoint connection string that you can use to connect to this serverless instance through a private endpoint.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Private endpoint connection string that you can use to connect to this serverless instance through a private endpoint. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[endpoints](#endpoints)** | list, tuple,  | tuple,  | List that contains the private endpoints through which you connect to MongoDB Cloud when you use **connectionStrings.privateEndpoint[n].srvConnectionString**. | [optional] 
**srvConnectionString** | str,  | str,  | Private endpoint-aware connection string that uses the &#x60;mongodb+srv://&#x60; protocol to connect to MongoDB Cloud through a private endpoint. The &#x60;mongodb+srv&#x60; protocol tells the driver to look up the seed list of hosts in the Domain Name System (DNS). | [optional] 
**type** | str,  | str,  | MongoDB process type to which your application connects. | [optional] must be one of ["MONGOS", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# endpoints

List that contains the private endpoints through which you connect to MongoDB Cloud when you use **connectionStrings.privateEndpoint[n].srvConnectionString**.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains the private endpoints through which you connect to MongoDB Cloud when you use **connectionStrings.privateEndpoint[n].srvConnectionString**. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ServerlessInstanceDescriptionConnectionStringsPrivateEndpointEndpoint**](ServerlessInstanceDescriptionConnectionStringsPrivateEndpointEndpoint.md) | [**ServerlessInstanceDescriptionConnectionStringsPrivateEndpointEndpoint**](ServerlessInstanceDescriptionConnectionStringsPrivateEndpointEndpoint.md) | [**ServerlessInstanceDescriptionConnectionStringsPrivateEndpointEndpoint**](ServerlessInstanceDescriptionConnectionStringsPrivateEndpointEndpoint.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

