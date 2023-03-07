# atlas.model.connected_org_config_view.ConnectedOrgConfigView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**domainRestrictionEnabled** | bool,  | BoolClass,  | Value that indicates whether domain restriction is enabled for this connected org. | 
**orgId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the connected organization configuration. | 
**identityProviderId** | str,  | str,  | Unique 20-hexadecimal digit string that identifies the identity provider that this connected org config is associated with. | 
**[domainAllowList](#domainAllowList)** | list, tuple,  | tuple,  | Approved domains that restrict users who can join the organization based on their email address. | [optional] 
**[postAuthRoleGrants](#postAuthRoleGrants)** | list, tuple,  | tuple,  | Atlas roles that are granted to a user in this organization after authenticating. | [optional] 
**[roleMappings](#roleMappings)** | list, tuple,  | tuple,  | Role mappings that are configured in this organization. | [optional] 
**[userConflicts](#userConflicts)** | list, tuple,  | tuple,  | List that contains the users who have an email address that doesn&#x27;t match any domain on the allowed list. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# domainAllowList

Approved domains that restrict users who can join the organization based on their email address.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Approved domains that restrict users who can join the organization based on their email address. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# postAuthRoleGrants

Atlas roles that are granted to a user in this organization after authenticating.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Atlas roles that are granted to a user in this organization after authenticating. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Organization role the user has in Atlas. | must be one of ["GLOBAL_AUTOMATION_ADMIN", "GLOBAL_BACKUP_ADMIN", "GLOBAL_METERING_USER", "GLOBAL_METRICS_INTERNAL_USER", "GLOBAL_MONITORING_ADMIN", "GLOBAL_OWNER", "GLOBAL_READ_ONLY", "GLOBAL_USER_ADMIN", "GLOBAL_USER_READ_ONLY", "GLOBAL_ACCOUNT_SUSPENSION_ADMIN", "GLOBAL_BILLING_ADMIN", "GLOBAL_LEGAL_ADMIN", "GLOBAL_FEATURE_FLAG_ADMIN", "GLOBAL_ATLAS_TSE", "GLOBAL_ATLAS_OPERATOR", "GLOBAL_ATLAS_MONGODB_ROLLOUT_ADMIN", "GLOBAL_ATLAS_ADMIN", "GLOBAL_STITCH_ADMIN", "GLOBAL_CHARTS_ADMIN", "GLOBAL_EXPERIMENT_ASSIGNMENT_USER", "GLOBAL_STITCH_INTERNAL_ADMIN", "GLOBAL_BAAS_FEATURE_ADMIN", "GLOBAL_SECURITY_ADMIN", "GLOBAL_QUERY_ENGINE_INTERNAL_ADMIN", "GLOBAL_PROACTIVE_SUPPORT_ADMIN", "GLOBAL_INFRASTRUCTURE_INTERNAL_ADMIN", "GLOBAL_SALESFORCE_ADMIN", "GLOBAL_SALESFORCE_READ_ONLY", "GLOBAL_APP_SERVICES_CLUSTER_DEBUG_DATA_ACCESS", "ORG_MEMBER", "ORG_READ_ONLY", "ORG_BILLING_ADMIN", "ORG_GROUP_CREATOR", "ORG_OWNER", "ORG_TEAM_MEMBERS_ADMIN", "GROUP_AUTOMATION_ADMIN", "GROUP_BACKUP_ADMIN", "GROUP_MONITORING_ADMIN", "GROUP_OWNER", "GROUP_READ_ONLY", "GROUP_USER_ADMIN", "GROUP_BILLING_ADMIN", "GROUP_DATA_ACCESS_ADMIN", "GROUP_DATA_ACCESS_READ_ONLY", "GROUP_DATA_ACCESS_READ_WRITE", "GROUP_CHARTS_ADMIN", "GROUP_CLUSTER_MANAGER", "GROUP_SEARCH_INDEX_EDITOR", ] 

# roleMappings

Role mappings that are configured in this organization.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Role mappings that are configured in this organization. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RoleMappingView**](RoleMappingView.md) | [**RoleMappingView**](RoleMappingView.md) | [**RoleMappingView**](RoleMappingView.md) |  | 

# userConflicts

List that contains the users who have an email address that doesn't match any domain on the allowed list.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains the users who have an email address that doesn&#x27;t match any domain on the allowed list. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**FederatedUserView**](FederatedUserView.md) | [**FederatedUserView**](FederatedUserView.md) | [**FederatedUserView**](FederatedUserView.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

