# atlas.model.weekly_schedule_view.WeeklyScheduleView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**type** | str,  | str,  |  | 
**dayOfWeek** | decimal.Decimal, int,  | decimal.Decimal,  | Day of the week when the scheduled archive starts. The week starts with Monday (&#x60;1&#x60;) and ends with Sunday (&#x60;7&#x60;). | [optional] value must be a 32 bit integer
**endHour** | decimal.Decimal, int,  | decimal.Decimal,  | Hour of the day when the scheduled window to run one online archive ends. | [optional] value must be a 32 bit integer
**endMinute** | decimal.Decimal, int,  | decimal.Decimal,  | Minute of the hour when the scheduled window to run one online archive ends. | [optional] value must be a 32 bit integer
**startHour** | decimal.Decimal, int,  | decimal.Decimal,  | Hour of the day when the when the scheduled window to run one online archive starts. | [optional] value must be a 32 bit integer
**startMinute** | decimal.Decimal, int,  | decimal.Decimal,  | Minute of the hour when the scheduled window to run one online archive starts. | [optional] value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

