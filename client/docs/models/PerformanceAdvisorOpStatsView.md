# atlas.model.performance_advisor_op_stats_view.PerformanceAdvisorOpStatsView

Details that this resource returned about the specified query.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Details that this resource returned about the specified query. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ms** | decimal.Decimal, int,  | decimal.Decimal,  | Length of time expressed during which the query finds suggested indexes among the managed namespaces in the cluster. This parameter expresses its value in milliseconds. This parameter relates to the **duration** query parameter. | [optional] value must be a 64 bit integer
**nReturned** | decimal.Decimal, int,  | decimal.Decimal,  | Number of results that the query returns. | [optional] value must be a 64 bit integer
**nScanned** | decimal.Decimal, int,  | decimal.Decimal,  | Number of documents that the query read. | [optional] value must be a 64 bit integer
**ts** | decimal.Decimal, int,  | decimal.Decimal,  | Date and time from which the query retrieves the suggested indexes. This parameter expresses its value in the number of seconds that have elapsed since the [UNIX epoch](https://en.wikipedia.org/wiki/Unix_time). This parameter relates to the **since** query parameter. | [optional] value must be a 64 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

