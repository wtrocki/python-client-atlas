# atlas.model.gcp_peer_vpc.GCPPeerVpc

Group of Network Peering connection settings.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Group of Network Peering connection settings. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**gcpProjectId** | str,  | str,  | Human-readable label that identifies the GCP project that contains the network that you want to peer with the MongoDB Cloud VPC. | 
**networkName** | str,  | str,  | Human-readable label that identifies the network to peer with the MongoDB Cloud VPC. | 
**containerId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the MongoDB Cloud network container that contains the specified network peering connection. | 
**errorMessage** | str,  | str,  | Details of the error returned when requesting a GCP network peering resource. The resource returns &#x60;null&#x60; if the request succeeded. | [optional] 
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the network peering connection. | [optional] 
**status** | str,  | str,  | State of the network peering connection at the time you made the request. | [optional] must be one of ["ADDING_PEER", "WAITING_FOR_USER", "AVAILABLE", "FAILED", "DELETING", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

