# atlas.model.event_view_for_nds_group.EventViewForNdsGroup

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**apiKeyId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the [API Key](https://dochub.mongodb.org/core/atlas-create-prog-api-key) that triggered the event. If this resource returns this parameter, it doesn&#x27;t return the **userId** parameter. | [optional] 
**created** | str, datetime,  | str,  | Date and time when this event occurred. This parameter expresses its value in the &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_8601\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;ISO 8601&lt;/a&gt; timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**eventTypeName** | [**UserEventTypeViewForNdsGroup**](UserEventTypeViewForNdsGroup.md) | [**UserEventTypeViewForNdsGroup**](UserEventTypeViewForNdsGroup.md) |  | [optional] 
**groupId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the project in which the event occurred. The **eventId** identifies the specific event. | [optional] 
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the event. | [optional] 
**isGlobalAdmin** | bool,  | BoolClass,  | Flag that indicates whether a MongoDB employee triggered the specified event. | [optional] if omitted the server will use the default value of False
**[links](#links)** | list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | [optional] 
**orgId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the organization to which these events apply. | [optional] 
**publicKey** | str,  | str,  | Public part of the [API Key](https://dochub.mongodb.org/core/atlas-create-prog-api-key) that triggered the event. If this resource returns this parameter, it doesn&#x27;t return the **username** parameter. | [optional] 
**raw** | [**Raw**](Raw.md) | [**Raw**](Raw.md) |  | [optional] 
**remoteAddress** | str,  | str,  | IPv4 or IPv6 address from which the user triggered this event. | [optional] 
**userId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the console user who triggered the event. If this resource returns this parameter, it doesn&#x27;t return the **apiKeyId** parameter. | [optional] 
**username** | str,  | str,  | Email address for the user who triggered this event. If this resource returns this parameter, it doesn&#x27;t return the **publicApiKey** parameter. | [optional] 
**alertId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the alert associated with the event. | [optional] 
**alertConfigId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the alert configuration associated with the **alertId**. | [optional] 
**invoiceId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies of the invoice associated with the event. | [optional] 
**paymentId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the invoice payment associated with this event. | [optional] 
**shardName** | str,  | str,  | Human-readable label of the shard associated with the event. | [optional] 
**collection** | str,  | str,  | Human-readable label of the collection on which the event occurred. The resource returns this parameter when the **eventTypeName** includes &#x60;DATA_EXPLORER&#x60;. | [optional] 
**database** | str,  | str,  | Human-readable label of the database on which this incident occurred. The resource returns this parameter when &#x60;\&quot;eventTypeName\&quot; : \&quot;DATA_EXPLORER\&quot;&#x60; or &#x60;\&quot;eventTypeName\&quot; : \&quot;DATA_EXPLORER_CRUD\&quot;&#x60;. | [optional] 
**opType** | str,  | str,  | Action that the database attempted to execute when the event triggered. The response returns this parameter when &#x60;eventTypeName\&quot; : \&quot;DATA_EXPLORER\&quot;&#x60;. | [optional] 
**port** | decimal.Decimal, int,  | decimal.Decimal,  | IANA port on which the MongoDB process listens for requests. | [optional] value must be a 32 bit integer
**replicaSetName** | str,  | str,  | Human-readable label of the replica set associated with the event. | [optional] 
**currentValue** | [**HostMetricValueView**](HostMetricValueView.md) | [**HostMetricValueView**](HostMetricValueView.md) |  | [optional] 
**metricName** | str,  | str,  | Human-readable label of the metric associated with the **alertId**. This field may change type of **currentValue** field. | [optional] 
**whitelistEntry** | str,  | str,  | Entry in the list of source host addresses that the API key accepts and this event targets. | [optional] 
**endpointId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the endpoint associated with this event. | [optional] 
**providerEndpointId** | str,  | str,  | Unique identification string that the cloud provider uses to identify the private endpoint. | [optional] 
**teamId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the organization team associated with this event. | [optional] 
**targetUsername** | str,  | str,  | Email address for the console user that this event targets. The resource returns this parameter when &#x60;\&quot;eventTypeName\&quot; : \&quot;USER\&quot;&#x60;. | [optional] 
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

