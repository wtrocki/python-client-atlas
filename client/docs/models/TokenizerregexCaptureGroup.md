# atlas.model.tokenizerregex_capture_group.TokenizerregexCaptureGroup

Tokenizer that uses a regular expression pattern to extract tokens.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Tokenizer that uses a regular expression pattern to extract tokens. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**pattern** | str,  | str,  | Regular expression to match against. | 
**type** | str,  | str,  | Human-readable label that identifies this tokenizer type. | must be one of ["regexCaptureGroup", ] 
**group** | decimal.Decimal, int,  | decimal.Decimal,  | Index of the character group within the matching expression to extract into tokens. Use &#x60;0&#x60; to extract all character groups. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

