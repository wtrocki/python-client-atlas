# atlas.model.raw.Raw

Additional meta information captured about this event. The response returns this parameter as a JSON object when the query parameter `includeRaw=true`. The list of fields in the raw document may change. Don't rely on raw values for formal monitoring.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Additional meta information captured about this event. The response returns this parameter as a JSON object when the query parameter &#x60;includeRaw&#x3D;true&#x60;. The list of fields in the raw document may change. Don&#x27;t rely on raw values for formal monitoring. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**_t** | str,  | str,  | Unique identifier of event type. | [optional] 
**alertConfigId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the alert configuration related to the event. | [optional] 
**cid** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the project in which the event occurred. | [optional] 
**cre** | str, datetime,  | str,  | Date and time when this event occurred. This parameter expresses its value in the &lt;a href&#x3D;\&quot;https://en.wikipedia.org/wiki/ISO_8601\&quot; target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener noreferrer\&quot;&gt;ISO 8601&lt;/a&gt; timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**description** | str,  | str,  | Description of the event. | [optional] 
**gn** | str,  | str,  | Human-readable label that identifies the project. | [optional] 
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the event. | [optional] 
**orgId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the organization to which these events apply. | [optional] 
**orgName** | str,  | str,  | Human-readable label that identifies the organization that contains the project. | [optional] 
**severity** | str,  | str,  |  | [optional] must be one of ["INFO", "WARNING", "ERROR", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

