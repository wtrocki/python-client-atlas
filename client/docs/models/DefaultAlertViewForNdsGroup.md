# atlas.model.default_alert_view_for_nds_group.DefaultAlertViewForNdsGroup

Other alerts which don't have extra details beside of basic one.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Other alerts which don&#x27;t have extra details beside of basic one. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**acknowledgedUntil** | str, datetime,  | str,  | Date and time until which this alert has been acknowledged. This parameter expresses its value in the &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_8601\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;ISO 8601&lt;/a&gt; timestamp format in UTC. The resource returns this parameter if a MongoDB User previously acknowledged this alert.  - To acknowledge this alert forever, set the parameter value to 100 years in the future.  - To unacknowledge a previously acknowledged alert, set the parameter value to a date in the past. | value must conform to RFC-3339 date-time
**created** | str, datetime,  | str,  | Date and time when MongoDB Cloud created this alert. This parameter expresses its value in the &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_8601\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;ISO 8601&lt;/a&gt; timestamp format in UTC. | value must conform to RFC-3339 date-time
**alertConfigId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the alert configuration that sets this alert. | 
**eventTypeName** | str,  | str,  | Incident that triggered this alert. | must be one of ["CREDIT_CARD_ABOUT_TO_EXPIRE", "PENDING_INVOICE_OVER_THRESHOLD", "DAILY_BILL_OVER_THRESHOLD", "CPS_SNAPSHOT_SUCCESSFUL", "CPS_SNAPSHOT_BEHIND", "CPS_SNAPSHOT_FALLBACK_SUCCESSFUL", "CPS_SNAPSHOT_FALLBACK_FAILED", "CPS_RESTORE_SUCCESSFUL", "CPS_EXPORT_SUCCESSFUL", "CPS_RESTORE_FAILED", "CPS_EXPORT_FAILED", "CPS_SNAPSHOT_DOWNLOAD_REQUEST_FAILED", "AWS_ENCRYPTION_KEY_NEEDS_ROTATION", "AZURE_ENCRYPTION_KEY_NEEDS_ROTATION", "GCP_ENCRYPTION_KEY_NEEDS_ROTATION", "FTS_INDEX_DELETION_FAILED", "FTS_INDEX_BUILD_COMPLETE", "FTS_INDEX_BUILD_FAILED", "USERS_WITHOUT_MULTI_FACTOR_AUTH", "USERS_WITHOUT_MULTIFACTOR_AUTH", "MAX_M0_CLUSTERS_PER_GROUP_EXCEEDED", "CLUSTER_INSTANCE_STOP_START", "CLUSTER_INSTANCE_RESYNC_REQUESTED", "CLUSTER_INSTANCE_UPDATE_REQUESTED", "SAMPLE_DATASET_LOAD_REQUESTED", "TENANT_UPGRADE_TO_SERVERLESS_SUCCESSFUL", "TENANT_UPGRADE_TO_SERVERLESS_FAILED", "MAINTENANCE_IN_ADVANCED", "MAINTENANCE_AUTO_DEFERRED", "MAINTENANCE_STARTED", "MAINTENANCE_NO_LONGER_NEEDED", "NDS_X509_USER_AUTHENTICATION_CUSTOMER_CA_EXPIRATION_CHECK", "NDS_X509_USER_AUTHENTICATION_CUSTOMER_CRL_EXPIRATION_CHECK", "NDS_X509_USER_AUTHENTICATION_MANAGED_USER_CERTS_EXPIRATION_CHECK", "ONLINE_ARCHIVE_INSUFFICIENT_INDEXES_CHECK", "ONLINE_ARCHIVE_MAX_CONSECUTIVE_OFFLOAD_WINDOWS_CHECK", "OUTSIDE_SERVERLESS_METRIC_THRESHOLD", "JOINED_GROUP", "REMOVED_FROM_GROUP", "USER_ROLES_CHANGED_AUDIT", ] 
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies this alert. | 
**updated** | str, datetime,  | str,  | Date and time when someone last updated this alert. This parameter expresses its value in the &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_8601\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;ISO 8601&lt;/a&gt; timestamp format in UTC. | value must conform to RFC-3339 date-time
**status** | str,  | str,  | State of this alert at the time you requested its details. | must be one of ["CANCELLED", "CLOSED", "OPEN", "TRACKING", ] 
**acknowledgementComment** | str,  | str,  | Comment that a MongoDB Cloud user submitted when acknowledging the alert. | [optional] 
**acknowledgingUsername** | str,  | str,  | MongoDB Cloud username of the person who acknowledged the alert. The response returns this parameter if a MongoDB Cloud user previously acknowledged this alert. | [optional] 
**groupId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the project that owns this alert. | [optional] 
**lastNotified** | str, datetime,  | str,  | Date and time that any notifications were last sent for this alert. This parameter expresses its value in the &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_8601\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;ISO 8601&lt;/a&gt; timestamp format in UTC. The resource returns this parameter if MongoDB Cloud has sent notifications for this alert. | [optional] value must conform to RFC-3339 date-time
**[links](#links)** | list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | [optional] 
**orgId** | str,  | str,  | Unique 24-hexadecimal character string that identifies the organization that owns the project to which this alert applies. | [optional] 
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

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

