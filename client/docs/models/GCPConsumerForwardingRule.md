# atlas.model.gcp_consumer_forwarding_rule.GCPConsumerForwardingRule

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**endpointName** | str,  | str,  | Human-readable label that identifies the Google Cloud consumer forwarding rule that you created. | [optional] 
**ipAddress** | str,  | str,  | One Private Internet Protocol version 4 (IPv4) address to which this Google Cloud consumer forwarding rule resolves. | [optional] 
**status** | str,  | str,  | State of the MongoDB Cloud endpoint group when MongoDB Cloud received this request. | [optional] must be one of ["INITIATING", "AVAILABLE", "FAILED", "DELETING", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

