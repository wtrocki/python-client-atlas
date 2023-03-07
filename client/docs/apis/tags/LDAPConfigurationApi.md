<a name="__pageTop"></a>
# atlas.apis.tags.ldap_configuration_api.LDAPConfigurationApi

All URIs are relative to *https://cloud.mongodb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_ldap_configuration**](#delete_ldap_configuration) | **delete** /api/atlas/v2/groups/{groupId}/userSecurity/ldap/userToDNMapping | Remove the Current LDAP User to DN Mapping
[**get_ldap_configuration**](#get_ldap_configuration) | **get** /api/atlas/v2/groups/{groupId}/userSecurity | Return the Current LDAP or X.509 Configuration
[**get_ldap_configuration_status**](#get_ldap_configuration_status) | **get** /api/atlas/v2/groups/{groupId}/userSecurity/ldap/verify/{requestId} | Return the Status of One Verify LDAP Configuration Request
[**save_ldap_configuration**](#save_ldap_configuration) | **patch** /api/atlas/v2/groups/{groupId}/userSecurity | Edit the LDAP or X.509 Configuration
[**verify_ldap_configuration**](#verify_ldap_configuration) | **post** /api/atlas/v2/groups/{groupId}/userSecurity/ldap/verify | Verify the LDAP Configuration in One Project

# **delete_ldap_configuration**
<a name="delete_ldap_configuration"></a>
> delete_ldap_configuration(group_id)

Remove the Current LDAP User to DN Mapping

Removes the current LDAP Distinguished Name mapping captured in the ``userToDNMapping`` document from the LDAP configuration for the specified project. To use this resource, the requesting API Key must have the Project Atlas Admin role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import ldap_configuration_api
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
    api_instance = ldap_configuration_api.LDAPConfigurationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    try:
        # Remove the Current LDAP User to DN Mapping
        api_response = api_instance.delete_ldap_configuration(
            path_params=path_params,
            query_params=query_params,
        )
    except atlas.ApiException as e:
        print("Exception when calling LDAPConfigurationApi->delete_ldap_configuration: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    try:
        # Remove the Current LDAP User to DN Mapping
        api_response = api_instance.delete_ldap_configuration(
            path_params=path_params,
            query_params=query_params,
        )
    except atlas.ApiException as e:
        print("Exception when calling LDAPConfigurationApi->delete_ldap_configuration: %s\n" % e)
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
204 | [ApiResponseFor204](#delete_ldap_configuration.ApiResponseFor204) | This endpoint does not return a response body.
404 | [ApiResponseFor404](#delete_ldap_configuration.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#delete_ldap_configuration.ApiResponseFor500) | Internal Server Error

#### delete_ldap_configuration.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### delete_ldap_configuration.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### delete_ldap_configuration.ApiResponseFor500
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

# **get_ldap_configuration**
<a name="get_ldap_configuration"></a>
> UserSecurity get_ldap_configuration(group_id)

Return the Current LDAP or X.509 Configuration

Returns the current LDAP configuration for the specified project. To use this resource, the requesting API Key must have the Project Owner role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import ldap_configuration_api
from atlas.model.user_security import UserSecurity
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
    api_instance = ldap_configuration_api.LDAPConfigurationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    try:
        # Return the Current LDAP or X.509 Configuration
        api_response = api_instance.get_ldap_configuration(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling LDAPConfigurationApi->get_ldap_configuration: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    try:
        # Return the Current LDAP or X.509 Configuration
        api_response = api_instance.get_ldap_configuration(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling LDAPConfigurationApi->get_ldap_configuration: %s\n" % e)
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
200 | [ApiResponseFor200](#get_ldap_configuration.ApiResponseFor200) | OK
404 | [ApiResponseFor404](#get_ldap_configuration.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_ldap_configuration.ApiResponseFor500) | Internal Server Error

#### get_ldap_configuration.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**UserSecurity**](../../models/UserSecurity.md) |  | 


#### get_ldap_configuration.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_ldap_configuration.ApiResponseFor500
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

# **get_ldap_configuration_status**
<a name="get_ldap_configuration_status"></a>
> NDSLDAPVerifyConnectivityJobRequest get_ldap_configuration_status(group_idrequest_id)

Return the Status of One Verify LDAP Configuration Request

Returns the status of one request to verify one LDAP configuration for the specified project. To use this resource, the requesting API Key must have the Project Atlas Admin role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import ldap_configuration_api
from atlas.model.ndsldap_verify_connectivity_job_request import NDSLDAPVerifyConnectivityJobRequest
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
    api_instance = ldap_configuration_api.LDAPConfigurationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'requestId': "bf325375e030fccba0091731",
    }
    query_params = {
    }
    try:
        # Return the Status of One Verify LDAP Configuration Request
        api_response = api_instance.get_ldap_configuration_status(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling LDAPConfigurationApi->get_ldap_configuration_status: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'requestId': "bf325375e030fccba0091731",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    try:
        # Return the Status of One Verify LDAP Configuration Request
        api_response = api_instance.get_ldap_configuration_status(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling LDAPConfigurationApi->get_ldap_configuration_status: %s\n" % e)
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
requestId | RequestIdSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RequestIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_ldap_configuration_status.ApiResponseFor200) | OK
404 | [ApiResponseFor404](#get_ldap_configuration_status.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_ldap_configuration_status.ApiResponseFor500) | Internal Server Error

#### get_ldap_configuration_status.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**NDSLDAPVerifyConnectivityJobRequest**](../../models/NDSLDAPVerifyConnectivityJobRequest.md) |  | 


#### get_ldap_configuration_status.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_ldap_configuration_status.ApiResponseFor500
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

# **save_ldap_configuration**
<a name="save_ldap_configuration"></a>
> UserSecurity save_ldap_configuration(group_iduser_security)

Edit the LDAP or X.509 Configuration

Edits the LDAP configuration for the specified project. To use this resource, the requesting API Key must have the Project Owner role. This resource doesn't require the API Key to have an Access List.  Updating this configuration triggers a rolling restart of the database.

### Example

```python
import atlas
from atlas.apis.tags import ldap_configuration_api
from atlas.model.user_security import UserSecurity
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
    api_instance = ldap_configuration_api.LDAPConfigurationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    body = UserSecurity(
        customer_x509=CustomerX509(
            cas="cas_example",
            links=[
                Link(
                    href="https://cloud.mongodb.com/api/atlas",
                    rel="self",
                )
            ],
        ),
        ldap=NDSLDAP(
            authentication_enabled=True,
            authorization_enabled=True,
            authz_query_template="{USER}?memberOf?base",
            bind_password="bind_password_example",
            bind_username="CN=BindUser,CN=Users,DC=myldapserver,DC=mycompany,DC=com",
            ca_certificate="ca_certificate_example",
            hostname="zgckec0l3o4gi7xhk0jcy075ua034pgmug8iq37llr1plnjktgos9hdvpwi4jdixdxxml6j.j4swhsa064e9ybn07an7dc0zj1z3o53ghg9.6qsiyk0h9c8fvw06p7a54pxfjl9qsi30bx456v41d30994wetshbws0p64c4bfiki6y.4mr9nwr1as4j3pfv8kcss4s7m7nnl4lz25sh3v1r9goy8pxfv2ryzgt6aeydd7zuvbrt5wycaueook.ju6otpoj5ifautvjjct5108mvhj5wimaijj5ar4ihaucunk5lbvuwh2p5benpr8sw.qa9woex6dzpdz.prol4oxf1vlovr8vywu4jqkr6ra0y0uv60djw9.0jt9hauo5bs93ajxhzwa2z47zs3p378bgcyme5828j7l.igyo1l0q6ct94n9yu4ivrxn214gibpahdtf93e57lhwd589nqiyhhil1f8etzy5.szasferyixqnrpbfvwlblzdbnyyeuf",
,
            port=636,
            user_to_dn_mapping=[
                NDSUserToDNMapping(
                    ldap_query="ldap_query_example",
                    match="(.*)",
                    substitution="CN={0},CN=Users,DC=my-atlas-ldap-server,DC=example,DC=com",
                )
            ],
        ),
,
    )
    try:
        # Edit the LDAP or X.509 Configuration
        api_response = api_instance.save_ldap_configuration(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling LDAPConfigurationApi->save_ldap_configuration: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    body = UserSecurity(
        customer_x509=CustomerX509(
            cas="cas_example",
            links=[
                Link(
                    href="https://cloud.mongodb.com/api/atlas",
                    rel="self",
                )
            ],
        ),
        ldap=NDSLDAP(
            authentication_enabled=True,
            authorization_enabled=True,
            authz_query_template="{USER}?memberOf?base",
            bind_password="bind_password_example",
            bind_username="CN=BindUser,CN=Users,DC=myldapserver,DC=mycompany,DC=com",
            ca_certificate="ca_certificate_example",
            hostname="zgckec0l3o4gi7xhk0jcy075ua034pgmug8iq37llr1plnjktgos9hdvpwi4jdixdxxml6j.j4swhsa064e9ybn07an7dc0zj1z3o53ghg9.6qsiyk0h9c8fvw06p7a54pxfjl9qsi30bx456v41d30994wetshbws0p64c4bfiki6y.4mr9nwr1as4j3pfv8kcss4s7m7nnl4lz25sh3v1r9goy8pxfv2ryzgt6aeydd7zuvbrt5wycaueook.ju6otpoj5ifautvjjct5108mvhj5wimaijj5ar4ihaucunk5lbvuwh2p5benpr8sw.qa9woex6dzpdz.prol4oxf1vlovr8vywu4jqkr6ra0y0uv60djw9.0jt9hauo5bs93ajxhzwa2z47zs3p378bgcyme5828j7l.igyo1l0q6ct94n9yu4ivrxn214gibpahdtf93e57lhwd589nqiyhhil1f8etzy5.szasferyixqnrpbfvwlblzdbnyyeuf",
,
            port=636,
            user_to_dn_mapping=[
                NDSUserToDNMapping(
                    ldap_query="ldap_query_example",
                    match="(.*)",
                    substitution="CN={0},CN=Users,DC=my-atlas-ldap-server,DC=example,DC=com",
                )
            ],
        ),
,
    )
    try:
        # Edit the LDAP or X.509 Configuration
        api_response = api_instance.save_ldap_configuration(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling LDAPConfigurationApi->save_ldap_configuration: %s\n" % e)
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
[**UserSecurity**](../../models/UserSecurity.md) |  | 


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
200 | [ApiResponseFor200](#save_ldap_configuration.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#save_ldap_configuration.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#save_ldap_configuration.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#save_ldap_configuration.ApiResponseFor500) | Internal Server Error

#### save_ldap_configuration.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**UserSecurity**](../../models/UserSecurity.md) |  | 


#### save_ldap_configuration.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### save_ldap_configuration.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### save_ldap_configuration.ApiResponseFor500
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

# **verify_ldap_configuration**
<a name="verify_ldap_configuration"></a>
> NDSLDAPVerifyConnectivityJobRequest verify_ldap_configuration(group_idndsldap_verify_connectivity_job_request_params)

Verify the LDAP Configuration in One Project

Verifies the LDAP configuration for the specified project. To use this resource, the requesting API Key must have the Project Owner role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import ldap_configuration_api
from atlas.model.ndsldap_verify_connectivity_job_request import NDSLDAPVerifyConnectivityJobRequest
from atlas.model.api_error import ApiError
from atlas.model.ndsldap_verify_connectivity_job_request_params import NDSLDAPVerifyConnectivityJobRequestParams
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ldap_configuration_api.LDAPConfigurationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    body = NDSLDAPVerifyConnectivityJobRequestParams(
        authz_query_template="{USER}?memberOf?base",
        bind_password="bind_password_example",
        bind_username="CN=BindUser,CN=Users,DC=myldapserver,DC=mycompany,DC=com",
        ca_certificate="ca_certificate_example",
        hostname="zgckec0l3o4gi7xhk0jcy075ua034pgmug8iq37llr1plnjktgos9hdvpwi4jdixdxxml6j.j4swhsa064e9ybn07an7dc0zj1z3o53ghg9.6qsiyk0h9c8fvw06p7a54pxfjl9qsi30bx456v41d30994wetshbws0p64c4bfiki6y.4mr9nwr1as4j3pfv8kcss4s7m7nnl4lz25sh3v1r9goy8pxfv2ryzgt6aeydd7zuvbrt5wycaueook.ju6otpoj5ifautvjjct5108mvhj5wimaijj5ar4ihaucunk5lbvuwh2p5benpr8sw.qa9woex6dzpdz.prol4oxf1vlovr8vywu4jqkr6ra0y0uv60djw9.0jt9hauo5bs93ajxhzwa2z47zs3p378bgcyme5828j7l.igyo1l0q6ct94n9yu4ivrxn214gibpahdtf93e57lhwd589nqiyhhil1f8etzy5.szasferyixqnrpbfvwlblzdbnyyeuf",
        links=[
            Link(
                href="https://cloud.mongodb.com/api/atlas",
                rel="self",
            )
        ],
        port=636,
    )
    try:
        # Verify the LDAP Configuration in One Project
        api_response = api_instance.verify_ldap_configuration(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling LDAPConfigurationApi->verify_ldap_configuration: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    body = NDSLDAPVerifyConnectivityJobRequestParams(
        authz_query_template="{USER}?memberOf?base",
        bind_password="bind_password_example",
        bind_username="CN=BindUser,CN=Users,DC=myldapserver,DC=mycompany,DC=com",
        ca_certificate="ca_certificate_example",
        hostname="zgckec0l3o4gi7xhk0jcy075ua034pgmug8iq37llr1plnjktgos9hdvpwi4jdixdxxml6j.j4swhsa064e9ybn07an7dc0zj1z3o53ghg9.6qsiyk0h9c8fvw06p7a54pxfjl9qsi30bx456v41d30994wetshbws0p64c4bfiki6y.4mr9nwr1as4j3pfv8kcss4s7m7nnl4lz25sh3v1r9goy8pxfv2ryzgt6aeydd7zuvbrt5wycaueook.ju6otpoj5ifautvjjct5108mvhj5wimaijj5ar4ihaucunk5lbvuwh2p5benpr8sw.qa9woex6dzpdz.prol4oxf1vlovr8vywu4jqkr6ra0y0uv60djw9.0jt9hauo5bs93ajxhzwa2z47zs3p378bgcyme5828j7l.igyo1l0q6ct94n9yu4ivrxn214gibpahdtf93e57lhwd589nqiyhhil1f8etzy5.szasferyixqnrpbfvwlblzdbnyyeuf",
        links=[
            Link(
                href="https://cloud.mongodb.com/api/atlas",
                rel="self",
            )
        ],
        port=636,
    )
    try:
        # Verify the LDAP Configuration in One Project
        api_response = api_instance.verify_ldap_configuration(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling LDAPConfigurationApi->verify_ldap_configuration: %s\n" % e)
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
[**NDSLDAPVerifyConnectivityJobRequestParams**](../../models/NDSLDAPVerifyConnectivityJobRequestParams.md) |  | 


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
200 | [ApiResponseFor200](#verify_ldap_configuration.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#verify_ldap_configuration.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#verify_ldap_configuration.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#verify_ldap_configuration.ApiResponseFor500) | Internal Server Error

#### verify_ldap_configuration.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**NDSLDAPVerifyConnectivityJobRequest**](../../models/NDSLDAPVerifyConnectivityJobRequest.md) |  | 


#### verify_ldap_configuration.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### verify_ldap_configuration.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### verify_ldap_configuration.ApiResponseFor500
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

