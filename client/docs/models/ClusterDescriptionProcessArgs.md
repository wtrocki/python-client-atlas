# atlas.model.cluster_description_process_args.ClusterDescriptionProcessArgs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**defaultReadConcern** | str,  | str,  | [Default level of acknowledgment requested from MongoDB for read operations](https://docs.mongodb.com/manual/reference/read-concern/) set for this cluster.  MongoDB 4.4 clusters default to &#x60;available&#x60;. MongoDB 5.0 and later clusters default to &#x60;local&#x60;. | [optional] must be one of ["local", "available", "majority", "linearizable", "snapshot", ] if omitted the server will use the default value of "available"
**defaultWriteConcern** | str,  | str,  | [Default level of acknowledgment requested from MongoDB for write operations](https://docs.mongodb.com/manual/reference/write-concern/) set for this cluster.  MongoDB 4.4 clusters default to &#x60;1&#x60;. MongoDB 5.0 and later clusters default to &#x60;majority&#x60;. | [optional] if omitted the server will use the default value of "1"
**failIndexKeyTooLong** | bool,  | BoolClass,  | Flag that indicates whether you can insert or update documents where all indexed entries don&#x27;t exceed 1024 bytes. If you set this to false, [mongod](https://docs.mongodb.com/upcoming/reference/program/mongod/#mongodb-binary-bin.mongod) writes documents that exceed this limit but doesn&#x27;t index them. | [optional] if omitted the server will use the default value of True
**javascriptEnabled** | bool,  | BoolClass,  | Flag that indicates whether the cluster allows execution of operations that perform server-side executions of JavaScript. | [optional] if omitted the server will use the default value of True
**minimumEnabledTlsProtocol** | str,  | str,  | Minimum Transport Layer Security (TLS) version that the cluster accepts for incoming connections. Clusters using TLS 1.0 or 1.1 should consider setting TLS 1.2 as the minimum TLS protocol version. | [optional] must be one of ["TLS1_0", "TLS1_1", "TLS1_2", ] 
**noTableScan** | bool,  | BoolClass,  | Flag that indicates whether the cluster disables executing any query that requires a collection scan to return results. | [optional] if omitted the server will use the default value of False
**oplogMinRetentionHours** | None, decimal.Decimal, int, float,  | NoneClass, decimal.Decimal,  | Minimum retention window for cluster&#x27;s oplog expressed in hours. A value of null indicates that the cluster uses the default minimum oplog window that MongoDB Cloud calculates. | [optional] value must be a 64 bit float
**oplogSizeMB** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  | Storage limit of cluster&#x27;s oplog expressed in megabytes. A value of null indicates that the cluster uses the default oplog size that MongoDB Cloud calculates. | [optional] value must be a 32 bit integer
**sampleRefreshIntervalBIConnector** | decimal.Decimal, int,  | decimal.Decimal,  | Interval in seconds at which the mongosqld process re-samples data to create its relational schema. | [optional] if omitted the server will use the default value of 0value must be a 32 bit integer
**sampleSizeBIConnector** | decimal.Decimal, int,  | decimal.Decimal,  | Number of documents per database to sample when gathering schema information. | [optional] if omitted the server will use the default value of 1000value must be a 32 bit integer
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

