# atlas.model.audit_log.AuditLog

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**auditAuthorizationSuccess** | bool,  | BoolClass,  | Flag that indicates whether someone set auditing to track successful authentications. This only applies to the &#x60;\&quot;atype\&quot; : \&quot;authCheck\&quot;&#x60; audit filter. Setting this parameter to &#x60;true&#x60; degrades cluster performance. | if omitted the server will use the default value of False
**auditFilter** | str,  | str,  | JSON document that specifies which events to record. Escape any characters that may prevent parsing, such as single or double quotes, using a backslash (&#x60;\\&#x60;). | 
**enabled** | bool,  | BoolClass,  | Flag that indicates whether someone enabled database auditing for the specified project. | if omitted the server will use the default value of False
**configurationType** | str,  | str,  | Human-readable label that displays how to configure the audit filter. | [optional] must be one of ["NONE", "FILTER_BUILDER", "FILTER_JSON", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

