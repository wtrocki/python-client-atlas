<a name="__pageTop"></a>
# atlas.apis.tags.rolling_index_api.RollingIndexApi

All URIs are relative to *https://cloud.mongodb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rolling_index**](#create_rolling_index) | **post** /api/atlas/v2/groups/{groupId}/clusters/{clusterName}/index | Create One Rolling Index

# **create_rolling_index**
<a name="create_rolling_index"></a>
> create_rolling_index(group_idcluster_nameapi_index_request_view)

Create One Rolling Index

Creates an index on the cluster identified by its name in a rolling manner. Creating the index in this way allows index builds on one replica set member as a standalone at a time, starting with the secondary members. Creating indexes in this way requires at least one replica set election. To use this resource, the requesting API Key must have the Project Data Access Admin role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import rolling_index_api
from atlas.model.api_index_request_view import ApiIndexRequestView
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
    api_instance = rolling_index_api.RollingIndexApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'clusterName': "gqW,C",
    }
    query_params = {
    }
    body = ApiIndexRequestView(
        collation=Collation(
            alternate="non-ignorable",
            backwards=False,
            case_first="false",
            case_level=False,
            locale="af",
            max_variable="punct",
            normalization=False,
            numeric_ordering=False,
            strength=3,
        ),
        collection="collection_example",
        db="db_example",
        keys=[
            dict(
                "key": "key_example",
            )
        ],
        options=IndexOptions(
            _2dsphere_index_version=3,
            background=False,
            bits=26,
            bucket_size=1,
            default_language="english",
            expire_after_seconds=1,
            hidden=False,
            language_override="language",
            max=180,
            min=-180,
            name="name_example",
            partial_filter_expression=dict(
                "key": dict(),
            ),
            sparse=False,
            storage_engine=dict(
                "key": dict(),
            ),
            text_index_version=3,
            unique=False,
            weights=dict(
                "key": dict(),
            ),
        ),
    )
    try:
        # Create One Rolling Index
        api_response = api_instance.create_rolling_index(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except atlas.ApiException as e:
        print("Exception when calling RollingIndexApi->create_rolling_index: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'clusterName': "gqW,C",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    body = ApiIndexRequestView(
        collation=Collation(
            alternate="non-ignorable",
            backwards=False,
            case_first="false",
            case_level=False,
            locale="af",
            max_variable="punct",
            normalization=False,
            numeric_ordering=False,
            strength=3,
        ),
        collection="collection_example",
        db="db_example",
        keys=[
            dict(
                "key": "key_example",
            )
        ],
        options=IndexOptions(
            _2dsphere_index_version=3,
            background=False,
            bits=26,
            bucket_size=1,
            default_language="english",
            expire_after_seconds=1,
            hidden=False,
            language_override="language",
            max=180,
            min=-180,
            name="name_example",
            partial_filter_expression=dict(
                "key": dict(),
            ),
            sparse=False,
            storage_engine=dict(
                "key": dict(),
            ),
            text_index_version=3,
            unique=False,
            weights=dict(
                "key": dict(),
            ),
        ),
    )
    try:
        # Create One Rolling Index
        api_response = api_instance.create_rolling_index(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
    except atlas.ApiException as e:
        print("Exception when calling RollingIndexApi->create_rolling_index: %s\n" % e)
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
[**ApiIndexRequestView**](../../models/ApiIndexRequestView.md) |  | 


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
204 | [ApiResponseFor204](#create_rolling_index.ApiResponseFor204) | This endpoint does not return a response body.
400 | [ApiResponseFor400](#create_rolling_index.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#create_rolling_index.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#create_rolling_index.ApiResponseFor500) | Internal Server Error

#### create_rolling_index.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### create_rolling_index.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### create_rolling_index.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### create_rolling_index.ApiResponseFor500
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

