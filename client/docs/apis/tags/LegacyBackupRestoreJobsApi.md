<a name="__pageTop"></a>
# atlas.apis.tags.legacy_backup_restore_jobs_api.LegacyBackupRestoreJobsApi

All URIs are relative to *https://cloud.mongodb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_legacy_backup_restore_job**](#create_legacy_backup_restore_job) | **post** /api/atlas/v2/groups/{groupId}/clusters/{clusterName}/restoreJobs | Create One Legacy Backup Restore Job

# **create_legacy_backup_restore_job**
<a name="create_legacy_backup_restore_job"></a>
> PaginatedRestoreJobView create_legacy_backup_restore_job(group_idcluster_nameapi_restore_job_view)

Create One Legacy Backup Restore Job

Restores one legacy backup for one cluster in the specified project. To use this resource, the requesting API Key must have the Project Atlas Admin role and an entry for the project access list.

### Example

```python
import atlas
from atlas.apis.tags import legacy_backup_restore_jobs_api
from atlas.model.api_error import ApiError
from atlas.model.api_restore_job_view import ApiRestoreJobView
from atlas.model.paginated_restore_job_view import PaginatedRestoreJobView
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = legacy_backup_restore_jobs_api.LegacyBackupRestoreJobsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'clusterName': "gqW,C",
    }
    query_params = {
    }
    body = ApiRestoreJobView(
        batch_id="32b6e34b3d91647abb20e7b8",
        checkpoint_id="32b6e34b3d91647abb20e7b8",
        cluster_id="32b6e34b3d91647abb20e7b8",
        cluster_name="gqW,C",
        created="1970-01-01T00:00:00.00Z",
        delivery=ApiRestoreJobDeliveryView(
            auth_header="auth_header_example",
            auth_value="auth_value_example",
            expiration_hours=1,
            expires="1970-01-01T00:00:00.00Z",
            max_downloads=1,
            method_name="CLIENT_PIT_HTTP",
            status_name="NOT_STARTED",
            target_cluster_id="32b6e34b3d91647abb20e7b8",
            target_cluster_name="gqW,C",
            target_group_id="32b6e34b3d91647abb20e7b8",
            url="url_example",
            url_v2="url_v2_example",
        ),
        encryption_enabled=True,
        group_id="32b6e34b3d91647abb20e7b8",
        hashes=[
            ApiRestoreJobFileHashView(
                file_name="file_name_example",
                hash="hash_example",
                links=[
                    Link(
                        href="https://cloud.mongodb.com/api/atlas",
                        rel="self",
                    )
                ],
                type_name="SHA1",
            )
        ],
        id="32b6e34b3d91647abb20e7b8",
,
        master_key_uuid="master_key_uuid_example",
        oplog_inc=1,
        oplog_ts="2800-02-29T0\d:2\d:2\dZ",
        point_in_time_utc_millis=1199145600000,
        snapshot_id="32b6e34b3d91647abb20e7b8",
        status_name="IN_PROGRESS",
        timestamp=ApiBSONTimestampView(
            date="1970-01-01T00:00:00.00Z",
            increment=1199145600,
        ),
    )
    try:
        # Create One Legacy Backup Restore Job
        api_response = api_instance.create_legacy_backup_restore_job(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling LegacyBackupRestoreJobsApi->create_legacy_backup_restore_job: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'clusterName': "gqW,C",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    body = ApiRestoreJobView(
        batch_id="32b6e34b3d91647abb20e7b8",
        checkpoint_id="32b6e34b3d91647abb20e7b8",
        cluster_id="32b6e34b3d91647abb20e7b8",
        cluster_name="gqW,C",
        created="1970-01-01T00:00:00.00Z",
        delivery=ApiRestoreJobDeliveryView(
            auth_header="auth_header_example",
            auth_value="auth_value_example",
            expiration_hours=1,
            expires="1970-01-01T00:00:00.00Z",
            max_downloads=1,
            method_name="CLIENT_PIT_HTTP",
            status_name="NOT_STARTED",
            target_cluster_id="32b6e34b3d91647abb20e7b8",
            target_cluster_name="gqW,C",
            target_group_id="32b6e34b3d91647abb20e7b8",
            url="url_example",
            url_v2="url_v2_example",
        ),
        encryption_enabled=True,
        group_id="32b6e34b3d91647abb20e7b8",
        hashes=[
            ApiRestoreJobFileHashView(
                file_name="file_name_example",
                hash="hash_example",
                links=[
                    Link(
                        href="https://cloud.mongodb.com/api/atlas",
                        rel="self",
                    )
                ],
                type_name="SHA1",
            )
        ],
        id="32b6e34b3d91647abb20e7b8",
,
        master_key_uuid="master_key_uuid_example",
        oplog_inc=1,
        oplog_ts="2800-02-29T0\d:2\d:2\dZ",
        point_in_time_utc_millis=1199145600000,
        snapshot_id="32b6e34b3d91647abb20e7b8",
        status_name="IN_PROGRESS",
        timestamp=ApiBSONTimestampView(
            date="1970-01-01T00:00:00.00Z",
            increment=1199145600,
        ),
    )
    try:
        # Create One Legacy Backup Restore Job
        api_response = api_instance.create_legacy_backup_restore_job(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling LegacyBackupRestoreJobsApi->create_legacy_backup_restore_job: %s\n" % e)
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
[**ApiRestoreJobView**](../../models/ApiRestoreJobView.md) |  | 


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
200 | [ApiResponseFor200](#create_legacy_backup_restore_job.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#create_legacy_backup_restore_job.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#create_legacy_backup_restore_job.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#create_legacy_backup_restore_job.ApiResponseFor500) | Internal Server Error

#### create_legacy_backup_restore_job.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedRestoreJobView**](../../models/PaginatedRestoreJobView.md) |  | 


#### create_legacy_backup_restore_job.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### create_legacy_backup_restore_job.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### create_legacy_backup_restore_job.ApiResponseFor500
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

