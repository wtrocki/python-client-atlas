<a name="__pageTop"></a>
# atlas.apis.tags.shared_tier_restore_jobs_api.SharedTierRestoreJobsApi

All URIs are relative to *https://cloud.mongodb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shared_cluster_backup_restore_job**](#create_shared_cluster_backup_restore_job) | **post** /api/atlas/v2/groups/{groupId}/clusters/{clusterName}/backup/tenant/restore | Create One Restore Job from One M2 or M5 Cluster
[**get_shared_cluster_backup_restore_job**](#get_shared_cluster_backup_restore_job) | **get** /api/atlas/v2/groups/{groupId}/clusters/{clusterName}/backup/tenant/restores/{restoreId} | Return One Restore Job for One M2 or M5 Cluster
[**list_shared_cluster_backup_restore_jobs**](#list_shared_cluster_backup_restore_jobs) | **get** /api/atlas/v2/groups/{groupId}/clusters/{clusterName}/backup/tenant/restores | Return All Restore Jobs for One M2 or M5 Cluster

# **create_shared_cluster_backup_restore_job**
<a name="create_shared_cluster_backup_restore_job"></a>
> TenantRestore create_shared_cluster_backup_restore_job(cluster_namegroup_idtenant_restore)

Create One Restore Job from One M2 or M5 Cluster

Restores the specified cluster. MongoDB Cloud limits which clusters can be the target clusters of a restore. The target cluster can't use encryption at rest, run a major release MongoDB version different than the snapshot, or receive client requests during restores. MongoDB Cloud deletes all existing data on the target cluster prior to the restore operation. To use this resource, the requesting API Key must have the Project Owner role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import shared_tier_restore_jobs_api
from atlas.model.tenant_restore import TenantRestore
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
    api_instance = shared_tier_restore_jobs_api.SharedTierRestoreJobsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'clusterName': "gqW,C",
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    body = TenantRestore(
        cluster_name="gqW,C",
        delivery_type="RESTORE",
        expiration_date="1970-01-01T00:00:00.00Z",
        id="32b6e34b3d91647abb20e7b8",
        links=[
            Link(
                href="https://cloud.mongodb.com/api/atlas",
                rel="self",
            )
        ],
        project_id="32b6e34b3d91647abb20e7b8",
        restore_finished_date="1970-01-01T00:00:00.00Z",
        restore_scheduled_date="1970-01-01T00:00:00.00Z",
        snapshot_finished_date="1970-01-01T00:00:00.00Z",
        snapshot_id="32b6e34b3d91647abb20e7b8",
        snapshot_url="snapshot_url_example",
        status="PENDING",
        target_deployment_item_name="})(,).,{&)&}__NL&&@'.)'._,.+..)'&&N}&)N,}_-'+:-",
        target_project_id="32b6e34b3d91647abb20e7b8",
    )
    try:
        # Create One Restore Job from One M2 or M5 Cluster
        api_response = api_instance.create_shared_cluster_backup_restore_job(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling SharedTierRestoreJobsApi->create_shared_cluster_backup_restore_job: %s\n" % e)

    # example passing only optional values
    path_params = {
        'clusterName': "gqW,C",
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    body = TenantRestore(
        cluster_name="gqW,C",
        delivery_type="RESTORE",
        expiration_date="1970-01-01T00:00:00.00Z",
        id="32b6e34b3d91647abb20e7b8",
        links=[
            Link(
                href="https://cloud.mongodb.com/api/atlas",
                rel="self",
            )
        ],
        project_id="32b6e34b3d91647abb20e7b8",
        restore_finished_date="1970-01-01T00:00:00.00Z",
        restore_scheduled_date="1970-01-01T00:00:00.00Z",
        snapshot_finished_date="1970-01-01T00:00:00.00Z",
        snapshot_id="32b6e34b3d91647abb20e7b8",
        snapshot_url="snapshot_url_example",
        status="PENDING",
        target_deployment_item_name="})(,).,{&)&}__NL&&@'.)'._,.+..)'&&N}&)N,}_-'+:-",
        target_project_id="32b6e34b3d91647abb20e7b8",
    )
    try:
        # Create One Restore Job from One M2 or M5 Cluster
        api_response = api_instance.create_shared_cluster_backup_restore_job(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling SharedTierRestoreJobsApi->create_shared_cluster_backup_restore_job: %s\n" % e)
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
[**TenantRestore**](../../models/TenantRestore.md) |  | 


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
clusterName | ClusterNameSchema | | 
groupId | GroupIdSchema | | 

# ClusterNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_shared_cluster_backup_restore_job.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#create_shared_cluster_backup_restore_job.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#create_shared_cluster_backup_restore_job.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#create_shared_cluster_backup_restore_job.ApiResponseFor404) | Not Found
409 | [ApiResponseFor409](#create_shared_cluster_backup_restore_job.ApiResponseFor409) | Conflict
500 | [ApiResponseFor500](#create_shared_cluster_backup_restore_job.ApiResponseFor500) | Internal Server Error

#### create_shared_cluster_backup_restore_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**TenantRestore**](../../models/TenantRestore.md) |  | 


#### create_shared_cluster_backup_restore_job.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### create_shared_cluster_backup_restore_job.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### create_shared_cluster_backup_restore_job.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### create_shared_cluster_backup_restore_job.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### create_shared_cluster_backup_restore_job.ApiResponseFor500
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

# **get_shared_cluster_backup_restore_job**
<a name="get_shared_cluster_backup_restore_job"></a>
> TenantRestore get_shared_cluster_backup_restore_job(cluster_namegroup_idrestore_id)

Return One Restore Job for One M2 or M5 Cluster

Returns the specified restore job. To use this resource, the requesting API Key must have the Project Read Only role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import shared_tier_restore_jobs_api
from atlas.model.tenant_restore import TenantRestore
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
    api_instance = shared_tier_restore_jobs_api.SharedTierRestoreJobsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'clusterName': "gqW,C",
        'groupId': "32b6e34b3d91647abb20e7b8",
        'restoreId': "bf325375e030fccba0091731",
    }
    query_params = {
    }
    try:
        # Return One Restore Job for One M2 or M5 Cluster
        api_response = api_instance.get_shared_cluster_backup_restore_job(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling SharedTierRestoreJobsApi->get_shared_cluster_backup_restore_job: %s\n" % e)

    # example passing only optional values
    path_params = {
        'clusterName': "gqW,C",
        'groupId': "32b6e34b3d91647abb20e7b8",
        'restoreId': "bf325375e030fccba0091731",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    try:
        # Return One Restore Job for One M2 or M5 Cluster
        api_response = api_instance.get_shared_cluster_backup_restore_job(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling SharedTierRestoreJobsApi->get_shared_cluster_backup_restore_job: %s\n" % e)
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
clusterName | ClusterNameSchema | | 
groupId | GroupIdSchema | | 
restoreId | RestoreIdSchema | | 

# ClusterNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RestoreIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_shared_cluster_backup_restore_job.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_shared_cluster_backup_restore_job.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#get_shared_cluster_backup_restore_job.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_shared_cluster_backup_restore_job.ApiResponseFor500) | Internal Server Error

#### get_shared_cluster_backup_restore_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**TenantRestore**](../../models/TenantRestore.md) |  | 


#### get_shared_cluster_backup_restore_job.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_shared_cluster_backup_restore_job.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_shared_cluster_backup_restore_job.ApiResponseFor500
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

# **list_shared_cluster_backup_restore_jobs**
<a name="list_shared_cluster_backup_restore_jobs"></a>
> PaginatedTenantRestoreView list_shared_cluster_backup_restore_jobs(cluster_namegroup_id)

Return All Restore Jobs for One M2 or M5 Cluster

Returns all restore jobs for the specified M2 or M5 cluster. Restore jobs restore a cluster using a snapshot. To use this resource, the requesting API Key must have the Project Read Only role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import shared_tier_restore_jobs_api
from atlas.model.paginated_tenant_restore_view import PaginatedTenantRestoreView
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
    api_instance = shared_tier_restore_jobs_api.SharedTierRestoreJobsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'clusterName': "gqW,C",
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    try:
        # Return All Restore Jobs for One M2 or M5 Cluster
        api_response = api_instance.list_shared_cluster_backup_restore_jobs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling SharedTierRestoreJobsApi->list_shared_cluster_backup_restore_jobs: %s\n" % e)

    # example passing only optional values
    path_params = {
        'clusterName': "gqW,C",
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    try:
        # Return All Restore Jobs for One M2 or M5 Cluster
        api_response = api_instance.list_shared_cluster_backup_restore_jobs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling SharedTierRestoreJobsApi->list_shared_cluster_backup_restore_jobs: %s\n" % e)
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
clusterName | ClusterNameSchema | | 
groupId | GroupIdSchema | | 

# ClusterNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_shared_cluster_backup_restore_jobs.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#list_shared_cluster_backup_restore_jobs.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#list_shared_cluster_backup_restore_jobs.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#list_shared_cluster_backup_restore_jobs.ApiResponseFor500) | Internal Server Error

#### list_shared_cluster_backup_restore_jobs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedTenantRestoreView**](../../models/PaginatedTenantRestoreView.md) |  | 


#### list_shared_cluster_backup_restore_jobs.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### list_shared_cluster_backup_restore_jobs.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### list_shared_cluster_backup_restore_jobs.ApiResponseFor500
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

