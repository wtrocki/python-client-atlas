# atlas.model.api_instance_size_view.ApiInstanceSizeView

List of instances sizes that this cloud provider supports.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | List of instances sizes that this cloud provider supports. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[availableRegions](#availableRegions)** | list, tuple,  | tuple,  | List of regions that this cloud provider supports for this instance size. | [optional] 
**name** | str,  | str,  | Human-readable label that identifies the instance size or cluster tier. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# availableRegions

List of regions that this cloud provider supports for this instance size.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of regions that this cloud provider supports for this instance size. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiAvailableRegionView**](ApiAvailableRegionView.md) | [**ApiAvailableRegionView**](ApiAvailableRegionView.md) | [**ApiAvailableRegionView**](ApiAvailableRegionView.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

