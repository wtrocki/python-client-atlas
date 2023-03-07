# atlas.model.cluster_description_connection_strings.ClusterDescriptionConnectionStrings

Collection of Uniform Resource Locators that point to the MongoDB database.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Collection of Uniform Resource Locators that point to the MongoDB database. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[awsPrivateLink](#awsPrivateLink)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Private endpoint-aware connection strings that use AWS-hosted clusters with Amazon Web Services (AWS) PrivateLink. Each key identifies an Amazon Web Services (AWS) interface endpoint. Each value identifies the related &#x60;mongodb://&#x60; connection string that you use to connect to MongoDB Cloud through the interface endpoint that the key names. | [optional] 
**[awsPrivateLinkSrv](#awsPrivateLinkSrv)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Private endpoint-aware connection strings that use AWS-hosted clusters with Amazon Web Services (AWS) PrivateLink. Each key identifies an Amazon Web Services (AWS) interface endpoint. Each value identifies the related &#x60;mongodb://&#x60; connection string that you use to connect to Atlas through the interface endpoint that the key names. | [optional] 
**private** | str,  | str,  | Network peering connection strings for each interface Virtual Private Cloud (VPC) endpoint that you configured to connect to this cluster. This connection string uses the &#x60;mongodb+srv://&#x60; protocol. The resource returns this parameter once someone creates a network peering connection to this cluster. This protocol tells the application to look up the host seed list in the Domain Name System (DNS). This list synchronizes with the nodes in a cluster. If the connection string uses this Uniform Resource Identifier (URI) format, you don&#x27;t need to append the seed list or change the URI if the nodes change. Use this URI format if your driver supports it. If it doesn&#x27;t, use connectionStrings.private. For Amazon Web Services (AWS) clusters, this resource returns this parameter only if you enable custom DNS. | [optional] 
**[privateEndpoint](#privateEndpoint)** | list, tuple,  | tuple,  | List of private endpoint-aware connection strings that you can use to connect to this cluster through a private endpoint. This parameter returns only if you deployed a private endpoint to all regions to which you deployed this clusters&#x27; nodes. | [optional] 
**privateSrv** | str,  | str,  | Network peering connection strings for each interface Virtual Private Cloud (VPC) endpoint that you configured to connect to this cluster. This connection string uses the &#x60;mongodb+srv://&#x60; protocol. The resource returns this parameter when someone creates a network peering connection to this cluster. This protocol tells the application to look up the host seed list in the Domain Name System (DNS). This list synchronizes with the nodes in a cluster. If the connection string uses this Uniform Resource Identifier (URI) format, you don&#x27;t need to append the seed list or change the Uniform Resource Identifier (URI) if the nodes change. Use this Uniform Resource Identifier (URI) format if your driver supports it. If it doesn&#x27;t, use &#x60;connectionStrings.private&#x60;. For Amazon Web Services (AWS) clusters, this parameter returns only if you [enable custom DNS](https://docs.atlas.mongodb.com/reference/api/aws-custom-dns-update/). | [optional] 
**standard** | str,  | str,  | Public connection string that you can use to connect to this cluster. This connection string uses the &#x60;mongodb://&#x60; protocol. | [optional] 
**standardSrv** | str,  | str,  | Public connection string that you can use to connect to this cluster. This connection string uses the &#x60;mongodb+srv://&#x60; protocol. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# awsPrivateLink

Private endpoint-aware connection strings that use AWS-hosted clusters with Amazon Web Services (AWS) PrivateLink. Each key identifies an Amazon Web Services (AWS) interface endpoint. Each value identifies the related `mongodb://` connection string that you use to connect to MongoDB Cloud through the interface endpoint that the key names.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Private endpoint-aware connection strings that use AWS-hosted clusters with Amazon Web Services (AWS) PrivateLink. Each key identifies an Amazon Web Services (AWS) interface endpoint. Each value identifies the related &#x60;mongodb://&#x60; connection string that you use to connect to MongoDB Cloud through the interface endpoint that the key names. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type Private endpoint-aware connection strings that use AWS-hosted clusters with Amazon Web Services (AWS) PrivateLink. Each key identifies an Amazon Web Services (AWS) interface endpoint. Each value identifies the related &#x60;mongodb://&#x60; connection string that you use to connect to MongoDB Cloud through the interface endpoint that the key names. | [optional] 

# awsPrivateLinkSrv

Private endpoint-aware connection strings that use AWS-hosted clusters with Amazon Web Services (AWS) PrivateLink. Each key identifies an Amazon Web Services (AWS) interface endpoint. Each value identifies the related `mongodb://` connection string that you use to connect to Atlas through the interface endpoint that the key names.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Private endpoint-aware connection strings that use AWS-hosted clusters with Amazon Web Services (AWS) PrivateLink. Each key identifies an Amazon Web Services (AWS) interface endpoint. Each value identifies the related &#x60;mongodb://&#x60; connection string that you use to connect to Atlas through the interface endpoint that the key names. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type Private endpoint-aware connection strings that use AWS-hosted clusters with Amazon Web Services (AWS) PrivateLink. Each key identifies an Amazon Web Services (AWS) interface endpoint. Each value identifies the related &#x60;mongodb://&#x60; connection string that you use to connect to Atlas through the interface endpoint that the key names. | [optional] 

# privateEndpoint

List of private endpoint-aware connection strings that you can use to connect to this cluster through a private endpoint. This parameter returns only if you deployed a private endpoint to all regions to which you deployed this clusters' nodes.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of private endpoint-aware connection strings that you can use to connect to this cluster through a private endpoint. This parameter returns only if you deployed a private endpoint to all regions to which you deployed this clusters&#x27; nodes. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ClusterDescriptionConnectionStringsPrivateEndpoint**](ClusterDescriptionConnectionStringsPrivateEndpoint.md) | [**ClusterDescriptionConnectionStringsPrivateEndpoint**](ClusterDescriptionConnectionStringsPrivateEndpoint.md) | [**ClusterDescriptionConnectionStringsPrivateEndpoint**](ClusterDescriptionConnectionStringsPrivateEndpoint.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

