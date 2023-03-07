# atlas.model.serverless_instance_description.ServerlessInstanceDescription

Group of settings that configure a MongoDB serverless instance.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Group of settings that configure a MongoDB serverless instance. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**providerSettings** | [**ServerlessProviderSettings**](ServerlessProviderSettings.md) | [**ServerlessProviderSettings**](ServerlessProviderSettings.md) |  | 
**connectionStrings** | [**ServerlessInstanceDescriptionConnectionStrings**](ServerlessInstanceDescriptionConnectionStrings.md) | [**ServerlessInstanceDescriptionConnectionStrings**](ServerlessInstanceDescriptionConnectionStrings.md) |  | [optional] 
**createDate** | str, datetime,  | str,  | Date and time when MongoDB Cloud created this serverless instance. MongoDB Cloud represents this timestamp in ISO 8601 format in UTC. | [optional] value must conform to RFC-3339 date-time
**groupId** | str,  | str,  | Unique 24-hexadecimal character string that identifies the project. | [optional] 
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the serverless instance. | [optional] 
**[links](#links)** | list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | [optional] 
**mongoDBVersion** | str,  | str,  | Version of MongoDB that the serverless instance runs. | [optional] 
**name** | str,  | str,  | Human-readable label that identifies the serverless instance. | [optional] 
**serverlessBackupOptions** | [**ServerlessBackupOptions**](ServerlessBackupOptions.md) | [**ServerlessBackupOptions**](ServerlessBackupOptions.md) |  | [optional] 
**stateName** | str,  | str,  | Human-readable label that indicates the current operating condition of the serverless instance. | [optional] must be one of ["IDLE", "CREATING", "UPDATING", "DELETING", "DELETED", "REPAIRING", ] 
**terminationProtectionEnabled** | bool,  | BoolClass,  | Flag that indicates whether termination protection is enabled on the serverless instance. If set to &#x60;true&#x60;, MongoDB Cloud won&#x27;t delete the serverless instance. If set to &#x60;false&#x60;, MongoDB Cloud will delete the serverless instance. | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# links

List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Link**](Link.md) | [**Link**](Link.md) | [**Link**](Link.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

