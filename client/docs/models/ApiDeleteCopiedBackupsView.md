# atlas.model.api_delete_copied_backups_view.ApiDeleteCopiedBackupsView

Deleted copy setting whose backup copies need to also be deleted.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Deleted copy setting whose backup copies need to also be deleted. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**cloudProvider** | str,  | str,  | Human-readable label that identifies the cloud provider for the deleted copy setting whose backup copies you want to delete. | [optional] must be one of ["AWS", "AZURE", "GCP", ] 
**regionName** | str,  | str,  | Target region for the deleted copy setting whose backup copies you want to delete. Please supply the &#x27;Atlas Region&#x27; which can be found under [Cloud Providers](https://www.mongodb.com/docs/atlas/reference/cloud-providers/) &#x27;regions&#x27; link. | [optional] 
**replicationSpecId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the replication object for a zone in a cluster. For global clusters, there can be multiple zones to choose from. For sharded clusters and replica setclusters, there is only one zone in the cluster. To find the Replication Spec Id, do a GET request to Return One Cluster in One Project and consult the replicationSpecs array [Return One Cluster in One Project](#operation/getLegacyCluster). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

