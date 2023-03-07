# atlas.model.team_notification_view.TeamNotificationView

Team notification configuration for MongoDB Cloud to send information when an event triggers an alert condition.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Team notification configuration for MongoDB Cloud to send information when an event triggers an alert condition. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**typeName** | str,  | str,  | Human-readable label that displays the alert notification type. | must be one of ["TEAM", ] 
**delayMin** | decimal.Decimal, int,  | decimal.Decimal,  | Number of minutes that MongoDB Cloud waits after detecting an alert condition before it sends out the first notification. | [optional] value must be a 32 bit integer
**emailEnabled** | bool,  | BoolClass,  | Flag that indicates whether MongoDB Cloud should send email notifications. The resource requires this parameter when one of the following values have been set:  - &#x60;\&quot;notifications.[n].typeName\&quot; : \&quot;ORG\&quot;&#x60; - &#x60;\&quot;notifications.[n].typeName\&quot; : \&quot;GROUP\&quot;&#x60; - &#x60;\&quot;notifications.[n].typeName\&quot; : \&quot;USER\&quot;&#x60; | [optional] 
**intervalMin** | decimal.Decimal, int,  | decimal.Decimal,  | Number of minutes to wait between successive notifications. MongoDB Cloud sends notifications until someone acknowledges the unacknowledged alert.  PagerDuty, VictorOps, and OpsGenie notifications don&#x27;t return this element. Configure and manage the notification interval within each of those services. | [optional] value must be a 32 bit integer
**smsEnabled** | bool,  | BoolClass,  | Flag that indicates whether MongoDB Cloud should send text message notifications. The resource requires this parameter when one of the following values have been set:  - &#x60;\&quot;notifications.[n].typeName\&quot; : \&quot;ORG\&quot;&#x60; - &#x60;\&quot;notifications.[n].typeName\&quot; : \&quot;GROUP\&quot;&#x60; - &#x60;\&quot;notifications.[n].typeName\&quot; : \&quot;USER\&quot;&#x60; | [optional] 
**teamId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies one MongoDB Cloud team. The resource requires this parameter when &#x60;\&quot;notifications.[n].typeName\&quot; : \&quot;TEAM\&quot;&#x60;. | [optional] 
**teamName** | str,  | str,  | Name of the MongoDB Cloud team that receives this notification. The resource requires this parameter when &#x60;\&quot;notifications.[n].typeName\&quot; : \&quot;TEAM\&quot;&#x60;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

