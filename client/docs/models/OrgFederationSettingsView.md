# atlas.model.org_federation_settings_view.OrgFederationSettingsView

Details that define how to connect one MongoDB Cloud organization to one federated authentication service.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Details that define how to connect one MongoDB Cloud organization to one federated authentication service. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[federatedDomains](#federatedDomains)** | list, tuple,  | tuple,  | List of domains associated with the organization&#x27;s identity provider. | [optional] 
**hasRoleMappings** | bool,  | BoolClass,  | Flag that indicates whether this organization has role mappings configured. | [optional] 
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies this federation. | [optional] 
**identityProviderId** | str,  | str,  | Unique 20-hexadecimal digit string that identifies the identity provider connected to this organization. | [optional] 
**identityProviderStatus** | str,  | str,  | String enum that indicates whether the identity provider is active. | [optional] must be one of ["ACTIVE", "INACTIVE", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# federatedDomains

List of domains associated with the organization's identity provider.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of domains associated with the organization&#x27;s identity provider. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

