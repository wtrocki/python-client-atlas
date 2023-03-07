# atlas.model.db_resource.DBResource

Namespace to which this database user has access.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Namespace to which this database user has access. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cluster** | bool,  | BoolClass,  | Flag that indicates whether to grant the action on the cluster resource. If &#x60;true&#x60;, MongoDB Cloud ignores the **actions.resources.collection** and **actions.resources.db** parameters. | 
**collection** | str,  | str,  | Human-readable label that identifies the collection on which you grant the action to one MongoDB user. If you don&#x27;t set this parameter, you grant the action to all collections in the database specified in the **actions.resources.db** parameter. If you set &#x60;\&quot;actions.resources.cluster\&quot; : true&#x60;, MongoDB Cloud ignores this parameter. | 
**db** | str,  | str,  | Human-readable label that identifies the database on which you grant the action to one MongoDB user. If you set &#x60;\&quot;actions.resources.cluster\&quot; : true&#x60;, MongoDB Cloud ignores this parameter. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

