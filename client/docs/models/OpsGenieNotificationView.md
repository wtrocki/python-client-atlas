# atlas.model.ops_genie_notification_view.OpsGenieNotificationView

OpsGenie notification configuration for MongoDB Cloud to send information when an event triggers an alert condition.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | OpsGenie notification configuration for MongoDB Cloud to send information when an event triggers an alert condition. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**typeName** | str,  | str,  | Human-readable label that displays the alert notification type. | must be one of ["OPS_GENIE", ] 
**delayMin** | decimal.Decimal, int,  | decimal.Decimal,  | Number of minutes that MongoDB Cloud waits after detecting an alert condition before it sends out the first notification. | [optional] value must be a 32 bit integer
**intervalMin** | decimal.Decimal, int,  | decimal.Decimal,  | Number of minutes to wait between successive notifications. MongoDB Cloud sends notifications until someone acknowledges the unacknowledged alert.  PagerDuty, VictorOps, and OpsGenie notifications don&#x27;t return this element. Configure and manage the notification interval within each of those services. | [optional] value must be a 32 bit integer
**opsGenieApiKey** | str,  | str,  | API Key that MongoDB Cloud needs to send this notification via Opsgenie. The resource requires this parameter when &#x60;\&quot;notifications.[n].typeName\&quot; : \&quot;OPS_GENIE\&quot;&#x60;. If the key later becomes invalid, MongoDB Cloud sends an email to the project owners. If the key remains invalid, MongoDB Cloud removes it.  **NOTE**: After you create a notification which requires an API or integration key, the key appears partially redacted when you:  * View or edit the alert through the Atlas UI.  * Query the alert for the notification through the Atlas Administration API. | [optional] 
**opsGenieRegion** | str,  | str,  | Opsgenie region that indicates which API Uniform Resource Locator (URL) to use. | [optional] must be one of ["US", "EU", ] if omitted the server will use the default value of "US"
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

