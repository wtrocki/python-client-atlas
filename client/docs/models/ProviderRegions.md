# atlas.model.provider_regions.ProviderRegions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[instanceSizes](#instanceSizes)** | list, tuple,  | tuple,  | List of instances sizes that this cloud provider supports. | [optional] 
**provider** | str,  | str,  | Human-readable label that identifies the Cloud provider. | [optional] must be one of ["AWS", "GSP", "AZURE", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# instanceSizes

List of instances sizes that this cloud provider supports.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of instances sizes that this cloud provider supports. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiInstanceSizeView**](ApiInstanceSizeView.md) | [**ApiInstanceSizeView**](ApiInstanceSizeView.md) | [**ApiInstanceSizeView**](ApiInstanceSizeView.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

