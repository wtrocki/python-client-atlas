# atlas.model.source.Source

Document that describes the source of the migration.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Document that describes the source of the migration. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**clusterName** | str,  | str,  | Label that identifies the source cluster name. | 
**groupId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the source project. | 
**ssl** | bool,  | BoolClass,  | Flag that indicates whether you have SSL enabled. | 
**managedAuthentication** | bool,  | BoolClass,  | Flag that indicates whether MongoDB Automation manages authentication to the source cluster. If true, do not provide values for username and password. | 
**caCertificatePath** | str,  | str,  | Path to the CA certificate that signed SSL certificates use to authenticate to the source cluster. | [optional] 
**password** | str,  | str,  | Password that authenticates the username to the source cluster. | [optional] 
**username** | str,  | str,  | Label that identifies the SCRAM-SHA user that connects to the source cluster. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

