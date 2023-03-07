# atlas.model.cloud_provider_access_export_snapshot_feature_usage.CloudProviderAccessExportSnapshotFeatureUsage

Details that describe the Amazon Web Services (AWS) Simple Storage Service (S3) export buckets linked to this AWS Identity and Access Management (IAM) role.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Details that describe the Amazon Web Services (AWS) Simple Storage Service (S3) export buckets linked to this AWS Identity and Access Management (IAM) role. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**featureId** | [**CloudProviderAccessFeatureUsageExportSnapshotFeatureId**](CloudProviderAccessFeatureUsageExportSnapshotFeatureId.md) | [**CloudProviderAccessFeatureUsageExportSnapshotFeatureId**](CloudProviderAccessFeatureUsageExportSnapshotFeatureId.md) |  | [optional] 
**featureType** | str,  | str,  | Human-readable label that describes one MongoDB Cloud feature linked to this Amazon Web Services (AWS) Identity and Access Management (IAM) role. | [optional] must be one of ["ATLAS_DATA_LAKE", "ENCRYPTION_AT_REST", "EXPORT_SNAPSHOT", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

