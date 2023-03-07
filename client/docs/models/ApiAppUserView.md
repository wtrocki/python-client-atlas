# atlas.model.api_app_user_view.ApiAppUserView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**country** | str,  | str,  | Two alphabet characters that identifies MongoDB Cloud user&#x27;s geographic location. This parameter uses the ISO 3166-1a2 code format. | 
**firstName** | str,  | str,  | First or given name that belongs to the MongoDB Cloud user. | 
**lastName** | str,  | str,  | Last name, family name, or surname that belongs to the MongoDB Cloud user. | 
**emailAddress** | str,  | str,  | Email address that belongs to the MongoDB Cloud user. | 
**password** | str,  | str,  | Password applied with the username to log in to MongoDB Cloud. MongoDB Cloud does not return this parameter except in response to creating a new MongoDB Cloud user. Only the MongoDB Cloud user can update their password after it has been set from the MongoDB Cloud console. | 
**mobileNumber** | str,  | str,  | Mobile phone number that belongs to the MongoDB Cloud user. | 
**username** | str,  | str,  | Email address that represents the username of the MongoDB Cloud user. | 
**createdAt** | str, datetime,  | str,  | Date and time when the current account is created. This value is in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the MongoDB Cloud user. | [optional] 
**lastAuth** | str, datetime,  | str,  | Date and time when the current account last authenticated. This value is in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**[links](#links)** | list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | [optional] 
**[roles](#roles)** | list, tuple,  | tuple,  | List of objects that display the MongoDB Cloud user&#x27;s roles and the corresponding organization or project to which that role applies. A role can apply to one organization or one project but not both. | [optional] 
**[teamIds](#teamIds)** | list, tuple,  | tuple,  | List of unique 24-hexadecimal digit strings that identifies the teams to which this MongoDB Cloud user belongs. | [optional] 
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

List of objects that display the MongoDB Cloud user's roles and the corresponding organization or project to which that role applies. A role can apply to one organization or one project but not both.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of objects that display the MongoDB Cloud user&#x27;s roles and the corresponding organization or project to which that role applies. A role can apply to one organization or one project but not both. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiRoleAssignmentView**](ApiRoleAssignmentView.md) | [**ApiRoleAssignmentView**](ApiRoleAssignmentView.md) | [**ApiRoleAssignmentView**](ApiRoleAssignmentView.md) |  | 

# teamIds

List of unique 24-hexadecimal digit strings that identifies the teams to which this MongoDB Cloud user belongs.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of unique 24-hexadecimal digit strings that identifies the teams to which this MongoDB Cloud user belongs. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Unique 24-hexadecimal digit string that identifies the team to which this MongoDB Cloud user belongs. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

