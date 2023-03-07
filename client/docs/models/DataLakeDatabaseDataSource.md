# atlas.model.data_lake_database_data_source.DataLakeDatabaseDataSource

Data store that maps to a collection for this data lake.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Data store that maps to a collection for this data lake. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**allowInsecure** | bool,  | BoolClass,  | Flag that validates the scheme in the specified URLs. If &#x60;true&#x60;, allows insecure &#x60;HTTP&#x60; scheme, doesn&#x27;t verify the server&#x27;s certificate chain and hostname, and accepts any certificate with any hostname presented by the server. If &#x60;false&#x60;, allows secure &#x60;HTTPS&#x60; scheme only. | [optional] if omitted the server will use the default value of False
**collection** | str,  | str,  | Human-readable label that identifies the collection in the database. For creating a wildcard (&#x60;*&#x60;) collection, you must omit this parameter. | [optional] 
**collectionRegex** | str,  | str,  | Regex pattern to use for creating the wildcard (*) collection. To learn more about the regex syntax, see [Go programming language](https://pkg.go.dev/regexp). | [optional] 
**database** | str,  | str,  | Human-readable label that identifies the database, which contains the collection in the cluster. You must omit this parameter to generate wildcard (&#x60;*&#x60;) collections for dynamically generated databases. | [optional] 
**databaseRegex** | str,  | str,  | Regex pattern to use for creating the wildcard (*) database. To learn more about the regex syntax, see [Go programming language](https://pkg.go.dev/regexp). | [optional] 
**defaultFormat** | str,  | str,  | File format that MongoDB Cloud uses if it encounters a file without a file extension while searching **storeName**. | [optional] must be one of [".avro", ".avro.bz2", ".avro.gz", ".bson", ".bson.bz2", ".bson.gz", ".bsonx", ".csv", ".csv.bz2", ".csv.gz", ".json", ".json.bz2", ".json.gz", ".orc", ".parquet", ".tsv", ".tsv.bz2", ".tsv.gz", ] 
**path** | str,  | str,  | File path that controls how MongoDB Cloud searches for and parses files in the **storeName** before mapping them to a collection.Specify &#x60;&#x60;/&#x60;&#x60; to capture all files and folders from the &#x60;&#x60;prefix&#x60;&#x60; path. | [optional] 
**provenanceFieldName** | str,  | str,  | Name for the field that includes the provenance of the documents in the results. MongoDB Cloud returns different fields in the results for each supported provider. | [optional] 
**storeName** | str,  | str,  | Human-readable label that identifies the data store that MongoDB Cloud maps to the collection. | [optional] 
**[urls](#urls)** | list, tuple,  | tuple,  | URLs of the publicly accessible data files. You can&#x27;t specify URLs that require authentication. Atlas Data Lake creates a partition for each URL. If empty or omitted, Data Lake uses the URLs from the store specified in the **dataSources.storeName** parameter. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# urls

URLs of the publicly accessible data files. You can't specify URLs that require authentication. Atlas Data Lake creates a partition for each URL. If empty or omitted, Data Lake uses the URLs from the store specified in the **dataSources.storeName** parameter.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | URLs of the publicly accessible data files. You can&#x27;t specify URLs that require authentication. Atlas Data Lake creates a partition for each URL. If empty or omitted, Data Lake uses the URLs from the store specified in the **dataSources.storeName** parameter. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

