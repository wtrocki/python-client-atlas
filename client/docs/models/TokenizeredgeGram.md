# atlas.model.tokenizeredge_gram.TokenizeredgeGram

Tokenizer that splits input from the left side, or \"edge\", of a text input into n-grams of given sizes. You can't use the edgeGram tokenizer in synonym or autocomplete mapping definitions.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Tokenizer that splits input from the left side, or \&quot;edge\&quot;, of a text input into n-grams of given sizes. You can&#x27;t use the edgeGram tokenizer in synonym or autocomplete mapping definitions. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**maxGram** | decimal.Decimal, int,  | decimal.Decimal,  | Characters to include in the longest token that Atlas Search creates. | 
**type** | str,  | str,  | Human-readable label that identifies this tokenizer type. | must be one of ["edgeGram", ] 
**minGram** | decimal.Decimal, int,  | decimal.Decimal,  | Characters to include in the shortest token that Atlas Search creates. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

