# atlas.model.google_cloud_kms.GoogleCloudKMS

Details that define the configuration of Encryption at Rest using Google Cloud Key Management Service (KMS).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Details that define the configuration of Encryption at Rest using Google Cloud Key Management Service (KMS). | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**enabled** | bool,  | BoolClass,  | Flag that indicates whether someone enabled encryption at rest for the specified  project. To disable encryption at rest using customer key management and remove the configuration details, pass only this parameter with a value of &#x60;false&#x60;. | [optional] 
**keyVersionResourceID** | str,  | str,  | Resource path that displays the key version resource ID for your Google Cloud KMS. | [optional] 
**serviceAccountKey** | str,  | str,  | JavaScript Object Notation (JSON) object that contains the Google Cloud Key Management Service (KMS). Format the JSON as a string and not as an object. | [optional] 
**valid** | bool,  | BoolClass,  | Flag that indicates whether the Google Cloud Key Management Service (KMS) encryption key can encrypt and decrypt data. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

