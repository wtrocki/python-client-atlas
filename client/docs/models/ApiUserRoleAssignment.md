# atlas.model.api_user_role_assignment.ApiUserRoleAssignment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**apiUserId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the organization API key. | [optional] 
**[roles](#roles)** | list, tuple,  | tuple,  | List of roles to grant this API key. If you provide this list, provide a minimum of one role and ensure each role applies to this project. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# roles

List of roles to grant this API key. If you provide this list, provide a minimum of one role and ensure each role applies to this project.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of roles to grant this API key. If you provide this list, provide a minimum of one role and ensure each role applies to this project. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["GROUP_CLUSTER_MANAGER", "GROUP_DATA_ACCESS_ADMIN", "GROUP_DATA_ACCESS_READ_ONLY", "GROUP_DATA_ACCESS_READ_WRITE", "GROUP_SEARCH_INDEX_EDITOR", "GROUP_OWNER", "GROUP_READ_ONLY", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

