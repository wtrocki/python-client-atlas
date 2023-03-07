# atlas.model.cluster_description_connection_strings_private_endpoint.ClusterDescriptionConnectionStringsPrivateEndpoint

Private endpoint-aware connection string that you can use to connect to this cluster through a private endpoint.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Private endpoint-aware connection string that you can use to connect to this cluster through a private endpoint. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**connectionString** | str,  | str,  | Private endpoint-aware connection string that uses the &#x60;mongodb://&#x60; protocol to connect to MongoDB Cloud through a private endpoint. | [optional] 
**[endpoints](#endpoints)** | list, tuple,  | tuple,  | List that contains the private endpoints through which you connect to MongoDB Cloud when you use **connectionStrings.privateEndpoint[n].connectionString** or **connectionStrings.privateEndpoint[n].srvConnectionString**. | [optional] 
**srvConnectionString** | str,  | str,  | Private endpoint-aware connection string that uses the &#x60;mongodb+srv://&#x60; protocol to connect to MongoDB Cloud through a private endpoint. The &#x60;mongodb+srv&#x60; protocol tells the driver to look up the seed list of hosts in the Domain Name System (DNS). This list synchronizes with the nodes in a cluster. If the connection string uses this Uniform Resource Identifier (URI) format, you don&#x27;t need to append the seed list or change the Uniform Resource Identifier (URI) if the nodes change. Use this Uniform Resource Identifier (URI) format if your application supports it. If it doesn&#x27;t, use connectionStrings.privateEndpoint[n].connectionString. | [optional] 
**srvShardOptimizedConnectionString** | str,  | str,  | Private endpoint-aware connection string optimized for sharded clusters that uses the &#x60;mongodb+srv://&#x60; protocol to connect to MongoDB Cloud through a private endpoint. If the connection string uses this Uniform Resource Identifier (URI) format, you don&#x27;t need to change the Uniform Resource Identifier (URI) if the nodes change. Use this Uniform Resource Identifier (URI) format if your application and Atlas cluster supports it. If it doesn&#x27;t, use and consult the documentation for connectionStrings.privateEndpoint[n].srvConnectionString. | [optional] 
**type** | str,  | str,  | MongoDB process type to which your application connects. Use &#x60;MONGOD&#x60; for replica sets and &#x60;MONGOS&#x60; for sharded clusters. | [optional] must be one of ["MONGOD", "MONGOS", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# endpoints

List that contains the private endpoints through which you connect to MongoDB Cloud when you use **connectionStrings.privateEndpoint[n].connectionString** or **connectionStrings.privateEndpoint[n].srvConnectionString**.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains the private endpoints through which you connect to MongoDB Cloud when you use **connectionStrings.privateEndpoint[n].connectionString** or **connectionStrings.privateEndpoint[n].srvConnectionString**. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ClusterDescriptionConnectionStringsPrivateEndpointEndpoint**](ClusterDescriptionConnectionStringsPrivateEndpointEndpoint.md) | [**ClusterDescriptionConnectionStringsPrivateEndpointEndpoint**](ClusterDescriptionConnectionStringsPrivateEndpointEndpoint.md) | [**ClusterDescriptionConnectionStringsPrivateEndpointEndpoint**](ClusterDescriptionConnectionStringsPrivateEndpointEndpoint.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

