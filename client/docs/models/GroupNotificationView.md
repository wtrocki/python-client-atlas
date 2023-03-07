# atlas.model.group_notification_view.GroupNotificationView

Group notification configuration for MongoDB Cloud to send information when an event triggers an alert condition.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Group notification configuration for MongoDB Cloud to send information when an event triggers an alert condition. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**typeName** | str,  | str,  | Human-readable label that displays the alert notification type. | must be one of ["GROUP", ] 
**delayMin** | decimal.Decimal, int,  | decimal.Decimal,  | Number of minutes that MongoDB Cloud waits after detecting an alert condition before it sends out the first notification. | [optional] value must be a 32 bit integer
**emailEnabled** | bool,  | BoolClass,  | Flag that indicates whether MongoDB Cloud should send email notifications. The resource requires this parameter when one of the following values have been set:  - &#x60;\&quot;notifications.[n].typeName\&quot; : \&quot;ORG\&quot;&#x60; - &#x60;\&quot;notifications.[n].typeName\&quot; : \&quot;GROUP\&quot;&#x60; - &#x60;\&quot;notifications.[n].typeName\&quot; : \&quot;USER\&quot;&#x60; | [optional] 
**intervalMin** | decimal.Decimal, int,  | decimal.Decimal,  | Number of minutes to wait between successive notifications. MongoDB Cloud sends notifications until someone acknowledges the unacknowledged alert.  PagerDuty, VictorOps, and OpsGenie notifications don&#x27;t return this element. Configure and manage the notification interval within each of those services. | [optional] value must be a 32 bit integer
**[roles](#roles)** | list, tuple,  | tuple,  | List that contains the one or more [organization](https://dochub.mongodb.org/core/atlas-org-roles) or [project roles](https://dochub.mongodb.org/core/atlas-proj-roles) that receive the configured alert. The resource requires this parameter when &#x60;\&quot;notifications.[n].typeName\&quot; : \&quot;GROUP\&quot;&#x60; or &#x60;\&quot;notifications.[n].typeName\&quot; : \&quot;ORG\&quot;&#x60;. If you include this parameter, MongoDB Cloud sends alerts only to users assigned the roles you specify in the array. If you omit this parameter, MongoDB Cloud sends alerts to users assigned any role. | [optional] 
**smsEnabled** | bool,  | BoolClass,  | Flag that indicates whether MongoDB Cloud should send text message notifications. The resource requires this parameter when one of the following values have been set:  - &#x60;\&quot;notifications.[n].typeName\&quot; : \&quot;ORG\&quot;&#x60; - &#x60;\&quot;notifications.[n].typeName\&quot; : \&quot;GROUP\&quot;&#x60; - &#x60;\&quot;notifications.[n].typeName\&quot; : \&quot;USER\&quot;&#x60; | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# roles

List that contains the one or more [organization](https://dochub.mongodb.org/core/atlas-org-roles) or [project roles](https://dochub.mongodb.org/core/atlas-proj-roles) that receive the configured alert. The resource requires this parameter when `\"notifications.[n].typeName\" : \"GROUP\"` or `\"notifications.[n].typeName\" : \"ORG\"`. If you include this parameter, MongoDB Cloud sends alerts only to users assigned the roles you specify in the array. If you omit this parameter, MongoDB Cloud sends alerts to users assigned any role.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains the one or more [organization](https://dochub.mongodb.org/core/atlas-org-roles) or [project roles](https://dochub.mongodb.org/core/atlas-proj-roles) that receive the configured alert. The resource requires this parameter when &#x60;\&quot;notifications.[n].typeName\&quot; : \&quot;GROUP\&quot;&#x60; or &#x60;\&quot;notifications.[n].typeName\&quot; : \&quot;ORG\&quot;&#x60;. If you include this parameter, MongoDB Cloud sends alerts only to users assigned the roles you specify in the array. If you omit this parameter, MongoDB Cloud sends alerts to users assigned any role. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | One organization or project role that receive the configured alert. | must be one of ["GROUP_CLUSTER_MANAGER", "GROUP_DATA_ACCESS_ADMIN", "GROUP_DATA_ACCESS_READ_ONLY", "GROUP_DATA_ACCESS_READ_WRITE", "GROUP_OWNER", "GROUP_READ_WRITE", "ORG_OWNER", "ORG_MEMBER", "ORG_GROUP_CREATOR", "ORG_BILLING_ADMIN", "ORG_READ_ONLY", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

