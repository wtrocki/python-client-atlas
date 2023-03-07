# atlas.model.azure_peer_network.AzurePeerNetwork

Group of Network Peering connection settings.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Group of Network Peering connection settings. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**resourceGroupName** | str,  | str,  | Human-readable label that identifies the resource group in which the VNet to peer with the MongoDB Cloud VNet resides. | 
**azureDirectoryId** | str,  | str,  | Unique string that identifies the Azure AD directory in which the VNet peered with the MongoDB Cloud VNet resides. | 
**vnetName** | str,  | str,  | Human-readable label that identifies the VNet that you want to peer with the MongoDB Cloud VNet. | 
**containerId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the MongoDB Cloud network container that contains the specified network peering connection. | 
**azureSubscriptionId** | str,  | str,  | Unique string that identifies the Azure subscription in which the VNet you peered with the MongoDB Cloud VNet resides. | 
**errorState** | str,  | str,  | Error message returned when a requested Azure network peering resource returns &#x60;\&quot;status\&quot; : \&quot;FAILED\&quot;&#x60;. The resource returns &#x60;null&#x60; if the request succeeded. | [optional] 
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the network peering connection. | [optional] 
**status** | str,  | str,  | State of the network peering connection at the time you made the request. | [optional] must be one of ["ADDING_PEER", "AVAILABLE", "FAILED", "DELETION_FAILED", "DELETING", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

