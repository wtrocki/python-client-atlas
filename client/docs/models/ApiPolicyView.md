# atlas.model.api_policy_view.ApiPolicyView

List that contains a document for each backup policy item in the desired backup policy.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | List that contains a document for each backup policy item in the desired backup policy. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies this backup policy. | [optional] 
**[policyItems](#policyItems)** | list, tuple,  | tuple,  | List that contains the specifications for one policy. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# policyItems

List that contains the specifications for one policy.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains the specifications for one policy. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiPolicyItemView**](ApiPolicyItemView.md) | [**ApiPolicyItemView**](ApiPolicyItemView.md) | [**ApiPolicyItemView**](ApiPolicyItemView.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

