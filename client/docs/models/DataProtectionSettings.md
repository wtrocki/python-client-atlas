# atlas.model.data_protection_settings.DataProtectionSettings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**copyProtectionEnabled** | bool,  | BoolClass,  | Flag that indicates whether to enable additional backup copies for the cluster. | [optional] 
**encryptionAtRestEnabled** | bool,  | BoolClass,  | Flag that indicates whether Encryption at Rest using Customer Key  Management is required for all clusters with a Data Protection Policy. | [optional] 
**onDemandPolicyItem** | [**ApiPolicyItemView**](ApiPolicyItemView.md) | [**ApiPolicyItemView**](ApiPolicyItemView.md) |  | [optional] 
**pitEnabled** | bool,  | BoolClass,  | Flag that indicates whether the cluster uses Continuous Cloud Backups with a Data Protection Policy. | [optional] 
**projectId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the project for the Data Protection Policy. | [optional] 
**restoreWindowDays** | decimal.Decimal, int,  | decimal.Decimal,  | Number of previous days that you can restore back to with Continuous Cloud Backup with a Data Protection Policy. You must specify a positive, non-zero integer, and the maximum retention window can&#x27;t exceed the hourly retention time. This parameter applies only to Continuous Cloud Backups with a Data Protection Policy. | [optional] value must be a 32 bit integer
**[scheduledPolicyItems](#scheduledPolicyItems)** | list, tuple,  | tuple,  | List that contains the specifications for one scheduled policy. | [optional] 
**state** | str,  | str,  | Label that indicates the state of the Data Protection Policy settings. | [optional] must be one of ["ACTIVE", "ENABLING", "UPDATING", "DISABLING", ] 
**updatedDate** | str, datetime,  | str,  | ISO 8601 timestamp format in UTC that indicates when the user updated the Data Protection Policy settings. | [optional] value must conform to RFC-3339 date-time
**updatedUser** | str,  | str,  | Email address that identifies the user who updated the Data Protection Policy settings. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# scheduledPolicyItems

List that contains the specifications for one scheduled policy.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains the specifications for one scheduled policy. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiPolicyItemView**](ApiPolicyItemView.md) | [**ApiPolicyItemView**](ApiPolicyItemView.md) | [**ApiPolicyItemView**](ApiPolicyItemView.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

