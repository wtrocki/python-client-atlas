# atlas.model.cloud_provider_access.CloudProviderAccess

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[awsIamRoles](#awsIamRoles)** | list, tuple,  | tuple,  | List that contains the Amazon Web Services (AWS) IAM roles registered and authorized with MongoDB Cloud. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# awsIamRoles

List that contains the Amazon Web Services (AWS) IAM roles registered and authorized with MongoDB Cloud.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains the Amazon Web Services (AWS) IAM roles registered and authorized with MongoDB Cloud. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CloudProviderAccessAWSIAMRole**](CloudProviderAccessAWSIAMRole.md) | [**CloudProviderAccessAWSIAMRole**](CloudProviderAccessAWSIAMRole.md) | [**CloudProviderAccessAWSIAMRole**](CloudProviderAccessAWSIAMRole.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

