<a name="__pageTop"></a>
# atlas.apis.tags.monitoring_and_logs_api.MonitoringAndLogsApi

All URIs are relative to *https://cloud.mongodb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_atlas_process**](#get_atlas_process) | **get** /api/atlas/v2/groups/{groupId}/processes/{processId} | Return One MongoDB Process by ID
[**get_database**](#get_database) | **get** /api/atlas/v2/groups/{groupId}/processes/{processId}/databases/{databaseName} | Return One Database for a MongoDB Process
[**get_database_measurements**](#get_database_measurements) | **get** /api/atlas/v2/groups/{groupId}/processes/{processId}/databases/{databaseName}/measurements | Return Measurements of One Database for One MongoDB Process
[**get_disk_measurements**](#get_disk_measurements) | **get** /api/atlas/v2/groups/{groupId}/processes/{processId}/disks/{partitionName}/measurements | Return Measurements of One Disk for One MongoDB Process
[**get_host_logs**](#get_host_logs) | **get** /api/atlas/v2/groups/{groupId}/clusters/{hostName}/logs/{logName}.gz | Download Logs for One Multi-Cloud Cluster Host in One Project
[**get_host_measurements**](#get_host_measurements) | **get** /api/atlas/v2/groups/{groupId}/processes/{processId}/measurements | Return Measurements for One MongoDB Process
[**get_index_metrics**](#get_index_metrics) | **get** /api/atlas/v2/groups/{groupId}/hosts/{processId}/fts/metrics/indexes/{databaseName}/{collectionName}/{indexName}/measurements | Return Atlas Search Metrics for One Index in One Specified Namespace
[**get_measurements**](#get_measurements) | **get** /api/atlas/v2/groups/{groupId}/hosts/{processId}/fts/metrics/measurements | Return Atlas Search Hardware and Status Metrics
[**list_atlas_processes**](#list_atlas_processes) | **get** /api/atlas/v2/groups/{groupId}/processes | Return All MongoDB Processes in One Project
[**list_databases**](#list_databases) | **get** /api/atlas/v2/groups/{groupId}/processes/{processId}/databases | Return Available Databases for One MongoDB Process
[**list_disk_measurements**](#list_disk_measurements) | **get** /api/atlas/v2/groups/{groupId}/processes/{processId}/disks/{partitionName} | Return Measurements of One Disk
[**list_disk_partitions**](#list_disk_partitions) | **get** /api/atlas/v2/groups/{groupId}/processes/{processId}/disks | Return Available Disks for One MongoDB Process
[**list_index_metrics**](#list_index_metrics) | **get** /api/atlas/v2/groups/{groupId}/hosts/{processId}/fts/metrics/indexes/{databaseName}/{collectionName}/measurements | Return All Atlas Search Index Metrics for One Namespace
[**list_metric_types**](#list_metric_types) | **get** /api/atlas/v2/groups/{groupId}/hosts/{processId}/fts/metrics | Return All Atlas Search Metric Types for One Process

# **get_atlas_process**
<a name="get_atlas_process"></a>
> ApiHostViewAtlas get_atlas_process(group_idprocess_id)

Return One MongoDB Process by ID

Returns the processes for the specified host for the specified project. To use this resource, the requesting API Key must have the Project Read Only role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import monitoring_and_logs_api
from atlas.model.api_error import ApiError
from atlas.model.api_host_view_atlas import ApiHostViewAtlas
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_and_logs_api.MonitoringAndLogsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'processId': "mongodb.example.com:27017",
    }
    query_params = {
    }
    try:
        # Return One MongoDB Process by ID
        api_response = api_instance.get_atlas_process(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->get_atlas_process: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'processId': "mongodb.example.com:27017",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    try:
        # Return One MongoDB Process by ID
        api_response = api_instance.get_atlas_process(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->get_atlas_process: %s\n" % e)
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
processId | ProcessIdSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProcessIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_atlas_process.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#get_atlas_process.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#get_atlas_process.ApiResponseFor500) | Internal Server Error

#### get_atlas_process.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiHostViewAtlas**](../../models/ApiHostViewAtlas.md) |  | 


#### get_atlas_process.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_atlas_process.ApiResponseFor500
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

# **get_database**
<a name="get_database"></a>
> ApiDatabaseView get_database(group_iddatabase_nameprocess_id)

Return One Database for a MongoDB Process

Returns one database running on the specified host for the specified project. To use this resource, the requesting API Key must have the Project Read Only role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import monitoring_and_logs_api
from atlas.model.api_database_view import ApiDatabaseView
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
    api_instance = monitoring_and_logs_api.MonitoringAndLogsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'databaseName': "databaseName_example",
        'processId': "mongodb.example.com:27017",
    }
    query_params = {
    }
    try:
        # Return One Database for a MongoDB Process
        api_response = api_instance.get_database(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->get_database: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'databaseName': "databaseName_example",
        'processId': "mongodb.example.com:27017",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    try:
        # Return One Database for a MongoDB Process
        api_response = api_instance.get_database(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->get_database: %s\n" % e)
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
databaseName | DatabaseNameSchema | | 
processId | ProcessIdSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DatabaseNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProcessIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_database.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#get_database.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#get_database.ApiResponseFor500) | Internal Server Error

#### get_database.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDatabaseView**](../../models/ApiDatabaseView.md) |  | 


#### get_database.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_database.ApiResponseFor500
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

# **get_database_measurements**
<a name="get_database_measurements"></a>
> ApiMeasurementsGeneralViewAtlas get_database_measurements(group_iddatabase_nameprocess_id)

Return Measurements of One Database for One MongoDB Process

Returns the measurements of one database for the specified host for the specified project. Returns the database's on-disk storage space based on the MongoDB `dbStats` command output. To use this resource, the requesting API Key must have the Project Read Only role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import monitoring_and_logs_api
from atlas.model.api_measurements_general_view_atlas import ApiMeasurementsGeneralViewAtlas
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
    api_instance = monitoring_and_logs_api.MonitoringAndLogsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'databaseName': "databaseName_example",
        'processId': "mongodb.example.com:27017",
    }
    query_params = {
    }
    try:
        # Return Measurements of One Database for One MongoDB Process
        api_response = api_instance.get_database_measurements(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->get_database_measurements: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'databaseName': "databaseName_example",
        'processId': "mongodb.example.com:27017",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
        'm': [
        "DATABASE_AVERAGE_OBJECT_SIZE"
    ],
    }
    try:
        # Return Measurements of One Database for One MongoDB Process
        api_response = api_instance.get_database_measurements(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->get_database_measurements: %s\n" % e)
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
m | MSchema | | optional


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

# MSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | One measurement requested for this MongoDB process. | must be one of ["DATABASE_AVERAGE_OBJECT_SIZE", "DATABASE_COLLECTION_COUNT", "DATABASE_DATA_SIZE", "DATABASE_STORAGE_SIZE", "DATABASE_INDEX_SIZE", "DATABASE_INDEX_COUNT", "DATABASE_EXTENT_COUNT", "DATABASE_OBJECT_COUNT", "DATABASE_VIEW_COUNT", ] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupId | GroupIdSchema | | 
databaseName | DatabaseNameSchema | | 
processId | ProcessIdSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DatabaseNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProcessIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_database_measurements.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#get_database_measurements.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#get_database_measurements.ApiResponseFor500) | Internal Server Error

#### get_database_measurements.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiMeasurementsGeneralViewAtlas**](../../models/ApiMeasurementsGeneralViewAtlas.md) |  | 


#### get_database_measurements.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_database_measurements.ApiResponseFor500
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

# **get_disk_measurements**
<a name="get_disk_measurements"></a>
> ApiMeasurementsGeneralViewAtlas get_disk_measurements(group_idpartition_nameprocess_id)

Return Measurements of One Disk for One MongoDB Process

Returns the measurements of one disk or partition for the specified host for the specified project. Returned value can be one of the following: - Throughput of I/O operations for the disk partition used for the MongoDB process - Percentage of time during which requests the partition issued and serviced - Latency per operation type of the disk partition used for the MongoDB process - Amount of free and used disk space on the disk partition used for the MongoDB process  To use this resource, the requesting API Key must have the Project Read Only role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import monitoring_and_logs_api
from atlas.model.api_measurements_general_view_atlas import ApiMeasurementsGeneralViewAtlas
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
    api_instance = monitoring_and_logs_api.MonitoringAndLogsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'partitionName': "partitionName_example",
        'processId': "mongodb.example.com:27017",
    }
    query_params = {
    }
    try:
        # Return Measurements of One Disk for One MongoDB Process
        api_response = api_instance.get_disk_measurements(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->get_disk_measurements: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'partitionName': "partitionName_example",
        'processId': "mongodb.example.com:27017",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
        'm': [
        "DISK_PARTITION_IOPS_READ"
    ],
    }
    try:
        # Return Measurements of One Disk for One MongoDB Process
        api_response = api_instance.get_disk_measurements(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->get_disk_measurements: %s\n" % e)
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
m | MSchema | | optional


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

# MSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | One measurement requested for this MongoDB process. | must be one of ["DISK_PARTITION_IOPS_READ", "MAX_DISK_PARTITION_IOPS_READ", "DISK_PARTITION_IOPS_WRITE", "MAX_DISK_PARTITION_IOPS_WRITE", "DISK_PARTITION_IOPS_TOTAL", "MAX_DISK_PARTITION_IOPS_TOTAL", "DISK_PARTITION_UTILIZATION", "MAX_DISK_PARTITION_UTILIZATION", "DISK_PARTITION_LATENCY_READ", "MAX_DISK_PARTITION_LATENCY_READ", "DISK_PARTITION_LATENCY_WRITE", "MAX_DISK_PARTITION_LATENCY_WRITE", "DISK_PARTITION_SPACE_FREE", "MAX_DISK_PARTITION_SPACE_FREE", "DISK_PARTITION_SPACE_USED", "MAX_DISK_PARTITION_SPACE_USED", "DISK_PARTITION_SPACE_PERCENT_FREE", "MAX_DISK_PARTITION_SPACE_PERCENT_FREE", "DISK_PARTITION_SPACE_PERCENT_USED", "MAX_DISK_PARTITION_SPACE_PERCENT_USED", ] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupId | GroupIdSchema | | 
partitionName | PartitionNameSchema | | 
processId | ProcessIdSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PartitionNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProcessIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_disk_measurements.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#get_disk_measurements.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#get_disk_measurements.ApiResponseFor500) | Internal Server Error

#### get_disk_measurements.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiMeasurementsGeneralViewAtlas**](../../models/ApiMeasurementsGeneralViewAtlas.md) |  | 


#### get_disk_measurements.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_disk_measurements.ApiResponseFor500
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

# **get_host_logs**
<a name="get_host_logs"></a>
> file_type get_host_logs(group_idhost_namelog_name)

Download Logs for One Multi-Cloud Cluster Host in One Project

Returns a compressed (.gz) log file that contains a range of log messages for the specified host for the specified project. To use this resource, the requesting API Key must have the Project Owner or Project Data Access Read Write roles. This resource doesn't require the API Key to have an Access List. Deprecated versions: v2-{2023-01-01}

### Example

```python
import atlas
from atlas.apis.tags import monitoring_and_logs_api
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
    api_instance = monitoring_and_logs_api.MonitoringAndLogsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'hostName': "hostName_example",
        'logName': "mongodb",
    }
    query_params = {
    }
    try:
        # Download Logs for One Multi-Cloud Cluster Host in One Project
        api_response = api_instance.get_host_logs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->get_host_logs: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'hostName': "hostName_example",
        'logName': "mongodb",
    }
    query_params = {
        'endDate': 1199145600,
        'startDate': 1199145600,
    }
    try:
        # Download Logs for One Multi-Cloud Cluster Host in One Project
        api_response = api_instance.get_host_logs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->get_host_logs: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.atlas.2023-02-01+gzip', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
endDate | EndDateSchema | | optional
startDate | StartDateSchema | | optional


# EndDateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

# StartDateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupId | GroupIdSchema | | 
hostName | HostNameSchema | | 
logName | LogNameSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# HostNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LogNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["mongodb", "mongos", "mongodb-audit-log", "mongos-audit-log", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_host_logs.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_host_logs.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_host_logs.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#get_host_logs.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_host_logs.ApiResponseFor404) | Not Found
409 | [ApiResponseFor409](#get_host_logs.ApiResponseFor409) | Conflict
500 | [ApiResponseFor500](#get_host_logs.ApiResponseFor500) | Internal Server Error

#### get_host_logs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230201gzip, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230201gzip

Compressed (.gz) log file that contains a range of log messages for the specified host for the specified project

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bytes, io.FileIO, io.BufferedReader,  | bytes, FileIO,  | Compressed (.gz) log file that contains a range of log messages for the specified host for the specified project | 

#### get_host_logs.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_host_logs.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_host_logs.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_host_logs.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_host_logs.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_host_logs.ApiResponseFor500
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

# **get_host_measurements**
<a name="get_host_measurements"></a>
> ApiMeasurementsGeneralViewAtlas get_host_measurements(group_idprocess_id)

Return Measurements for One MongoDB Process

Returns measurements of the disk or partition per process for the specified host for the specified project. Returned value can be one of the following: - Throughput of I/O operations for the disk partition used for the MongoDB process - Percentage of time during which requests the partition issued and serviced - Latency per operation type of the disk partition used for the MongoDB process - Amount of free and used disk space on the disk partition used for the MongoDB process   To use this resource, the requesting API Key must have the Project Read Only role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import monitoring_and_logs_api
from atlas.model.api_measurements_general_view_atlas import ApiMeasurementsGeneralViewAtlas
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
    api_instance = monitoring_and_logs_api.MonitoringAndLogsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'processId': "mongodb.example.com:27017",
    }
    query_params = {
    }
    try:
        # Return Measurements for One MongoDB Process
        api_response = api_instance.get_host_measurements(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->get_host_measurements: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'processId': "mongodb.example.com:27017",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
        'm': [
        "ASSERT_MSG"
    ],
        'period': "1970-01-01T00:00:00.00Z",
    }
    try:
        # Return Measurements for One MongoDB Process
        api_response = api_instance.get_host_measurements(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->get_host_measurements: %s\n" % e)
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
m | MSchema | | optional
period | PeriodSchema | | optional


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

# MSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | One measurement requested for this MongoDB process. | must be one of ["ASSERT_MSG", "ASSERT_REGULAR", "ASSERT_USER", "ASSERT_WARNING", "BACKGROUND_FLUSH_AVG", "CACHE_BYTES_READ_INTO", "CACHE_BYTES_WRITTEN_FROM", "CACHE_DIRTY_BYTES", "CACHE_USED_BYTES", "COMPUTED_MEMORY", "CONNECTIONS", "CURSORS_TOTAL_OPEN", "CURSORS_TOTAL_TIMED_OUT", "DB_DATA_SIZE_TOTAL", "DB_STORAGE_TOTAL", "DOCUMENT_METRICS_DELETED", "DOCUMENT_METRICS_INSERTED", "DOCUMENT_METRICS_RETURNED", "DOCUMENT_METRICS_UPDATED", "EXTRA_INFO_PAGE_FAULTS", "FTS_DISK_UTILIZATION", "FTS_MEMORY_MAPPED", "FTS_MEMORY_RESIDENT", "FTS_MEMORY_VIRTUAL", "FTS_PROCESS_CPU_KERNEL", "FTS_PROCESS_CPU_USER", "FTS_PROCESS_NORMALIZED_CPU_KERNEL", "FTS_PROCESS_NORMALIZED_CPU_USER", "GLOBAL_ACCESSES_NOT_IN_MEMORY", "GLOBAL_LOCK_CURRENT_QUEUE_READERS", "GLOBAL_LOCK_CURRENT_QUEUE_TOTAL", "GLOBAL_LOCK_CURRENT_QUEUE_WRITERS", "GLOBAL_PAGE_FAULT_EXCEPTIONS_THROWN", "INDEX_COUNTERS_BTREE_ACCESSES", "INDEX_COUNTERS_BTREE_HITS", "INDEX_COUNTERS_BTREE_MISS_RATIO", "INDEX_COUNTERS_BTREE_MISSES", "JOURNALING_COMMITS_IN_WRITE_LOCK", "JOURNALING_MB", "JOURNALING_WRITE_DATA_FILES_MB", "MAX_PROCESS_CPU_CHILDREN_KERNEL", "MAX_PROCESS_CPU_CHILDREN_USER", "MAX_PROCESS_CPU_KERNEL", "MAX_PROCESS_CPU_USER", "MAX_PROCESS_NORMALIZED_CPU_CHILDREN_KERNEL", "MAX_PROCESS_NORMALIZED_CPU_CHILDREN_USER", "MAX_PROCESS_NORMALIZED_CPU_KERNEL", "MAX_PROCESS_NORMALIZED_CPU_USER", "MAX_SWAP_USAGE_FREE", "MAX_SWAP_USAGE_USED ", "MAX_SYSTEM_CPU_GUEST", "MAX_SYSTEM_CPU_IOWAIT", "MAX_SYSTEM_CPU_IRQ", "MAX_SYSTEM_CPU_KERNEL", "MAX_SYSTEM_CPU_SOFTIRQ", "MAX_SYSTEM_CPU_STEAL", "MAX_SYSTEM_CPU_USER", "MAX_SYSTEM_MEMORY_AVAILABLE", "MAX_SYSTEM_MEMORY_FREE", "MAX_SYSTEM_MEMORY_USED", "MAX_SYSTEM_NETWORK_IN", "MAX_SYSTEM_NETWORK_OUT", "MAX_SYSTEM_NORMALIZED_CPU_GUEST", "MAX_SYSTEM_NORMALIZED_CPU_IOWAIT", "MAX_SYSTEM_NORMALIZED_CPU_IRQ", "MAX_SYSTEM_NORMALIZED_CPU_KERNEL", "MAX_SYSTEM_NORMALIZED_CPU_NICE", "MAX_SYSTEM_NORMALIZED_CPU_SOFTIRQ", "MAX_SYSTEM_NORMALIZED_CPU_STEAL", "MAX_SYSTEM_NORMALIZED_CPU_USER", "MEMORY_MAPPED", "MEMORY_RESIDENT", "MEMORY_VIRTUAL", "NETWORK_BYTES_IN", "NETWORK_BYTES_OUT", "NETWORK_NUM_REQUESTS", "OP_EXECUTION_TIME_COMMANDS", "OP_EXECUTION_TIME_READS", "OP_EXECUTION_TIME_WRITES", "OPCOUNTER_CMD", "OPCOUNTER_DELETE", "OPCOUNTER_GETMORE", "OPCOUNTER_INSERT", "OPCOUNTER_QUERY", "OPCOUNTER_REPL_CMD", "OPCOUNTER_REPL_DELETE", "OPCOUNTER_REPL_INSERT", "OPCOUNTER_REPL_UPDATE", "OPCOUNTER_UPDATE", "OPERATIONS_SCAN_AND_ORDER", "OPLOG_MASTER_LAG_TIME_DIFF", "OPLOG_MASTER_TIME", "OPLOG_RATE_GB_PER_HOUR", "OPLOG_SLAVE_LAG_MASTER_TIME", "OPLOG_REPLICATION_LAG", "PROCESS_CPU_CHILDREN_KERNEL", "PROCESS_CPU_CHILDREN_USER", "PROCESS_CPU_KERNEL", "PROCESS_CPU_USER", "PROCESS_NORMALIZED_CPU_CHILDREN_KERNEL", "PROCESS_NORMALIZED_CPU_CHILDREN_USER", "PROCESS_NORMALIZED_CPU_KERNEL", "PROCESS_NORMALIZED_CPU_USER", "QUERY_EXECUTOR_SCANNED", "QUERY_EXECUTOR_SCANNED_OBJECTS", "QUERY_TARGETING_SCANNED_OBJECTS_PER_RETURNED", "QUERY_TARGETING_SCANNED_PER_RETURNED", "RESTARTS_IN_LAST_HOUR", "SWAP_USAGE_FREE", "SWAP_USAGE_USED", "SYSTEM_CPU_GUEST", "SYSTEM_CPU_IOWAIT", "SYSTEM_CPU_IRQ", "SYSTEM_CPU_KERNEL", "SYSTEM_CPU_NICE", "SYSTEM_CPU_SOFTIRQ", "SYSTEM_CPU_STEAL", "SYSTEM_CPU_USER", "SYSTEM_MEMORY_AVAILABLE", "SYSTEM_MEMORY_FREE", "SYSTEM_MEMORY_USED", "SYSTEM_NETWORK_IN", "SYSTEM_NETWORK_OUT", "SYSTEM_NORMALIZED_CPU_GUEST", "SYSTEM_NORMALIZED_CPU_IOWAIT", "SYSTEM_NORMALIZED_CPU_IRQ", "SYSTEM_NORMALIZED_CPU_KERNEL", "SYSTEM_NORMALIZED_CPU_NICE", "SYSTEM_NORMALIZED_CPU_SOFTIRQ", "SYSTEM_NORMALIZED_CPU_STEAL", "SYSTEM_NORMALIZED_CPU_USER", "TICKETS_AVAILABLE_READS", "TICKETS_AVAILABLE_WRITE", ] 

# PeriodSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
groupId | GroupIdSchema | | 
processId | ProcessIdSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProcessIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_host_measurements.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#get_host_measurements.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#get_host_measurements.ApiResponseFor500) | Internal Server Error

#### get_host_measurements.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiMeasurementsGeneralViewAtlas**](../../models/ApiMeasurementsGeneralViewAtlas.md) |  | 


#### get_host_measurements.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_host_measurements.ApiResponseFor500
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

# **get_index_metrics**
<a name="get_index_metrics"></a>
> ApiMeasurementsIndexesView get_index_metrics(process_idindex_namedatabase_namecollection_namegroup_idgranularitymetrics)

Return Atlas Search Metrics for One Index in One Specified Namespace

Returns the Atlas Search metrics data series within the provided time range for one namespace and index name on the specified process.

### Example

```python
import atlas
from atlas.apis.tags import monitoring_and_logs_api
from atlas.model.api_measurements_indexes_view import ApiMeasurementsIndexesView
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
    api_instance = monitoring_and_logs_api.MonitoringAndLogsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'processId': "my.host.name.com:27017",
        'indexName': "myindex",
        'databaseName': "mydb",
        'collectionName': "mycoll",
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'granularity': "PT1M",
        'metrics': [
        "INDEX_SIZE_ON_DISK"
    ],
    }
    try:
        # Return Atlas Search Metrics for One Index in One Specified Namespace
        api_response = api_instance.get_index_metrics(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->get_index_metrics: %s\n" % e)

    # example passing only optional values
    path_params = {
        'processId': "my.host.name.com:27017",
        'indexName': "myindex",
        'databaseName': "mydb",
        'collectionName': "mycoll",
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'granularity': "PT1M",
        'period': "PT10H",
        'start': "1970-01-01T00:00:00.00Z",
        'end': "1970-01-01T00:00:00.00Z",
        'envelope': False,
        'metrics': [
        "INDEX_SIZE_ON_DISK"
    ],
    }
    try:
        # Return Atlas Search Metrics for One Index in One Specified Namespace
        api_response = api_instance.get_index_metrics(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->get_index_metrics: %s\n" % e)
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
granularity | GranularitySchema | | 
period | PeriodSchema | | optional
start | StartSchema | | optional
end | EndSchema | | optional
envelope | EnvelopeSchema | | optional
metrics | MetricsSchema | | 


# GranularitySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PeriodSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StartSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EndSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EnvelopeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# MetricsSchema

List that contains the measurements that MongoDB Atlas reports for the associated data series.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains the measurements that MongoDB Atlas reports for the associated data series. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["INDEX_SIZE_ON_DISK", "NUMBER_OF_DELETES", "NUMBER_OF_ERROR_QUERIES", "NUMBER_OF_GETMORE_COMMANDS", "NUMBER_OF_INDEX_FIELDS", "NUMBER_OF_INSERTS", "NUMBER_OF_SUCCESS_QUERIES", "NUMBER_OF_UPDATES", "REPLICATION_LAG", "TOTAL_NUMBER_OF_QUERIES", ] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
processId | ProcessIdSchema | | 
indexName | IndexNameSchema | | 
databaseName | DatabaseNameSchema | | 
collectionName | CollectionNameSchema | | 
groupId | GroupIdSchema | | 

# ProcessIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IndexNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DatabaseNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CollectionNameSchema

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
200 | [ApiResponseFor200](#get_index_metrics.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_index_metrics.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#get_index_metrics.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_index_metrics.ApiResponseFor500) | Internal Server Error

#### get_index_metrics.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiMeasurementsIndexesView**](../../models/ApiMeasurementsIndexesView.md) |  | 


#### get_index_metrics.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_index_metrics.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_index_metrics.ApiResponseFor500
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

# **get_measurements**
<a name="get_measurements"></a>
> ApiMeasurementsNonIndexView get_measurements(process_idgroup_idgranularitymetrics)

Return Atlas Search Hardware and Status Metrics

Returns the Atlas Search hardware and status data series within the provided time range for one process in the specified project.

### Example

```python
import atlas
from atlas.apis.tags import monitoring_and_logs_api
from atlas.model.api_error import ApiError
from atlas.model.api_measurements_non_index_view import ApiMeasurementsNonIndexView
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_and_logs_api.MonitoringAndLogsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'processId': "my.host.name.com:27017",
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'granularity': "PT1M",
        'metrics': [
        "FTS_DISK_USAGE"
    ],
    }
    try:
        # Return Atlas Search Hardware and Status Metrics
        api_response = api_instance.get_measurements(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->get_measurements: %s\n" % e)

    # example passing only optional values
    path_params = {
        'processId': "my.host.name.com:27017",
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'granularity': "PT1M",
        'period': "PT10H",
        'start': "1970-01-01T00:00:00.00Z",
        'end': "1970-01-01T00:00:00.00Z",
        'envelope': False,
        'metrics': [
        "FTS_DISK_USAGE"
    ],
    }
    try:
        # Return Atlas Search Hardware and Status Metrics
        api_response = api_instance.get_measurements(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->get_measurements: %s\n" % e)
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
granularity | GranularitySchema | | 
period | PeriodSchema | | optional
start | StartSchema | | optional
end | EndSchema | | optional
envelope | EnvelopeSchema | | optional
metrics | MetricsSchema | | 


# GranularitySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PeriodSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StartSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EndSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EnvelopeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# MetricsSchema

List that contains the metrics that you want MongoDB Atlas to report for the associated data series. If you don't set this parameter, this resource returns all hardware and status metrics for the associated data series.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains the metrics that you want MongoDB Atlas to report for the associated data series. If you don&#x27;t set this parameter, this resource returns all hardware and status metrics for the associated data series. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["FTS_DISK_USAGE", "FTS_PROCESS_CPU_KERNEL", "FTS_PROCESS_CPU_USER", "FTS_PROCESS_NORMALIZED_CPU_KERNEL", "FTS_PROCESS_NORMALIZED_CPU_USER", "FTS_PROCESS_RESIDENT_MEMORY", "FTS_PROCESS_SHARED_MEMORY", "FTS_PROCESS_VIRTUAL_MEMORY", "JVM_CURRENT_MEMORY", "JVM_MAX_MEMORY", ] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
processId | ProcessIdSchema | | 
groupId | GroupIdSchema | | 

# ProcessIdSchema

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
200 | [ApiResponseFor200](#get_measurements.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_measurements.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#get_measurements.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_measurements.ApiResponseFor500) | Internal Server Error

#### get_measurements.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiMeasurementsNonIndexView**](../../models/ApiMeasurementsNonIndexView.md) |  | 


#### get_measurements.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_measurements.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_measurements.ApiResponseFor500
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

# **list_atlas_processes**
<a name="list_atlas_processes"></a>
> PaginatedHostViewAtlas list_atlas_processes(group_id)

Return All MongoDB Processes in One Project

Returns details of all processes for the specified project. A MongoDB process can be either a `mongod` or `mongos`. To use this resource, the requesting API Key must have the Project Read Only role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import monitoring_and_logs_api
from atlas.model.paginated_host_view_atlas import PaginatedHostViewAtlas
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
    api_instance = monitoring_and_logs_api.MonitoringAndLogsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    try:
        # Return All MongoDB Processes in One Project
        api_response = api_instance.list_atlas_processes(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->list_atlas_processes: %s\n" % e)

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
        # Return All MongoDB Processes in One Project
        api_response = api_instance.list_atlas_processes(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->list_atlas_processes: %s\n" % e)
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
200 | [ApiResponseFor200](#list_atlas_processes.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#list_atlas_processes.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#list_atlas_processes.ApiResponseFor500) | Internal Server Error

#### list_atlas_processes.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedHostViewAtlas**](../../models/PaginatedHostViewAtlas.md) |  | 


#### list_atlas_processes.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### list_atlas_processes.ApiResponseFor500
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

# **list_databases**
<a name="list_databases"></a>
> PaginatedDatabaseView list_databases(group_idprocess_id)

Return Available Databases for One MongoDB Process

Returns the list of databases running on the specified host for the specified project. To use this resource, the requesting API Key must have the Project Read Only role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import monitoring_and_logs_api
from atlas.model.api_error import ApiError
from atlas.model.paginated_database_view import PaginatedDatabaseView
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_and_logs_api.MonitoringAndLogsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'processId': "mongodb.example.com:27017",
    }
    query_params = {
    }
    try:
        # Return Available Databases for One MongoDB Process
        api_response = api_instance.list_databases(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->list_databases: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'processId': "mongodb.example.com:27017",
    }
    query_params = {
        'envelope': False,
        'includeCount': True,
        'itemsPerPage': 100,
        'pageNum': 1,
        'pretty': False,
    }
    try:
        # Return Available Databases for One MongoDB Process
        api_response = api_instance.list_databases(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->list_databases: %s\n" % e)
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
processId | ProcessIdSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProcessIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_databases.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#list_databases.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#list_databases.ApiResponseFor500) | Internal Server Error

#### list_databases.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedDatabaseView**](../../models/PaginatedDatabaseView.md) |  | 


#### list_databases.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### list_databases.ApiResponseFor500
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

# **list_disk_measurements**
<a name="list_disk_measurements"></a>
> ApiDiskPartitionView list_disk_measurements(partition_namegroup_idprocess_id)

Return Measurements of One Disk

Returns the measurements of one disk or partition for the specified host for the specified project. Returned value can be one of the following: - Throughput of I/O operations for the disk partition used for the MongoDB process - Percentage of time during which requests the partition issued and serviced - Latency per operation type of the disk partition used for the MongoDB process - Amount of free and used disk space on the disk partition used for the MongoDB process   To use this resource, the requesting API Key must have the Project Read Only role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import monitoring_and_logs_api
from atlas.model.api_disk_partition_view import ApiDiskPartitionView
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
    api_instance = monitoring_and_logs_api.MonitoringAndLogsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'partitionName': "partitionName_example",
        'groupId': "32b6e34b3d91647abb20e7b8",
        'processId': "mongodb.example.com:27017",
    }
    query_params = {
    }
    try:
        # Return Measurements of One Disk
        api_response = api_instance.list_disk_measurements(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->list_disk_measurements: %s\n" % e)

    # example passing only optional values
    path_params = {
        'partitionName': "partitionName_example",
        'groupId': "32b6e34b3d91647abb20e7b8",
        'processId': "mongodb.example.com:27017",
    }
    query_params = {
        'envelope': False,
    }
    try:
        # Return Measurements of One Disk
        api_response = api_instance.list_disk_measurements(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->list_disk_measurements: %s\n" % e)
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
partitionName | PartitionNameSchema | | 
groupId | GroupIdSchema | | 
processId | ProcessIdSchema | | 

# PartitionNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProcessIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_disk_measurements.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#list_disk_measurements.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#list_disk_measurements.ApiResponseFor500) | Internal Server Error

#### list_disk_measurements.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiDiskPartitionView**](../../models/ApiDiskPartitionView.md) |  | 


#### list_disk_measurements.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### list_disk_measurements.ApiResponseFor500
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

# **list_disk_partitions**
<a name="list_disk_partitions"></a>
> PaginatedDiskPartitionView list_disk_partitions(group_idprocess_id)

Return Available Disks for One MongoDB Process

Returns the list of disks or partitions for the specified host for the specified project. To use this resource, the requesting API Key must have the Project Read Only role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import monitoring_and_logs_api
from atlas.model.paginated_disk_partition_view import PaginatedDiskPartitionView
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
    api_instance = monitoring_and_logs_api.MonitoringAndLogsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'processId': "mongodb.example.com:27017",
    }
    query_params = {
    }
    try:
        # Return Available Disks for One MongoDB Process
        api_response = api_instance.list_disk_partitions(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->list_disk_partitions: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'processId': "mongodb.example.com:27017",
    }
    query_params = {
        'envelope': False,
        'includeCount': True,
        'itemsPerPage': 100,
        'pageNum': 1,
        'pretty': False,
    }
    try:
        # Return Available Disks for One MongoDB Process
        api_response = api_instance.list_disk_partitions(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->list_disk_partitions: %s\n" % e)
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
processId | ProcessIdSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ProcessIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_disk_partitions.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#list_disk_partitions.ApiResponseFor401) | Unauthorized
500 | [ApiResponseFor500](#list_disk_partitions.ApiResponseFor500) | Internal Server Error

#### list_disk_partitions.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedDiskPartitionView**](../../models/PaginatedDiskPartitionView.md) |  | 


#### list_disk_partitions.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### list_disk_partitions.ApiResponseFor500
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

# **list_index_metrics**
<a name="list_index_metrics"></a>
> ApiMeasurementsIndexesView list_index_metrics(process_iddatabase_namecollection_namegroup_idgranularitymetrics)

Return All Atlas Search Index Metrics for One Namespace

Returns the Atlas Search index metrics within the specified time range for one namespace in the specified process.

### Example

```python
import atlas
from atlas.apis.tags import monitoring_and_logs_api
from atlas.model.api_measurements_indexes_view import ApiMeasurementsIndexesView
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
    api_instance = monitoring_and_logs_api.MonitoringAndLogsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'processId': "my.host.name.com:27017",
        'databaseName': "mydb",
        'collectionName': "mycoll",
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'granularity': "PT1M",
        'metrics': [
        "INDEX_SIZE_ON_DISK"
    ],
    }
    try:
        # Return All Atlas Search Index Metrics for One Namespace
        api_response = api_instance.list_index_metrics(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->list_index_metrics: %s\n" % e)

    # example passing only optional values
    path_params = {
        'processId': "my.host.name.com:27017",
        'databaseName': "mydb",
        'collectionName': "mycoll",
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'granularity': "PT1M",
        'period': "PT10H",
        'start': "1970-01-01T00:00:00.00Z",
        'end': "1970-01-01T00:00:00.00Z",
        'envelope': False,
        'metrics': [
        "INDEX_SIZE_ON_DISK"
    ],
    }
    try:
        # Return All Atlas Search Index Metrics for One Namespace
        api_response = api_instance.list_index_metrics(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->list_index_metrics: %s\n" % e)
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
granularity | GranularitySchema | | 
period | PeriodSchema | | optional
start | StartSchema | | optional
end | EndSchema | | optional
envelope | EnvelopeSchema | | optional
metrics | MetricsSchema | | 


# GranularitySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PeriodSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# StartSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EndSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  |  | value must conform to RFC-3339 date-time

# EnvelopeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  |  | if omitted the server will use the default value of False

# MetricsSchema

List that contains the measurements that MongoDB Atlas reports for the associated data series.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains the measurements that MongoDB Atlas reports for the associated data series. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["INDEX_SIZE_ON_DISK", "NUMBER_OF_DELETES", "NUMBER_OF_ERROR_QUERIES", "NUMBER_OF_GETMORE_COMMANDS", "NUMBER_OF_INDEX_FIELDS", "NUMBER_OF_INSERTS", "NUMBER_OF_SUCCESS_QUERIES", "NUMBER_OF_UPDATES", "REPLICATION_LAG", "TOTAL_NUMBER_OF_QUERIES", ] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
processId | ProcessIdSchema | | 
databaseName | DatabaseNameSchema | | 
collectionName | CollectionNameSchema | | 
groupId | GroupIdSchema | | 

# ProcessIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DatabaseNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CollectionNameSchema

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
200 | [ApiResponseFor200](#list_index_metrics.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#list_index_metrics.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#list_index_metrics.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#list_index_metrics.ApiResponseFor500) | Internal Server Error

#### list_index_metrics.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiMeasurementsIndexesView**](../../models/ApiMeasurementsIndexesView.md) |  | 


#### list_index_metrics.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### list_index_metrics.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### list_index_metrics.ApiResponseFor500
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

# **list_metric_types**
<a name="list_metric_types"></a>
> ApiFTSMetricsView list_metric_types(process_idgroup_id)

Return All Atlas Search Metric Types for One Process

Return all Atlas Search metric types available for one process in the specified project.

### Example

```python
import atlas
from atlas.apis.tags import monitoring_and_logs_api
from atlas.model.api_error import ApiError
from atlas.model.api_fts_metrics_view import ApiFTSMetricsView
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = monitoring_and_logs_api.MonitoringAndLogsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'processId': "my.host.name.com:27017",
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    try:
        # Return All Atlas Search Metric Types for One Process
        api_response = api_instance.list_metric_types(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->list_metric_types: %s\n" % e)

    # example passing only optional values
    path_params = {
        'processId': "my.host.name.com:27017",
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'envelope': False,
    }
    try:
        # Return All Atlas Search Metric Types for One Process
        api_response = api_instance.list_metric_types(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MonitoringAndLogsApi->list_metric_types: %s\n" % e)
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
processId | ProcessIdSchema | | 
groupId | GroupIdSchema | | 

# ProcessIdSchema

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
200 | [ApiResponseFor200](#list_metric_types.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#list_metric_types.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#list_metric_types.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#list_metric_types.ApiResponseFor500) | Internal Server Error

#### list_metric_types.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiFTSMetricsView**](../../models/ApiFTSMetricsView.md) |  | 


#### list_metric_types.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### list_metric_types.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### list_metric_types.ApiResponseFor500
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

