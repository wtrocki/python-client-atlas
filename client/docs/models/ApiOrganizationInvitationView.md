# atlas.model.api_organization_invitation_view.ApiOrganizationInvitationView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**orgName** | str,  | str,  | Human-readable label that identifies this organization. | 
**createdAt** | str, datetime,  | str,  | Date and time when MongoDB Cloud sent the invitation. MongoDB Cloud represents this timestamp in ISO 8601 format in UTC. | [optional] value must conform to RFC-3339 date-time
**expiresAt** | str, datetime,  | str,  | Date and time when the invitation from MongoDB Cloud expires. MongoDB Cloud represents this timestamp in ISO 8601 format in UTC. | [optional] value must conform to RFC-3339 date-time
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies this organization. | [optional] 
**inviterUsername** | str,  | str,  | Email address of the MongoDB Cloud user who sent the invitation to join the organization. | [optional] 
**[links](#links)** | list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | [optional] 
**orgId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the organization. | [optional] 
**[roles](#roles)** | list, tuple,  | tuple,  | One or more organization or project level roles to assign to the MongoDB Cloud user. | [optional] 
**[teamIds](#teamIds)** | list, tuple,  | tuple,  | List of unique 24-hexadecimal digit strings that identifies each team. | [optional] 
**username** | str,  | str,  | Email address of the MongoDB Cloud user invited to join the organization. | [optional] 
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

# roles

One or more organization or project level roles to assign to the MongoDB Cloud user.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | One or more organization or project level roles to assign to the MongoDB Cloud user. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["ORG_OWNER", "ORG_MEMBER", "ORG_GROUP_CREATOR", "ORG_BILLING_ADMIN", "ORG_READ_ONLY", "GROUP_CLUSTER_MANAGER", "GROUP_DATA_ACCESS_ADMIN", "GROUP_DATA_ACCESS_READ_ONLY", "GROUP_DATA_ACCESS_READ_WRITE", "GROUP_OWNER", "GROUP_READ_ONLY", ] 

# teamIds

List of unique 24-hexadecimal digit strings that identifies each team.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of unique 24-hexadecimal digit strings that identifies each team. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Unique 24-hexadecimal digit string that identifies the team. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

