# atlas.model.token_filterstopword.TokenFilterstopword

Filter that removes tokens that correspond to the specified stop words. This token filter doesn't analyze the stop words that you specify.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Filter that removes tokens that correspond to the specified stop words. This token filter doesn&#x27;t analyze the stop words that you specify. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[tokens](#tokens)** | list, tuple,  | tuple,  | The stop words that correspond to the tokens to remove. Value must be one or more stop words. | 
**type** | str,  | str,  | Human-readable label that identifies this token filter type. | must be one of ["stopword", ] 
**ignoreCase** | bool,  | BoolClass,  | Flag that indicates whether to ignore the case of stop words when filtering the tokens to remove. | [optional] if omitted the server will use the default value of True
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tokens

The stop words that correspond to the tokens to remove. Value must be one or more stop words.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The stop words that correspond to the tokens to remove. Value must be one or more stop words. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

