# atlas.model.date_criteria_view.DateCriteriaView

**DATE criteria.type**.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | **DATE criteria.type**. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dateField** | str,  | str,  | Indexed database parameter that stores the date that determines when data moves to the online archive. MongoDB Cloud archives the data when the current date exceeds the date in this database parameter plus the number of days specified through the **expireAfterDays** parameter. Set this parameter when you set &#x60;\&quot;criteria.type\&quot; : \&quot;DATE\&quot;&#x60;. | [optional] 
**dateFormat** | str,  | str,  | Syntax used to write the date after which data moves to the online archive. Date can be expressed as ISO 8601 or Epoch timestamps. The Epoch timestamp can be expressed as nanoseconds, milliseconds, or seconds. Set this parameter when **\&quot;criteria.type\&quot; : \&quot;DATE\&quot;**. You must set **\&quot;criteria.type\&quot; : \&quot;DATE\&quot;** if **\&quot;collectionType\&quot;: \&quot;TIMESERIES\&quot;**. | [optional] must be one of ["ISODATE", "EPOCH_SECONDS", "EPOCH_MILLIS", "EPOCH_NANOSECONDS", ] if omitted the server will use the default value of "ISODATE"
**expireAfterDays** | decimal.Decimal, int,  | decimal.Decimal,  | Number of days after the value in the **criteria.dateField** when MongoDB Cloud archives data in the specified cluster. Set this parameter when you set **\&quot;criteria.type\&quot; : \&quot;DATE\&quot;**. | [optional] value must be a 32 bit integer
**type** | str,  | str,  | Means by which MongoDB Cloud selects data to archive. Data can be chosen using the age of the data or a MongoDB query. **DATE** selects documents to archive based on a date. **CUSTOM** selects documents to archive based on a custom JSON query. MongoDB Cloud doesn&#x27;t support **CUSTOM** when &#x60;\&quot;collectionType\&quot;: \&quot;TIMESERIES\&quot;&#x60;. | [optional] must be one of ["DATE", "CUSTOM", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

