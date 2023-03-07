# atlas.model.api_organization_invitation_request_view.ApiOrganizationInvitationRequestView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[roles](#roles)** | list, tuple,  | tuple,  | One or more organization or project level roles to assign to the MongoDB Cloud user. | [optional] 
**[teamIds](#teamIds)** | list, tuple,  | tuple,  | List of teams to which you want to invite the desired MongoDB Cloud user. | [optional] 
**username** | str,  | str,  | Email address that belongs to the desired MongoDB Cloud user. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# roles

One or more organization or project level roles to assign to the MongoDB Cloud user.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | One or more organization or project level roles to assign to the MongoDB Cloud user. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["ORG_OWNER", "ORG_MEMBER", "ORG_GROUP_CREATOR", "ORG_BILLING_ADMIN", "ORG_READ_ONLY", ] 

# teamIds

List of teams to which you want to invite the desired MongoDB Cloud user.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of teams to which you want to invite the desired MongoDB Cloud user. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Unique 24-hexadecimal digit string that identifies the team. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

