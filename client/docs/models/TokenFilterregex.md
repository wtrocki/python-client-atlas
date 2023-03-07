# atlas.model.token_filterregex.TokenFilterregex

Filter that applies a regular expression to each token, replacing matches with a specified string.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Filter that applies a regular expression to each token, replacing matches with a specified string. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**pattern** | str,  | str,  | Regular expression pattern to apply to each token. | 
**type** | str,  | str,  | Human-readable label that identifies this token filter type. | must be one of ["regex", ] 
**matches** | str,  | str,  | Value that indicates whether to replace only the first matching pattern or all matching patterns. | must be one of ["all", "first", ] 
**replacement** | str,  | str,  | Replacement string to substitute wherever a matching pattern occurs. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

