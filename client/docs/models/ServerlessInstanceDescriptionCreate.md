# atlas.model.serverless_instance_description_create.ServerlessInstanceDescriptionCreate

Settings that you can specify when you create a serverless instance.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Settings that you can specify when you create a serverless instance. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Human-readable label that identifies the serverless instance. | 
**providerSettings** | [**ServerlessProviderSettings**](ServerlessProviderSettings.md) | [**ServerlessProviderSettings**](ServerlessProviderSettings.md) |  | 
**serverlessBackupOptions** | [**ServerlessBackupOptions**](ServerlessBackupOptions.md) | [**ServerlessBackupOptions**](ServerlessBackupOptions.md) |  | [optional] 
**stateName** | str,  | str,  | Human-readable label that indicates the current operating condition of the serverless instance. | [optional] must be one of ["IDLE", "CREATING", "UPDATING", "DELETING", "DELETED", "REPAIRING", ] 
**terminationProtectionEnabled** | bool,  | BoolClass,  | Flag that indicates whether termination protection is enabled on the serverless instance. If set to &#x60;true&#x60;, MongoDB Cloud won&#x27;t delete the serverless instance. If set to &#x60;false&#x60;, MongoDB Cloud will delete the serverless instance. | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

