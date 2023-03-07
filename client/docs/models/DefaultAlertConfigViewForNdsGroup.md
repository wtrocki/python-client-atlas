# atlas.model.default_alert_config_view_for_nds_group.DefaultAlertConfigViewForNdsGroup

Other alerts which don't have extra details beside of basic one.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Other alerts which don&#x27;t have extra details beside of basic one. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**eventTypeName** | str,  | str,  | Incident that triggered this alert. | must be one of ["CREDIT_CARD_ABOUT_TO_EXPIRE", "CPS_SNAPSHOT_SUCCESSFUL", "CPS_SNAPSHOT_FALLBACK_SUCCESSFUL", "CPS_SNAPSHOT_FALLBACK_FAILED", "CPS_RESTORE_SUCCESSFUL", "CPS_EXPORT_SUCCESSFUL", "CPS_RESTORE_FAILED", "CPS_EXPORT_FAILED", "CPS_SNAPSHOT_DOWNLOAD_REQUEST_FAILED", "FTS_INDEX_DELETION_FAILED", "FTS_INDEX_BUILD_COMPLETE", "FTS_INDEX_BUILD_FAILED", "USERS_WITHOUT_MULTI_FACTOR_AUTH", "USERS_WITHOUT_MULTIFACTOR_AUTH", "MAX_M0_CLUSTERS_PER_GROUP_EXCEEDED", "CLUSTER_INSTANCE_STOP_START", "CLUSTER_INSTANCE_RESYNC_REQUESTED", "CLUSTER_INSTANCE_UPDATE_REQUESTED", "SAMPLE_DATASET_LOAD_REQUESTED", "TENANT_UPGRADE_TO_SERVERLESS_SUCCESSFUL", "TENANT_UPGRADE_TO_SERVERLESS_FAILED", "MAINTENANCE_IN_ADVANCED", "MAINTENANCE_AUTO_DEFERRED", "MAINTENANCE_STARTED", "MAINTENANCE_NO_LONGER_NEEDED", "ONLINE_ARCHIVE_INSUFFICIENT_INDEXES_CHECK", "ONLINE_ARCHIVE_MAX_CONSECUTIVE_OFFLOAD_WINDOWS_CHECK", "JOINED_GROUP", "REMOVED_FROM_GROUP", "USER_ROLES_CHANGED_AUDIT", ] 
**created** | str, datetime,  | str,  | Date and time when MongoDB Cloud created the alert configuration. This parameter expresses its value in the &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_8601\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;ISO 8601&lt;/a&gt; timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**enabled** | bool,  | BoolClass,  | Flag that indicates whether someone enabled this alert configuration for the specified project. | [optional] if omitted the server will use the default value of False
**groupId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the project that owns this alert configuration. | [optional] 
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies this alert configuration. | [optional] 
**[links](#links)** | list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | [optional] 
**[matchers](#matchers)** | list, tuple,  | tuple,  |  | [optional] 
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

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MatcherView**](MatcherView.md) | [**MatcherView**](MatcherView.md) | [**MatcherView**](MatcherView.md) |  | 

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

