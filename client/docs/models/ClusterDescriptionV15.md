# atlas.model.cluster_description_v15.ClusterDescriptionV15

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**backupEnabled** | bool,  | BoolClass,  | Flag that indicates whether the cluster can perform backups. If set to &#x60;true&#x60;, the cluster can perform backups. You must set this value to &#x60;true&#x60; for NVMe clusters. Backup uses [Cloud Backups](https://docs.atlas.mongodb.com/backup/cloud-backup/overview/) for dedicated clusters and [Shared Cluster Backups](https://docs.atlas.mongodb.com/backup/shared-tier/overview/) for tenant clusters. If set to &#x60;false&#x60;, the cluster doesn&#x27;t use backups. | [optional] if omitted the server will use the default value of False
**biConnector** | [**BiConnector**](BiConnector.md) | [**BiConnector**](BiConnector.md) |  | [optional] 
**clusterType** | str,  | str,  | Configuration of nodes that comprise the cluster. | [optional] must be one of ["REPLICASET", "SHARDED", "GEOSHARDED", ] 
**connectionStrings** | [**ClusterDescriptionConnectionStrings**](ClusterDescriptionConnectionStrings.md) | [**ClusterDescriptionConnectionStrings**](ClusterDescriptionConnectionStrings.md) |  | [optional] 
**createDate** | str, datetime,  | str,  | Date and time when MongoDB Cloud created this cluster. This parameter expresses its value in ISO 8601 format in UTC. | [optional] value must conform to RFC-3339 date-time
**diskSizeGB** | decimal.Decimal, int, float,  | decimal.Decimal,  | Storage capacity that the host&#x27;s root volume possesses expressed in gigabytes. Increase this number to add capacity. MongoDB Cloud requires this parameter if you set **replicationSpecs**. If you specify a disk size below the minimum (10 GB), this parameter defaults to the minimum disk size value. Storage charge calculations depend on whether you choose the default value or a custom value.  The maximum value for disk storage cannot exceed 50 times the maximum RAM for the selected cluster. If you require more storage space, consider upgrading your cluster to a higher tier. | [optional] value must be a 64 bit float
**encryptionAtRestProvider** | str,  | str,  | Cloud service provider that manages your customer keys to provide an additional layer of encryption at rest for the cluster. To enable customer key management for encryption at rest, the cluster **replicationSpecs[n].regionConfigs[m].{type}Specs.instanceSize** setting must be &#x60;M10&#x60; or higher and &#x60;\&quot;backupEnabled\&quot; : false&#x60; or omitted entirely. | [optional] must be one of ["NONE", "AWS", "AZURE", "GCP", ] 
**groupId** | str,  | str,  | Unique 24-hexadecimal character string that identifies the project. | [optional] 
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the replication object for a zone in a Global Cluster. If you include existing zones in the request, you must specify this parameter. If you add a new zone to an existing Global Cluster, you may specify this parameter. The request deletes any existing zones in a Global Cluster that you exclude from the request. | [optional] 
**[labels](#labels)** | list, tuple,  | tuple,  | Collection of key-value pairs between 1 to 255 characters in length that tag and categorize the cluster. The MongoDB Cloud console doesn&#x27;t display your labels. | [optional] 
**[links](#links)** | list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | [optional] 
**mongoDBMajorVersion** | str,  | str,  | Major MongoDB version of the cluster. MongoDB Cloud deploys the cluster with the latest stable release of the specified version. | [optional] must be one of ["4.2", "4.4", "5.0", "6.0", ] if omitted the server will use the default value of "5.0"
**mongoDBVersion** | str,  | str,  | Version of MongoDB that the cluster runs. | [optional] 
**name** | str,  | str,  | Human-readable label that identifies the advanced cluster. | [optional] 
**paused** | bool,  | BoolClass,  | Flag that indicates whether the cluster is paused. | [optional] 
**pitEnabled** | bool,  | BoolClass,  | Flag that indicates whether the cluster uses continuous cloud backups. | [optional] 
**[replicationSpecs](#replicationSpecs)** | list, tuple,  | tuple,  | List of settings that configure your cluster regions. For Global Clusters, each object in the array represents a zone where your clusters nodes deploy. For non-Global sharded clusters and replica sets, this array has one object representing where your clusters nodes deploy. | [optional] 
**rootCertType** | str,  | str,  | Root Certificate Authority that MongoDB Cloud cluster uses. MongoDB Cloud supports Internet Security Research Group. | [optional] must be one of ["ISRGROOTX1", ] if omitted the server will use the default value of "ISRGROOTX1"
**stateName** | str,  | str,  | Human-readable label that indicates the current operating condition of this cluster. | [optional] must be one of ["IDLE", "CREATING", "UPDATING", "DELETING", "DELETED", "REPAIRING", ] 
**terminationProtectionEnabled** | bool,  | BoolClass,  | Flag that indicates whether termination protection is enabled on the cluster. If set to &#x60;true&#x60;, MongoDB Cloud won&#x27;t delete the cluster. If set to &#x60;false&#x60;, MongoDB Cloud will delete the cluster. | [optional] if omitted the server will use the default value of False
**versionReleaseSystem** | str,  | str,  | Method by which the cluster maintains the MongoDB versions. If value is &#x60;CONTINUOUS&#x60;, you must not specify **mongoDBMajorVersion**. | [optional] must be one of ["LTS", "CONTINUOUS", ] if omitted the server will use the default value of "LTS"
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# labels

Collection of key-value pairs between 1 to 255 characters in length that tag and categorize the cluster. The MongoDB Cloud console doesn't display your labels.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Collection of key-value pairs between 1 to 255 characters in length that tag and categorize the cluster. The MongoDB Cloud console doesn&#x27;t display your labels. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**NDSLabel**](NDSLabel.md) | [**NDSLabel**](NDSLabel.md) | [**NDSLabel**](NDSLabel.md) |  | 

# links

List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Link**](Link.md) | [**Link**](Link.md) | [**Link**](Link.md) |  | 

# replicationSpecs

List of settings that configure your cluster regions. For Global Clusters, each object in the array represents a zone where your clusters nodes deploy. For non-Global sharded clusters and replica sets, this array has one object representing where your clusters nodes deploy.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of settings that configure your cluster regions. For Global Clusters, each object in the array represents a zone where your clusters nodes deploy. For non-Global sharded clusters and replica sets, this array has one object representing where your clusters nodes deploy. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ReplicationSpec**](ReplicationSpec.md) | [**ReplicationSpec**](ReplicationSpec.md) | [**ReplicationSpec**](ReplicationSpec.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

