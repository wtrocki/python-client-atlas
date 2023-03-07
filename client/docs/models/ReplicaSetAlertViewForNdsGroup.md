# atlas.model.replica_set_alert_view_for_nds_group.ReplicaSetAlertViewForNdsGroup

ReplicaSet alert notifies about different activities on replica set of mongod instances.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | ReplicaSet alert notifies about different activities on replica set of mongod instances. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**acknowledgedUntil** | str, datetime,  | str,  | Date and time until which this alert has been acknowledged. This parameter expresses its value in the &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_8601\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;ISO 8601&lt;/a&gt; timestamp format in UTC. The resource returns this parameter if a MongoDB User previously acknowledged this alert.  - To acknowledge this alert forever, set the parameter value to 100 years in the future.  - To unacknowledge a previously acknowledged alert, set the parameter value to a date in the past. | value must conform to RFC-3339 date-time
**created** | str, datetime,  | str,  | Date and time when MongoDB Cloud created this alert. This parameter expresses its value in the &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_8601\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;ISO 8601&lt;/a&gt; timestamp format in UTC. | value must conform to RFC-3339 date-time
**alertConfigId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the alert configuration that sets this alert. | 
**eventTypeName** | [**ReplicaSetEventTypeViewForNdsGroupAlertable**](ReplicaSetEventTypeViewForNdsGroupAlertable.md) | [**ReplicaSetEventTypeViewForNdsGroupAlertable**](ReplicaSetEventTypeViewForNdsGroupAlertable.md) |  | 
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies this alert. | 
**updated** | str, datetime,  | str,  | Date and time when someone last updated this alert. This parameter expresses its value in the &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_8601\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;ISO 8601&lt;/a&gt; timestamp format in UTC. | value must conform to RFC-3339 date-time
**status** | str,  | str,  | State of this alert at the time you requested its details. | must be one of ["CANCELLED", "CLOSED", "OPEN", "TRACKING", ] 
**acknowledgementComment** | str,  | str,  | Comment that a MongoDB Cloud user submitted when acknowledging the alert. | [optional] 
**acknowledgingUsername** | str,  | str,  | MongoDB Cloud username of the person who acknowledged the alert. The response returns this parameter if a MongoDB Cloud user previously acknowledged this alert. | [optional] 
**clusterName** | str,  | str,  | Human-readable label that identifies the cluster to which this alert applies. This resource returns this parameter for alerts of events impacting backups, replica sets, or sharded clusters. | [optional] 
**groupId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the project that owns this alert. | [optional] 
**hostnameAndPort** | str,  | str,  | Hostname and port of the host to which this alert applies. The resource returns this parameter for alerts of events impacting hosts or replica sets. | [optional] 
**lastNotified** | str, datetime,  | str,  | Date and time that any notifications were last sent for this alert. This parameter expresses its value in the &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_8601\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;ISO 8601&lt;/a&gt; timestamp format in UTC. The resource returns this parameter if MongoDB Cloud has sent notifications for this alert. | [optional] value must conform to RFC-3339 date-time
**[links](#links)** | list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | [optional] 
**[nonRunningHostIds](#nonRunningHostIds)** | list, tuple,  | tuple,  |  | [optional] 
**orgId** | str,  | str,  | Unique 24-hexadecimal character string that identifies the organization that owns the project to which this alert applies. | [optional] 
**parentClusterId** | str,  | str,  | Unique 24-hexadecimal character string that identifies the parent cluster to which this alert applies. The parent cluster contains the sharded nodes. MongoDB Cloud returns this parameter only for alerts of events impacting sharded clusters. | [optional] 
**replicaSetName** | str,  | str,  | Name of the replica set to which this alert applies. The response returns this parameter for alerts of events impacting backups, hosts, or replica sets. | [optional] 
**resolved** | str, datetime,  | str,  | Date and time that this alert changed to &#x60;\&quot;status\&quot; : \&quot;CLOSED\&quot;&#x60;. This parameter expresses its value in the &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_8601\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;ISO 8601&lt;/a&gt; timestamp format in UTC. The resource returns this parameter once &#x60;\&quot;status\&quot; : \&quot;CLOSED\&quot;&#x60;. | [optional] value must conform to RFC-3339 date-time
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

# nonRunningHostIds

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | List of unique 24-hexadecimal character strings that identify the replica set members that are not in PRIMARY nor SECONDARY state. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
