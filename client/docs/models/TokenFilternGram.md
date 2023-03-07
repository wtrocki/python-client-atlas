# atlas.model.token_filtern_gram.TokenFilternGram

Filter that tokenizes input into n-grams of configured sizes. You can't use this token filter in synonym or autocomplete mapping definitions.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Filter that tokenizes input into n-grams of configured sizes. You can&#x27;t use this token filter in synonym or autocomplete mapping definitions. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**maxGram** | decimal.Decimal, int,  | decimal.Decimal,  | Value that specifies the maximum length of generated n-grams. This value must be greater than or equal to **minGram**. | 
**type** | str,  | str,  | Human-readable label that identifies this token filter type. | must be one of ["nGram", ] 
**minGram** | decimal.Decimal, int,  | decimal.Decimal,  | Value that specifies the minimum length of generated n-grams. This value must be less than or equal to **maxGram**. | 
**termNotInBounds** | str,  | str,  | Value that indicates whether to index tokens shorter than **minGram** or longer than **maxGram**. | [optional] must be one of ["omit", "include", ] if omitted the server will use the default value of "omit"
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

