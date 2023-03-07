# atlas.model.token_filtershingle.TokenFiltershingle

Filter that constructs shingles (token n-grams) from a series of tokens. You can't use this token filter in synonym or autocomplete mapping definitions.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Filter that constructs shingles (token n-grams) from a series of tokens. You can&#x27;t use this token filter in synonym or autocomplete mapping definitions. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**minShingleSize** | decimal.Decimal, int,  | decimal.Decimal,  | Value that specifies the minimum number of tokens per shingle. This value must be less than or equal to **maxShingleSize**. | 
**type** | str,  | str,  | Human-readable label that identifies this token filter type. | must be one of ["shingle", ] 
**maxShingleSize** | decimal.Decimal, int,  | decimal.Decimal,  | Value that specifies the maximum number of tokens per shingle. This value must be greater than or equal to **minShingleSize**. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

