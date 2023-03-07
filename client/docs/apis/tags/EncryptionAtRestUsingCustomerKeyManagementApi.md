<a name="__pageTop"></a>
# atlas.apis.tags.encryption_at_rest_using_customer_key_management_api.EncryptionAtRestUsingCustomerKeyManagementApi

All URIs are relative to *https://cloud.mongodb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**return_one_configuration_for_encryption_at_rest_using_customer_managed_keys_for_one_project**](#return_one_configuration_for_encryption_at_rest_using_customer_managed_keys_for_one_project) | **get** /api/atlas/v2/groups/{groupId}/encryptionAtRest | Return One Configuration for Encryption at Rest using Customer-Managed Keys for One Project
[**update_encryption_at_rest**](#update_encryption_at_rest) | **patch** /api/atlas/v2/groups/{groupId}/encryptionAtRest | Update Configuration for Encryption at Rest using Customer-Managed Keys for One Project

# **return_one_configuration_for_encryption_at_rest_using_customer_managed_keys_for_one_project**
<a name="return_one_configuration_for_encryption_at_rest_using_customer_managed_keys_for_one_project"></a>
> EncryptionAtRest return_one_configuration_for_encryption_at_rest_using_customer_managed_keys_for_one_project(group_id)

Return One Configuration for Encryption at Rest using Customer-Managed Keys for One Project

Returns the configuration for encryption at rest using the keys you manage through your cloud provider. MongoDB Cloud encrypts all storage even if you don't use your own key management. This resource requires the requesting API Key to have the Project Owner role.  **LIMITED TO M10 OR GREATER:** MongoDB Cloud limits this feature to dedicated cluster tiers of M10 and greater.

### Example

```python
import atlas
from atlas.apis.tags import encryption_at_rest_using_customer_key_management_api
from atlas.model.api_error import ApiError
from atlas.model.encryption_at_rest import EncryptionAtRest
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = encryption_at_rest_using_customer_key_management_api.EncryptionAtRestUsingCustomerKeyManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    try:
        # Return One Configuration for Encryption at Rest using Customer-Managed Keys for One Project
        api_response = api_instance.return_one_configuration_for_encryption_at_rest_using_customer_managed_keys_for_one_project(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling EncryptionAtRestUsingCustomerKeyManagementApi->return_one_configuration_for_encryption_at_rest_using_customer_managed_keys_for_one_project: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    try:
        # Return One Configuration for Encryption at Rest using Customer-Managed Keys for One Project
        api_response = api_instance.return_one_configuration_for_encryption_at_rest_using_customer_managed_keys_for_one_project(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling EncryptionAtRestUsingCustomerKeyManagementApi->return_one_configuration_for_encryption_at_rest_using_customer_managed_keys_for_one_project: %s\n" % e)
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
200 | [ApiResponseFor200](#return_one_configuration_for_encryption_at_rest_using_customer_managed_keys_for_one_project.ApiResponseFor200) | OK
404 | [ApiResponseFor404](#return_one_configuration_for_encryption_at_rest_using_customer_managed_keys_for_one_project.ApiResponseFor404) | Not Found
500 | [ApiResponseFor500](#return_one_configuration_for_encryption_at_rest_using_customer_managed_keys_for_one_project.ApiResponseFor500) | Internal Server Error

#### return_one_configuration_for_encryption_at_rest_using_customer_managed_keys_for_one_project.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**EncryptionAtRest**](../../models/EncryptionAtRest.md) |  | 


#### return_one_configuration_for_encryption_at_rest_using_customer_managed_keys_for_one_project.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### return_one_configuration_for_encryption_at_rest_using_customer_managed_keys_for_one_project.ApiResponseFor500
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

# **update_encryption_at_rest**
<a name="update_encryption_at_rest"></a>
> EncryptionAtRest update_encryption_at_rest(group_idencryption_at_rest)

Update Configuration for Encryption at Rest using Customer-Managed Keys for One Project

Updates the configuration for encryption at rest using the keys you manage through your cloud provider. MongoDB Cloud encrypts all storage even if you don't use your own key management. This resource requires the requesting API Key to have the Project Atlas Admin role.  **LIMITED TO M10 OR GREATER:** MongoDB Cloud limits this feature to dedicated cluster tiers of M10 and greater.

### Example

```python
import atlas
from atlas.apis.tags import encryption_at_rest_using_customer_key_management_api
from atlas.model.api_error import ApiError
from atlas.model.encryption_at_rest import EncryptionAtRest
from pprint import pprint
# Defining the host is optional and defaults to https://cloud.mongodb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = atlas.Configuration(
    host = "https://cloud.mongodb.com"
)

