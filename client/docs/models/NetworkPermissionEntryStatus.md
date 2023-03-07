# atlas.model.network_permission_entry_status.NetworkPermissionEntryStatus

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**STATUS** | str,  | str,  | State of the access list entry when MongoDB Cloud made this request.  | Status | Activity | |---|---| | &#x60;ACTIVE&#x60; | This access list entry applies to all relevant cloud providers. | | &#x60;PENDING&#x60; | MongoDB Cloud has started to add access list entry. This access list entry may not apply to all cloud providers at the time of this request. | | &#x60;FAILED&#x60; | MongoDB Cloud didn&#x27;t succeed in adding this access list entry. |  | must be one of ["PENDING", "FAILED", "ACTIVE", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

