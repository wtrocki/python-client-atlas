# atlas.model.azure_provider_settings.AzureProviderSettings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**providerName** | str,  | str,  |  | 
**autoScaling** | [**AzureAutoScaling**](AzureAutoScaling.md) | [**AzureAutoScaling**](AzureAutoScaling.md) |  | [optional] 
**diskTypeName** | str,  | str,  | Disk type that corresponds to the host&#x27;s root volume for Azure instances. If omitted, the default disk type for the selected **providerSettings.instanceSizeName** applies. | [optional] must be one of ["P2", "P3", "P4", "P6", "P10", "P15", "P20", "P30", "P40", "P50", ] 
**instanceSizeName** | str,  | str,  | Cluster tier, with a default storage and memory capacity, that applies to all the data-bearing hosts in your cluster. | [optional] must be one of ["M10", "M20", "M30", "M40", "M50", "M60", "M80", "M90", "M200", "R40", "R50", "R60", "R80", "R200", "R300", "R400", "M60_NVME", "M80_NVME", "M200_NVME", "M300_NVME", "M400_NVME", "M600_NVME", ] 
**regionName** | str,  | str,  | Microsoft Azure Regions. | [optional] must be one of ["US_CENTRAL", "US_EAST", "US_EAST_2", "US_NORTH_CENTRAL", "US_WEST", "US_SOUTH_CENTRAL", "EUROPE_NORTH", "EUROPE_WEST", "US_WEST_CENTRAL", "US_WEST_2", "US_WEST_3", "CANADA_EAST", "CANADA_CENTRAL", "BRAZIL_SOUTH", "BRAZIL_SOUTHEAST", "AUSTRALIA_CENTRAL", "AUSTRALIA_CENTRAL_2", "AUSTRALIA_EAST", "AUSTRALIA_SOUTH_EAST", "GERMANY_CENTRAL", "GERMANY_NORTH_EAST", "GERMANY_WEST_CENTRAL", "GERMANY_NORTH", "SWEDEN_CENTRAL", "SWEDEN_SOUTH", "SWITZERLAND_NORTH", "SWITZERLAND_WEST", "UK_SOUTH", "UK_WEST", "NORWAY_EAST", "NORWAY_WEST", "INDIA_CENTRAL", "INDIA_SOUTH", "INDIA_WEST", "CHINA_EAST", "CHINA_NORTH", "ASIA_EAST", "JAPAN_EAST", "JAPAN_WEST", "ASIA_SOUTH_EAST", "KOREA_CENTRAL", "KOREA_SOUTH", "FRANCE_CENTRAL", "FRANCE_SOUTH", "SOUTH_AFRICA_NORTH", "SOUTH_AFRICA_WEST", "UAE_CENTRAL", "UAE_NORTH", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

