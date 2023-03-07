# atlas.model.gcp_provider_settings.GCPProviderSettings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**providerName** | str,  | str,  |  | 
**autoScaling** | [**GCPAutoScaling**](GCPAutoScaling.md) | [**GCPAutoScaling**](GCPAutoScaling.md) |  | [optional] 
**instanceSizeName** | str,  | str,  | Cluster tier, with a default storage and memory capacity, that applies to all the data-bearing hosts in your cluster. | [optional] must be one of ["M10", "M20", "M30", "M40", "M50", "M60", "M80", "M140", "M200", "M250", "M300", "M400", "R40", "R50", "R60", "R80", "R200", "R300", "R400", "R600", ] 
**regionName** | str,  | str,  | Google Compute Regions. | [optional] must be one of ["EASTERN_US", "US_EAST_4", "US_WEST_2", "US_WEST_3", "US_WEST_4", "CENTRAL_US", "WESTERN_US", "NORTH_AMERICA_NORTHEAST_1", "NORTH_AMERICA_NORTHEAST_2", "SOUTH_AMERICA_EAST_1", "SOUTH_AMERICA_WEST_1", "WESTERN_EUROPE", "EUROPE_NORTH_1", "EUROPE_WEST_2", "EUROPE_WEST_3", "EUROPE_WEST_4", "EUROPE_WEST_6", "EUROPE_WEST_8", "EUROPE_WEST_9", "EUROPE_SOUTHWEST_1", "EUROPE_CENTRAL_2", "AUSTRALIA_SOUTHEAST_1", "AUSTRALIA_SOUTHEAST_2", "EASTERN_ASIA_PACIFIC", "NORTHEASTERN_ASIA_PACIFIC", "SOUTHEASTERN_ASIA_PACIFIC", "ASIA_EAST_2", "ASIA_NORTHEAST_2", "ASIA_NORTHEAST_3", "ASIA_SOUTH_1", "ASIA_SOUTH_2", "ASIA_SOUTHEAST_2", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

