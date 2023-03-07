# atlas.model.api_measurements_general_view_atlas.ApiMeasurementsGeneralViewAtlas

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**databaseName** | str,  | str,  | Human-readable label that identifies the database that the specified MongoDB process serves. | [optional] 
**end** | str, datetime,  | str,  | Date and time that specifies when to stop retrieving measurements. If you set **end**, you must set **start**. You can&#x27;t set this parameter and **period** in the same request. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**granularity** | str,  | str,  | Duration that specifies the interval between measurement data points. The parameter expresses its value in ISO 8601 timestamp format in UTC. If you set this parameter, you must set either **period** or **start** and **end**. | [optional] must be one of ["PT1M", "PT5M", "PT1H", "P1D", ] 
**groupId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the project. The project contains MongoDB processes that you want to return. The MongoDB process can be either the &#x60;mongod&#x60; or &#x60;mongos&#x60;. | [optional] 
**hostId** | str,  | str,  | Combination of hostname and Internet Assigned Numbers Authority (IANA) port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (&#x60;mongod&#x60; or &#x60;mongos&#x60;). The port must be the IANA port on which the MongoDB process listens for requests. | [optional] 
**[links](#links)** | list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | [optional] 
**[measurements](#measurements)** | list, tuple,  | tuple,  | List that contains measurements and their data points. | [optional] 
**partitionName** | str,  | str,  | Human-readable label of the disk or partition to which the measurements apply. | [optional] 
**processId** | str,  | str,  | Combination of hostname and Internet Assigned Numbers Authority (IANA) port that serves the MongoDB process. The host must be the hostname, fully qualified domain name (FQDN), or Internet Protocol address (IPv4 or IPv6) of the host that runs the MongoDB process (&#x60;mongod&#x60; or &#x60;mongos&#x60;). The port must be the IANA port on which the MongoDB process listens for requests. | [optional] 
**start** | str, datetime,  | str,  | Date and time that specifies when to start retrieving measurements. If you set **start**, you must set **end**. You can&#x27;t set this parameter and **period** in the same request. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# links

List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**LinkAtlas**](LinkAtlas.md) | [**LinkAtlas**](LinkAtlas.md) | [**LinkAtlas**](LinkAtlas.md) |  | 

# measurements

List that contains measurements and their data points.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains measurements and their data points. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiMeasurementViewAtlas**](ApiMeasurementViewAtlas.md) | [**ApiMeasurementViewAtlas**](ApiMeasurementViewAtlas.md) | [**ApiMeasurementViewAtlas**](ApiMeasurementViewAtlas.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
