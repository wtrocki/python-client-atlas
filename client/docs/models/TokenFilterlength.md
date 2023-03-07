# atlas.model.token_filterlength.TokenFilterlength

Filter that removes tokens that are too short or too long.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Filter that removes tokens that are too short or too long. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  | Human-readable label that identifies this token filter type. | must be one of ["length", ] 
**max** | decimal.Decimal, int,  | decimal.Decimal,  | Number that specifies the maximum length of a token. Value must be greater than or equal to **min**. | [optional] if omitted the server will use the default value of 255
**min** | decimal.Decimal, int,  | decimal.Decimal,  | Number that specifies the minimum length of a token. This value must be less than or equal to **max**. | [optional] if omitted the server will use the default value of 0
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

