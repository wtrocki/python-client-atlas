# atlas.model.cluster_outage_simulation.ClusterOutageSimulation

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**clusterName** | str,  | str,  | Human-readable label that identifies the cluster that undergoes outage simulation. | [optional] 
**groupId** | str,  | str,  | Unique 24-hexadecimal character string that identifies the project that contains the cluster to undergo outage simulation. | [optional] 
**id** | str,  | str,  | Unique 24-hexadecimal character string that identifies the outage simulation. | [optional] 
**[outageFilters](#outageFilters)** | list, tuple,  | tuple,  | List of settings that specify the type of cluster outage simulation. | [optional] 
**startRequestDate** | str, datetime,  | str,  | Date and time when MongoDB Cloud started the regional outage simulation. | [optional] value must conform to RFC-3339 date-time
**state** | str,  | str,  | Phase of the outage simulation.  | State       | Indication | |-------------|------------| | &#x60;START_REQUESTED&#x60;    | User has requested cluster outage simulation.| | &#x60;STARTING&#x60;           | MongoDB Cloud is starting cluster outage simulation.| | &#x60;SIMULATING&#x60;         | MongoDB Cloud is simulating cluster outage.| | &#x60;RECOVERY_REQUESTED&#x60; | User has requested recovery from the simulated outage.| | &#x60;RECOVERING&#x60;         | MongoDB Cloud is recovering the cluster from the simulated outage.| | &#x60;COMPLETE&#x60;           | MongoDB Cloud has completed the cluster outage simulation.| | [optional] must be one of ["START_REQUESTED", "STARTING", "SIMULATING", "RECOVERY_REQUESTED", "RECOVERING", "COMPLETE", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# outageFilters

List of settings that specify the type of cluster outage simulation.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of settings that specify the type of cluster outage simulation. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ClusterOutageSimulationOutageFilter**](ClusterOutageSimulationOutageFilter.md) | [**ClusterOutageSimulationOutageFilter**](ClusterOutageSimulationOutageFilter.md) | [**ClusterOutageSimulationOutageFilter**](ClusterOutageSimulationOutageFilter.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

