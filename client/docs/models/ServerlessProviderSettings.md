# atlas.model.serverless_provider_settings.ServerlessProviderSettings

Group of cloud provider settings that configure the provisioned MongoDB serverless instance.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Group of cloud provider settings that configure the provisioned MongoDB serverless instance. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**regionName** | str,  | str,  | Human-readable label that identifies the geographic location of your MongoDB serverless instance. The region you choose can affect network latency for clients accessing your databases. For a complete list of region names, see [AWS](https://docs.atlas.mongodb.com/reference/amazon-aws/#std-label-amazon-aws), [GCP](https://docs.atlas.mongodb.com/reference/google-gcp/), and [Azure](https://docs.atlas.mongodb.com/reference/microsoft-azure/). | 
**backingProviderName** | str,  | str,  | Cloud service provider on which MongoDB Cloud provisioned the serverless instance. | must be one of ["AWS", "AZURE", "GCP", ] 
**providerName** | str,  | str,  | Human-readable label that identifies the cloud service provider. | [optional] must be one of ["SERVERLESS", ] if omitted the server will use the default value of "SERVERLESS"
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

