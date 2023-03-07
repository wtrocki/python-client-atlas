# atlas.model.legacy_cluster_description.LegacyClusterDescription

Group of settings that configure a MongoDB cluster.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Group of settings that configure a MongoDB cluster. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**autoScaling** | [**AutoScaling**](AutoScaling.md) | [**AutoScaling**](AutoScaling.md) |  | [optional] 
**backupEnabled** | bool,  | BoolClass,  | Flag that indicates whether the cluster can perform backups. If set to &#x60;true&#x60;, the cluster can perform backups. You must set this value to &#x60;true&#x60; for NVMe clusters. Backup uses Cloud Backups for dedicated clusters and Shared Cluster Backups for tenant clusters. If set to &#x60;false&#x60;, the cluster doesn&#x27;t use MongoDB Cloud backups. | [optional] 
**biConnector** | [**BiConnector**](BiConnector.md) | [**BiConnector**](BiConnector.md) |  | [optional] 
**clusterType** | str,  | str,  | Configuration of nodes that comprise the cluster. | [optional] must be one of ["REPLICASET", "SHARDED", "GEOSHARDED", ] 
**connectionStrings** | [**ClusterDescriptionConnectionStrings**](ClusterDescriptionConnectionStrings.md) | [**ClusterDescriptionConnectionStrings**](ClusterDescriptionConnectionStrings.md) |  | [optional] 
**createDate** | str, datetime,  | str,  | Date and time when MongoDB Cloud created this serverless instance. MongoDB Cloud represents this timestamp in ISO 8601 format in UTC. | [optional] value must conform to RFC-3339 date-time
**diskSizeGB** | decimal.Decimal, int, float,  | decimal.Decimal,  | Storage capacity that the host&#x27;s root volume possesses expressed in gigabytes. Increase this number to add capacity. MongoDB Cloud requires this parameter if you set **replicationSpecs**. If you specify a disk size below the minimum (10 GB), this parameter defaults to the minimum disk size value. Storage charge calculations depend on whether you choose the default value or a custom value.  The maximum value for disk storage cannot exceed 50 times the maximum RAM for the selected cluster. If you require more storage space, consider upgrading your cluster to a higher tier. | [optional] value must be a 64 bit float
**encryptionAtRestProvider** | str,  | str,  | Cloud service provider that manages your customer keys to provide an additional layer of Encryption at Rest for the cluster. | [optional] must be one of ["NONE", "AWS", "AZURE", "GCP", ] 
**groupId** | str,  | str,  | Unique 24-hexadecimal character string that identifies the project. | [optional] 
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the cluster. | [optional] 
**[labels](#labels)** | list, tuple,  | tuple,  | Collection of key-value pairs between 1 to 255 characters in length that tag and categorize the cluster. The MongoDB Cloud console doesn&#x27;t display your labels. | [optional] 
**[links](#links)** | list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | [optional] 
**mongoDBMajorVersion** | str,  | str,  | Major MongoDB version of the cluster. MongoDB Cloud deploys the cluster with the latest stable release of the specified version. | [optional] must be one of ["4.2", "4.4", "5.0", "6.0", ] if omitted the server will use the default value of "5.0"
**mongoDBVersion** | str,  | str,  | Version of MongoDB that the cluster runs. | [optional] 
**mongoURI** | str,  | str,  | Base connection string that you can use to connect to the cluster. MongoDB Cloud displays the string only after the cluster starts, not while it builds the cluster. | [optional] 
**mongoURIUpdated** | str, datetime,  | str,  | Date and time when someone last updated the connection string. MongoDB Cloud represents this timestamp in ISO 8601 format in UTC. | [optional] value must conform to RFC-3339 date-time
**mongoURIWithOptions** | str,  | str,  | Connection string that you can use to connect to the cluster including the &#x60;replicaSet&#x60;, &#x60;ssl&#x60;, and &#x60;authSource&#x60; query parameters with values appropriate for the cluster. You may need to add MongoDB database users. The response returns this parameter once the cluster can receive requests, not while it builds the cluster. | [optional] 
**name** | str,  | str,  | Human-readable label that identifies the cluster. | [optional] 
**numShards** | decimal.Decimal, int,  | decimal.Decimal,  | Number of shards up to 50 to deploy for a sharded cluster. The resource returns &#x60;1&#x60; to indicate a replica set and values of &#x60;2&#x60; and higher to indicate a sharded cluster. The returned value equals the number of shards in the cluster. | [optional] if omitted the server will use the default value of 1value must be a 32 bit integer
**paused** | bool,  | BoolClass,  | Flag that indicates whether the cluster is paused. | [optional] 
**pitEnabled** | bool,  | BoolClass,  | Flag that indicates whether the cluster uses continuous cloud backups. | [optional] 
**providerBackupEnabled** | bool,  | BoolClass,  | Flag that indicates whether the M10 or higher cluster can perform Cloud Backups. If set to &#x60;true&#x60;, the cluster can perform backups. If this and **backupEnabled** are set to &#x60;false&#x60;, the cluster doesn&#x27;t use MongoDB Cloud backups. | [optional] 
**providerSettings** | [**ClusterProviderSettings**](ClusterProviderSettings.md) | [**ClusterProviderSettings**](ClusterProviderSettings.md) |  | [optional] 
**replicationFactor** | decimal.Decimal, int,  | decimal.Decimal,  | Number of members that belong to the replica set. Each member retains a copy of your databases, providing high availability and data redundancy. Use **replicationSpecs** instead. | [optional] must be one of [3, 5, 7, ] if omitted the server will use the default value of 3value must be a 32 bit integer
**[replicationSpec](#replicationSpec)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Physical location where MongoDB Cloud provisions cluster nodes. | [optional] 
**[replicationSpecs](#replicationSpecs)** | list, tuple,  | tuple,  | List of settings that configure your cluster regions.  - For Global Clusters, each object in the array represents one zone where MongoDB Cloud deploys your clusters nodes. - For non-Global sharded clusters and replica sets, the single object represents where MongoDB Cloud deploys your clusters nodes. | [optional] 
**rootCertType** | str,  | str,  | Root Certificate Authority that MongoDB Atlas clusters uses. MongoDB Cloud supports Internet Security Research Group. | [optional] must be one of ["ISRGROOTX1", ] if omitted the server will use the default value of "ISRGROOTX1"
**srvAddress** | str,  | str,  | Connection string that you can use to connect to the cluster. The &#x60;+srv&#x60; modifier forces the connection to use Transport Layer Security (TLS). The &#x60;mongoURI&#x60; parameter lists additional options. | [optional] 
**stateName** | str,  | str,  | Human-readable label that indicates the current operating condition of the cluster. | [optional] must be one of ["IDLE", "CREATING", "UPDATING", "DELETING", "DELETED", "REPAIRING", ] 
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

# replicationSpec

Physical location where MongoDB Cloud provisions cluster nodes.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Physical location where MongoDB Cloud provisions cluster nodes. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**RegionSpec**](RegionSpec.md) | [**RegionSpec**](RegionSpec.md) | any string name can be used but the value must be the correct type | [optional] 

# replicationSpecs

List of settings that configure your cluster regions.  - For Global Clusters, each object in the array represents one zone where MongoDB Cloud deploys your clusters nodes. - For non-Global sharded clusters and replica sets, the single object represents where MongoDB Cloud deploys your clusters nodes.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of settings that configure your cluster regions.  - For Global Clusters, each object in the array represents one zone where MongoDB Cloud deploys your clusters nodes. - For non-Global sharded clusters and replica sets, the single object represents where MongoDB Cloud deploys your clusters nodes. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**LegacyReplicationSpec**](LegacyReplicationSpec.md) | [**LegacyReplicationSpec**](LegacyReplicationSpec.md) | [**LegacyReplicationSpec**](LegacyReplicationSpec.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

