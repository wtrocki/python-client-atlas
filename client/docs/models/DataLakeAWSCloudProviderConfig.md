# atlas.model.data_lake_aws_cloud_provider_config.DataLakeAWSCloudProviderConfig

Name of the cloud service that hosts the data lake's data stores.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Name of the cloud service that hosts the data lake&#x27;s data stores. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**testS3Bucket** | str,  | str,  | Name of the S3 data bucket that the provided role ID is authorized to access.Required if specifying cloudProviderConfig. | 
**roleId** | str,  | str,  | Unique identifier of the role that the data lake can use to access the data stores.Required if specifying cloudProviderConfig. | 
**externalId** | str,  | str,  | Unique identifier associated with the Identity and Access Management (IAM) role that the data lake assumes when accessing the data stores. | [optional] 
**iamAssumedRoleARN** | str,  | str,  | Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that the data lake assumes when accessing data stores. | [optional] 
**iamUserARN** | str,  | str,  | Amazon Resource Name (ARN) of the user that the data lake assumes when accessing data stores. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

