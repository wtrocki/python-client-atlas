# atlas.model.group_maintenance_window.GroupMaintenanceWindow

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dayOfWeek** | decimal.Decimal, int,  | decimal.Decimal,  | One-based integer that represents the day of the week that the maintenance window starts.  | Value | Day of Week | |---|---| | &#x60;1&#x60; | Sunday | | &#x60;2&#x60; | Monday | | &#x60;3&#x60; | Tuesday | | &#x60;4&#x60; | Wednesday | | &#x60;5&#x60; | Thursday | | &#x60;6&#x60; | Friday | | &#x60;7&#x60; | Saturday |  | value must be a 32 bit integer
**hourOfDay** | decimal.Decimal, int,  | decimal.Decimal,  | Zero-based integer that represents the hour of the of the day that the maintenance window starts according to a 24-hour clock. Use &#x60;0&#x60; for midnight and &#x60;12&#x60; for noon. | value must be a 32 bit integer
**autoDeferOnceEnabled** | bool,  | BoolClass,  | Flag that indicates whether MongoDB Cloud should defer all maintenance windows for one week after you enable them. | [optional] 
**startASAP** | bool,  | BoolClass,  | Flag that indicates whether MongoDB Cloud starts the maintenance window immediately upon receiving this request. To start the maintenance window immediately for your project, MongoDB Cloud must have maintenance scheduled and you must set a maintenance window. This flag resets to &#x60;false&#x60; after MongoDB Cloud completes maintenance. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

