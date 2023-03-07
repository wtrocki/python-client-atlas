# atlas.model.destination.Destination

Document that describes the destination of the migration.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Document that describes the destination of the migration. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**clusterName** | str,  | str,  | Label that identifies the destination cluster. | 
**groupId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the destination project. | 
**hostnameSchemaType** | str,  | str,  | The network type to use between the migration host and the target cluster. | must be one of ["PUBLIC", "PRIVATE_LINK", "VPC_PEERING", ] if omitted the server will use the default value of "PUBLIC"
**privateLinkId** | str,  | str,  | Represents the endpoint to use when the host schema type is &#x60;PRIVATE_LINK&#x60;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

