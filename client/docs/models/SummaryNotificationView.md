# atlas.model.summary_notification_view.SummaryNotificationView

Summary notification configuration for MongoDB Cloud to send information when an event triggers an alert condition.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Summary notification configuration for MongoDB Cloud to send information when an event triggers an alert condition. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**typeName** | str,  | str,  | Human-readable label that displays the alert notification type. | must be one of ["SUMMARY", ] 
**delayMin** | decimal.Decimal, int,  | decimal.Decimal,  | Number of minutes that MongoDB Cloud waits after detecting an alert condition before it sends out the first notification. | [optional] value must be a 32 bit integer
**emailAddress** | str,  | str,  | Email address to which MongoDB Cloud sends alert notifications. The resource requires this parameter when &#x60;\&quot;notifications.[n].typeName\&quot; : \&quot;EMAIL\&quot;&#x60;. You don’t need to set this value to send emails to individual or groups of MongoDB Cloud users including:  - specific MongoDB Cloud users (&#x60;\&quot;notifications.[n].typeName\&quot; : \&quot;USER\&quot;&#x60;) - MongoDB Cloud users with specific project roles (&#x60;\&quot;notifications.[n].typeName\&quot; : \&quot;GROUP\&quot;&#x60;) - MongoDB Cloud users with specific organization roles (&#x60;\&quot;notifications.[n].typeName\&quot; : \&quot;ORG\&quot;&#x60;) - MongoDB Cloud teams (&#x60;\&quot;notifications.[n].typeName\&quot; : \&quot;TEAM\&quot;&#x60;)  To send emails to one MongoDB Cloud user or grouping of users, set the **notifications.[n].emailEnabled** parameter. | [optional] 
**intervalMin** | decimal.Decimal, int,  | decimal.Decimal,  | Number of minutes to wait between successive notifications. MongoDB Cloud sends notifications until someone acknowledges the unacknowledged alert.  PagerDuty, VictorOps, and OpsGenie notifications don&#x27;t return this element. Configure and manage the notification interval within each of those services. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

