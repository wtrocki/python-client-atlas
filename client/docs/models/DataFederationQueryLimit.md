# atlas.model.data_federation_query_limit.DataFederationQueryLimit

Details of a query limit for Data Federation. Query limit is the limit on the amount of usage during a time period based on cost.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Details of a query limit for Data Federation. Query limit is the limit on the amount of usage during a time period based on cost. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Human-readable label that identifies the user-managed limit to modify. | 
**value** | decimal.Decimal, int,  | decimal.Decimal,  | Amount to set the limit to. | value must be a 64 bit integer
**currentUsage** | decimal.Decimal, int,  | decimal.Decimal,  | Amount that indicates the current usage of the limit. | [optional] value must be a 64 bit integer
**defaultLimit** | decimal.Decimal, int,  | decimal.Decimal,  | Default value of the limit. | [optional] value must be a 64 bit integer
**lastModifiedDate** | str, datetime,  | str,  | Only used for Data Federation limits. Timestamp that indicates when this usage limit was last modified. This field uses the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**maximumLimit** | decimal.Decimal, int,  | decimal.Decimal,  | Maximum value of the limit. | [optional] value must be a 64 bit integer
**overrunPolicy** | str,  | str,  | Only used for Data Federation limits. Action to take when the usage limit is exceeded. If limit span is set to QUERY, this is ignored because MongoDB Cloud stops the query when it exceeds the usage limit. | [optional] must be one of ["BLOCK", "BLOCK_AND_KILL", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

