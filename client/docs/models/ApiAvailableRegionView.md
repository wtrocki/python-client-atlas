# atlas.model.api_available_region_view.ApiAvailableRegionView

List of regions that this cloud provider supports for this instance size.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | List of regions that this cloud provider supports for this instance size. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**default** | bool,  | BoolClass,  | Flag that indicates whether the cloud provider sets this region as its default. AWS defaults to US_EAST_1, GCP defaults to CENTRAL_US, and AZURE defaults to US_WEST_2. | [optional] 
**name** | str,  | str,  | Human-readable label that identifies the supported region. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

