# atlas.model.azure_key_vault.AzureKeyVault

Details that define the configuration of Encryption at Rest using Azure Key Vault (AKV).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Details that define the configuration of Encryption at Rest using Azure Key Vault (AKV). | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**azureEnvironment** | str,  | str,  | Azure environment in which your account credentials reside. | [optional] must be one of ["AZURE", "AZURE_CHINA", "AZURE_GERMANY", ] 
**clientID** | str, uuid.UUID,  | str,  | Unique 36-hexadecimal character string that identifies an Azure application associated with your Azure Active Directory tenant. | [optional] value must be a uuid
**enabled** | bool,  | BoolClass,  | Flag that indicates whether someone enabled encryption at rest for the specified  project. To disable encryption at rest using customer key management and remove the configuration details, pass only this parameter with a value of &#x60;false&#x60;. | [optional] 
**keyIdentifier** | str,  | str,  | Web address with a unique key that identifies for your Azure Key Vault. | [optional] 
**keyVaultName** | str,  | str,  | Unique string that identifies the Azure Key Vault that contains your key. | [optional] 
**resourceGroupName** | str,  | str,  | Name of the Azure resource group that contains your Azure Key Vault. | [optional] 
**secret** | str,  | str,  | Private data that you need secured and that belongs to the specified Azure Key Vault (AKV) tenant (**azureKeyVault.tenantID**). This data can include any type of sensitive data such as passwords, database connection strings, API keys, and the like. AKV stores this information as encrypted binary data. | [optional] 
**subscriptionID** | str, uuid.UUID,  | str,  | Unique 36-hexadecimal character string that identifies your Azure subscription. | [optional] value must be a uuid
**tenantID** | str, uuid.UUID,  | str,  | Unique 36-hexadecimal character string that identifies the Azure Active Directory tenant within your Azure subscription. | [optional] value must be a uuid
**valid** | bool,  | BoolClass,  | Flag that indicates whether the Azure encryption key can encrypt and decrypt data. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

