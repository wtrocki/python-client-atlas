# atlas.model.default_event_view_for_org.DefaultEventViewForOrg

Other events which don't have extra details beside of basic one.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Other events which don&#x27;t have extra details beside of basic one. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**created** | str, datetime,  | str,  | Date and time when this event occurred. This parameter expresses its value in the &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_8601\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;ISO 8601&lt;/a&gt; timestamp format in UTC. | value must conform to RFC-3339 date-time
**eventTypeName** | str,  | str,  | Unique identifier of event type. | must be one of ["FEDERATION_SETTINGS_CREATED", "FEDERATION_SETTINGS_DELETED", "FEDERATION_SETTINGS_UPDATED", "IDENTITY_PROVIDER_CREATED", "IDENTITY_PROVIDER_UPDATED", "IDENTITY_PROVIDER_DELETED", "IDENTITY_PROVIDER_ACTIVATED", "IDENTITY_PROVIDER_DEACTIVATED", "DOMAINS_ASSOCIATED", "DOMAIN_CREATED", "DOMAIN_DELETED", "DOMAIN_VERIFIED", "ORG_SETTINGS_CONFIGURED", "ORG_SETTINGS_UPDATED", "ORG_SETTINGS_DELETED", "RESTRICT_ORG_MEMBERSHIP_ENABLED", "RESTRICT_ORG_MEMBERSHIP_DISABLED", "ROLE_MAPPING_CREATED", "ROLE_MAPPING_UPDATED", "ROLE_MAPPING_DELETED", "GROUP_DELETED", "GROUP_CREATED", "GROUP_MOVED", "MLAB_MIGRATION_COMPLETED", "MLAB_MIGRATION_TARGET_CLUSTER_CREATED", "MLAB_MIGRATION_DATABASE_USERS_IMPORTED", "MLAB_MIGRATION_IP_WHITELIST_IMPORTED", "MLAB_MIGRATION_TARGET_CLUSTER_SET", "MLAB_MIGRATION_DATABASE_RENAMED", "MLAB_MIGRATION_LIVE_IMPORT_STARTED", "MLAB_MIGRATION_LIVE_IMPORT_READY_FOR_CUTOVER", "MLAB_MIGRATION_LIVE_IMPORT_CUTOVER_COMPLETE", "MLAB_MIGRATION_LIVE_IMPORT_ERROR", "MLAB_MIGRATION_LIVE_IMPORT_CANCELLED", "MLAB_MIGRATION_DUMP_AND_RESTORE_TEST_STARTED", "MLAB_MIGRATION_DUMP_AND_RESTORE_TEST_SKIPPED", "MLAB_MIGRATION_DUMP_AND_RESTORE_STARTED", "MLAB_MIGRATION_SUPPORT_PLAN_SELECTED", "MLAB_MIGRATION_SUPPORT_PLAN_OPTED_OUT", "AWS_SELF_SERVE_ACCOUNT_LINKED", "AWS_SELF_SERVE_ACCOUNT_LINK_PENDING", "AWS_SELF_SERVE_ACCOUNT_CANCELLED", "AWS_SELF_SERVE_ACCOUNT_LINK_FAILED", "GCP_SELF_SERVE_ACCOUNT_LINK_PENDING", "GCP_SELF_SERVE_ACCOUNT_LINK_FAILED", "AZURE_SELF_SERVE_ACCOUNT_LINKED", "AZURE_SELF_SERVE_ACCOUNT_LINK_PENDING", "AZURE_SELF_SERVE_ACCOUNT_CANCELLED", "AZURE_SELF_SERVE_ACCOUNT_LINK_FAILED", "GCP_SELF_SERVE_ACCOUNT_LINKED", "GCP_SELF_SERVE_ACCOUNT_CANCELLED", "ORG_POLICY_CREATED", "ORG_POLICY_DELETED", "ORG_POLICY_EDITED", "ORG_POLICY_CLONED", "SUPPORT_EMAILS_SENT_SUCCESSFULLY", "SUPPORT_EMAILS_SENT_FAILURE", ] 
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the event. | 
**apiKeyId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the [API Key](https://dochub.mongodb.org/core/atlas-create-prog-api-key) that triggered the event. If this resource returns this parameter, it doesn&#x27;t return the **userId** parameter. | [optional] 
**groupId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the project in which the event occurred. The **eventId** identifies the specific event. | [optional] 
**isGlobalAdmin** | bool,  | BoolClass,  | Flag that indicates whether a MongoDB employee triggered the specified event. | [optional] if omitted the server will use the default value of False
**[links](#links)** | list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | [optional] 
**orgId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the organization to which these events apply. | [optional] 
**publicKey** | str,  | str,  | Public part of the [API Key](https://dochub.mongodb.org/core/atlas-create-prog-api-key) that triggered the event. If this resource returns this parameter, it doesn&#x27;t return the **username** parameter. | [optional] 
**raw** | [**Raw**](Raw.md) | [**Raw**](Raw.md) |  | [optional] 
**remoteAddress** | str,  | str,  | IPv4 or IPv6 address from which the user triggered this event. | [optional] 
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

