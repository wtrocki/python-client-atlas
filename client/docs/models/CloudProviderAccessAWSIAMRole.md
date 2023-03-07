# atlas.model.cloud_provider_access_awsiam_role.CloudProviderAccessAWSIAMRole

Details that describe the features linked to the Amazon Web Services (AWS) Identity and Access Management (IAM) role.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Details that describe the features linked to the Amazon Web Services (AWS) Identity and Access Management (IAM) role. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**providerName** | str,  | str,  | Human-readable label that identifies the cloud provider of the role. | must be one of ["AWS", ] 
**atlasAWSAccountArn** | str,  | str,  | Amazon Resource Name that identifies the Amazon Web Services (AWS) user account that MongoDB Cloud uses when it assumes the Identity and Access Management (IAM) role. | [optional] 
**atlasAssumedRoleExternalId** | str, uuid.UUID,  | str,  | Unique external ID that MongoDB Cloud uses when it assumes the IAM role in your Amazon Web Services (AWS) account. | [optional] value must be a uuid
**authorizedDate** | str, datetime,  | str,  | Date and time when someone authorized this role for the specified cloud service provider. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**createdDate** | str, datetime,  | str,  | Date and time when someone created this role for the specified cloud service provider. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**[featureUsages](#featureUsages)** | list, tuple,  | tuple,  | List that contains application features associated with this Amazon Web Services (AWS) Identity and Access Management (IAM) role. | [optional] 
**iamAssumedRoleArn** | str,  | str,  | Amazon Resource Name (ARN) that identifies the Amazon Web Services (AWS) Identity and Access Management (IAM) role that MongoDB Cloud assumes when it accesses resources in your AWS account. | [optional] 
**roleId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the role. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# featureUsages

List that contains application features associated with this Amazon Web Services (AWS) Identity and Access Management (IAM) role.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains application features associated with this Amazon Web Services (AWS) Identity and Access Management (IAM) role. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CloudProviderAccessFeatureUsage**](CloudProviderAccessFeatureUsage.md) | [**CloudProviderAccessFeatureUsage**](CloudProviderAccessFeatureUsage.md) | [**CloudProviderAccessFeatureUsage**](CloudProviderAccessFeatureUsage.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

