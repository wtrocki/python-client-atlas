# atlas.model.ndsldap_verify_connectivity_job_request_validation.NDSLDAPVerifyConnectivityJobRequestValidation

One test that MongoDB Cloud runs to test verification of the provided Lightweight Directory Access Protocol (LDAP) over Transport Layer Security (TLS) configuration details.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | One test that MongoDB Cloud runs to test verification of the provided Lightweight Directory Access Protocol (LDAP) over Transport Layer Security (TLS) configuration details. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**status** | str,  | str,  | Human-readable string that indicates the result of this verification test. | [optional] must be one of ["FAIL", "OK", ] 
**validationType** | str,  | str,  | Human-readable label that identifies this verification test that MongoDB Cloud runs. | [optional] must be one of ["AUTHENTICATE", "AUTHORIZATION_ENABLED", "CONNECT", "PARSE_AUTHZ_QUERY", "QUERY_SERVER", "SERVER_SPECIFIED", "TEMPLATE", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

