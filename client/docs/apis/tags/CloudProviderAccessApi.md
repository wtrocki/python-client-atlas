<a name="__pageTop"></a>
# atlas.apis.tags.cloud_provider_access_api.CloudProviderAccessApi

All URIs are relative to *https://cloud.mongodb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_cloud_provider_access_role**](#authorize_cloud_provider_access_role) | **patch** /api/atlas/v2/groups/{groupId}/cloudProviderAccess/{roleId} | Authorize One Cloud Provider Access Role
[**create_cloud_provider_access_role**](#create_cloud_provider_access_role) | **post** /api/atlas/v2/groups/{groupId}/cloudProviderAccess | Create One Cloud Provider Access Role
[**deauthorize_cloud_provider_access_role**](#deauthorize_cloud_provider_access_role) | **delete** /api/atlas/v2/groups/{groupId}/cloudProviderAccess/{cloudProvider}/{roleId} | Deauthorize One Cloud Provider Access Role
[**get_cloud_provider_access_role**](#get_cloud_provider_access_role) | **get** /api/atlas/v2/groups/{groupId}/cloudProviderAccess/{roleId} | Return specified Cloud Provider Access Role
[**list_cloud_provider_access_roles**](#list_cloud_provider_access_roles) | **get** /api/atlas/v2/groups/{groupId}/cloudProviderAccess | Return All Cloud Provider Access Roles

# **authorize_cloud_provider_access_role**
<a name="authorize_cloud_provider_access_role"></a>
> CloudProviderAccessRole authorize_cloud_provider_access_role(group_idrole_idcloud_provider_access_role)

Authorize One Cloud Provider Access Role

Grants access to the specified project for the specified Amazon Web Services (AWS) Identity and Access Management (IAM) role. To use this resource, the requesting API Key must have the Project Owner role. This resource doesn't require the API Key to have an Access List. This API endpoint is one step in a procedure to create unified AWS access for MongoDB Cloud services.

### Example

```python
import atlas
from atlas.apis.tags import cloud_provider_access_api
from atlas.model.cloud_provider_access_role import CloudProviderAccessRole
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
    api_instance = cloud_provider_access_api.CloudProviderAccessApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'roleId': "bf325375e030fccba0091731",
    }
    query_params = {
    }
    body = CloudProviderAccessRole(
        atlas_aws_account_arn="arn:aws:iam::772401394250:role/my-test-aws-role",
        atlas_assumed_role_external_id="atlas_assumed_role_external_id_example",
        authorized_date="1970-01-01T00:00:00.00Z",
        created_date="1970-01-01T00:00:00.00Z",
        feature_usages=[
            CloudProviderAccessFeatureUsage(
                feature_id=CloudProviderAccessFeatureUsageDataLakeFeatureId(
                    group_id="32b6e34b3d91647abb20e7b8",
                    name="name_example",
                ),
                feature_type="ATLAS_DATA_LAKE",
            )
        ],
        iam_assumed_role_arn="arn:aws:iam::123456789012:root",
        role_id="32b6e34b3d91647abb20e7b8",
        provider_name="AWS",
    )
    try:
        # Authorize One Cloud Provider Access Role
        api_response = api_instance.authorize_cloud_provider_access_role(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling CloudProviderAccessApi->authorize_cloud_provider_access_role: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'roleId': "bf325375e030fccba0091731",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    body = CloudProviderAccessRole(
        atlas_aws_account_arn="arn:aws:iam::772401394250:role/my-test-aws-role",
        atlas_assumed_role_external_id="atlas_assumed_role_external_id_example",
        authorized_date="1970-01-01T00:00:00.00Z",
        created_date="1970-01-01T00:00:00.00Z",
        feature_usages=[
            CloudProviderAccessFeatureUsage(
                feature_id=CloudProviderAccessFeatureUsageDataLakeFeatureId(
                    group_id="32b6e34b3d91647abb20e7b8",
                    name="name_example",
                ),
                feature_type="ATLAS_DATA_LAKE",
            )
        ],
        iam_assumed_role_arn="arn:aws:iam::123456789012:root",
        role_id="32b6e34b3d91647abb20e7b8",
        provider_name="AWS",
    )
    try:
        # Authorize One Cloud Provider Access Role
        api_response = api_instance.authorize_cloud_provider_access_role(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling CloudProviderAccessApi->authorize_cloud_provider_access_role: %s\n" % e)
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
[**CloudProviderAccessRole**](../../models/CloudProviderAccessRole.md) |  | 


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
roleId | RoleIdSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RoleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#authorize_cloud_provider_access_role.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#authorize_cloud_provider_access_role.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#authorize_cloud_provider_access_role.ApiResponseFor404) | Not Found
409 | [ApiResponseFor409](#authorize_cloud_provider_access_role.ApiResponseFor409) | Conflict
500 | [ApiResponseFor500](#authorize_cloud_provider_access_role.ApiResponseFor500) | Internal Server Error

#### authorize_cloud_provider_access_role.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**CloudProviderAccessRole**](../../models/CloudProviderAccessRole.md) |  | 


#### authorize_cloud_provider_access_role.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### authorize_cloud_provider_access_role.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### authorize_cloud_provider_access_role.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### authorize_cloud_provider_access_role.ApiResponseFor500
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

# **create_cloud_provider_access_role**
<a name="create_cloud_provider_access_role"></a>
> CloudProviderAccessRole create_cloud_provider_access_role(group_idcloud_provider_access_role)

Create One Cloud Provider Access Role

Creates one Amazon Web Services (AWS) Identity and Access Management (IAM) role. Some MongoDB Cloud features use AWS IAM roles for authentication. To use this resource, the requesting API Key must have the Project Owner role. This resource doesn't require the API Key to have an Access List.  After a successful request to this API endpoint, you can add the **atlasAWSAccountArn** and **atlasAssumedRoleExternalId** values to the trust policy in your AWS console to create an IAM Assumed Amazon Resource Name (ARN).

### Example

```python
import atlas
from atlas.apis.tags import cloud_provider_access_api
from atlas.model.cloud_provider_access_role import CloudProviderAccessRole
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
    api_instance = cloud_provider_access_api.CloudProviderAccessApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    body = CloudProviderAccessRole(
        atlas_aws_account_arn="arn:aws:iam::772401394250:role/my-test-aws-role",
        atlas_assumed_role_external_id="atlas_assumed_role_external_id_example",
        authorized_date="1970-01-01T00:00:00.00Z",
        created_date="1970-01-01T00:00:00.00Z",
        feature_usages=[
            CloudProviderAccessFeatureUsage(
                feature_id=CloudProviderAccessFeatureUsageDataLakeFeatureId(
                    group_id="32b6e34b3d91647abb20e7b8",
                    name="name_example",
                ),
                feature_type="ATLAS_DATA_LAKE",
            )
        ],
        iam_assumed_role_arn="arn:aws:iam::123456789012:root",
        role_id="32b6e34b3d91647abb20e7b8",
        provider_name="AWS",
    )
    try:
        # Create One Cloud Provider Access Role
        api_response = api_instance.create_cloud_provider_access_role(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling CloudProviderAccessApi->create_cloud_provider_access_role: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    body = CloudProviderAccessRole(
        atlas_aws_account_arn="arn:aws:iam::772401394250:role/my-test-aws-role",
        atlas_assumed_role_external_id="atlas_assumed_role_external_id_example",
        authorized_date="1970-01-01T00:00:00.00Z",
        created_date="1970-01-01T00:00:00.00Z",
        feature_usages=[
            CloudProviderAccessFeatureUsage(
                feature_id=CloudProviderAccessFeatureUsageDataLakeFeatureId(
                    group_id="32b6e34b3d91647abb20e7b8",
                    name="name_example",
                ),
                feature_type="ATLAS_DATA_LAKE",
            )
        ],
        iam_assumed_role_arn="arn:aws:iam::123456789012:root",
        role_id="32b6e34b3d91647abb20e7b8",
        provider_name="AWS",
    )
    try:
        # Create One Cloud Provider Access Role
        api_response = api_instance.create_cloud_provider_access_role(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling CloudProviderAccessApi->create_cloud_provider_access_role: %s\n" % e)
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
[**CloudProviderAccessRole**](../../models/CloudProviderAccessRole.md) |  | 


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
200 | [ApiResponseFor200](#create_cloud_provider_access_role.ApiResponseFor200) | OK
404 | [ApiResponseFor404](#create_cloud_provider_access_role.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#create_cloud_provider_access_role.ApiResponseFor500) | Internal Server Error

#### create_cloud_provider_access_role.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**CloudProviderAccessRole**](../../models/CloudProviderAccessRole.md) |  | 


#### create_cloud_provider_access_role.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### create_cloud_provider_access_role.ApiResponseFor500
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

# **deauthorize_cloud_provider_access_role**
<a name="deauthorize_cloud_provider_access_role"></a>
> deauthorize_cloud_provider_access_role(group_idcloud_providerrole_id)

Deauthorize One Cloud Provider Access Role

Revokes access to the specified project for the specified AWS IAM role. To use this resource,the requesting API Key must have the Project Owner role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import cloud_provider_access_api
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
    api_instance = cloud_provider_access_api.CloudProviderAccessApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'cloudProvider': "AWS",
        'roleId': "bf325375e030fccba0091731",
    }
    query_params = {
    }
    try:
        # Deauthorize One Cloud Provider Access Role
        api_response = api_instance.deauthorize_cloud_provider_access_role(
            path_params=path_params,
            query_params=query_params,
        )
    except atlas.ApiException as e:
        print("Exception when calling CloudProviderAccessApi->deauthorize_cloud_provider_access_role: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'cloudProvider': "AWS",
        'roleId': "bf325375e030fccba0091731",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    try:
        # Deauthorize One Cloud Provider Access Role
        api_response = api_instance.deauthorize_cloud_provider_access_role(
            path_params=path_params,
            query_params=query_params,
        )
    except atlas.ApiException as e:
        print("Exception when calling CloudProviderAccessApi->deauthorize_cloud_provider_access_role: %s\n" % e)
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
roleId | RoleIdSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CloudProviderSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["AWS", ] 

# RoleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#deauthorize_cloud_provider_access_role.ApiResponseFor204) | No Content
400 | [ApiResponseFor400](#deauthorize_cloud_provider_access_role.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#deauthorize_cloud_provider_access_role.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#deauthorize_cloud_provider_access_role.ApiResponseFor500) | Internal Server Error

#### deauthorize_cloud_provider_access_role.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[Unset, ] |  |
headers | Unset | headers were not defined |

#### deauthorize_cloud_provider_access_role.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### deauthorize_cloud_provider_access_role.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### deauthorize_cloud_provider_access_role.ApiResponseFor500
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

# **get_cloud_provider_access_role**
<a name="get_cloud_provider_access_role"></a>
> CloudProviderAccess get_cloud_provider_access_role(group_idrole_id)

Return specified Cloud Provider Access Role

Returns the Amazon Web Services (AWS) Identity and Access Management (IAM) role with the specified id and with access to the specified project. To use this resource, the requesting API Key must have the Project Owner role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import cloud_provider_access_api
from atlas.model.api_error import ApiError
from atlas.model.cloud_provider_access import CloudProviderAccess
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_provider_access_api.CloudProviderAccessApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'roleId': "bf325375e030fccba0091731",
    }
    query_params = {
    }
    try:
        # Return specified Cloud Provider Access Role
        api_response = api_instance.get_cloud_provider_access_role(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling CloudProviderAccessApi->get_cloud_provider_access_role: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
        'roleId': "bf325375e030fccba0091731",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    try:
        # Return specified Cloud Provider Access Role
        api_response = api_instance.get_cloud_provider_access_role(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling CloudProviderAccessApi->get_cloud_provider_access_role: %s\n" % e)
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
roleId | RoleIdSchema | | 

# GroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RoleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_cloud_provider_access_role.ApiResponseFor200) | OK
404 | [ApiResponseFor404](#get_cloud_provider_access_role.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#get_cloud_provider_access_role.ApiResponseFor500) | Internal Server Error

#### get_cloud_provider_access_role.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**CloudProviderAccess**](../../models/CloudProviderAccess.md) |  | 


#### get_cloud_provider_access_role.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### get_cloud_provider_access_role.ApiResponseFor500
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

# **list_cloud_provider_access_roles**
<a name="list_cloud_provider_access_roles"></a>
> CloudProviderAccess list_cloud_provider_access_roles(group_id)

Return All Cloud Provider Access Roles

Returns all Amazon Web Services (AWS) Identity and Access Management (IAM) roles with access to the specified project. To use this resource, the requesting API Key must have the Project Owner role. This resource doesn't require the API Key to have an Access List.

### Example

```python
import atlas
from atlas.apis.tags import cloud_provider_access_api
from atlas.model.api_error import ApiError
from atlas.model.cloud_provider_access import CloudProviderAccess
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cloud_provider_access_api.CloudProviderAccessApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    try:
        # Return All Cloud Provider Access Roles
        api_response = api_instance.list_cloud_provider_access_roles(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling CloudProviderAccessApi->list_cloud_provider_access_roles: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    try:
        # Return All Cloud Provider Access Roles
        api_response = api_instance.list_cloud_provider_access_roles(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling CloudProviderAccessApi->list_cloud_provider_access_roles: %s\n" % e)
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
200 | [ApiResponseFor200](#list_cloud_provider_access_roles.ApiResponseFor200) | OK
404 | [ApiResponseFor404](#list_cloud_provider_access_roles.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#list_cloud_provider_access_roles.ApiResponseFor500) | Internal Server Error

#### list_cloud_provider_access_roles.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**CloudProviderAccess**](../../models/CloudProviderAccess.md) |  | 


#### list_cloud_provider_access_roles.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### list_cloud_provider_access_roles.ApiResponseFor500
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

