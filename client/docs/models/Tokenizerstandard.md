# atlas.model.tokenizerstandard.Tokenizerstandard

Tokenizer that splits tokens based on word break rules from the Unicode Text Segmentation algorithm.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Tokenizer that splits tokens based on word break rules from the Unicode Text Segmentation algorithm. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | Human-readable label that identifies this tokenizer type. | must be one of ["standard", ] 
**maxTokenLength** | decimal.Decimal, int,  | decimal.Decimal,  | Maximum number of characters in a single token. Tokens greater than this length are split at this length into multiple tokens. | [optional] if omitted the server will use the default value of 255
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

