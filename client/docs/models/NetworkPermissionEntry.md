# atlas.model.network_permission_entry.NetworkPermissionEntry

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**awsSecurityGroup** | str,  | str,  | Unique string of the Amazon Web Services (AWS) security group that you want to add to the project&#x27;s IP access list. Your IP access list entry can be one **awsSecurityGroup**, one **cidrBlock**, or one **ipAddress**. You must configure Virtual Private Connection (VPC) peering for your project before you can add an AWS security group to an IP access list. You cannot set AWS security groups as temporary access list entries. Don&#x27;t set this parameter if you set **cidrBlock** or **ipAddress**. | [optional] 
**cidrBlock** | str,  | str,  | Range of IP addresses in Classless Inter-Domain Routing (CIDR) notation that you want to add to the project&#x27;s IP access list. Your IP access list entry can be one **awsSecurityGroup**, one **cidrBlock**, or one **ipAddress**. Don&#x27;t set this parameter if you set **awsSecurityGroup** or **ipAddress**. | [optional] 
**comment** | str,  | str,  | Remark that explains the purpose or scope of this IP access list entry. | [optional] 
**deleteAfterDate** | str, datetime,  | str,  | Date and time after which MongoDB Cloud deletes the temporary access list entry. This parameter expresses its value in the ISO 8601 timestamp format in UTC and can include the time zone designation. The date must be later than the current date but no later than one week after you submit this request. The resource returns this parameter if you specified an expiration date when creating this IP access list entry. | [optional] value must conform to RFC-3339 date-time
**groupId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the project that contains the IP access list to which you want to add one or more entries. | [optional] 
**ipAddress** | str,  | str,  | IP address that you want to add to the project&#x27;s IP access list. Your IP access list entry can be one **awsSecurityGroup**, one **cidrBlock**, or one **ipAddress**. Don&#x27;t set this parameter if you set **awsSecurityGroup** or **cidrBlock**. | [optional] 
**[links](#links)** | list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# links

List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Link**](Link.md) | [**Link**](Link.md) | [**Link**](Link.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

