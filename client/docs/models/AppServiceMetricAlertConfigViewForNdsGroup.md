# atlas.model.app_service_metric_alert_config_view_for_nds_group.AppServiceMetricAlertConfigViewForNdsGroup

App Services metric alert configuration allows to select which app service metrics trigger alerts and how users are notified.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | App Services metric alert configuration allows to select which app service metrics trigger alerts and how users are notified. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**eventTypeName** | [**AppServiceEventTypeViewAlertableWithThreshold**](AppServiceEventTypeViewAlertableWithThreshold.md) | [**AppServiceEventTypeViewAlertableWithThreshold**](AppServiceEventTypeViewAlertableWithThreshold.md) |  | 
**created** | str, datetime,  | str,  | Date and time when MongoDB Cloud created the alert configuration. This parameter expresses its value in the &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_8601\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;ISO 8601&lt;/a&gt; timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**enabled** | bool,  | BoolClass,  | Flag that indicates whether someone enabled this alert configuration for the specified project. | [optional] if omitted the server will use the default value of False
**groupId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the project that owns this alert configuration. | [optional] 
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies this alert configuration. | [optional] 
**[links](#links)** | list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | [optional] 
**[matchers](#matchers)** | list, tuple,  | tuple,  | List of rules that determine whether MongoDB Cloud checks an object for the alert configuration. You can filter using the matchers array if the **eventTypeName** specifies an event for a host, replica set, or sharded cluster. | [optional] 
**metricThreshold** | [**AppServiceMetricThresholdView**](AppServiceMetricThresholdView.md) | [**AppServiceMetricThresholdView**](AppServiceMetricThresholdView.md) |  | [optional] 
**[notifications](#notifications)** | list, tuple,  | tuple,  | List that contains the targets that MongoDB Cloud sends notifications. | [optional] 
**updated** | str, datetime,  | str,  | Date and time when someone last updated this alert configuration. This parameter expresses its value in the &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_8601\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;ISO 8601&lt;/a&gt; timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
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

# matchers

List of rules that determine whether MongoDB Cloud checks an object for the alert configuration. You can filter using the matchers array if the **eventTypeName** specifies an event for a host, replica set, or sharded cluster.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of rules that determine whether MongoDB Cloud checks an object for the alert configuration. You can filter using the matchers array if the **eventTypeName** specifies an event for a host, replica set, or sharded cluster. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AppServiceMetricMatcherView**](AppServiceMetricMatcherView.md) | [**AppServiceMetricMatcherView**](AppServiceMetricMatcherView.md) | [**AppServiceMetricMatcherView**](AppServiceMetricMatcherView.md) |  | 

# notifications

List that contains the targets that MongoDB Cloud sends notifications.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains the targets that MongoDB Cloud sends notifications. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NotificationViewForNdsGroup**](NotificationViewForNdsGroup.md) | [**NotificationViewForNdsGroup**](NotificationViewForNdsGroup.md) | [**NotificationViewForNdsGroup**](NotificationViewForNdsGroup.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

