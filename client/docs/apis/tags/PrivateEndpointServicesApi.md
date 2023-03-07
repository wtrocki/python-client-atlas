<a name="__pageTop"></a>
# atlas.apis.tags.private_endpoint_services_api.PrivateEndpointServicesApi

All URIs are relative to *https://cloud.mongodb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_private_endpoint**](#create_private_endpoint) | **post** /api/atlas/v2/groups/{groupId}/privateEndpoint/{cloudProvider}/endpointService/{endpointServiceId}/endpoint | Create One Private Endpoint for One Provider
[**create_private_endpoint_service**](#create_private_endpoint_service) | **post** /api/atlas/v2/groups/{groupId}/privateEndpoint/endpointService | Create One Private Endpoint Service for One Provider
[**delete_private_endpoint**](#delete_private_endpoint) | **delete** /api/atlas/v2/groups/{groupId}/privateEndpoint/{cloudProvider}/endpointService/{endpointServiceId}/endpoint/{endpointId} | Remove One Private Endpoint for One Provider
[**delete_private_endpoint_service**](#delete_private_endpoint_service) | **delete** /api/atlas/v2/groups/{groupId}/privateEndpoint/{cloudProvider}/endpointService/{endpointServiceId} | Remove One Private Endpoint Service for One Provider
[**get_private_endpoint**](#get_private_endpoint) | **get** /api/atlas/v2/groups/{groupId}/privateEndpoint/{cloudProvider}/endpointService/{endpointServiceId}/endpoint/{endpointId} | Return One Private Endpoint for One Provider
[**get_private_endpoint_service**](#get_private_endpoint_service) | **get** /api/atlas/v2/groups/{groupId}/privateEndpoint/{cloudProvider}/endpointService/{endpointServiceId} | Return One Private Endpoint Service for One Provider
[**get_regionalized_private_endpoint_setting**](#get_regionalized_private_endpoint_setting) | **get** /api/atlas/v2/groups/{groupId}/privateEndpoint/regionalMode | Return Regionalized Private Endpoint Status
[**list_private_endpoint_services**](#list_private_endpoint_services) | **get** /api/atlas/v2/groups/{groupId}/privateEndpoint/{cloudProvider}/endpointService | Return All Private Endpoint Services for One Provider
[**toggle_regionalized_private_endpoint_setting**](#toggle_regionalized_private_endpoint_setting) | **patch** /api/atlas/v2/groups/{groupId}/privateEndpoint/regionalMode | Toggle Regionalized Private Endpoint Status

# **create_private_endpoint**
<a name="create_private_endpoint"></a>
> Endpoint create_private_endpoint(group_idendpoint_service_idany_type)

Create One Private Endpoint for One Provider

Creates one private resource in the specified private resource service hosted from one cloud service provider. This cloud service provider manages the private resource service for the project. To use this resource, the requesting API Key must have the Project Atlas Admin role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import private_endpoint_services_api
from atlas.model.api_error import ApiError
from atlas.model.create_azure_endpoint_request import CreateAzureEndpointRequest
from atlas.model.endpoint import Endpoint
from atlas.model.create_aws_endpoint_request import CreateAWSEndpointRequest
from atlas.model.create_gcp_endpoint_group_request import CreateGCPEndpointGroupRequest
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = private_endpoint_services_api.PrivateEndpointServicesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'cloudProvider': "AWS",
        'endpointServiceId': "bf325375e030fccba0091731",
    }
    query_params = {
    }
    body = dict()
    try:
        # Create One Private Endpoint for One Provider
        api_response = api_instance.create_private_endpoint(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling PrivateEndpointServicesApi->create_private_endpoint: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'cloudProvider': "AWS",
        'endpointServiceId': "bf325375e030fccba0091731",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    body = dict()
    try:
        # Create One Private Endpoint for One Provider
        api_response = api_instance.create_private_endpoint(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling PrivateEndpointServicesApi->create_private_endpoint: %s\n" % e)
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

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[CreateAWSEndpointRequest]({{complexTypePrefix}}CreateAWSEndpointRequest.md) | [**CreateAWSEndpointRequest**]({{complexTypePrefix}}CreateAWSEndpointRequest.md) | [**CreateAWSEndpointRequest**]({{complexTypePrefix}}CreateAWSEndpointRequest.md) |  | 
[CreateAzureEndpointRequest]({{complexTypePrefix}}CreateAzureEndpointRequest.md) | [**CreateAzureEndpointRequest**]({{complexTypePrefix}}CreateAzureEndpointRequest.md) | [**CreateAzureEndpointRequest**]({{complexTypePrefix}}CreateAzureEndpointRequest.md) |  | 
[CreateGCPEndpointGroupRequest]({{complexTypePrefix}}CreateGCPEndpointGroupRequest.md) | [**CreateGCPEndpointGroupRequest**]({{complexTypePrefix}}CreateGCPEndpointGroupRequest.md) | [**CreateGCPEndpointGroupRequest**]({{complexTypePrefix}}CreateGCPEndpointGroupRequest.md) |  | 

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
cloudProvider | CloudProviderSchema | | 
endpointServiceId | EndpointServiceIdSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CloudProviderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["AWS", "AZURE", "GCP", ] if omitted the server will use the default value of "AWS"

# EndpointServiceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_private_endpoint.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#create_private_endpoint.ApiResponseFor400) | Bad Request
402 | [ApiResponseFor402](#create_private_endpoint.ApiResponseFor402) | Payment Required
404 | [ApiResponseFor404](#create_private_endpoint.ApiResponseFor404) | Not Found
409 | [ApiResponseFor409](#create_private_endpoint.ApiResponseFor409) | Conflict
500 | [ApiResponseFor500](#create_private_endpoint.ApiResponseFor500) | Internal Server Error

#### create_private_endpoint.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**Endpoint**](../../models/Endpoint.md) |  | 


#### create_private_endpoint.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### create_private_endpoint.ApiResponseFor402
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor402ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor402ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### create_private_endpoint.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### create_private_endpoint.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### create_private_endpoint.ApiResponseFor500
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

# **create_private_endpoint_service**
<a name="create_private_endpoint_service"></a>
> EndpointService create_private_endpoint_service(group_idcreate_endpoint_service_request)

Create One Private Endpoint Service for One Provider

Creates one private resource service for the specified cloud service provider. This cloud service provider manages the private resource service for the project. To use this resource, the requesting API Key must have the Project Atlas Admin role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import private_endpoint_services_api
from atlas.model.api_error import ApiError
from atlas.model.create_endpoint_service_request import CreateEndpointServiceRequest
from atlas.model.endpoint_service import EndpointService
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = private_endpoint_services_api.PrivateEndpointServicesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    body = CreateEndpointServiceRequest(
        provider_name="AWS",
        region="region_example",
    )
    try:
        # Create One Private Endpoint Service for One Provider
        api_response = api_instance.create_private_endpoint_service(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling PrivateEndpointServicesApi->create_private_endpoint_service: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    body = CreateEndpointServiceRequest(
        provider_name="AWS",
        region="region_example",
    )
    try:
        # Create One Private Endpoint Service for One Provider
        api_response = api_instance.create_private_endpoint_service(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling PrivateEndpointServicesApi->create_private_endpoint_service: %s\n" % e)
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
[**CreateEndpointServiceRequest**](../../models/CreateEndpointServiceRequest.md) |  | 


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
200 | [ApiResponseFor200](#create_private_endpoint_service.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#create_private_endpoint_service.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#create_private_endpoint_service.ApiResponseFor500) | Internal Server Error

#### create_private_endpoint_service.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**EndpointService**](../../models/EndpointService.md) |  | 


#### create_private_endpoint_service.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### create_private_endpoint_service.ApiResponseFor500
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

# **delete_private_endpoint**
<a name="delete_private_endpoint"></a>
> delete_private_endpoint(group_idendpoint_idendpoint_service_id)

Remove One Private Endpoint for One Provider

Removes one private resource from the specified project. This cloud service provider manages the private resource service that manages the private resource that belongs to the project. To use this resource, the requesting API Key must have the Project Atlas Admin role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import private_endpoint_services_api
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
    api_instance = private_endpoint_services_api.PrivateEndpointServicesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'cloudProvider': "AWS",
        'endpointId': "%2fsubscriptions%2F25375e03-0fcc-ba00-9173-17c574773100%2fresourcegroups%2F8KoK01UH0)8)kQEFkLkvyHfCdEAAg8zj4gGu)(shjbE0Eva55tk-LlJwL3CTLxzWhej1zFvhjFRboDzLsp6gf0OAK%2fproviders%2fMicrosoft.Network%2fprivateEndpoints%2Fl(uFEEYdpfNsNsac1)SIo6lS-8RLNCj.v",
        'endpointServiceId': "bf325375e030fccba0091731",
    }
    query_params = {
    }
    try:
        # Remove One Private Endpoint for One Provider
        api_response = api_instance.delete_private_endpoint(
            path_params=path_params,
            query_params=query_params,
        )
    except atlas.ApiException as e:
        print("Exception when calling PrivateEndpointServicesApi->delete_private_endpoint: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'cloudProvider': "AWS",
        'endpointId': "%2fsubscriptions%2F25375e03-0fcc-ba00-9173-17c574773100%2fresourcegroups%2F8KoK01UH0)8)kQEFkLkvyHfCdEAAg8zj4gGu)(shjbE0Eva55tk-LlJwL3CTLxzWhej1zFvhjFRboDzLsp6gf0OAK%2fproviders%2fMicrosoft.Network%2fprivateEndpoints%2Fl(uFEEYdpfNsNsac1)SIo6lS-8RLNCj.v",
        'endpointServiceId': "bf325375e030fccba0091731",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    try:
        # Remove One Private Endpoint for One Provider
        api_response = api_instance.delete_private_endpoint(
            path_params=path_params,
            query_params=query_params,
        )
    except atlas.ApiException as e:
        print("Exception when calling PrivateEndpointServicesApi->delete_private_endpoint: %s\n" % e)
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
cloudProvider | CloudProviderSchema | | 
endpointId | EndpointIdSchema | | 
endpointServiceId | EndpointServiceIdSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CloudProviderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["AWS", "AZURE", "GCP", ] if omitted the server will use the default value of "AWS"

# EndpointIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EndpointServiceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_private_endpoint.ApiResponseFor204) | This endpoint does not return a response body.
400 | [ApiResponseFor400](#delete_private_endpoint.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#delete_private_endpoint.ApiResponseFor500) | Internal Server Error

#### delete_private_endpoint.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_private_endpoint.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### delete_private_endpoint.ApiResponseFor500
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

# **delete_private_endpoint_service**
<a name="delete_private_endpoint_service"></a>
> delete_private_endpoint_service(group_idendpoint_service_id)

Remove One Private Endpoint Service for One Provider

Removes one private resource service from the specified project. This cloud service provider manages the private resource service that belongs to the project. To use this resource, the requesting API Key must have the Project Atlas Admin role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import private_endpoint_services_api
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
    api_instance = private_endpoint_services_api.PrivateEndpointServicesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'cloudProvider': "AWS",
        'endpointServiceId': "bf325375e030fccba0091731",
    }
    query_params = {
    }
    try:
        # Remove One Private Endpoint Service for One Provider
        api_response = api_instance.delete_private_endpoint_service(
            path_params=path_params,
            query_params=query_params,
        )
    except atlas.ApiException as e:
        print("Exception when calling PrivateEndpointServicesApi->delete_private_endpoint_service: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'cloudProvider': "AWS",
        'endpointServiceId': "bf325375e030fccba0091731",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    try:
        # Remove One Private Endpoint Service for One Provider
        api_response = api_instance.delete_private_endpoint_service(
            path_params=path_params,
            query_params=query_params,
        )
    except atlas.ApiException as e:
        print("Exception when calling PrivateEndpointServicesApi->delete_private_endpoint_service: %s\n" % e)
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
cloudProvider | CloudProviderSchema | | 
endpointServiceId | EndpointServiceIdSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CloudProviderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["AWS", "AZURE", "GCP", ] if omitted the server will use the default value of "AWS"

# EndpointServiceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_private_endpoint_service.ApiResponseFor204) | This endpoint does not return a response body.
400 | [ApiResponseFor400](#delete_private_endpoint_service.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#delete_private_endpoint_service.ApiResponseFor500) | Internal Server Error

#### delete_private_endpoint_service.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_private_endpoint_service.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### delete_private_endpoint_service.ApiResponseFor500
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

# **get_private_endpoint**
<a name="get_private_endpoint"></a>
> Endpoint get_private_endpoint(group_idendpoint_idendpoint_service_id)

Return One Private Endpoint for One Provider

Returns the connection state of the specified private resource. The private resource service manages this private resource which belongs to one project hosted from one cloud service provider. To use this resource, the requesting API Key must have the Project Read Only role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import private_endpoint_services_api
from atlas.model.api_error import ApiError
from atlas.model.endpoint import Endpoint
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = private_endpoint_services_api.PrivateEndpointServicesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'cloudProvider': "AWS",
        'endpointId': "%2fsubscriptions%2F25375e03-0fcc-ba00-9173-17c574773100%2fresourcegroups%2F8KoK01UH0)8)kQEFkLkvyHfCdEAAg8zj4gGu)(shjbE0Eva55tk-LlJwL3CTLxzWhej1zFvhjFRboDzLsp6gf0OAK%2fproviders%2fMicrosoft.Network%2fprivateEndpoints%2Fl(uFEEYdpfNsNsac1)SIo6lS-8RLNCj.v",
        'endpointServiceId': "bf325375e030fccba0091731",
    }
    query_params = {
    }
    try:
        # Return One Private Endpoint for One Provider
        api_response = api_instance.get_private_endpoint(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling PrivateEndpointServicesApi->get_private_endpoint: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'cloudProvider': "AWS",
        'endpointId': "%2fsubscriptions%2F25375e03-0fcc-ba00-9173-17c574773100%2fresourcegroups%2F8KoK01UH0)8)kQEFkLkvyHfCdEAAg8zj4gGu)(shjbE0Eva55tk-LlJwL3CTLxzWhej1zFvhjFRboDzLsp6gf0OAK%2fproviders%2fMicrosoft.Network%2fprivateEndpoints%2Fl(uFEEYdpfNsNsac1)SIo6lS-8RLNCj.v",
        'endpointServiceId': "bf325375e030fccba0091731",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    try:
        # Return One Private Endpoint for One Provider
        api_response = api_instance.get_private_endpoint(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling PrivateEndpointServicesApi->get_private_endpoint: %s\n" % e)
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
cloudProvider | CloudProviderSchema | | 
endpointId | EndpointIdSchema | | 
endpointServiceId | EndpointServiceIdSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CloudProviderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["AWS", "AZURE", "GCP", ] if omitted the server will use the default value of "AWS"

# EndpointIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# EndpointServiceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_private_endpoint.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_private_endpoint.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#get_private_endpoint.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_private_endpoint.ApiResponseFor500) | Internal Server Error

#### get_private_endpoint.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**Endpoint**](../../models/Endpoint.md) |  | 


#### get_private_endpoint.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_private_endpoint.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_private_endpoint.ApiResponseFor500
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

# **get_private_endpoint_service**
<a name="get_private_endpoint_service"></a>
> EndpointService get_private_endpoint_service(group_idendpoint_service_id)

Return One Private Endpoint Service for One Provider

Returns the name, interfaces, and state of the specified private resource service from one project. The cloud service provider hosted this private resource service that belongs to the project. To use this resource, the requesting API Key must have the Project Read Only role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import private_endpoint_services_api
from atlas.model.api_error import ApiError
from atlas.model.endpoint_service import EndpointService
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = private_endpoint_services_api.PrivateEndpointServicesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'cloudProvider': "AWS",
        'endpointServiceId': "bf325375e030fccba0091731",
    }
    query_params = {
    }
    try:
        # Return One Private Endpoint Service for One Provider
        api_response = api_instance.get_private_endpoint_service(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling PrivateEndpointServicesApi->get_private_endpoint_service: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'cloudProvider': "AWS",
        'endpointServiceId': "bf325375e030fccba0091731",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    try:
        # Return One Private Endpoint Service for One Provider
        api_response = api_instance.get_private_endpoint_service(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling PrivateEndpointServicesApi->get_private_endpoint_service: %s\n" % e)
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
cloudProvider | CloudProviderSchema | | 
endpointServiceId | EndpointServiceIdSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CloudProviderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["AWS", "AZURE", "GCP", ] if omitted the server will use the default value of "AWS"

# EndpointServiceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_private_endpoint_service.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_private_endpoint_service.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#get_private_endpoint_service.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_private_endpoint_service.ApiResponseFor500) | Internal Server Error

#### get_private_endpoint_service.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**EndpointService**](../../models/EndpointService.md) |  | 


#### get_private_endpoint_service.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_private_endpoint_service.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_private_endpoint_service.ApiResponseFor500
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

# **get_regionalized_private_endpoint_setting**
<a name="get_regionalized_private_endpoint_setting"></a>
> ProjectSettingItemView get_regionalized_private_endpoint_setting(group_id)

Return Regionalized Private Endpoint Status

Checks whether each region in the specified cloud service provider can create multiple private resources per region. The cloud service provider manages the private resource for the project. To use this resource, the requesting API Key must have the Project Read Only role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import private_endpoint_services_api
from atlas.model.api_error import ApiError
from atlas.model.project_setting_item_view import ProjectSettingItemView
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = private_endpoint_services_api.PrivateEndpointServicesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    try:
        # Return Regionalized Private Endpoint Status
        api_response = api_instance.get_regionalized_private_endpoint_setting(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling PrivateEndpointServicesApi->get_regionalized_private_endpoint_setting: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    try:
        # Return Regionalized Private Endpoint Status
        api_response = api_instance.get_regionalized_private_endpoint_setting(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling PrivateEndpointServicesApi->get_regionalized_private_endpoint_setting: %s\n" % e)
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
200 | [ApiResponseFor200](#get_regionalized_private_endpoint_setting.ApiResponseFor200) | OK
403 | [ApiResponseFor403](#get_regionalized_private_endpoint_setting.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#get_regionalized_private_endpoint_setting.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_regionalized_private_endpoint_setting.ApiResponseFor500) | Internal Server Error

#### get_regionalized_private_endpoint_setting.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectSettingItemView**](../../models/ProjectSettingItemView.md) |  | 


#### get_regionalized_private_endpoint_setting.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_regionalized_private_endpoint_setting.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_regionalized_private_endpoint_setting.ApiResponseFor500
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

# **list_private_endpoint_services**
<a name="list_private_endpoint_services"></a>
> PaginatedPrivateLinkConnectionView list_private_endpoint_services(group_id)

Return All Private Endpoint Services for One Provider

Returns the name, interfaces, and state of all private resource services for the specified cloud service provider. This cloud service provider manages the private resource service for the project. To use this resource, the requesting API Key must have the Project Read Only role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import private_endpoint_services_api
from atlas.model.paginated_private_link_connection_view import PaginatedPrivateLinkConnectionView
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
    api_instance = private_endpoint_services_api.PrivateEndpointServicesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'cloudProvider': "AWS",
    }
    query_params = {
    }
    try:
        # Return All Private Endpoint Services for One Provider
        api_response = api_instance.list_private_endpoint_services(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling PrivateEndpointServicesApi->list_private_endpoint_services: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'cloudProvider': "AWS",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    try:
        # Return All Private Endpoint Services for One Provider
        api_response = api_instance.list_private_endpoint_services(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling PrivateEndpointServicesApi->list_private_endpoint_services: %s\n" % e)
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
cloudProvider | CloudProviderSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CloudProviderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["AWS", "AZURE", "GCP", ] if omitted the server will use the default value of "AWS"

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_private_endpoint_services.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#list_private_endpoint_services.ApiResponseFor400) | Bad Request
500 | [ApiResponseFor500](#list_private_endpoint_services.ApiResponseFor500) | Internal Server Error

#### list_private_endpoint_services.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**PaginatedPrivateLinkConnectionView**](../../models/PaginatedPrivateLinkConnectionView.md) |  | 


#### list_private_endpoint_services.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### list_private_endpoint_services.ApiResponseFor500
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

# **toggle_regionalized_private_endpoint_setting**
<a name="toggle_regionalized_private_endpoint_setting"></a>
> ProjectSettingItemView toggle_regionalized_private_endpoint_setting(group_idproject_setting_item_view)

Toggle Regionalized Private Endpoint Status

Enables or disables the ability can create multiple private resources per region in all cloud service providers in one project. The cloud service provider manages the private resource for the project. To use this resource, the requesting API Key must have the Project Atlas Admin role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import private_endpoint_services_api
from atlas.model.api_error import ApiError
from atlas.model.project_setting_item_view import ProjectSettingItemView
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = private_endpoint_services_api.PrivateEndpointServicesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    body = ProjectSettingItemView(
        enabled=True,
    )
    try:
        # Toggle Regionalized Private Endpoint Status
        api_response = api_instance.toggle_regionalized_private_endpoint_setting(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling PrivateEndpointServicesApi->toggle_regionalized_private_endpoint_setting: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    body = ProjectSettingItemView(
        enabled=True,
    )
    try:
        # Toggle Regionalized Private Endpoint Status
        api_response = api_instance.toggle_regionalized_private_endpoint_setting(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling PrivateEndpointServicesApi->toggle_regionalized_private_endpoint_setting: %s\n" % e)
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
[**ProjectSettingItemView**](../../models/ProjectSettingItemView.md) |  | 


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
200 | [ApiResponseFor200](#toggle_regionalized_private_endpoint_setting.ApiResponseFor200) | OK
404 | [ApiResponseFor404](#toggle_regionalized_private_endpoint_setting.ApiResponseFor404) | Not Found
409 | [ApiResponseFor409](#toggle_regionalized_private_endpoint_setting.ApiResponseFor409) | Conflict
500 | [ApiResponseFor500](#toggle_regionalized_private_endpoint_setting.ApiResponseFor500) | Internal Server Error

#### toggle_regionalized_private_endpoint_setting.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**ProjectSettingItemView**](../../models/ProjectSettingItemView.md) |  | 


#### toggle_regionalized_private_endpoint_setting.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### toggle_regionalized_private_endpoint_setting.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### toggle_regionalized_private_endpoint_setting.ApiResponseFor500
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

