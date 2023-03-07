# atlas.model.org_group_view.OrgGroupView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[clusters](#clusters)** | list, tuple,  | tuple,  | Settings that describe the clusters in each project that the API key is authorized to view. | [optional] 
**groupId** | str,  | str,  | Unique 24-hexadecimal character string that identifies the project. | [optional] 
**groupName** | str,  | str,  | Human-readable label that identifies the project. | [optional] 
**orgId** | str,  | str,  | Unique 24-hexadecimal character string that identifies the organization that contains the project. | [optional] 
**orgName** | str,  | str,  | Human-readable label that identifies the organization that contains the project. | [optional] 
**planType** | str,  | str,  | Human-readable label that indicates the plan type. | [optional] 
**[tags](#tags)** | list, tuple,  | tuple,  | List of human-readable labels that categorize the specified project. MongoDB Cloud returns an empty array. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# clusters

Settings that describe the clusters in each project that the API key is authorized to view.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Settings that describe the clusters in each project that the API key is authorized to view. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ClusterView**](ClusterView.md) | [**ClusterView**](ClusterView.md) | [**ClusterView**](ClusterView.md) |  | 

# tags

List of human-readable labels that categorize the specified project. MongoDB Cloud returns an empty array.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of human-readable labels that categorize the specified project. MongoDB Cloud returns an empty array. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

