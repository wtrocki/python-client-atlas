# atlas.model.nds_notification_view.NDSNotificationView

NDS notification configuration for MongoDB Cloud to send information when an event triggers an alert condition.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | NDS notification configuration for MongoDB Cloud to send information when an event triggers an alert condition. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**typeName** | str,  | str,  | Human-readable label that displays the alert notification type. | must be one of ["NDS", ] 
**delayMin** | decimal.Decimal, int,  | decimal.Decimal,  | Number of minutes that MongoDB Cloud waits after detecting an alert condition before it sends out the first notification. | [optional] value must be a 32 bit integer
**intervalMin** | decimal.Decimal, int,  | decimal.Decimal,  | Number of minutes to wait between successive notifications. MongoDB Cloud sends notifications until someone acknowledges the unacknowledged alert.  PagerDuty, VictorOps, and OpsGenie notifications don&#x27;t return this element. Configure and manage the notification interval within each of those services. | [optional] value must be a 32 bit integer
**severity** | str,  | str,  | Degree of seriousness given to this notification. | [optional] must be one of ["CRITICAL", "ERROR", "WARNING", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

