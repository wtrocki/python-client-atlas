# atlas.model.aws_peer_vpc.AWSPeerVpc

Group of Network Peering connection settings.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Group of Network Peering connection settings. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**awsAccountId** | str,  | str,  | Unique twelve-digit string that identifies the Amazon Web Services (AWS) account that owns the VPC that you peered with the MongoDB Cloud VPC. | 
**accepterRegionName** | str,  | str,  | Amazon Web Services (AWS) region where the Virtual Peering Connection (VPC) that you peered with the MongoDB Cloud VPC resides. The resource returns &#x60;null&#x60; if your VPC and the MongoDB Cloud VPC reside in the same region. | 
**vpcId** | str,  | str,  | Unique string that identifies the VPC on Amazon Web Services (AWS) that you want to peer with the MongoDB Cloud VPC. | 
**routeTableCidrBlock** | str,  | str,  | Internet Protocol (IP) addresses expressed in Classless Inter-Domain Routing (CIDR) notation of the VPC&#x27;s subnet that you want to peer with the MongoDB Cloud VPC. | 
**containerId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the MongoDB Cloud network container that contains the specified network peering connection. | 
**connectionId** | str,  | str,  | Unique string that identifies the peering connection on AWS. | [optional] 
**errorStateName** | str,  | str,  | Type of error that can be returned when requesting an Amazon Web Services (AWS) peering connection. The resource returns &#x60;null&#x60; if the request succeeded. | [optional] must be one of ["REJECTED", "EXPIRED", "INVALID_ARGUMENT", ] 
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the network peering connection. | [optional] 
**statusName** | str,  | str,  | State of the network peering connection at the time you made the request. | [optional] must be one of ["INITIATING", "PENDING_ACCEPTANCE", "FAILED", "FINALIZING", "AVAILABLE", "TERMINATING", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

