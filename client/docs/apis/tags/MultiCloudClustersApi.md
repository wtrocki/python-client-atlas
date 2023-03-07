<a name="__pageTop"></a>
# atlas.apis.tags.multi_cloud_clusters_api.MultiCloudClustersApi

All URIs are relative to *https://cloud.mongodb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cluster**](#create_cluster) | **post** /api/atlas/v2/groups/{groupId}/clusters | Create One Multi-Cloud Cluster from One Project
[**delete_cluster**](#delete_cluster) | **delete** /api/atlas/v2/groups/{groupId}/clusters/{clusterName} | Remove One Multi-Cloud Cluster from One Project
[**get_cluster**](#get_cluster) | **get** /api/atlas/v2/groups/{groupId}/clusters/{clusterName} | Return One Multi-Cloud Cluster from One Project
[**list_clusters**](#list_clusters) | **get** /api/atlas/v2/groups/{groupId}/clusters | Return All Multi-Cloud Clusters from One Project
[**test_failover**](#test_failover) | **post** /api/atlas/v2/groups/{groupId}/clusters/{clusterName}/restartPrimaries | Test Failover for One Multi-Cloud Cluster
[**update_cluster**](#update_cluster) | **patch** /api/atlas/v2/groups/{groupId}/clusters/{clusterName} | Modify One Multi-Cloud Cluster from One Project

# **create_cluster**
<a name="create_cluster"></a>
> ClusterDescriptionV15 create_cluster(group_idcluster_description_v15)

Create One Multi-Cloud Cluster from One Project

Creates one cluster in the specific project. Clusters contain a group of hosts that maintain the same data set. This resource can create multi-cloud clusters. To use this resource, the requesting API Key must have the Project Atlas Admin role. This resource doesn't require the API Key to have an Access List. Deprecated versions: v2-{2023-01-01}

### Example

```python
import atlas
from atlas.apis.tags import multi_cloud_clusters_api
from atlas.model.api_error import ApiError
from atlas.model.cluster_description_v15 import ClusterDescriptionV15
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = multi_cloud_clusters_api.MultiCloudClustersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    body = ClusterDescriptionV15(
        backup_enabled=False,
        bi_connector=BiConnector(
            enabled=True,
            read_preference="PRIMARY",
        ),
        cluster_type="REPLICASET",
        connection_strings=ClusterDescriptionConnectionStrings(
            aws_private_link=dict(
                "key": "key_example",
            ),
            aws_private_link_srv=dict(
                "key": "key_example",
            ),
            private="private_example",
            private_endpoint=[
                ClusterDescriptionConnectionStringsPrivateEndpoint(
                    connection_string="connection_string_example",
                    endpoints=[
                        ClusterDescriptionConnectionStringsPrivateEndpointEndpoint(
                            endpoint_id="endpoint_id_example",
                            provider_name="AWS",
                            region="region_example",
                        )
                    ],
                    srv_connection_string="srv_connection_string_example",
                    srv_shard_optimized_connection_string="srv_shard_optimized_connection_string_example",
                    type="MONGOD",
                )
            ],
            private_srv="private_srv_example",
            standard="standard_example",
            standard_srv="standard_srv_example",
        ),
        create_date="1970-01-01T00:00:00.00Z",
        disk_size_gb=10,
        encryption_at_rest_provider="NONE",
        group_id="32b6e34b3d91647abb20e7b8",
        id="32b6e34b3d91647abb20e7b8",
        labels=[
            NDSLabel(
                key="key_example",
                value="value_example",
            )
        ],
        links=[
            Link(
                href="https://cloud.mongodb.com/api/atlas",
                rel="self",
            )
        ],
        mongo_db_major_version="5.0",
        mongo_db_version="4.072888001528021798096225500850762068629.39333975650685139102691291732729478601482026",
        name="gqW,C",
        paused=True,
        pit_enabled=True,
        replication_specs=[
            ReplicationSpec(
                id="32b6e34b3d91647abb20e7b8",
                num_shards=1,
                region_configs=[
                    RegionConfig(
                        analytics_auto_scaling=AutoScalingV15(
                            compute=ComputeAutoScalingV15(
                                enabled=True,
                                max_instance_size=InstanceSize("M10"),
                                min_instance_size=InstanceSize("M10"),
                                scale_down_enabled=True,
                            ),
                            disk_gb=DiskGBAutoScaling(
                                enabled=True,
                            ),
                        ),
                        analytics_specs=DedicatedHardwareSpec(
                            node_count=1,
                            disk_iops=1,
                            ebs_volume_type="STANDARD",
                            instance_size="M10",
                        ),
                        auto_scaling=AutoScalingV15(),
,
                        electable_specs=HardwareSpec(
                            disk_iops=1,
                            ebs_volume_type="STANDARD",
                            instance_size="M0",
                            node_count=1,
                        ),
                        priority=0,
                        provider_name="AWS",
                        region_name="US_GOV_WEST_1",
                    )
                ],
                zone_name="zone_name_example",
            )
        ],
        root_cert_type="ISRGROOTX1",
        state_name="IDLE",
        termination_protection_enabled=False,
        version_release_system="LTS",
    )
    try:
        # Create One Multi-Cloud Cluster from One Project
        api_response = api_instance.create_cluster(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MultiCloudClustersApi->create_cluster: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    body = ClusterDescriptionV15(
        backup_enabled=False,
        bi_connector=BiConnector(
            enabled=True,
            read_preference="PRIMARY",
        ),
        cluster_type="REPLICASET",
        connection_strings=ClusterDescriptionConnectionStrings(
            aws_private_link=dict(
                "key": "key_example",
            ),
            aws_private_link_srv=dict(
                "key": "key_example",
            ),
            private="private_example",
            private_endpoint=[
                ClusterDescriptionConnectionStringsPrivateEndpoint(
                    connection_string="connection_string_example",
                    endpoints=[
                        ClusterDescriptionConnectionStringsPrivateEndpointEndpoint(
                            endpoint_id="endpoint_id_example",
                            provider_name="AWS",
                            region="region_example",
                        )
                    ],
                    srv_connection_string="srv_connection_string_example",
                    srv_shard_optimized_connection_string="srv_shard_optimized_connection_string_example",
                    type="MONGOD",
                )
            ],
            private_srv="private_srv_example",
            standard="standard_example",
            standard_srv="standard_srv_example",
        ),
        create_date="1970-01-01T00:00:00.00Z",
        disk_size_gb=10,
        encryption_at_rest_provider="NONE",
        group_id="32b6e34b3d91647abb20e7b8",
        id="32b6e34b3d91647abb20e7b8",
        labels=[
            NDSLabel(
                key="key_example",
                value="value_example",
            )
        ],
        links=[
            Link(
                href="https://cloud.mongodb.com/api/atlas",
                rel="self",
            )
        ],
        mongo_db_major_version="5.0",
        mongo_db_version="4.072888001528021798096225500850762068629.39333975650685139102691291732729478601482026",
        name="gqW,C",
        paused=True,
        pit_enabled=True,
        replication_specs=[
            ReplicationSpec(
                id="32b6e34b3d91647abb20e7b8",
                num_shards=1,
                region_configs=[
                    RegionConfig(
                        analytics_auto_scaling=AutoScalingV15(
                            compute=ComputeAutoScalingV15(
                                enabled=True,
                                max_instance_size=InstanceSize("M10"),
                                min_instance_size=InstanceSize("M10"),
                                scale_down_enabled=True,
                            ),
                            disk_gb=DiskGBAutoScaling(
                                enabled=True,
                            ),
                        ),
                        analytics_specs=DedicatedHardwareSpec(
                            node_count=1,
                            disk_iops=1,
                            ebs_volume_type="STANDARD",
                            instance_size="M10",
                        ),
                        auto_scaling=AutoScalingV15(),
,
                        electable_specs=HardwareSpec(
                            disk_iops=1,
                            ebs_volume_type="STANDARD",
                            instance_size="M0",
                            node_count=1,
                        ),
                        priority=0,
                        provider_name="AWS",
                        region_name="US_GOV_WEST_1",
                    )
                ],
                zone_name="zone_name_example",
            )
        ],
        root_cert_type="ISRGROOTX1",
        state_name="IDLE",
        termination_protection_enabled=False,
        version_release_system="LTS",
    )
    try:
        # Create One Multi-Cloud Cluster from One Project
        api_response = api_instance.create_cluster(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MultiCloudClustersApi->create_cluster: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationVndAtlas20230201json] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/vnd.atlas.2023-02-01+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.atlas.2023-02-01+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationVndAtlas20230201json
Type | Description  | Notes
------------- | ------------- | -------------
[**ClusterDescriptionV15**](../../models/ClusterDescriptionV15.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
envelope | EnvelopeSchema | | optional
pretty | PrettySchema | | optional


# EnvelopeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupId | GroupIdSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_cluster.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#create_cluster.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#create_cluster.ApiResponseFor401) | Unauthorized
402 | [ApiResponseFor402](#create_cluster.ApiResponseFor402) | Payment Required
403 | [ApiResponseFor403](#create_cluster.ApiResponseFor403) | Forbidden
409 | [ApiResponseFor409](#create_cluster.ApiResponseFor409) | Conflict
500 | [ApiResponseFor500](#create_cluster.ApiResponseFor500) | Internal Server Error

#### create_cluster.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationVndAtlas20230201json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationVndAtlas20230201json
Type | Description  | Notes
------------- | ------------- | -------------
[**ClusterDescriptionV15**](../../models/ClusterDescriptionV15.md) |  | 


#### create_cluster.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### create_cluster.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### create_cluster.ApiResponseFor402
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor402ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor402ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### create_cluster.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### create_cluster.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### create_cluster.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_cluster**
<a name="delete_cluster"></a>
> delete_cluster(group_idcluster_name)

Remove One Multi-Cloud Cluster from One Project

Removes one cluster with advanced features from the specified project. The cluster must have termination protection disabled in order to be deleted. To use this resource, the requesting API Key must have the Project Atlas Admin role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import multi_cloud_clusters_api
from atlas.model.api_error import ApiError
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = multi_cloud_clusters_api.MultiCloudClustersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'clusterName': "gqW,C",
    }
    query_params = {
    }
    try:
        # Remove One Multi-Cloud Cluster from One Project
        api_response = api_instance.delete_cluster(
            path_params=path_params,
            query_params=query_params,
        )
    except atlas.ApiException as e:
        print("Exception when calling MultiCloudClustersApi->delete_cluster: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'clusterName': "gqW,C",
    }
    query_params = {
        'envelope': False,
        'retainBackups': True,
    }
    try:
        # Remove One Multi-Cloud Cluster from One Project
        api_response = api_instance.delete_cluster(
            path_params=path_params,
            query_params=query_params,
        )
    except atlas.ApiException as e:
        print("Exception when calling MultiCloudClustersApi->delete_cluster: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
envelope | EnvelopeSchema | | optional
retainBackups | RetainBackupsSchema | | optional


# EnvelopeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# RetainBackupsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupId | GroupIdSchema | | 
clusterName | ClusterNameSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ClusterNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_cluster.ApiResponseFor204) | This endpoint does not return a response body.
400 | [ApiResponseFor400](#delete_cluster.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#delete_cluster.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#delete_cluster.ApiResponseFor404) | Not Found
409 | [ApiResponseFor409](#delete_cluster.ApiResponseFor409) | Conflict
500 | [ApiResponseFor500](#delete_cluster.ApiResponseFor500) | Internal Server Error

#### delete_cluster.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_cluster.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### delete_cluster.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### delete_cluster.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### delete_cluster.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### delete_cluster.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_cluster**
<a name="get_cluster"></a>
> ClusterDescriptionV15 get_cluster(group_idcluster_name)

Return One Multi-Cloud Cluster from One Project

Returns the details for one cluster in the specified project. Clusters contain a group of hosts that maintain the same data set. The response includes multi-cloud clusters. To use this resource, the requesting API Key must have the Project Read Only role. This resource doesn't require the API Key to have an Access List. Deprecated versions: v2-{2023-01-01}

### Example

```python
import atlas
from atlas.apis.tags import multi_cloud_clusters_api
from atlas.model.api_error import ApiError
from atlas.model.cluster_description_v15 import ClusterDescriptionV15
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = multi_cloud_clusters_api.MultiCloudClustersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'clusterName': "gqW,C",
    }
    query_params = {
    }
    try:
        # Return One Multi-Cloud Cluster from One Project
        api_response = api_instance.get_cluster(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MultiCloudClustersApi->get_cluster: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'clusterName': "gqW,C",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    try:
        # Return One Multi-Cloud Cluster from One Project
        api_response = api_instance.get_cluster(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MultiCloudClustersApi->get_cluster: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.atlas.2023-02-01+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
envelope | EnvelopeSchema | | optional
pretty | PrettySchema | | optional


# EnvelopeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupId | GroupIdSchema | | 
clusterName | ClusterNameSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ClusterNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_cluster.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#get_cluster.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#get_cluster.ApiResponseFor500) | Internal Server Error

#### get_cluster.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230201json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230201json
Type | Description  | Notes
------------- | ------------- | -------------
[**ClusterDescriptionV15**](../../models/ClusterDescriptionV15.md) |  | 


#### get_cluster.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_cluster.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_clusters**
<a name="list_clusters"></a>
> PaginatedClusterDescriptionV15View list_clusters(group_id)

Return All Multi-Cloud Clusters from One Project

Returns the details for all clusters in the specific project to which you have access. Clusters contain a group of hosts that maintain the same data set. The response includes multi-cloud clusters. To use this resource, the requesting API Key must have the Project Read Only role. This resource doesn't require the API Key to have an Access List. Deprecated versions: v2-{2023-01-01}

### Example

```python
import atlas
from atlas.apis.tags import multi_cloud_clusters_api
from atlas.model.paginated_cluster_description_v15_view import PaginatedClusterDescriptionV15View
from atlas.model.api_error import ApiError
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = multi_cloud_clusters_api.MultiCloudClustersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    try:
        # Return All Multi-Cloud Clusters from One Project
        api_response = api_instance.list_clusters(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MultiCloudClustersApi->list_clusters: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'envelope': False,
        'includeCount': True,
        'itemsPerPage': 100,
        'pageNum': 1,
        'pretty': False,
    }
    try:
        # Return All Multi-Cloud Clusters from One Project
        api_response = api_instance.list_clusters(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MultiCloudClustersApi->list_clusters: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.atlas.2023-02-01+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
envelope | EnvelopeSchema | | optional
includeCount | IncludeCountSchema | | optional
itemsPerPage | ItemsPerPageSchema | | optional
pageNum | PageNumSchema | | optional
pretty | PrettySchema | | optional


# EnvelopeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# IncludeCountSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of True

# ItemsPerPageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 100

# PageNumSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | if omitted the server will use the default value of 1

# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupId | GroupIdSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_clusters.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#list_clusters.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#list_clusters.ApiResponseFor500) | Internal Server Error

#### list_clusters.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230201json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230201json
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedClusterDescriptionV15View**](../../models/PaginatedClusterDescriptionV15View.md) |  | 


#### list_clusters.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### list_clusters.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **test_failover**
<a name="test_failover"></a>
> test_failover(group_idcluster_name)

Test Failover for One Multi-Cloud Cluster

Starts a failover test for the specified cluster in the specified project. Clusters contain a group of hosts that maintain the same data set. A failover test checks how MongoDB Cloud handles the failure of the cluster's primary node. During the test, MongoDB Cloud shuts down the primary node and elects a new primary. To use this resource, the requesting API Key must have the Project Cluster Manager role. This resource doesn't require the API Key to have an Access List. Deprecated versions: v2-{2023-01-01}

### Example

```python
import atlas
from atlas.apis.tags import multi_cloud_clusters_api
from atlas.model.api_error import ApiError
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = multi_cloud_clusters_api.MultiCloudClustersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'clusterName': "gqW,C",
    }
    query_params = {
    }
    try:
        # Test Failover for One Multi-Cloud Cluster
        api_response = api_instance.test_failover(
            path_params=path_params,
            query_params=query_params,
        )
    except atlas.ApiException as e:
        print("Exception when calling MultiCloudClustersApi->test_failover: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'clusterName': "gqW,C",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    try:
        # Test Failover for One Multi-Cloud Cluster
        api_response = api_instance.test_failover(
            path_params=path_params,
            query_params=query_params,
        )
    except atlas.ApiException as e:
        print("Exception when calling MultiCloudClustersApi->test_failover: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.atlas.2023-02-01+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
envelope | EnvelopeSchema | | optional
pretty | PrettySchema | | optional


# EnvelopeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupId | GroupIdSchema | | 
clusterName | ClusterNameSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ClusterNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#test_failover.ApiResponseFor204) | This endpoint does not return a response body.
401 | [ApiResponseFor401](#test_failover.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#test_failover.ApiResponseFor500) | Internal Server Error

#### test_failover.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### test_failover.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### test_failover.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_cluster**
<a name="update_cluster"></a>
> ClusterDescriptionV15 update_cluster(group_idcluster_namecluster_description_v15)

Modify One Multi-Cloud Cluster from One Project

Updates the details for one cluster in the specified project. Clusters contain a group of hosts that maintain the same data set. This resource can update multi-cloud clusters. To update a cluster's termination protection, the requesting API Key must have the Project Owner role. For all other updates, the requesting API Key must have the Project Cluster Manager role. This resource doesn't require the API Key to have an Access List. Deprecated versions: v2-{2023-01-01}

### Example

```python
import atlas
from atlas.apis.tags import multi_cloud_clusters_api
from atlas.model.api_error import ApiError
from atlas.model.cluster_description_v15 import ClusterDescriptionV15
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = multi_cloud_clusters_api.MultiCloudClustersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'clusterName': "gqW,C",
    }
    query_params = {
    }
    body = ClusterDescriptionV15(
        backup_enabled=False,
        bi_connector=BiConnector(
            enabled=True,
            read_preference="PRIMARY",
        ),
        cluster_type="REPLICASET",
        connection_strings=ClusterDescriptionConnectionStrings(
            aws_private_link=dict(
                "key": "key_example",
            ),
            aws_private_link_srv=dict(
                "key": "key_example",
            ),
            private="private_example",
            private_endpoint=[
                ClusterDescriptionConnectionStringsPrivateEndpoint(
                    connection_string="connection_string_example",
                    endpoints=[
                        ClusterDescriptionConnectionStringsPrivateEndpointEndpoint(
                            endpoint_id="endpoint_id_example",
                            provider_name="AWS",
                            region="region_example",
                        )
                    ],
                    srv_connection_string="srv_connection_string_example",
                    srv_shard_optimized_connection_string="srv_shard_optimized_connection_string_example",
                    type="MONGOD",
                )
            ],
            private_srv="private_srv_example",
            standard="standard_example",
            standard_srv="standard_srv_example",
        ),
        create_date="1970-01-01T00:00:00.00Z",
        disk_size_gb=10,
        encryption_at_rest_provider="NONE",
        group_id="32b6e34b3d91647abb20e7b8",
        id="32b6e34b3d91647abb20e7b8",
        labels=[
            NDSLabel(
                key="key_example",
                value="value_example",
            )
        ],
        links=[
            Link(
                href="https://cloud.mongodb.com/api/atlas",
                rel="self",
            )
        ],
        mongo_db_major_version="5.0",
        mongo_db_version="4.072888001528021798096225500850762068629.39333975650685139102691291732729478601482026",
        name="gqW,C",
        paused=True,
        pit_enabled=True,
        replication_specs=[
            ReplicationSpec(
                id="32b6e34b3d91647abb20e7b8",
                num_shards=1,
                region_configs=[
                    RegionConfig(
                        analytics_auto_scaling=AutoScalingV15(
                            compute=ComputeAutoScalingV15(
                                enabled=True,
                                max_instance_size=InstanceSize("M10"),
                                min_instance_size=InstanceSize("M10"),
                                scale_down_enabled=True,
                            ),
                            disk_gb=DiskGBAutoScaling(
                                enabled=True,
                            ),
                        ),
                        analytics_specs=DedicatedHardwareSpec(
                            node_count=1,
                            disk_iops=1,
                            ebs_volume_type="STANDARD",
                            instance_size="M10",
                        ),
                        auto_scaling=AutoScalingV15(),
,
                        electable_specs=HardwareSpec(
                            disk_iops=1,
                            ebs_volume_type="STANDARD",
                            instance_size="M0",
                            node_count=1,
                        ),
                        priority=0,
                        provider_name="AWS",
                        region_name="US_GOV_WEST_1",
                    )
                ],
                zone_name="zone_name_example",
            )
        ],
        root_cert_type="ISRGROOTX1",
        state_name="IDLE",
        termination_protection_enabled=False,
        version_release_system="LTS",
    )
    try:
        # Modify One Multi-Cloud Cluster from One Project
        api_response = api_instance.update_cluster(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MultiCloudClustersApi->update_cluster: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'clusterName': "gqW,C",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    body = ClusterDescriptionV15(
        backup_enabled=False,
        bi_connector=BiConnector(
            enabled=True,
            read_preference="PRIMARY",
        ),
        cluster_type="REPLICASET",
        connection_strings=ClusterDescriptionConnectionStrings(
            aws_private_link=dict(
                "key": "key_example",
            ),
            aws_private_link_srv=dict(
                "key": "key_example",
            ),
            private="private_example",
            private_endpoint=[
                ClusterDescriptionConnectionStringsPrivateEndpoint(
                    connection_string="connection_string_example",
                    endpoints=[
                        ClusterDescriptionConnectionStringsPrivateEndpointEndpoint(
                            endpoint_id="endpoint_id_example",
                            provider_name="AWS",
                            region="region_example",
                        )
                    ],
                    srv_connection_string="srv_connection_string_example",
                    srv_shard_optimized_connection_string="srv_shard_optimized_connection_string_example",
                    type="MONGOD",
                )
            ],
            private_srv="private_srv_example",
            standard="standard_example",
            standard_srv="standard_srv_example",
        ),
        create_date="1970-01-01T00:00:00.00Z",
        disk_size_gb=10,
        encryption_at_rest_provider="NONE",
        group_id="32b6e34b3d91647abb20e7b8",
        id="32b6e34b3d91647abb20e7b8",
        labels=[
            NDSLabel(
                key="key_example",
                value="value_example",
            )
        ],
        links=[
            Link(
                href="https://cloud.mongodb.com/api/atlas",
                rel="self",
            )
        ],
        mongo_db_major_version="5.0",
        mongo_db_version="4.072888001528021798096225500850762068629.39333975650685139102691291732729478601482026",
        name="gqW,C",
        paused=True,
        pit_enabled=True,
        replication_specs=[
            ReplicationSpec(
                id="32b6e34b3d91647abb20e7b8",
                num_shards=1,
                region_configs=[
                    RegionConfig(
                        analytics_auto_scaling=AutoScalingV15(
                            compute=ComputeAutoScalingV15(
                                enabled=True,
                                max_instance_size=InstanceSize("M10"),
                                min_instance_size=InstanceSize("M10"),
                                scale_down_enabled=True,
                            ),
                            disk_gb=DiskGBAutoScaling(
                                enabled=True,
                            ),
                        ),
                        analytics_specs=DedicatedHardwareSpec(
                            node_count=1,
                            disk_iops=1,
                            ebs_volume_type="STANDARD",
                            instance_size="M10",
                        ),
                        auto_scaling=AutoScalingV15(),
,
                        electable_specs=HardwareSpec(
                            disk_iops=1,
                            ebs_volume_type="STANDARD",
                            instance_size="M0",
                            node_count=1,
                        ),
                        priority=0,
                        provider_name="AWS",
                        region_name="US_GOV_WEST_1",
                    )
                ],
                zone_name="zone_name_example",
            )
        ],
        root_cert_type="ISRGROOTX1",
        state_name="IDLE",
        termination_protection_enabled=False,
        version_release_system="LTS",
    )
    try:
        # Modify One Multi-Cloud Cluster from One Project
        api_response = api_instance.update_cluster(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MultiCloudClustersApi->update_cluster: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationVndAtlas20230201json] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/vnd.atlas.2023-02-01+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.atlas.2023-02-01+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationVndAtlas20230201json
Type | Description  | Notes
------------- | ------------- | -------------
[**ClusterDescriptionV15**](../../models/ClusterDescriptionV15.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
envelope | EnvelopeSchema | | optional
pretty | PrettySchema | | optional


# EnvelopeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# PrettySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupId | GroupIdSchema | | 
clusterName | ClusterNameSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ClusterNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_cluster.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#update_cluster.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#update_cluster.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#update_cluster.ApiResponseFor404) | Not Found
409 | [ApiResponseFor409](#update_cluster.ApiResponseFor409) | Conflict
500 | [ApiResponseFor500](#update_cluster.ApiResponseFor500) | Internal Server Error

#### update_cluster.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230201json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230201json
Type | Description  | Notes
------------- | ------------- | -------------
[**ClusterDescriptionV15**](../../models/ClusterDescriptionV15.md) |  | 


#### update_cluster.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### update_cluster.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### update_cluster.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### update_cluster.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### update_cluster.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

