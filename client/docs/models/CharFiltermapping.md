# atlas.model.char_filtermapping.CharFiltermapping

Filter that applies normalization mappings that you specify to characters.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Filter that applies normalization mappings that you specify to characters. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[mappings](#mappings)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Comma-separated list of mappings. A mapping indicates that one character or group of characters should be substituted for another, using the following format:  &#x60;&lt;original&gt; : &lt;replacement&gt;&#x60; | 
**type** | str,  | str,  | Human-readable label that identifies this character filter type. | must be one of ["mapping", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# mappings

Comma-separated list of mappings. A mapping indicates that one character or group of characters should be substituted for another, using the following format:  `<original> : <replacement>`

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Comma-separated list of mappings. A mapping indicates that one character or group of characters should be substituted for another, using the following format:  &#x60;&lt;original&gt; : &lt;replacement&gt;&#x60; | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**additionalProperties** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

