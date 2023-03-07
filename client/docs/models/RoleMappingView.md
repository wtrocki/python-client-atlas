# atlas.model.role_mapping_view.RoleMappingView

Mapping settings that link one IdP and MongoDB Cloud.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Mapping settings that link one IdP and MongoDB Cloud. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**externalGroupName** | str,  | str,  | Unique human-readable label that identifies the identity provider group to whichthis role mapping applies. | 
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies this role mapping. | [optional] 
**[roleAssignments](#roleAssignments)** | list, tuple,  | tuple,  | Atlas roles and the unique identifiers of the groups and organizations associated with each role. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# roleAssignments

Atlas roles and the unique identifiers of the groups and organizations associated with each role.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Atlas roles and the unique identifiers of the groups and organizations associated with each role. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RoleAssignment**](RoleAssignment.md) | [**RoleAssignment**](RoleAssignment.md) | [**RoleAssignment**](RoleAssignment.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

