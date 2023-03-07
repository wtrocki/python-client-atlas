# atlas.model.api_limit_view.ApiLimitView

Details of user managed limits.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Details of user managed limits. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Human-readable label that identifies the user-managed limit to modify. | 
**value** | decimal.Decimal, int,  | decimal.Decimal,  | Amount to set the limit to. | value must be a 64 bit integer
**currentUsage** | decimal.Decimal, int,  | decimal.Decimal,  | Amount that indicates the current usage of the limit. | [optional] value must be a 64 bit integer
**defaultLimit** | decimal.Decimal, int,  | decimal.Decimal,  | Default value of the limit. | [optional] value must be a 64 bit integer
**maximumLimit** | decimal.Decimal, int,  | decimal.Decimal,  | Maximum value of the limit. | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

