<a name="__pageTop"></a>
# atlas.apis.tags.federated_authentication_api.FederatedAuthenticationApi

All URIs are relative to *https://cloud.mongodb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role_mapping**](#create_role_mapping) | **post** /api/atlas/v2/federationSettings/{federationSettingsId}/connectedOrgConfigs/{orgId}/roleMappings | Add One Role Mapping to One Organization
[**delete_federation_app**](#delete_federation_app) | **delete** /api/atlas/v2/federationSettings/{federationSettingsId} | Delete the federation settings instance.
[**delete_role_mapping**](#delete_role_mapping) | **delete** /api/atlas/v2/federationSettings/{federationSettingsId}/connectedOrgConfigs/{orgId}/roleMappings/{id} | Remove One Role Mapping from One Organization
[**get_connected_org_config**](#get_connected_org_config) | **get** /api/atlas/v2/federationSettings/{federationSettingsId}/connectedOrgConfigs/{orgId} | Return One Org Config Connected to One Federation
[**get_federation_settings**](#get_federation_settings) | **get** /api/atlas/v2/orgs/{orgId}/federationSettings | Return Federation Settings for One Organization
[**get_identity_provider**](#get_identity_provider) | **get** /api/atlas/v2/federationSettings/{federationSettingsId}/identityProviders/{identityProviderId} | Return one identity provider from the specified federation.
[**get_identity_provider_metadata**](#get_identity_provider_metadata) | **get** /api/atlas/v2/federationSettings/{federationSettingsId}/identityProviders/{identityProviderId}/metadata.xml | Return the metadata of one identity provider in the specified federation.
[**get_role_mapping**](#get_role_mapping) | **get** /api/atlas/v2/federationSettings/{federationSettingsId}/connectedOrgConfigs/{orgId}/roleMappings/{id} | Return One Role Mapping from One Organization
[**list_connected_org_configs**](#list_connected_org_configs) | **get** /api/atlas/v2/federationSettings/{federationSettingsId}/connectedOrgConfigs | Return All Connected Org Configs from the Federation
[**list_identity_providers**](#list_identity_providers) | **get** /api/atlas/v2/federationSettings/{federationSettingsId}/identityProviders | Return all identity providers from the specified federation.
[**list_role_mappings**](#list_role_mappings) | **get** /api/atlas/v2/federationSettings/{federationSettingsId}/connectedOrgConfigs/{orgId}/roleMappings | Return All Role Mappings from One Organization
[**remove_connected_org_config**](#remove_connected_org_config) | **delete** /api/atlas/v2/federationSettings/{federationSettingsId}/connectedOrgConfigs/{orgId} | Remove One Org Config Connected to One Federation
[**update_connected_org_config**](#update_connected_org_config) | **patch** /api/atlas/v2/federationSettings/{federationSettingsId}/connectedOrgConfigs/{orgId} | Update One Org Config Connected to One Federation
[**update_identity_provider**](#update_identity_provider) | **patch** /api/atlas/v2/federationSettings/{federationSettingsId}/identityProviders/{identityProviderId} | Update the identity provider.
[**update_role_mapping**](#update_role_mapping) | **put** /api/atlas/v2/federationSettings/{federationSettingsId}/connectedOrgConfigs/{orgId}/roleMappings/{id} | Update One Role Mapping in One Organization

# **create_role_mapping**
<a name="create_role_mapping"></a>
> RoleMappingView create_role_mapping(federation_settings_idorg_idrole_mapping_view)

Add One Role Mapping to One Organization

Adds one role mapping to the specified organization in the specified federation. To use this resource, the requesting API Key must have the Organization Owner role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import federated_authentication_api
from atlas.model.role_mapping_view import RoleMappingView
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
    api_instance = federated_authentication_api.FederatedAuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'federationSettingsId': "55fa922fb343282757d9554e",
        'orgId': "4888442a3354817a7320eb61",
    }
    query_params = {
    }
    body = RoleMappingView(
        external_group_name="external_group_name_example",
        id="32b6e34b3d91647abb20e7b8",
        role_assignments=[
            RoleAssignment(
                group_id="32b6e34b3d91647abb20e7b8",
                org_id="32b6e34b3d91647abb20e7b8",
                role="ORG_OWNER",
            )
        ],
    )
    try:
        # Add One Role Mapping to One Organization
        api_response = api_instance.create_role_mapping(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->create_role_mapping: %s\n" % e)

    # example passing only optional values
    path_params = {
        'federationSettingsId': "55fa922fb343282757d9554e",
        'orgId': "4888442a3354817a7320eb61",
    }
    query_params = {
        'envelope': False,
    }
    body = RoleMappingView(
        external_group_name="external_group_name_example",
        id="32b6e34b3d91647abb20e7b8",
        role_assignments=[
            RoleAssignment(
                group_id="32b6e34b3d91647abb20e7b8",
                org_id="32b6e34b3d91647abb20e7b8",
                role="ORG_OWNER",
            )
        ],
    )
    try:
        # Add One Role Mapping to One Organization
        api_response = api_instance.create_role_mapping(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->create_role_mapping: %s\n" % e)
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
[**RoleMappingView**](../../models/RoleMappingView.md) |  | 


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
federationSettingsId | FederationSettingsIdSchema | | 
orgId | OrgIdSchema | | 

# FederationSettingsIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrgIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_role_mapping.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#create_role_mapping.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#create_role_mapping.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#create_role_mapping.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#create_role_mapping.ApiResponseFor500) | Internal Server Error

#### create_role_mapping.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**RoleMappingView**](../../models/RoleMappingView.md) |  | 


#### create_role_mapping.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### create_role_mapping.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### create_role_mapping.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### create_role_mapping.ApiResponseFor500
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

# **delete_federation_app**
<a name="delete_federation_app"></a>
> delete_federation_app(federation_settings_id)

Delete the federation settings instance.

Deletes the federation settings instance and all associated data, including identity providers and domains. To use this resource, the requesting API Key must have the Organization Owner role in the last remaining connected organization. This resource doesn't require the API Key to have an Access List. **Note**: requests to this resource will fail if there is more than one connected organization in the federation.

### Example

```python
import atlas
from atlas.apis.tags import federated_authentication_api
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
    api_instance = federated_authentication_api.FederatedAuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'federationSettingsId': "55fa922fb343282757d9554e",
    }
    try:
        # Delete the federation settings instance.
        api_response = api_instance.delete_federation_app(
            path_params=path_params,
        )
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->delete_federation_app: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.atlas.2023-01-01+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
federationSettingsId | FederationSettingsIdSchema | | 

# FederationSettingsIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_federation_app.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_federation_app.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#delete_federation_app.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#delete_federation_app.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#delete_federation_app.ApiResponseFor500) | Internal Server Error

#### delete_federation_app.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### delete_federation_app.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### delete_federation_app.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### delete_federation_app.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### delete_federation_app.ApiResponseFor500
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

# **delete_role_mapping**
<a name="delete_role_mapping"></a>
> delete_role_mapping(federation_settings_ididorg_id)

Remove One Role Mapping from One Organization

Removes one role mapping in the specified organization from the specified federation. To use this resource, the requesting API Key must have the Organization Owner role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import federated_authentication_api
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
    api_instance = federated_authentication_api.FederatedAuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'federationSettingsId': "55fa922fb343282757d9554e",
        'id': "32b6e34b3d91647abb20e7b8",
        'orgId': "4888442a3354817a7320eb61",
    }
    query_params = {
    }
    try:
        # Remove One Role Mapping from One Organization
        api_response = api_instance.delete_role_mapping(
            path_params=path_params,
            query_params=query_params,
        )
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->delete_role_mapping: %s\n" % e)

    # example passing only optional values
    path_params = {
        'federationSettingsId': "55fa922fb343282757d9554e",
        'id': "32b6e34b3d91647abb20e7b8",
        'orgId': "4888442a3354817a7320eb61",
    }
    query_params = {
        'envelope': False,
    }
    try:
        # Remove One Role Mapping from One Organization
        api_response = api_instance.delete_role_mapping(
            path_params=path_params,
            query_params=query_params,
        )
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->delete_role_mapping: %s\n" % e)
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
federationSettingsId | FederationSettingsIdSchema | | 
id | IdSchema | | 
orgId | OrgIdSchema | | 

# FederationSettingsIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrgIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_role_mapping.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#delete_role_mapping.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#delete_role_mapping.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#delete_role_mapping.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#delete_role_mapping.ApiResponseFor500) | Internal Server Error

#### delete_role_mapping.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### delete_role_mapping.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### delete_role_mapping.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### delete_role_mapping.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### delete_role_mapping.ApiResponseFor500
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

# **get_connected_org_config**
<a name="get_connected_org_config"></a>
> ConnectedOrgConfigView get_connected_org_config(federation_settings_idorg_id)

Return One Org Config Connected to One Federation

Returns the specified connected org config from the specified federation. To use this resource, the requesting API Key must have the Organization Owner role in the connected org. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import federated_authentication_api
from atlas.model.api_error import ApiError
from atlas.model.connected_org_config_view import ConnectedOrgConfigView
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = federated_authentication_api.FederatedAuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'federationSettingsId': "55fa922fb343282757d9554e",
        'orgId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    try:
        # Return One Org Config Connected to One Federation
        api_response = api_instance.get_connected_org_config(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->get_connected_org_config: %s\n" % e)

    # example passing only optional values
    path_params = {
        'federationSettingsId': "55fa922fb343282757d9554e",
        'orgId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'envelope': False,
    }
    try:
        # Return One Org Config Connected to One Federation
        api_response = api_instance.get_connected_org_config(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->get_connected_org_config: %s\n" % e)
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
federationSettingsId | FederationSettingsIdSchema | | 
orgId | OrgIdSchema | | 

# FederationSettingsIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrgIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_connected_org_config.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_connected_org_config.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_connected_org_config.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_connected_org_config.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_connected_org_config.ApiResponseFor500) | Internal Server Error

#### get_connected_org_config.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**ConnectedOrgConfigView**](../../models/ConnectedOrgConfigView.md) |  | 


#### get_connected_org_config.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_connected_org_config.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_connected_org_config.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_connected_org_config.ApiResponseFor500
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

# **get_federation_settings**
<a name="get_federation_settings"></a>
> OrgFederationSettingsView get_federation_settings(org_id)

Return Federation Settings for One Organization

Returns information about the federation settings for the specified organization. To use this resource, the requesting API Key must have the Organization Owner role in the connected org. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import federated_authentication_api
from atlas.model.api_error import ApiError
from atlas.model.org_federation_settings_view import OrgFederationSettingsView
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = federated_authentication_api.FederatedAuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'orgId': "4888442a3354817a7320eb61",
    }
    query_params = {
    }
    try:
        # Return Federation Settings for One Organization
        api_response = api_instance.get_federation_settings(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->get_federation_settings: %s\n" % e)

    # example passing only optional values
    path_params = {
        'orgId': "4888442a3354817a7320eb61",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    try:
        # Return Federation Settings for One Organization
        api_response = api_instance.get_federation_settings(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->get_federation_settings: %s\n" % e)
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
orgId | OrgIdSchema | | 

# OrgIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_federation_settings.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_federation_settings.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_federation_settings.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_federation_settings.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_federation_settings.ApiResponseFor500) | Internal Server Error

#### get_federation_settings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**OrgFederationSettingsView**](../../models/OrgFederationSettingsView.md) |  | 


#### get_federation_settings.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_federation_settings.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_federation_settings.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_federation_settings.ApiResponseFor500
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

# **get_identity_provider**
<a name="get_identity_provider"></a>
> IdentityProviderView get_identity_provider(federation_settings_ididentity_provider_id)

Return one identity provider from the specified federation.

Returns one identity provider from the specified federation. To use this resource, the requesting API Key must have the Organization Owner role in one of the connected organizations. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import federated_authentication_api
from atlas.model.api_error import ApiError
from atlas.model.identity_provider_view import IdentityProviderView
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = federated_authentication_api.FederatedAuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'federationSettingsId': "55fa922fb343282757d9554e",
        'identityProviderId': "c2777a9eca931f29fc2f",
    }
    query_params = {
    }
    try:
        # Return one identity provider from the specified federation.
        api_response = api_instance.get_identity_provider(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->get_identity_provider: %s\n" % e)

    # example passing only optional values
    path_params = {
        'federationSettingsId': "55fa922fb343282757d9554e",
        'identityProviderId': "c2777a9eca931f29fc2f",
    }
    query_params = {
        'envelope': False,
    }
    try:
        # Return one identity provider from the specified federation.
        api_response = api_instance.get_identity_provider(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->get_identity_provider: %s\n" % e)
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
federationSettingsId | FederationSettingsIdSchema | | 
identityProviderId | IdentityProviderIdSchema | | 

# FederationSettingsIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdentityProviderIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_identity_provider.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_identity_provider.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_identity_provider.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_identity_provider.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_identity_provider.ApiResponseFor500) | Internal Server Error

#### get_identity_provider.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**IdentityProviderView**](../../models/IdentityProviderView.md) |  | 


#### get_identity_provider.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_identity_provider.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_identity_provider.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_identity_provider.ApiResponseFor500
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

# **get_identity_provider_metadata**
<a name="get_identity_provider_metadata"></a>
> str get_identity_provider_metadata(federation_settings_ididentity_provider_id)

Return the metadata of one identity provider in the specified federation.

Returns the metadata of one identity provider in the specified federation. To use this resource, the requesting API Key must have the Organization Owner role in one of the connected organizations. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import federated_authentication_api
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
    api_instance = federated_authentication_api.FederatedAuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'federationSettingsId': "55fa922fb343282757d9554e",
        'identityProviderId': "c2777a9eca931f29fc2f",
    }
    try:
        # Return the metadata of one identity provider in the specified federation.
        api_response = api_instance.get_identity_provider_metadata(
            path_params=path_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->get_identity_provider_metadata: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/vnd.atlas.2023-01-01+json', 'application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
federationSettingsId | FederationSettingsIdSchema | | 
identityProviderId | IdentityProviderIdSchema | | 

# FederationSettingsIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdentityProviderIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_identity_provider_metadata.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_identity_provider_metadata.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_identity_provider_metadata.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_identity_provider_metadata.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_identity_provider_metadata.ApiResponseFor500) | Internal Server Error

#### get_identity_provider_metadata.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

#### get_identity_provider_metadata.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_identity_provider_metadata.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_identity_provider_metadata.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_identity_provider_metadata.ApiResponseFor500
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

# **get_role_mapping**
<a name="get_role_mapping"></a>
> RoleMappingView get_role_mapping(federation_settings_ididorg_id)

Return One Role Mapping from One Organization

Returns one role mapping from the specified organization in the specified federation. To use this resource, the requesting API Key must have the Organization Owner role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import federated_authentication_api
from atlas.model.role_mapping_view import RoleMappingView
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
    api_instance = federated_authentication_api.FederatedAuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'federationSettingsId': "55fa922fb343282757d9554e",
        'id': "32b6e34b3d91647abb20e7b8",
        'orgId': "4888442a3354817a7320eb61",
    }
    query_params = {
    }
    try:
        # Return One Role Mapping from One Organization
        api_response = api_instance.get_role_mapping(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->get_role_mapping: %s\n" % e)

    # example passing only optional values
    path_params = {
        'federationSettingsId': "55fa922fb343282757d9554e",
        'id': "32b6e34b3d91647abb20e7b8",
        'orgId': "4888442a3354817a7320eb61",
    }
    query_params = {
        'envelope': False,
    }
    try:
        # Return One Role Mapping from One Organization
        api_response = api_instance.get_role_mapping(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->get_role_mapping: %s\n" % e)
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
federationSettingsId | FederationSettingsIdSchema | | 
id | IdSchema | | 
orgId | OrgIdSchema | | 

# FederationSettingsIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrgIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_role_mapping.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#get_role_mapping.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_role_mapping.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_role_mapping.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_role_mapping.ApiResponseFor500) | Internal Server Error

#### get_role_mapping.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**RoleMappingView**](../../models/RoleMappingView.md) |  | 


#### get_role_mapping.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_role_mapping.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_role_mapping.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_role_mapping.ApiResponseFor500
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

# **list_connected_org_configs**
<a name="list_connected_org_configs"></a>
> [ConnectedOrgConfigView] list_connected_org_configs(federation_settings_id)

Return All Connected Org Configs from the Federation

Returns all connected org configs in the specified federation. To use this resource, the requesting API Key must have the Organization Owner role in one of the connected orgs. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import federated_authentication_api
from atlas.model.api_error import ApiError
from atlas.model.connected_org_config_view import ConnectedOrgConfigView
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = federated_authentication_api.FederatedAuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'federationSettingsId': "55fa922fb343282757d9554e",
    }
    query_params = {
    }
    try:
        # Return All Connected Org Configs from the Federation
        api_response = api_instance.list_connected_org_configs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->list_connected_org_configs: %s\n" % e)

    # example passing only optional values
    path_params = {
        'federationSettingsId': "55fa922fb343282757d9554e",
    }
    query_params = {
        'envelope': False,
    }
    try:
        # Return All Connected Org Configs from the Federation
        api_response = api_instance.list_connected_org_configs(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->list_connected_org_configs: %s\n" % e)
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
federationSettingsId | FederationSettingsIdSchema | | 

# FederationSettingsIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_connected_org_configs.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#list_connected_org_configs.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#list_connected_org_configs.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#list_connected_org_configs.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#list_connected_org_configs.ApiResponseFor500) | Internal Server Error

#### list_connected_org_configs.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ConnectedOrgConfigView**]({{complexTypePrefix}}ConnectedOrgConfigView.md) | [**ConnectedOrgConfigView**]({{complexTypePrefix}}ConnectedOrgConfigView.md) | [**ConnectedOrgConfigView**]({{complexTypePrefix}}ConnectedOrgConfigView.md) |  | 

#### list_connected_org_configs.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### list_connected_org_configs.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### list_connected_org_configs.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### list_connected_org_configs.ApiResponseFor500
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

# **list_identity_providers**
<a name="list_identity_providers"></a>
> [IdentityProviderView] list_identity_providers(federation_settings_id)

Return all identity providers from the specified federation.

Returns all identity providers in the specified federation. To use this resource, the requesting API Key must have the Organization Owner role in one of the connected organizations. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import federated_authentication_api
from atlas.model.api_error import ApiError
from atlas.model.identity_provider_view import IdentityProviderView
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = federated_authentication_api.FederatedAuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'federationSettingsId': "55fa922fb343282757d9554e",
    }
    query_params = {
    }
    try:
        # Return all identity providers from the specified federation.
        api_response = api_instance.list_identity_providers(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->list_identity_providers: %s\n" % e)

    # example passing only optional values
    path_params = {
        'federationSettingsId': "55fa922fb343282757d9554e",
    }
    query_params = {
        'envelope': False,
    }
    try:
        # Return all identity providers from the specified federation.
        api_response = api_instance.list_identity_providers(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->list_identity_providers: %s\n" % e)
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
federationSettingsId | FederationSettingsIdSchema | | 

# FederationSettingsIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_identity_providers.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#list_identity_providers.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#list_identity_providers.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#list_identity_providers.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#list_identity_providers.ApiResponseFor500) | Internal Server Error

#### list_identity_providers.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IdentityProviderView**]({{complexTypePrefix}}IdentityProviderView.md) | [**IdentityProviderView**]({{complexTypePrefix}}IdentityProviderView.md) | [**IdentityProviderView**]({{complexTypePrefix}}IdentityProviderView.md) |  | 

#### list_identity_providers.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### list_identity_providers.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### list_identity_providers.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### list_identity_providers.ApiResponseFor500
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

# **list_role_mappings**
<a name="list_role_mappings"></a>
> [RoleMappingView] list_role_mappings(federation_settings_idorg_id)

Return All Role Mappings from One Organization

Returns all role mappings from the specified organization in the specified federation. To use this resource, the requesting API Key must have the Organization Owner role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import federated_authentication_api
from atlas.model.role_mapping_view import RoleMappingView
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
    api_instance = federated_authentication_api.FederatedAuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'federationSettingsId': "55fa922fb343282757d9554e",
        'orgId': "4888442a3354817a7320eb61",
    }
    query_params = {
    }
    try:
        # Return All Role Mappings from One Organization
        api_response = api_instance.list_role_mappings(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->list_role_mappings: %s\n" % e)

    # example passing only optional values
    path_params = {
        'federationSettingsId': "55fa922fb343282757d9554e",
        'orgId': "4888442a3354817a7320eb61",
    }
    query_params = {
        'envelope': False,
    }
    try:
        # Return All Role Mappings from One Organization
        api_response = api_instance.list_role_mappings(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->list_role_mappings: %s\n" % e)
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
federationSettingsId | FederationSettingsIdSchema | | 
orgId | OrgIdSchema | | 

# FederationSettingsIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrgIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_role_mappings.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#list_role_mappings.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#list_role_mappings.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#list_role_mappings.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#list_role_mappings.ApiResponseFor500) | Internal Server Error

#### list_role_mappings.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RoleMappingView**]({{complexTypePrefix}}RoleMappingView.md) | [**RoleMappingView**]({{complexTypePrefix}}RoleMappingView.md) | [**RoleMappingView**]({{complexTypePrefix}}RoleMappingView.md) |  | 

#### list_role_mappings.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### list_role_mappings.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### list_role_mappings.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### list_role_mappings.ApiResponseFor500
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

# **remove_connected_org_config**
<a name="remove_connected_org_config"></a>
> remove_connected_org_config(federation_settings_idorg_id)

Remove One Org Config Connected to One Federation

Removes one connected organization configuration from the specified federation. To use this resource, the requesting API Key must have the Organization Owner role. This resource doesn't require the API Key to have an Access List. Note: This request fails if only one connected organization exists in the federation.

### Example

```python
import atlas
from atlas.apis.tags import federated_authentication_api
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
    api_instance = federated_authentication_api.FederatedAuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'federationSettingsId': "55fa922fb343282757d9554e",
        'orgId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    try:
        # Remove One Org Config Connected to One Federation
        api_response = api_instance.remove_connected_org_config(
            path_params=path_params,
            query_params=query_params,
        )
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->remove_connected_org_config: %s\n" % e)

    # example passing only optional values
    path_params = {
        'federationSettingsId': "55fa922fb343282757d9554e",
        'orgId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'envelope': False,
    }
    try:
        # Remove One Org Config Connected to One Federation
        api_response = api_instance.remove_connected_org_config(
            path_params=path_params,
            query_params=query_params,
        )
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->remove_connected_org_config: %s\n" % e)
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
federationSettingsId | FederationSettingsIdSchema | | 
orgId | OrgIdSchema | | 

# FederationSettingsIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrgIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#remove_connected_org_config.ApiResponseFor204) | This endpoint does not return a response body.
400 | [ApiResponseFor400](#remove_connected_org_config.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#remove_connected_org_config.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#remove_connected_org_config.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#remove_connected_org_config.ApiResponseFor500) | Internal Server Error

#### remove_connected_org_config.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### remove_connected_org_config.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### remove_connected_org_config.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### remove_connected_org_config.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### remove_connected_org_config.ApiResponseFor500
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

# **update_connected_org_config**
<a name="update_connected_org_config"></a>
> ConnectedOrgConfigView update_connected_org_config(federation_settings_idorg_idconnected_org_config_view)

Update One Org Config Connected to One Federation

Updates one connected organization configuration from the specified federation. To use this resource, the requesting API Key must have the Organization Owner role. This resource doesn't require the API Key to have an Access List.   **Note** If the organization configuration has no associated identity provider, you can't use this resource to update role mappings or post authorization role grants.    **Note**: The domainRestrictionEnabled field defaults to false if not provided in the request.   **Note**: If the identityProviderId field is not provided, you will disconnect the organization and the identity provider.

### Example

```python
import atlas
from atlas.apis.tags import federated_authentication_api
from atlas.model.api_error import ApiError
from atlas.model.connected_org_config_view import ConnectedOrgConfigView
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = federated_authentication_api.FederatedAuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'federationSettingsId': "55fa922fb343282757d9554e",
        'orgId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    body = ConnectedOrgConfigView(
        domain_allow_list=[
            "domain_allow_list_example"
        ],
        domain_restriction_enabled=True,
        identity_provider_id="bf325375e030fccba009",
        org_id="32b6e34b3d91647abb20e7b8",
        post_auth_role_grants=[
            "GLOBAL_AUTOMATION_ADMIN"
        ],
        role_mappings=[
            RoleMappingView(
                external_group_name="external_group_name_example",
                id="32b6e34b3d91647abb20e7b8",
                role_assignments=[
                    RoleAssignment(
                        group_id="32b6e34b3d91647abb20e7b8",
                        org_id="32b6e34b3d91647abb20e7b8",
                        role="ORG_OWNER",
                    )
                ],
            )
        ],
        user_conflicts=[
            FederatedUserView(
                email_address="email_address_example",
                federation_settings_id="32b6e34b3d91647abb20e7b8",
                first_name="first_name_example",
                last_name="last_name_example",
                user_id="bf325375e030fccba0091731",
            )
        ],
    )
    try:
        # Update One Org Config Connected to One Federation
        api_response = api_instance.update_connected_org_config(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->update_connected_org_config: %s\n" % e)

    # example passing only optional values
    path_params = {
        'federationSettingsId': "55fa922fb343282757d9554e",
        'orgId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'envelope': False,
    }
    body = ConnectedOrgConfigView(
        domain_allow_list=[
            "domain_allow_list_example"
        ],
        domain_restriction_enabled=True,
        identity_provider_id="bf325375e030fccba009",
        org_id="32b6e34b3d91647abb20e7b8",
        post_auth_role_grants=[
            "GLOBAL_AUTOMATION_ADMIN"
        ],
        role_mappings=[
            RoleMappingView(
                external_group_name="external_group_name_example",
                id="32b6e34b3d91647abb20e7b8",
                role_assignments=[
                    RoleAssignment(
                        group_id="32b6e34b3d91647abb20e7b8",
                        org_id="32b6e34b3d91647abb20e7b8",
                        role="ORG_OWNER",
                    )
                ],
            )
        ],
        user_conflicts=[
            FederatedUserView(
                email_address="email_address_example",
                federation_settings_id="32b6e34b3d91647abb20e7b8",
                first_name="first_name_example",
                last_name="last_name_example",
                user_id="bf325375e030fccba0091731",
            )
        ],
    )
    try:
        # Update One Org Config Connected to One Federation
        api_response = api_instance.update_connected_org_config(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->update_connected_org_config: %s\n" % e)
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
[**ConnectedOrgConfigView**](../../models/ConnectedOrgConfigView.md) |  | 


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
federationSettingsId | FederationSettingsIdSchema | | 
orgId | OrgIdSchema | | 

# FederationSettingsIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrgIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_connected_org_config.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#update_connected_org_config.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#update_connected_org_config.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#update_connected_org_config.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#update_connected_org_config.ApiResponseFor500) | Internal Server Error

#### update_connected_org_config.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**ConnectedOrgConfigView**](../../models/ConnectedOrgConfigView.md) |  | 


#### update_connected_org_config.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### update_connected_org_config.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### update_connected_org_config.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### update_connected_org_config.ApiResponseFor500
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

# **update_identity_provider**
<a name="update_identity_provider"></a>
> IdentityProviderView update_identity_provider(federation_settings_ididentity_provider_ididentity_provider_update)

Update the identity provider.

Updates one identity provider in the specified federation. To use this resource, the requesting API Key must have the Organization Owner role in one of the connected organizations. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import federated_authentication_api
from atlas.model.api_error import ApiError
from atlas.model.identity_provider_view import IdentityProviderView
from atlas.model.identity_provider_update import IdentityProviderUpdate
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = federated_authentication_api.FederatedAuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'federationSettingsId': "55fa922fb343282757d9554e",
        'identityProviderId': "c2777a9eca931f29fc2f",
    }
    query_params = {
    }
    body = IdentityProviderUpdate(
        associated_domains=[
            "associated_domains_example"
        ],
        display_name="display_name_example",
        issuer_uri="urn:idp:default",
        pem_file_info=PemFileInfo(
            certificates=[
                X509Certificate(
                    content="content_example",
                    not_after="1970-01-01T00:00:00.00Z",
                    not_before="1970-01-01T00:00:00.00Z",
                )
            ],
            file_name="file_name_example",
        ),
        request_binding="HTTP-POST",
        response_signature_algorithm="SHA-1",
        sso_debug_enabled=True,
        sso_url="https://example.com",
        status="ACTIVE",
    )
    try:
        # Update the identity provider.
        api_response = api_instance.update_identity_provider(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->update_identity_provider: %s\n" % e)

    # example passing only optional values
    path_params = {
        'federationSettingsId': "55fa922fb343282757d9554e",
        'identityProviderId': "c2777a9eca931f29fc2f",
    }
    query_params = {
        'envelope': False,
    }
    body = IdentityProviderUpdate(
        associated_domains=[
            "associated_domains_example"
        ],
        display_name="display_name_example",
        issuer_uri="urn:idp:default",
        pem_file_info=PemFileInfo(
            certificates=[
                X509Certificate(
                    content="content_example",
                    not_after="1970-01-01T00:00:00.00Z",
                    not_before="1970-01-01T00:00:00.00Z",
                )
            ],
            file_name="file_name_example",
        ),
        request_binding="HTTP-POST",
        response_signature_algorithm="SHA-1",
        sso_debug_enabled=True,
        sso_url="https://example.com",
        status="ACTIVE",
    )
    try:
        # Update the identity provider.
        api_response = api_instance.update_identity_provider(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->update_identity_provider: %s\n" % e)
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
[**IdentityProviderUpdate**](../../models/IdentityProviderUpdate.md) |  | 


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
federationSettingsId | FederationSettingsIdSchema | | 
identityProviderId | IdentityProviderIdSchema | | 

# FederationSettingsIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdentityProviderIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_identity_provider.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#update_identity_provider.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#update_identity_provider.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_identity_provider.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#update_identity_provider.ApiResponseFor500) | Internal Server Error

#### update_identity_provider.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**IdentityProviderView**](../../models/IdentityProviderView.md) |  | 


#### update_identity_provider.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### update_identity_provider.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### update_identity_provider.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### update_identity_provider.ApiResponseFor500
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

# **update_role_mapping**
<a name="update_role_mapping"></a>
> RoleMappingView update_role_mapping(federation_settings_ididorg_idrole_mapping_view)

Update One Role Mapping in One Organization

Updates one role mapping in the specified organization in the specified federation. To use this resource, the requesting API Key must have the Organization Owner role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import federated_authentication_api
from atlas.model.role_mapping_view import RoleMappingView
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
    api_instance = federated_authentication_api.FederatedAuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'federationSettingsId': "55fa922fb343282757d9554e",
        'id': "32b6e34b3d91647abb20e7b8",
        'orgId': "4888442a3354817a7320eb61",
    }
    query_params = {
    }
    body = RoleMappingView(
        external_group_name="external_group_name_example",
        id="32b6e34b3d91647abb20e7b8",
        role_assignments=[
            RoleAssignment(
                group_id="32b6e34b3d91647abb20e7b8",
                org_id="32b6e34b3d91647abb20e7b8",
                role="ORG_OWNER",
            )
        ],
    )
    try:
        # Update One Role Mapping in One Organization
        api_response = api_instance.update_role_mapping(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->update_role_mapping: %s\n" % e)

    # example passing only optional values
    path_params = {
        'federationSettingsId': "55fa922fb343282757d9554e",
        'id': "32b6e34b3d91647abb20e7b8",
        'orgId': "4888442a3354817a7320eb61",
    }
    query_params = {
        'envelope': False,
    }
    body = RoleMappingView(
        external_group_name="external_group_name_example",
        id="32b6e34b3d91647abb20e7b8",
        role_assignments=[
            RoleAssignment(
                group_id="32b6e34b3d91647abb20e7b8",
                org_id="32b6e34b3d91647abb20e7b8",
                role="ORG_OWNER",
            )
        ],
    )
    try:
        # Update One Role Mapping in One Organization
        api_response = api_instance.update_role_mapping(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling FederatedAuthenticationApi->update_role_mapping: %s\n" % e)
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
[**RoleMappingView**](../../models/RoleMappingView.md) |  | 


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
federationSettingsId | FederationSettingsIdSchema | | 
id | IdSchema | | 
orgId | OrgIdSchema | | 

# FederationSettingsIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# IdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# OrgIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_role_mapping.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#update_role_mapping.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#update_role_mapping.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#update_role_mapping.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#update_role_mapping.ApiResponseFor500) | Internal Server Error

#### update_role_mapping.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**RoleMappingView**](../../models/RoleMappingView.md) |  | 


#### update_role_mapping.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### update_role_mapping.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### update_role_mapping.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### update_role_mapping.ApiResponseFor500
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

