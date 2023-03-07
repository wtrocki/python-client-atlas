<a name="__pageTop"></a>
# atlas.apis.tags.maintenance_windows_api.MaintenanceWindowsApi

All URIs are relative to *https://cloud.mongodb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**defer_maintenance_window**](#defer_maintenance_window) | **post** /api/atlas/v2/groups/{groupId}/maintenanceWindow/defer | Defer One Maintenance Window for One Project
[**get_maintenance_window**](#get_maintenance_window) | **get** /api/atlas/v2/groups/{groupId}/maintenanceWindow | Return One Maintenance Window for One Project
[**reset_maintenance_window**](#reset_maintenance_window) | **delete** /api/atlas/v2/groups/{groupId}/maintenanceWindow | Reset One Maintenance Window for One Project
[**toggle_maintenance_auto_defer**](#toggle_maintenance_auto_defer) | **post** /api/atlas/v2/groups/{groupId}/maintenanceWindow/autoDefer | Toggle Automatic Deferral of Maintenance for One Project
[**update_maintenance_window**](#update_maintenance_window) | **patch** /api/atlas/v2/groups/{groupId}/maintenanceWindow | Update Maintenance Window for One Project

# **defer_maintenance_window**
<a name="defer_maintenance_window"></a>
> defer_maintenance_window(group_id)

Defer One Maintenance Window for One Project

Defers the maintenance window for the specified project. To use this resource, the requesting API Key must have the Project Atlas Admin role.This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import maintenance_windows_api
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
    api_instance = maintenance_windows_api.MaintenanceWindowsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    try:
        # Defer One Maintenance Window for One Project
        api_response = api_instance.defer_maintenance_window(
            path_params=path_params,
            query_params=query_params,
        )
    except atlas.ApiException as e:
        print("Exception when calling MaintenanceWindowsApi->defer_maintenance_window: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'envelope': False,
    }
    try:
        # Defer One Maintenance Window for One Project
        api_response = api_instance.defer_maintenance_window(
            path_params=path_params,
            query_params=query_params,
        )
    except atlas.ApiException as e:
        print("Exception when calling MaintenanceWindowsApi->defer_maintenance_window: %s\n" % e)
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

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#defer_maintenance_window.ApiResponseFor204) | This endpoint does not return a response body.
400 | [ApiResponseFor400](#defer_maintenance_window.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#defer_maintenance_window.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#defer_maintenance_window.ApiResponseFor500) | Internal Server Error

#### defer_maintenance_window.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### defer_maintenance_window.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### defer_maintenance_window.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### defer_maintenance_window.ApiResponseFor500
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

# **get_maintenance_window**
<a name="get_maintenance_window"></a>
> GroupMaintenanceWindow get_maintenance_window(group_id)

Return One Maintenance Window for One Project

Returns the maintenance window for the specified project. To use this resource, the requesting API Key must have the Project Read Only role.This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import maintenance_windows_api
from atlas.model.group_maintenance_window import GroupMaintenanceWindow
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
    api_instance = maintenance_windows_api.MaintenanceWindowsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    try:
        # Return One Maintenance Window for One Project
        api_response = api_instance.get_maintenance_window(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MaintenanceWindowsApi->get_maintenance_window: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    try:
        # Return One Maintenance Window for One Project
        api_response = api_instance.get_maintenance_window(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling MaintenanceWindowsApi->get_maintenance_window: %s\n" % e)
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

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_maintenance_window.ApiResponseFor200) | OK
404 | [ApiResponseFor404](#get_maintenance_window.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_maintenance_window.ApiResponseFor500) | Internal Server Error

#### get_maintenance_window.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**GroupMaintenanceWindow**](../../models/GroupMaintenanceWindow.md) |  | 


#### get_maintenance_window.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_maintenance_window.ApiResponseFor500
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

# **reset_maintenance_window**
<a name="reset_maintenance_window"></a>
> reset_maintenance_window(group_id)

Reset One Maintenance Window for One Project

Resets the maintenance window for the specified project. To use this resource, the requesting API Key must have the Project Atlas Admin role.This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import maintenance_windows_api
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
    api_instance = maintenance_windows_api.MaintenanceWindowsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    try:
        # Reset One Maintenance Window for One Project
        api_response = api_instance.reset_maintenance_window(
            path_params=path_params,
            query_params=query_params,
        )
    except atlas.ApiException as e:
        print("Exception when calling MaintenanceWindowsApi->reset_maintenance_window: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'envelope': False,
    }
    try:
        # Reset One Maintenance Window for One Project
        api_response = api_instance.reset_maintenance_window(
            path_params=path_params,
            query_params=query_params,
        )
    except atlas.ApiException as e:
        print("Exception when calling MaintenanceWindowsApi->reset_maintenance_window: %s\n" % e)
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

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#reset_maintenance_window.ApiResponseFor204) | This endpoint does not return a response body.
400 | [ApiResponseFor400](#reset_maintenance_window.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#reset_maintenance_window.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#reset_maintenance_window.ApiResponseFor500) | Internal Server Error

#### reset_maintenance_window.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### reset_maintenance_window.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### reset_maintenance_window.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### reset_maintenance_window.ApiResponseFor500
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

# **toggle_maintenance_auto_defer**
<a name="toggle_maintenance_auto_defer"></a>
> toggle_maintenance_auto_defer(group_id)

Toggle Automatic Deferral of Maintenance for One Project

Toggles automatic deferral of the maintenance window for the specified project. To use this resource, the requesting API Key must have the Project Owner role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import maintenance_windows_api
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
    api_instance = maintenance_windows_api.MaintenanceWindowsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    try:
        # Toggle Automatic Deferral of Maintenance for One Project
        api_response = api_instance.toggle_maintenance_auto_defer(
            path_params=path_params,
            query_params=query_params,
        )
    except atlas.ApiException as e:
        print("Exception when calling MaintenanceWindowsApi->toggle_maintenance_auto_defer: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'envelope': False,
    }
    try:
        # Toggle Automatic Deferral of Maintenance for One Project
        api_response = api_instance.toggle_maintenance_auto_defer(
            path_params=path_params,
            query_params=query_params,
        )
    except atlas.ApiException as e:
        print("Exception when calling MaintenanceWindowsApi->toggle_maintenance_auto_defer: %s\n" % e)
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

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#toggle_maintenance_auto_defer.ApiResponseFor204) | This endpoint does not return a response body.
400 | [ApiResponseFor400](#toggle_maintenance_auto_defer.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#toggle_maintenance_auto_defer.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#toggle_maintenance_auto_defer.ApiResponseFor500) | Internal Server Error

#### toggle_maintenance_auto_defer.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### toggle_maintenance_auto_defer.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### toggle_maintenance_auto_defer.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### toggle_maintenance_auto_defer.ApiResponseFor500
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

# **update_maintenance_window**
<a name="update_maintenance_window"></a>
> update_maintenance_window(group_idgroup_maintenance_window)

Update Maintenance Window for One Project

Updates the maintenance window for the specified project. To use this resource, the requesting API Key must have the Project Atlas Admin role.This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import maintenance_windows_api
from atlas.model.group_maintenance_window import GroupMaintenanceWindow
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
    api_instance = maintenance_windows_api.MaintenanceWindowsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    body = GroupMaintenanceWindow(
        auto_defer_once_enabled=True,
        day_of_week=1,
        hour_of_day=0,
        start_asap=True,
    )
    try:
        # Update Maintenance Window for One Project
        api_response = api_instance.update_maintenance_window(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except atlas.ApiException as e:
        print("Exception when calling MaintenanceWindowsApi->update_maintenance_window: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'envelope': False,
    }
    body = GroupMaintenanceWindow(
        auto_defer_once_enabled=True,
        day_of_week=1,
        hour_of_day=0,
        start_asap=True,
    )
    try:
        # Update Maintenance Window for One Project
        api_response = api_instance.update_maintenance_window(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except atlas.ApiException as e:
        print("Exception when calling MaintenanceWindowsApi->update_maintenance_window: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationVndAtlas20230101json] | required |
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/vnd.atlas.2023-01-01+json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**GroupMaintenanceWindow**](../../models/GroupMaintenanceWindow.md) |  | 


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

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#update_maintenance_window.ApiResponseFor204) | This endpoint does not return a response body.
400 | [ApiResponseFor400](#update_maintenance_window.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#update_maintenance_window.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#update_maintenance_window.ApiResponseFor500) | Internal Server Error

#### update_maintenance_window.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_maintenance_window.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### update_maintenance_window.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### update_maintenance_window.ApiResponseFor500
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

