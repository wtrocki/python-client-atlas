# atlas.model.bi_connector.BiConnector

Settings needed to configure the MongoDB Connector for Business Intelligence for this cluster.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Settings needed to configure the MongoDB Connector for Business Intelligence for this cluster. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**enabled** | bool,  | BoolClass,  | Flag that indicates whether MongoDB Connector for Business Intelligence is enabled on the specified cluster. | [optional] 
**readPreference** | str,  | str,  | Data source node designated for the MongoDB Connector for Business Intelligence on MongoDB Cloud. The MongoDB Connector for Business Intelligence on MongoDB Cloud reads data from the primary, secondary, or analytics node based on your read preferences. Defaults to &#x60;ANALYTICS&#x60; node, or &#x60;SECONDARY&#x60; if there are no &#x60;ANALYTICS&#x60; nodes. | [optional] must be one of ["PRIMARY", "SECONDARY", "ANALYTICS", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

