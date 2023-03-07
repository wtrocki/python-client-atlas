<a name="__pageTop"></a>
# atlas.apis.tags.clusters_api.ClustersApi

All URIs are relative to *https://cloud.mongodb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cluster_advanced_configuration**](#get_cluster_advanced_configuration) | **get** /api/atlas/v2/groups/{groupId}/clusters/{clusterName}/processArgs | Return One Advanced Configuration Options for One Cluster
[**get_cluster_status**](#get_cluster_status) | **get** /api/atlas/v2/groups/{groupId}/clusters/{clusterName}/status | Return Status of All Cluster Operations
[**get_sample_dataset_load_status**](#get_sample_dataset_load_status) | **get** /api/atlas/v2/groups/{groupId}/sampleDatasetLoad/{sampleDatasetId} | Check Status of Cluster Sample Dataset Request
[**list_cloud_provider_regions**](#list_cloud_provider_regions) | **get** /api/atlas/v2/groups/{groupId}/clusters/provider/regions | Return All Cloud Provider Regions
[**list_clusters_for_all_projects**](#list_clusters_for_all_projects) | **get** /api/atlas/v2/clusters | Return All Authorized Clusters in All Projects
[**load_sample_dataset**](#load_sample_dataset) | **post** /api/atlas/v2/groups/{groupId}/sampleDatasetLoad/{name} | Load Sample Dataset Request into Cluster
[**update_cluster_advanced_configuration**](#update_cluster_advanced_configuration) | **patch** /api/atlas/v2/groups/{groupId}/clusters/{clusterName}/processArgs | Update Advanced Configuration Options for One Cluster
[**upgrade_shared_cluster**](#upgrade_shared_cluster) | **post** /api/atlas/v2/groups/{groupId}/clusters/tenantUpgrade | Upgrade One Shared-tier Cluster
[**upgrade_shared_cluster_to_serverless**](#upgrade_shared_cluster_to_serverless) | **post** /api/atlas/v2/groups/{groupId}/clusters/tenantUpgradeToServerless | Upgrades One Shared-Tier Cluster to the Serverless Instance

# **get_cluster_advanced_configuration**
<a name="get_cluster_advanced_configuration"></a>
> ClusterDescriptionProcessArgs get_cluster_advanced_configuration(group_idcluster_name)

Return One Advanced Configuration Options for One Cluster

Returns the advanced configuration details for one cluster in the specified project. Clusters contain a group of hosts that maintain the same data set. Advanced configuration details include the read/write concern, index and oplog limits, and other database settings.  Shared-tier clusters can't use this resource.  To use this resource, the requesting API Key must have the Project Read Only role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import clusters_api
from atlas.model.api_error import ApiError
from atlas.model.cluster_description_process_args import ClusterDescriptionProcessArgs
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clusters_api.ClustersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'clusterName': "gqW,C",
    }
    query_params = {
    }
    try:
        # Return One Advanced Configuration Options for One Cluster
        api_response = api_instance.get_cluster_advanced_configuration(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling ClustersApi->get_cluster_advanced_configuration: %s\n" % e)

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
        # Return One Advanced Configuration Options for One Cluster
        api_response = api_instance.get_cluster_advanced_configuration(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling ClustersApi->get_cluster_advanced_configuration: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.atlas.2023-01-01+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
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
200 | [ApiResponseFor200](#get_cluster_advanced_configuration.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_cluster_advanced_configuration.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_cluster_advanced_configuration.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#get_cluster_advanced_configuration.ApiResponseFor500) | Internal Server Error

#### get_cluster_advanced_configuration.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**ClusterDescriptionProcessArgs**](../../models/ClusterDescriptionProcessArgs.md) |  | 


#### get_cluster_advanced_configuration.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_cluster_advanced_configuration.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_cluster_advanced_configuration.ApiResponseFor500
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

# **get_cluster_status**
<a name="get_cluster_status"></a>
> ClusterStatus get_cluster_status(group_idcluster_name)

Return Status of All Cluster Operations

Returns the status of all changes that you made to the specified cluster in the specified project. Use this resource to check the progress MongoDB Cloud has made in processing your changes. The response does not include the deployment of new dedicated clusters. To use this resource, the requesting API Key must have the Project Read Only role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import clusters_api
from atlas.model.cluster_status import ClusterStatus
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
    api_instance = clusters_api.ClustersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'clusterName': "gqW,C",
    }
    query_params = {
    }
    try:
        # Return Status of All Cluster Operations
        api_response = api_instance.get_cluster_status(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling ClustersApi->get_cluster_status: %s\n" % e)

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
        # Return Status of All Cluster Operations
        api_response = api_instance.get_cluster_status(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling ClustersApi->get_cluster_status: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.atlas.2023-01-01+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
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
200 | [ApiResponseFor200](#get_cluster_status.ApiResponseFor200) | OK
404 | [ApiResponseFor404](#get_cluster_status.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_cluster_status.ApiResponseFor500) | Internal Server Error

#### get_cluster_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**ClusterStatus**](../../models/ClusterStatus.md) |  | 


#### get_cluster_status.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_cluster_status.ApiResponseFor500
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

# **get_sample_dataset_load_status**
<a name="get_sample_dataset_load_status"></a>
> SampleDatasetStatus get_sample_dataset_load_status(group_idsample_dataset_id)

Check Status of Cluster Sample Dataset Request

Checks the progress of loading the sample dataset into one cluster. To use this resource, the requesting API Key must have the Project Owner role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import clusters_api
from atlas.model.api_error import ApiError
from atlas.model.sample_dataset_status import SampleDatasetStatus
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clusters_api.ClustersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'sampleDatasetId': "bf325375e030fccba0091731",
    }
    query_params = {
    }
    try:
        # Check Status of Cluster Sample Dataset Request
        api_response = api_instance.get_sample_dataset_load_status(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling ClustersApi->get_sample_dataset_load_status: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'sampleDatasetId': "bf325375e030fccba0091731",
    }
    query_params = {
        'envelope': False,
    }
    try:
        # Check Status of Cluster Sample Dataset Request
        api_response = api_instance.get_sample_dataset_load_status(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling ClustersApi->get_sample_dataset_load_status: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.atlas.2023-01-01+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
envelope | EnvelopeSchema | | optional


# EnvelopeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupId | GroupIdSchema | | 
sampleDatasetId | SampleDatasetIdSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SampleDatasetIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_sample_dataset_load_status.ApiResponseFor200) | OK
404 | [ApiResponseFor404](#get_sample_dataset_load_status.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_sample_dataset_load_status.ApiResponseFor500) | Internal Server Error

#### get_sample_dataset_load_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**SampleDatasetStatus**](../../models/SampleDatasetStatus.md) |  | 


#### get_sample_dataset_load_status.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_sample_dataset_load_status.ApiResponseFor500
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

# **list_cloud_provider_regions**
<a name="list_cloud_provider_regions"></a>
> PaginatedApiAtlasProviderRegionsView list_cloud_provider_regions(group_id)

Return All Cloud Provider Regions

Returns the list of regions available for the specified cloud provider at the specified tier. To use this resource, the requesting API Key must have the Project Read Only role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import clusters_api
from atlas.model.api_error import ApiError
from atlas.model.paginated_api_atlas_provider_regions_view import PaginatedApiAtlasProviderRegionsView
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clusters_api.ClustersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    try:
        # Return All Cloud Provider Regions
        api_response = api_instance.list_cloud_provider_regions(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling ClustersApi->list_cloud_provider_regions: %s\n" % e)

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
        'providers': [
        "providers_example"
    ],
        'tier': "tier_example",
    }
    try:
        # Return All Cloud Provider Regions
        api_response = api_instance.list_cloud_provider_regions(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling ClustersApi->list_cloud_provider_regions: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.atlas.2023-01-01+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
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
providers | ProvidersSchema | | optional
tier | TierSchema | | optional


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

# ProvidersSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# TierSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

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
200 | [ApiResponseFor200](#list_cloud_provider_regions.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#list_cloud_provider_regions.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#list_cloud_provider_regions.ApiResponseFor500) | Internal Server Error

#### list_cloud_provider_regions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedApiAtlasProviderRegionsView**](../../models/PaginatedApiAtlasProviderRegionsView.md) |  | 


#### list_cloud_provider_regions.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### list_cloud_provider_regions.ApiResponseFor500
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

# **list_clusters_for_all_projects**
<a name="list_clusters_for_all_projects"></a>
> PaginatedOrgGroupView list_clusters_for_all_projects()

Return All Authorized Clusters in All Projects

Returns the details for all clusters in all projects to which you have access. Clusters contain a group of hosts that maintain the same data set. The response does not include multi-cloud clusters. To use this resource, the requesting API Key can have any cluster-level role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import clusters_api
from atlas.model.paginated_org_group_view import PaginatedOrgGroupView
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
    api_instance = clusters_api.ClustersApi(api_client)

    # example passing only optional values
    query_params = {
        'envelope': False,
        'includeCount': True,
        'itemsPerPage': 100,
        'pageNum': 1,
        'pretty': False,
    }
    try:
        # Return All Authorized Clusters in All Projects
        api_response = api_instance.list_clusters_for_all_projects(
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling ClustersApi->list_clusters_for_all_projects: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.atlas.2023-01-01+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_clusters_for_all_projects.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#list_clusters_for_all_projects.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#list_clusters_for_all_projects.ApiResponseFor500) | Internal Server Error

#### list_clusters_for_all_projects.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedOrgGroupView**](../../models/PaginatedOrgGroupView.md) |  | 


#### list_clusters_for_all_projects.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### list_clusters_for_all_projects.ApiResponseFor500
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

# **load_sample_dataset**
<a name="load_sample_dataset"></a>
> [SampleDatasetStatus] load_sample_dataset(group_idnamesample_dataset_status)

Load Sample Dataset Request into Cluster

Requests loading the MongoDB sample dataset into the specified cluster. To use this resource, the requesting API Key must have the Project Owner role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import clusters_api
from atlas.model.api_error import ApiError
from atlas.model.sample_dataset_status import SampleDatasetStatus
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clusters_api.ClustersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'name': "gqW,C",
    }
    query_params = {
    }
    body = SampleDatasetStatus(
        id="32b6e34b3d91647abb20e7b8",
        cluster_name="gqW,C",
        complete_date="1970-01-01T00:00:00.00Z",
        create_date="1970-01-01T00:00:00.00Z",
        error_message="error_message_example",
        state="WORKING",
    )
    try:
        # Load Sample Dataset Request into Cluster
        api_response = api_instance.load_sample_dataset(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling ClustersApi->load_sample_dataset: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'name': "gqW,C",
    }
    query_params = {
        'envelope': False,
    }
    body = SampleDatasetStatus(
        id="32b6e34b3d91647abb20e7b8",
        cluster_name="gqW,C",
        complete_date="1970-01-01T00:00:00.00Z",
        create_date="1970-01-01T00:00:00.00Z",
        error_message="error_message_example",
        state="WORKING",
    )
    try:
        # Load Sample Dataset Request into Cluster
        api_response = api_instance.load_sample_dataset(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling ClustersApi->load_sample_dataset: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationVndAtlas20230101json] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/vnd.atlas.2023-01-01+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.atlas.2023-01-01+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**SampleDatasetStatus**](../../models/SampleDatasetStatus.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
envelope | EnvelopeSchema | | optional


# EnvelopeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupId | GroupIdSchema | | 
name | NameSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#load_sample_dataset.ApiResponseFor201) | Created
400 | [ApiResponseFor400](#load_sample_dataset.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#load_sample_dataset.ApiResponseFor404) | Not Found
409 | [ApiResponseFor409](#load_sample_dataset.ApiResponseFor409) | Conflict
500 | [ApiResponseFor500](#load_sample_dataset.ApiResponseFor500) | Internal Server Error

#### load_sample_dataset.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationVndAtlas20230101json

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SampleDatasetStatus**]({{complexTypePrefix}}SampleDatasetStatus.md) | [**SampleDatasetStatus**]({{complexTypePrefix}}SampleDatasetStatus.md) | [**SampleDatasetStatus**]({{complexTypePrefix}}SampleDatasetStatus.md) |  | 

#### load_sample_dataset.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### load_sample_dataset.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### load_sample_dataset.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### load_sample_dataset.ApiResponseFor500
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

# **update_cluster_advanced_configuration**
<a name="update_cluster_advanced_configuration"></a>
> ClusterDescriptionProcessArgs update_cluster_advanced_configuration(group_idcluster_namecluster_description_process_args)

Update Advanced Configuration Options for One Cluster

Updates the advanced configuration details for one cluster in the specified project. Clusters contain a group of hosts that maintain the same data set. Advanced configuration details include the read/write concern, index and oplog limits, and other database settings. To use this resource, the requesting API Key must have the Project Cluster Manager role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import clusters_api
from atlas.model.api_error import ApiError
from atlas.model.cluster_description_process_args import ClusterDescriptionProcessArgs
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clusters_api.ClustersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'clusterName': "gqW,C",
    }
    query_params = {
    }
    body = ClusterDescriptionProcessArgs(
        default_read_concern="available",
        default_write_concern="1",
        fail_index_key_too_long=True,
        javascript_enabled=True,
        minimum_enabled_tls_protocol="TLS1_0",
        no_table_scan=False,
        oplog_min_retention_hours=3.14,
        oplog_size_mb=1,
        sample_refresh_interval_bi_connector=0,
        sample_size_bi_connector=1000,
    )
    try:
        # Update Advanced Configuration Options for One Cluster
        api_response = api_instance.update_cluster_advanced_configuration(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling ClustersApi->update_cluster_advanced_configuration: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'clusterName': "gqW,C",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    body = ClusterDescriptionProcessArgs(
        default_read_concern="available",
        default_write_concern="1",
        fail_index_key_too_long=True,
        javascript_enabled=True,
        minimum_enabled_tls_protocol="TLS1_0",
        no_table_scan=False,
        oplog_min_retention_hours=3.14,
        oplog_size_mb=1,
        sample_refresh_interval_bi_connector=0,
        sample_size_bi_connector=1000,
    )
    try:
        # Update Advanced Configuration Options for One Cluster
        api_response = api_instance.update_cluster_advanced_configuration(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling ClustersApi->update_cluster_advanced_configuration: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationVndAtlas20230101json] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/vnd.atlas.2023-01-01+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.atlas.2023-01-01+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**ClusterDescriptionProcessArgs**](../../models/ClusterDescriptionProcessArgs.md) |  | 


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
200 | [ApiResponseFor200](#update_cluster_advanced_configuration.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#update_cluster_advanced_configuration.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#update_cluster_advanced_configuration.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#update_cluster_advanced_configuration.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#update_cluster_advanced_configuration.ApiResponseFor500) | Internal Server Error

#### update_cluster_advanced_configuration.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**ClusterDescriptionProcessArgs**](../../models/ClusterDescriptionProcessArgs.md) |  | 


#### update_cluster_advanced_configuration.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### update_cluster_advanced_configuration.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### update_cluster_advanced_configuration.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### update_cluster_advanced_configuration.ApiResponseFor500
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

# **upgrade_shared_cluster**
<a name="upgrade_shared_cluster"></a>
> LegacyClusterDescription upgrade_shared_cluster(group_idlegacy_cluster_description)

Upgrade One Shared-tier Cluster

Upgrade a shared-tier cluster in the specified project. To use this resource, the requesting API key must have the Project Cluster Manager role. This resource doesn't require the API key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import clusters_api
from atlas.model.api_error import ApiError
from atlas.model.legacy_cluster_description import LegacyClusterDescription
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clusters_api.ClustersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    body = LegacyClusterDescription(
        auto_scaling=AutoScaling(
            compute=ComputeAutoScaling(
                enabled=True,
                scale_down_enabled=True,
            ),
            disk_gb_enabled=True,
        ),
        backup_enabled=True,
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
        mongo_uri="mongo_uri_example",
        mongo_uri_updated="1970-01-01T00:00:00.00Z",
        mongo_uri_with_options="mongo_uri_with_options_example",
        name="gqW,C",
        num_shards=1,
        paused=True,
        pit_enabled=True,
        provider_backup_enabled=True,
        provider_settings=ClusterProviderSettings(
            auto_scaling=AWSAutoScaling(
                compute=AWSComputeAutoScaling(
                    max_instance_size="M10",
                    min_instance_size="M10",
                ),
            ),
            disk_iops=1,
            encrypt_ebs_volume=True,
            instance_size_name="M10",
            region_name="US_GOV_WEST_1",
            volume_type="STANDARD",
            provider_name="AWS",
        ),
        replication_factor=3,
        replication_spec=dict(
            "key": RegionSpec(
                analytics_nodes=1,
                electable_nodes=0,
                priority=0,
                read_only_nodes=1,
            ),
        ),
        replication_specs=[
            LegacyReplicationSpec(
                id="32b6e34b3d91647abb20e7b8",
                num_shards=1,
                regions_config=dict(
                    "key": RegionSpec(),
                ),
                zone_name="zone_name_example",
            )
        ],
        root_cert_type="ISRGROOTX1",
        srv_address="srv_address_example",
        state_name="IDLE",
        termination_protection_enabled=False,
        version_release_system="LTS",
    )
    try:
        # Upgrade One Shared-tier Cluster
        api_response = api_instance.upgrade_shared_cluster(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling ClustersApi->upgrade_shared_cluster: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    body = LegacyClusterDescription(
        auto_scaling=AutoScaling(
            compute=ComputeAutoScaling(
                enabled=True,
                scale_down_enabled=True,
            ),
            disk_gb_enabled=True,
        ),
        backup_enabled=True,
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
        mongo_uri="mongo_uri_example",
        mongo_uri_updated="1970-01-01T00:00:00.00Z",
        mongo_uri_with_options="mongo_uri_with_options_example",
        name="gqW,C",
        num_shards=1,
        paused=True,
        pit_enabled=True,
        provider_backup_enabled=True,
        provider_settings=ClusterProviderSettings(
            auto_scaling=AWSAutoScaling(
                compute=AWSComputeAutoScaling(
                    max_instance_size="M10",
                    min_instance_size="M10",
                ),
            ),
            disk_iops=1,
            encrypt_ebs_volume=True,
            instance_size_name="M10",
            region_name="US_GOV_WEST_1",
            volume_type="STANDARD",
            provider_name="AWS",
        ),
        replication_factor=3,
        replication_spec=dict(
            "key": RegionSpec(
                analytics_nodes=1,
                electable_nodes=0,
                priority=0,
                read_only_nodes=1,
            ),
        ),
        replication_specs=[
            LegacyReplicationSpec(
                id="32b6e34b3d91647abb20e7b8",
                num_shards=1,
                regions_config=dict(
                    "key": RegionSpec(),
                ),
                zone_name="zone_name_example",
            )
        ],
        root_cert_type="ISRGROOTX1",
        srv_address="srv_address_example",
        state_name="IDLE",
        termination_protection_enabled=False,
        version_release_system="LTS",
    )
    try:
        # Upgrade One Shared-tier Cluster
        api_response = api_instance.upgrade_shared_cluster(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling ClustersApi->upgrade_shared_cluster: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationVndAtlas20230101json] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/vnd.atlas.2023-01-01+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.atlas.2023-01-01+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**LegacyClusterDescription**](../../models/LegacyClusterDescription.md) |  | 


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
200 | [ApiResponseFor200](#upgrade_shared_cluster.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#upgrade_shared_cluster.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#upgrade_shared_cluster.ApiResponseFor401) | Unauthorized
402 | [ApiResponseFor402](#upgrade_shared_cluster.ApiResponseFor402) | Payment Required
403 | [ApiResponseFor403](#upgrade_shared_cluster.ApiResponseFor403) | Forbidden
409 | [ApiResponseFor409](#upgrade_shared_cluster.ApiResponseFor409) | Conflict
500 | [ApiResponseFor500](#upgrade_shared_cluster.ApiResponseFor500) | Internal Server Error

#### upgrade_shared_cluster.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**LegacyClusterDescription**](../../models/LegacyClusterDescription.md) |  | 


#### upgrade_shared_cluster.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### upgrade_shared_cluster.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### upgrade_shared_cluster.ApiResponseFor402
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor402ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor402ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### upgrade_shared_cluster.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### upgrade_shared_cluster.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### upgrade_shared_cluster.ApiResponseFor500
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

# **upgrade_shared_cluster_to_serverless**
<a name="upgrade_shared_cluster_to_serverless"></a>
> ServerlessInstanceDescription upgrade_shared_cluster_to_serverless(group_idserverless_instance_description)

Upgrades One Shared-Tier Cluster to the Serverless Instance

Upgrades a shared-tier cluster to a serverless instance in the specified project. To use this resource, the requesting API key must have the Project Cluster Manager role. This resource doesn't require the API key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import clusters_api
from atlas.model.api_error import ApiError
from atlas.model.serverless_instance_description import ServerlessInstanceDescription
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = clusters_api.ClustersApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    body = ServerlessInstanceDescription(
        connection_strings=ServerlessInstanceDescriptionConnectionStrings(
            private_endpoint=[
                ServerlessInstanceDescriptionConnectionStringsPrivateEndpoint(
                    endpoints=[
                        ServerlessInstanceDescriptionConnectionStringsPrivateEndpointEndpoint(
                            endpoint_id="endpoint_id_example",
                            provider_name="AWS",
                            region="region_example",
                        )
                    ],
                    srv_connection_string="srv_connection_string_example",
                    type="MONGOS",
                )
            ],
            standard_srv="standard_srv_example",
        ),
        create_date="1970-01-01T00:00:00.00Z",
        group_id="32b6e34b3d91647abb20e7b8",
        id="32b6e34b3d91647abb20e7b8",
        links=[
            Link(
                href="https://cloud.mongodb.com/api/atlas",
                rel="self",
            )
        ],
        mongo_db_version="4.072888001528021798096225500850762068629.39333975650685139102691291732729478601482026",
        name="gqW,C",
        provider_settings=ServerlessProviderSettings(
            backing_provider_name="AWS",
            provider_name="SERVERLESS",
            region_name="region_name_example",
        ),
        serverless_backup_options=ServerlessBackupOptions(
            serverless_continuous_backup_enabled=True,
        ),
        state_name="IDLE",
        termination_protection_enabled=False,
    )
    try:
        # Upgrades One Shared-Tier Cluster to the Serverless Instance
        api_response = api_instance.upgrade_shared_cluster_to_serverless(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling ClustersApi->upgrade_shared_cluster_to_serverless: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    body = ServerlessInstanceDescription(
        connection_strings=ServerlessInstanceDescriptionConnectionStrings(
            private_endpoint=[
                ServerlessInstanceDescriptionConnectionStringsPrivateEndpoint(
                    endpoints=[
                        ServerlessInstanceDescriptionConnectionStringsPrivateEndpointEndpoint(
                            endpoint_id="endpoint_id_example",
                            provider_name="AWS",
                            region="region_example",
                        )
                    ],
                    srv_connection_string="srv_connection_string_example",
                    type="MONGOS",
                )
            ],
            standard_srv="standard_srv_example",
        ),
        create_date="1970-01-01T00:00:00.00Z",
        group_id="32b6e34b3d91647abb20e7b8",
        id="32b6e34b3d91647abb20e7b8",
        links=[
            Link(
                href="https://cloud.mongodb.com/api/atlas",
                rel="self",
            )
        ],
        mongo_db_version="4.072888001528021798096225500850762068629.39333975650685139102691291732729478601482026",
        name="gqW,C",
        provider_settings=ServerlessProviderSettings(
            backing_provider_name="AWS",
            provider_name="SERVERLESS",
            region_name="region_name_example",
        ),
        serverless_backup_options=ServerlessBackupOptions(
            serverless_continuous_backup_enabled=True,
        ),
        state_name="IDLE",
        termination_protection_enabled=False,
    )
    try:
        # Upgrades One Shared-Tier Cluster to the Serverless Instance
        api_response = api_instance.upgrade_shared_cluster_to_serverless(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling ClustersApi->upgrade_shared_cluster_to_serverless: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationVndAtlas20230101json] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/vnd.atlas.2023-01-01+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/vnd.atlas.2023-01-01+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**ServerlessInstanceDescription**](../../models/ServerlessInstanceDescription.md) |  | 


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
200 | [ApiResponseFor200](#upgrade_shared_cluster_to_serverless.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#upgrade_shared_cluster_to_serverless.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#upgrade_shared_cluster_to_serverless.ApiResponseFor401) | Unauthorized
402 | [ApiResponseFor402](#upgrade_shared_cluster_to_serverless.ApiResponseFor402) | Payment Required
403 | [ApiResponseFor403](#upgrade_shared_cluster_to_serverless.ApiResponseFor403) | Forbidden
409 | [ApiResponseFor409](#upgrade_shared_cluster_to_serverless.ApiResponseFor409) | Conflict
500 | [ApiResponseFor500](#upgrade_shared_cluster_to_serverless.ApiResponseFor500) | Internal Server Error

#### upgrade_shared_cluster_to_serverless.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**ServerlessInstanceDescription**](../../models/ServerlessInstanceDescription.md) |  | 


#### upgrade_shared_cluster_to_serverless.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### upgrade_shared_cluster_to_serverless.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### upgrade_shared_cluster_to_serverless.ApiResponseFor402
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor402ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor402ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### upgrade_shared_cluster_to_serverless.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### upgrade_shared_cluster_to_serverless.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### upgrade_shared_cluster_to_serverless.ApiResponseFor500
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

