# atlas.model.api_policy_item_view.ApiPolicyItemView

Specifications for one policy.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Specifications for one policy. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**frequencyInterval** | decimal.Decimal, int,  | decimal.Decimal,  | Number that indicates the frequency interval for a set of snapshots. A value of &#x60;1&#x60; specifies the first instance of the corresponding &#x60;frequencyType&#x60;.  - In a monthly policy item, &#x60;1&#x60; indicates that the monthly snapshot occurs on the first day of the month and &#x60;40&#x60; indicates the last day of the month.  - In a weekly policy item, &#x60;1&#x60; indicates that the weekly snapshot occurs on Monday and &#x60;7&#x60; indicates Sunday.  - In an hourly policy item, you can set the frequency interval to &#x60;1&#x60;, &#x60;2&#x60;, &#x60;4&#x60;, &#x60;6&#x60;, &#x60;8&#x60;, or &#x60;12&#x60;. For hourly policy items for NVMe clusters, MongoDB Cloud only accepts &#x60;12&#x60; as the frequency interval value. | must be one of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 40, ] value must be a 32 bit integer
**frequencyType** | str,  | str,  | Human-readable label that identifies the frequency type associated with the backup policy. | must be one of ["daily", "hourly", "monthly", "weekly", "ondemand", ] 
**retentionUnit** | str,  | str,  | Unit of time in which MongoDB Cloud measures snapshot retention. | must be one of ["days", "weeks", "months", ] 
**retentionValue** | decimal.Decimal, int,  | decimal.Decimal,  | Duration in days, weeks, or months that MongoDB Cloud retains the snapshot. For less frequent policy items, MongoDB Cloud requires that you specify a value greater than or equal to the value specified for more frequent policy items.  For example: If the hourly policy item specifies a retention of two days, you must specify two days or greater for the retention of the weekly policy item. | value must be a 32 bit integer
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies this backup policy item. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

