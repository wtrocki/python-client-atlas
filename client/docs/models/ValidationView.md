# atlas.model.validation_view.ValidationView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**_id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the validation. | [optional] 
**errorMessage** | None, str,  | NoneClass, str,  | Reason why the validation job failed. | [optional] 
**groupId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the project to validate. | [optional] 
**sourceGroupId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the source project. | [optional] 
**status** | None, str,  | NoneClass, str,  | State of the specified validation job returned at the time of the request. | [optional] must be one of ["PENDING", "SUCCESS", "FAILED", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

