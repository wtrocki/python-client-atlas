# atlas.model.cluster_outage_simulation_outage_filter.ClusterOutageSimulationOutageFilter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cloudProvider** | str,  | str,  | The cloud provider of the region that undergoes the outage simulation. | [optional] must be one of ["AWS", "GCP", "AZURE", ] 
**regionName** | str,  | str,  | The name of the region to undergo an outage simulation. | [optional] 
**type** | str,  | str,  | The type of cluster outage to simulate.  | Type       | Description | |------------|-------------| | &#x60;REGION&#x60;   | Simulates a cluster outage for a region.| | [optional] must be one of ["REGION", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

