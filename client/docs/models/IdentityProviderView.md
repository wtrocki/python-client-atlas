# atlas.model.identity_provider_view.IdentityProviderView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**oktaIdpId** | str,  | str,  | Unique 20-hexadecimal digit string that identifies the identity provider. | 
**acsUrl** | str,  | str,  | URL that points to where to send the SAML response. | [optional] 
**[associatedDomains](#associatedDomains)** | list, tuple,  | tuple,  | List that contains the domains associated with the identity provider. | [optional] 
**[associatedOrgs](#associatedOrgs)** | list, tuple,  | tuple,  | List that contains the connected organization configurations associated with the identity provider. | [optional] 
**audienceUri** | str,  | str,  | Unique string that identifies the intended audience of the SAML assertion. | [optional] 
**displayName** | str,  | str,  | Human-readable label that identifies the identity provider. | [optional] 
**issuerUri** | str,  | str,  | Unique string that identifies the issuer of the SAML Assertion. | [optional] 
**pemFileInfo** | [**PemFileInfoView**](PemFileInfoView.md) | [**PemFileInfoView**](PemFileInfoView.md) |  | [optional] 
**requestBinding** | str,  | str,  | SAML Authentication Request Protocol HTTP method binding (POST or REDIRECT) that Federated Authentication uses to send the authentication request. | [optional] must be one of ["HTTP-POST", "HTTP-REDIRECT", ] 
**responseSignatureAlgorithm** | str,  | str,  | Signature algorithm that Federated Authentication uses to encrypt the identity provider signature. | [optional] must be one of ["SHA-1", "SHA-256", ] 
**ssoDebugEnabled** | bool,  | BoolClass,  | Flag that indicates whether the identity provider has SSO debug enabled. | [optional] 
**ssoUrl** | str,  | str,  | URL that points to the receiver of the SAML authentication request. | [optional] 
**status** | str,  | str,  | String enum that indicates whether the identity provider is active. | [optional] must be one of ["ACTIVE", "INACTIVE", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# associatedDomains

List that contains the domains associated with the identity provider.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains the domains associated with the identity provider. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# associatedOrgs

List that contains the connected organization configurations associated with the identity provider.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains the connected organization configurations associated with the identity provider. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ConnectedOrgConfigView**](ConnectedOrgConfigView.md) | [**ConnectedOrgConfigView**](ConnectedOrgConfigView.md) | [**ConnectedOrgConfigView**](ConnectedOrgConfigView.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

