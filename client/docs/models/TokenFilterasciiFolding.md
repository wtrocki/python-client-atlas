# atlas.model.token_filterascii_folding.TokenFilterasciiFolding

Filter that converts alphabetic, numeric, and symbolic unicode characters that are not in the Basic Latin Unicode block to their ASCII equivalents, if available.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Filter that converts alphabetic, numeric, and symbolic unicode characters that are not in the Basic Latin Unicode block to their ASCII equivalents, if available. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | Human-readable label that identifies this token filter type. | must be one of ["asciiFolding", ] 
**originalTokens** | str,  | str,  | Value that indicates whether to include or omit the original tokens in the output of the token filter.  Choose &#x60;include&#x60; if you want to support queries on both the original tokens as well as the converted forms.   Choose &#x60;omit&#x60; if you want to query only on the converted forms of the original tokens. | [optional] must be one of ["omit", "include", ] if omitted the server will use the default value of "omit"
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

