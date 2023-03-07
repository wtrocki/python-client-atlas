# atlas.model.time_metric_event_view.TimeMetricEventView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**created** | str, datetime,  | str,  | Date and time when this event occurred. This parameter expresses its value in the &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_8601\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;ISO 8601&lt;/a&gt; timestamp format in UTC. | value must conform to RFC-3339 date-time
**eventTypeName** | [**HostMetricEventTypeView**](HostMetricEventTypeView.md) | [**HostMetricEventTypeView**](HostMetricEventTypeView.md) |  | 
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the event. | 
**apiKeyId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the [API Key](https://dochub.mongodb.org/core/atlas-create-prog-api-key) that triggered the event. If this resource returns this parameter, it doesn&#x27;t return the **userId** parameter. | [optional] 
**currentValue** | [**TimeMetricValueView**](TimeMetricValueView.md) | [**TimeMetricValueView**](TimeMetricValueView.md) |  | [optional] 
**groupId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the project in which the event occurred. The **eventId** identifies the specific event. | [optional] 
**isGlobalAdmin** | bool,  | BoolClass,  | Flag that indicates whether a MongoDB employee triggered the specified event. | [optional] if omitted the server will use the default value of False
**[links](#links)** | list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | [optional] 
**metricName** | str,  | str,  | Human-readable label of the metric associated with the **alertId**. This field may change type of **currentValue** field. | [optional] 
**orgId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the organization to which these events apply. | [optional] 
**port** | decimal.Decimal, int,  | decimal.Decimal,  | IANA port on which the MongoDB process listens for requests. | [optional] value must be a 32 bit integer
**publicKey** | str,  | str,  | Public part of the [API Key](https://dochub.mongodb.org/core/atlas-create-prog-api-key) that triggered the event. If this resource returns this parameter, it doesn&#x27;t return the **username** parameter. | [optional] 
**raw** | [**Raw**](Raw.md) | [**Raw**](Raw.md) |  | [optional] 
**remoteAddress** | str,  | str,  | IPv4 or IPv6 address from which the user triggered this event. | [optional] 
**replicaSetName** | str,  | str,  | Human-readable label of the replica set associated with the event. | [optional] 
**shardName** | str,  | str,  | Human-readable label of the shard associated with the event. | [optional] 
**userId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the console user who triggered the event. If this resource returns this parameter, it doesn&#x27;t return the **apiKeyId** parameter. | [optional] 
**username** | str,  | str,  | Email address for the user who triggered this event. If this resource returns this parameter, it doesn&#x27;t return the **publicApiKey** parameter. | [optional] 
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
