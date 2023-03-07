# atlas.model.custom_criteria_view.CustomCriteriaView

**CUSTOM criteria.type**.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | **CUSTOM criteria.type**. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**query** | str,  | str,  | MongoDB find query that selects documents to archive. The specified query follows the syntax of the &#x60;db.collection.find(query)&#x60; command. This query can&#x27;t use the empty document (&#x60;{}&#x60;) to return all documents. Set this parameter when **\&quot;criteria.type\&quot; : \&quot;CUSTOM\&quot;**. | 
**type** | str,  | str,  | Means by which MongoDB Cloud selects data to archive. Data can be chosen using the age of the data or a MongoDB query. **DATE** selects documents to archive based on a date. **CUSTOM** selects documents to archive based on a custom JSON query. MongoDB Cloud doesn&#x27;t support **CUSTOM** when &#x60;\&quot;collectionType\&quot;: \&quot;TIMESERIES\&quot;&#x60;. | [optional] must be one of ["DATE", "CUSTOM", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

