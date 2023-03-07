# atlas.model.custom_db_role.CustomDBRole

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**roleName** | str,  | str,  | Human-readable label that identifies the role for the request. This name must be unique for this custom role in this project. | 
**[actions](#actions)** | list, tuple,  | tuple,  | List of the individual privilege actions that the role grants. | [optional] 
**[inheritedRoles](#inheritedRoles)** | list, tuple,  | tuple,  | List of the built-in roles that this custom role inherits. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# actions

List of the individual privilege actions that the role grants.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of the individual privilege actions that the role grants. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DBAction**](DBAction.md) | [**DBAction**](DBAction.md) | [**DBAction**](DBAction.md) |  | 

# inheritedRoles

List of the built-in roles that this custom role inherits.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of the built-in roles that this custom role inherits. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**InheritedRole**](InheritedRole.md) | [**InheritedRole**](InheritedRole.md) | [**InheritedRole**](InheritedRole.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

