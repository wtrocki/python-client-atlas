# atlas.model.cluster_provider_settings.ClusterProviderSettings

Group of cloud provider settings that configure the provisioned MongoDB hosts.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Group of cloud provider settings that configure the provisioned MongoDB hosts. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[AWSProviderSettings](AWSProviderSettings.md) | [**AWSProviderSettings**](AWSProviderSettings.md) | [**AWSProviderSettings**](AWSProviderSettings.md) |  | 
[AzureProviderSettings](AzureProviderSettings.md) | [**AzureProviderSettings**](AzureProviderSettings.md) | [**AzureProviderSettings**](AzureProviderSettings.md) |  | 
[GCPProviderSettings](GCPProviderSettings.md) | [**GCPProviderSettings**](GCPProviderSettings.md) | [**GCPProviderSettings**](GCPProviderSettings.md) |  | 
[FreeProviderSettings](FreeProviderSettings.md) | [**FreeProviderSettings**](FreeProviderSettings.md) | [**FreeProviderSettings**](FreeProviderSettings.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

