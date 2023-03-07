# atlas.model.index_options.IndexOptions

One or more settings that determine how the MongoDB Cloud creates this MongoDB index.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | One or more settings that determine how the MongoDB Cloud creates this MongoDB index. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**2dsphereIndexVersion** | decimal.Decimal, int,  | decimal.Decimal,  | Index version number applied to the 2dsphere index. MongoDB 3.2 and later use version 3. Use this option to override the default version number. This option applies to the **2dsphere** index type only. | if omitted the server will use the default value of 3value must be a 32 bit integer
**background** | bool,  | BoolClass,  | Flag that indicates whether MongoDB should build the index in the background. This applies to MongoDB databases running feature compatibility version 4.0 or earlier. MongoDB databases running FCV 4.2 or later build indexes using an optimized build process. This process holds the exclusive lock only at the beginning and end of the build process. The rest of the build process yields to interleaving read and write operations. MongoDB databases running FCV 4.2 or later ignore this option. This option applies to all index types. | [optional] if omitted the server will use the default value of False
**bits** | decimal.Decimal, int,  | decimal.Decimal,  | Number of precision applied to the stored geohash value of the location data. This option applies to the **2d** index type only. | [optional] if omitted the server will use the default value of 26value must be a 32 bit integer
**bucketSize** | decimal.Decimal, int,  | decimal.Decimal,  | Number of units within which to group the location values. You could group in the same bucket those location values within the specified number of units to each other. This option applies to the geoHaystack index type only.  MongoDB 5.0 removed geoHaystack Indexes and the &#x60;geoSearch&#x60; command. | [optional] value must be a 32 bit integer
**default_language** | str,  | str,  | Human language that determines the list of stop words and the rules for the stemmer and tokenizer. This option accepts the supported languages using its name in lowercase english or the ISO 639-2 code. If you set this parameter to &#x60;\&quot;none\&quot;&#x60;, then the text search uses simple tokenization with no list of stop words and no stemming. This option applies to the **text** index type only. | [optional] if omitted the server will use the default value of "english"
**expireAfterSeconds** | decimal.Decimal, int,  | decimal.Decimal,  | Number of seconds that MongoDB retains documents in a Time To Live (TTL) index. | [optional] value must be a 32 bit integer
**hidden** | bool,  | BoolClass,  | Flag that determines whether the index is hidden from the query planner. A hidden index is not evaluated as part of the query plan selection. | [optional] if omitted the server will use the default value of False
**language_override** | str,  | str,  | Human-readable label that identifies the document parameter that contains the override language for the document. This option applies to the **text** index type only. | [optional] if omitted the server will use the default value of "language"
**max** | decimal.Decimal, int,  | decimal.Decimal,  | Upper inclusive boundary to limit the longitude and latitude values. This option applies to the 2d index type only. | [optional] if omitted the server will use the default value of 180value must be a 32 bit integer
**min** | decimal.Decimal, int,  | decimal.Decimal,  | Lower inclusive boundary to limit the longitude and latitude values. This option applies to the 2d index type only. | [optional] if omitted the server will use the default value of -180value must be a 32 bit integer
**name** | str,  | str,  | Human-readable label that identifies this index. This option applies to all index types. | [optional] 
**[partialFilterExpression](#partialFilterExpression)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Rules that limit the documents that the index references to a filter expression. All MongoDB index types accept a **partialFilterExpression** option. **partialFilterExpression** can include following expressions:  - equality (&#x60;\&quot;parameter\&quot; : \&quot;value\&quot;&#x60; or using the &#x60;$eq&#x60; operator) - &#x60;\&quot;$exists\&quot;: true&#x60; , maximum: &#x60;$gt&#x60;, &#x60;$gte&#x60;, &#x60;$lt&#x60;, &#x60;$lte&#x60; comparisons - &#x60;$type&#x60; - &#x60;$and&#x60; (top-level only)  This option applies to all index types. | [optional] 
**sparse** | bool,  | BoolClass,  | Flag that indicates whether the index references documents that only have the specified parameter. These indexes use less space but behave differently in some situations like when sorting. The following index types default to sparse and ignore this option: &#x60;2dsphere&#x60;, &#x60;2d&#x60;, &#x60;geoHaystack&#x60;, &#x60;text&#x60;.  Compound indexes that includes one or more indexes with &#x60;2dsphere&#x60; keys alongside other key types, only the &#x60;2dsphere&#x60; index parameters determine which documents the index references. If you run MongoDB 3.2 or later, use partial indexes. This option applies to all index types. | [optional] if omitted the server will use the default value of False
**[storageEngine](#storageEngine)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Storage engine set for the specific index. This value can be set only at creation. This option uses the following format: &#x60;\&quot;storageEngine\&quot; : { \&quot;&lt;storage-engine-name&gt;\&quot; : \&quot;&lt;options&gt;\&quot; }&#x60; MongoDB validates storage engine configuration options when creating indexes. To support replica sets with members with different storage engines, MongoDB logs these options to the oplog during replication. This option applies to all index types. | [optional] 
**textIndexVersion** | decimal.Decimal, int,  | decimal.Decimal,  | Version applied to this text index. MongoDB 3.2 and later use version &#x60;3&#x60;. Use this option to override the default version number. This option applies to the **text** index type only. | [optional] if omitted the server will use the default value of 3value must be a 32 bit integer
**unique** | bool,  | BoolClass,  | Flag that indicates whether this index can accept insertion or update of documents when the index key value matches an existing index key value. Set &#x60;\&quot;unique\&quot; : true&#x60; to set this index as unique. You can&#x27;t set a hashed index to be unique. This option applies to all index types. | [optional] if omitted the server will use the default value of False
**[weights](#weights)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Relative importance to place upon provided index parameters. This object expresses this as key/value pairs of index parameter and weight to apply to that parameter. You can specify weights for some or all the indexed parameters. The weight must be an integer between 1 and 99,999. MongoDB 5.0 and later can apply **weights** to **text** indexes only. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# partialFilterExpression

Rules that limit the documents that the index references to a filter expression. All MongoDB index types accept a **partialFilterExpression** option. **partialFilterExpression** can include following expressions:  - equality (`\"parameter\" : \"value\"` or using the `$eq` operator) - `\"$exists\": true` , maximum: `$gt`, `$gte`, `$lt`, `$lte` comparisons - `$type` - `$and` (top-level only)  This option applies to all index types.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Rules that limit the documents that the index references to a filter expression. All MongoDB index types accept a **partialFilterExpression** option. **partialFilterExpression** can include following expressions:  - equality (&#x60;\&quot;parameter\&quot; : \&quot;value\&quot;&#x60; or using the &#x60;$eq&#x60; operator) - &#x60;\&quot;$exists\&quot;: true&#x60; , maximum: &#x60;$gt&#x60;, &#x60;$gte&#x60;, &#x60;$lt&#x60;, &#x60;$lte&#x60; comparisons - &#x60;$type&#x60; - &#x60;$and&#x60; (top-level only)  This option applies to all index types. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[any_string_name](#any_string_name)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | any string name can be used but the value must be the correct type Rules that limit the documents that the index references to a filter expression. All MongoDB index types accept a **partialFilterExpression** option. **partialFilterExpression** can include following expressions:  - equality (&#x60;\&quot;parameter\&quot; : \&quot;value\&quot;&#x60; or using the &#x60;$eq&#x60; operator) - &#x60;\&quot;$exists\&quot;: true&#x60; , maximum: &#x60;$gt&#x60;, &#x60;$gte&#x60;, &#x60;$lt&#x60;, &#x60;$lte&#x60; comparisons - &#x60;$type&#x60; - &#x60;$and&#x60; (top-level only)  This option applies to all index types. | [optional] 

# any_string_name

Rules that limit the documents that the index references to a filter expression. All MongoDB index types accept a **partialFilterExpression** option. **partialFilterExpression** can include following expressions:  - equality (`\"parameter\" : \"value\"` or using the `$eq` operator) - `\"$exists\": true` , maximum: `$gt`, `$gte`, `$lt`, `$lte` comparisons - `$type` - `$and` (top-level only)  This option applies to all index types.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Rules that limit the documents that the index references to a filter expression. All MongoDB index types accept a **partialFilterExpression** option. **partialFilterExpression** can include following expressions:  - equality (&#x60;\&quot;parameter\&quot; : \&quot;value\&quot;&#x60; or using the &#x60;$eq&#x60; operator) - &#x60;\&quot;$exists\&quot;: true&#x60; , maximum: &#x60;$gt&#x60;, &#x60;$gte&#x60;, &#x60;$lt&#x60;, &#x60;$lte&#x60; comparisons - &#x60;$type&#x60; - &#x60;$and&#x60; (top-level only)  This option applies to all index types. | 

# storageEngine

Storage engine set for the specific index. This value can be set only at creation. This option uses the following format: `\"storageEngine\" : { \"<storage-engine-name>\" : \"<options>\" }` MongoDB validates storage engine configuration options when creating indexes. To support replica sets with members with different storage engines, MongoDB logs these options to the oplog during replication. This option applies to all index types.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Storage engine set for the specific index. This value can be set only at creation. This option uses the following format: &#x60;\&quot;storageEngine\&quot; : { \&quot;&lt;storage-engine-name&gt;\&quot; : \&quot;&lt;options&gt;\&quot; }&#x60; MongoDB validates storage engine configuration options when creating indexes. To support replica sets with members with different storage engines, MongoDB logs these options to the oplog during replication. This option applies to all index types. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[any_string_name](#any_string_name)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | any string name can be used but the value must be the correct type Storage engine set for the specific index. This value can be set only at creation. This option uses the following format: &#x60;\&quot;storageEngine\&quot; : { \&quot;&lt;storage-engine-name&gt;\&quot; : \&quot;&lt;options&gt;\&quot; }&#x60; MongoDB validates storage engine configuration options when creating indexes. To support replica sets with members with different storage engines, MongoDB logs these options to the oplog during replication. This option applies to all index types. | [optional] 

# any_string_name

Storage engine set for the specific index. This value can be set only at creation. This option uses the following format: `\"storageEngine\" : { \"<storage-engine-name>\" : \"<options>\" }` MongoDB validates storage engine configuration options when creating indexes. To support replica sets with members with different storage engines, MongoDB logs these options to the oplog during replication. This option applies to all index types.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Storage engine set for the specific index. This value can be set only at creation. This option uses the following format: &#x60;\&quot;storageEngine\&quot; : { \&quot;&lt;storage-engine-name&gt;\&quot; : \&quot;&lt;options&gt;\&quot; }&#x60; MongoDB validates storage engine configuration options when creating indexes. To support replica sets with members with different storage engines, MongoDB logs these options to the oplog during replication. This option applies to all index types. | 

# weights

Relative importance to place upon provided index parameters. This object expresses this as key/value pairs of index parameter and weight to apply to that parameter. You can specify weights for some or all the indexed parameters. The weight must be an integer between 1 and 99,999. MongoDB 5.0 and later can apply **weights** to **text** indexes only.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Relative importance to place upon provided index parameters. This object expresses this as key/value pairs of index parameter and weight to apply to that parameter. You can specify weights for some or all the indexed parameters. The weight must be an integer between 1 and 99,999. MongoDB 5.0 and later can apply **weights** to **text** indexes only. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[any_string_name](#any_string_name)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | any string name can be used but the value must be the correct type Relative importance to place upon provided index parameters. This object expresses this as key/value pairs of index parameter and weight to apply to that parameter. You can specify weights for some or all the indexed parameters. The weight must be an integer between 1 and 99,999. MongoDB 5.0 and later can apply **weights** to **text** indexes only. | [optional] 

# any_string_name

Relative importance to place upon provided index parameters. This object expresses this as key/value pairs of index parameter and weight to apply to that parameter. You can specify weights for some or all the indexed parameters. The weight must be an integer between 1 and 99,999. MongoDB 5.0 and later can apply **weights** to **text** indexes only.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Relative importance to place upon provided index parameters. This object expresses this as key/value pairs of index parameter and weight to apply to that parameter. You can specify weights for some or all the indexed parameters. The weight must be an integer between 1 and 99,999. MongoDB 5.0 and later can apply **weights** to **text** indexes only. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

