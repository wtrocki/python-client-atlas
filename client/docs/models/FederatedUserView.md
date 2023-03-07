# atlas.model.federated_user_view.FederatedUserView

MongoDB Cloud user linked to this federated authentication.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | MongoDB Cloud user linked to this federated authentication. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**firstName** | str,  | str,  | First or given name that belongs to the MongoDB Cloud user. | 
**lastName** | str,  | str,  | Last name, family name, or surname that belongs to the MongoDB Cloud user. | 
**emailAddress** | str,  | str,  | Email address of the MongoDB Cloud user linked to the federated organization. | 
**federationSettingsId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the federation to which this MongoDB Cloud user belongs. | 
**userId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies this user. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

