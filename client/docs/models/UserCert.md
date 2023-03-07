# atlas.model.user_cert.UserCert

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**_id** | decimal.Decimal, int,  | decimal.Decimal,  | Unique 24-hexadecimal character string that identifies this certificate. | [optional] value must be a 64 bit integer
**createdAt** | str, datetime,  | str,  | Date and time when MongoDB Cloud created this certificate. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**groupId** | str,  | str,  | Unique 24-hexadecimal character string that identifies the project. | [optional] 
**[links](#links)** | list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | [optional] 
**monthsUntilExpiration** | decimal.Decimal, int,  | decimal.Decimal,  | Number of months that the certificate remains valid until it expires. | [optional] if omitted the server will use the default value of 3value must be a 32 bit integer
**notAfter** | str, datetime,  | str,  | Date and time when this certificate expires. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**subject** | str,  | str,  | Subject Alternative Name associated with this certificate. This parameter expresses its value as a distinguished name as defined in [RFC 2253](https://tools.ietf.org/html/2253). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# links

List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Link**](Link.md) | [**Link**](Link.md) | [**Link**](Link.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