# Enter a context with an instance of the API client
with atlas.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = encryption_at_rest_using_customer_key_management_api.EncryptionAtRestUsingCustomerKeyManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
    }
    body = EncryptionAtRest(
        aws_kms=AWSKMS(
            access_key_id="019dd98d94b4bb778e7552e4",
            customer_master_key_id="customer_master_key_id_example",
            enabled=True,
            region="US_GOV_WEST_1",
            role_id="32b6e34b3d91647abb20e7b8",
            secret_access_key="secret_access_key_example",
            valid=True,
        ),
        azure_key_vault=AzureKeyVault(
            azure_environment="AZURE",
            client_id="client_id_example",
            enabled=True,
            key_identifier="https://EXAMPLEKeyVault.vault.azure.net/keys/EXAMPLEKey/d891821e3d364e9eb88fbd3d11807b86",
            key_vault_name="key_vault_name_example",
            resource_group_name="resource_group_name_example",
            secret="secret_example",
            subscription_id="subscription_id_example",
            tenant_id="tenant_id_example",
            valid=True,
        ),
        google_cloud_kms=GoogleCloudKMS(
            enabled=True,
            key_version_resource_id="projects/my-project-common-0/locations/us-east4/keyRings/my-key-ring-0/cryptoKeys/my-key-0/cryptoKeyVersions/1",
            service_account_key="service_account_key_example",
            valid=True,
        ),
    )
    try:
        # Update Configuration for Encryption at Rest using Customer-Managed Keys for One Project
        api_response = api_instance.update_encryption_at_rest(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling EncryptionAtRestUsingCustomerKeyManagementApi->update_encryption_at_rest: %s\n" % e)

    # example passing only optional values
    path_params = {
        'groupId': "32b6e34b3d91647abb20e7b8",
    }
    query_params = {
        'envelope': False,
        'pretty': False,
    }
    body = EncryptionAtRest(
        aws_kms=AWSKMS(
            access_key_id="019dd98d94b4bb778e7552e4",
            customer_master_key_id="customer_master_key_id_example",
            enabled=True,
            region="US_GOV_WEST_1",
            role_id="32b6e34b3d91647abb20e7b8",
            secret_access_key="secret_access_key_example",
            valid=True,
        ),
        azure_key_vault=AzureKeyVault(
            azure_environment="AZURE",
            client_id="client_id_example",
            enabled=True,
            key_identifier="https://EXAMPLEKeyVault.vault.azure.net/keys/EXAMPLEKey/d891821e3d364e9eb88fbd3d11807b86",
            key_vault_name="key_vault_name_example",
            resource_group_name="resource_group_name_example",
            secret="secret_example",
            subscription_id="subscription_id_example",
            tenant_id="tenant_id_example",
            valid=True,
        ),
        google_cloud_kms=GoogleCloudKMS(
            enabled=True,
            key_version_resource_id="projects/my-project-common-0/locations/us-east4/keyRings/my-key-ring-0/cryptoKeys/my-key-0/cryptoKeyVersions/1",
            service_account_key="service_account_key_example",
            valid=True,
        ),
    )
    try:
        # Update Configuration for Encryption at Rest using Customer-Managed Keys for One Project
        api_response = api_instance.update_encryption_at_rest(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except atlas.ApiException as e:
        print("Exception when calling EncryptionAtRestUsingCustomerKeyManagementApi->update_encryption_at_rest: %s\n" % e)
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
[**EncryptionAtRest**](../../models/EncryptionAtRest.md) |  | 


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
200 | [ApiResponseFor200](#update_encryption_at_rest.ApiResponseFor200) | OK
400 | [ApiResponseFor400](#update_encryption_at_rest.ApiResponseFor400) | Bad Request
403 | [ApiResponseFor403](#update_encryption_at_rest.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#update_encryption_at_rest.ApiResponseFor404) | Not Found
409 | [ApiResponseFor409](#update_encryption_at_rest.ApiResponseFor409) | Conflict
500 | [ApiResponseFor500](#update_encryption_at_rest.ApiResponseFor500) | Internal Server Error

#### update_encryption_at_rest.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationVndAtlas20230101json, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationVndAtlas20230101json
Type | Description  | Notes
------------- | ------------- | -------------
[**EncryptionAtRest**](../../models/EncryptionAtRest.md) |  | 


#### update_encryption_at_rest.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### update_encryption_at_rest.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### update_encryption_at_rest.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### update_encryption_at_rest.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApiError**](../../models/ApiError.md) |  | 


#### update_encryption_at_rest.ApiResponseFor500
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

