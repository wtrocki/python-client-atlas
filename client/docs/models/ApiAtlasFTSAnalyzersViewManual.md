# atlas.model.api_atlas_fts_analyzers_view_manual.ApiAtlasFTSAnalyzersViewManual

Settings that describe one Atlas Search custom analyzer.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Settings that describe one Atlas Search custom analyzer. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Human-readable name that identifies the custom analyzer. Names must be unique within an index, and must not start with any of the following strings: - &#x60;lucene.&#x60; - &#x60;builtin.&#x60; - &#x60;mongodb.&#x60; | 
**[tokenizer](#tokenizer)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Tokenizer that you want to use to create tokens. Tokens determine how Atlas Search splits up text into discrete chunks for indexing. | 
**[charFilters](#charFilters)** | list, tuple,  | tuple,  | Filters that examine text one character at a time and perform filtering operations. | [optional] 
**[tokenFilters](#tokenFilters)** | list, tuple,  | tuple,  | Filter that performs operations such as:  - Stemming, which reduces related words, such as \&quot;talking\&quot;, \&quot;talked\&quot;, and \&quot;talks\&quot; to their root word \&quot;talk\&quot;.  - Redaction, the removal of sensitive information from public documents. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# tokenizer

Tokenizer that you want to use to create tokens. Tokens determine how Atlas Search splits up text into discrete chunks for indexing.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Tokenizer that you want to use to create tokens. Tokens determine how Atlas Search splits up text into discrete chunks for indexing. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[TokenizeredgeGram](TokenizeredgeGram.md) | [**TokenizeredgeGram**](TokenizeredgeGram.md) | [**TokenizeredgeGram**](TokenizeredgeGram.md) |  | 
[Tokenizerkeyword](Tokenizerkeyword.md) | [**Tokenizerkeyword**](Tokenizerkeyword.md) | [**Tokenizerkeyword**](Tokenizerkeyword.md) |  | 
[TokenizernGram](TokenizernGram.md) | [**TokenizernGram**](TokenizernGram.md) | [**TokenizernGram**](TokenizernGram.md) |  | 
[TokenizerregexCaptureGroup](TokenizerregexCaptureGroup.md) | [**TokenizerregexCaptureGroup**](TokenizerregexCaptureGroup.md) | [**TokenizerregexCaptureGroup**](TokenizerregexCaptureGroup.md) |  | 
[TokenizerregexSplit](TokenizerregexSplit.md) | [**TokenizerregexSplit**](TokenizerregexSplit.md) | [**TokenizerregexSplit**](TokenizerregexSplit.md) |  | 
[Tokenizerstandard](Tokenizerstandard.md) | [**Tokenizerstandard**](Tokenizerstandard.md) | [**Tokenizerstandard**](Tokenizerstandard.md) |  | 
[TokenizeruaxUrlEmail](TokenizeruaxUrlEmail.md) | [**TokenizeruaxUrlEmail**](TokenizeruaxUrlEmail.md) | [**TokenizeruaxUrlEmail**](TokenizeruaxUrlEmail.md) |  | 
[Tokenizerwhitespace](Tokenizerwhitespace.md) | [**Tokenizerwhitespace**](Tokenizerwhitespace.md) | [**Tokenizerwhitespace**](Tokenizerwhitespace.md) |  | 

# charFilters

Filters that examine text one character at a time and perform filtering operations.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Filters that examine text one character at a time and perform filtering operations. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[CharFilterhtmlStrip](CharFilterhtmlStrip.md) | [**CharFilterhtmlStrip**](CharFilterhtmlStrip.md) | [**CharFilterhtmlStrip**](CharFilterhtmlStrip.md) |  | 
[CharFiltericuNormalize](CharFiltericuNormalize.md) | [**CharFiltericuNormalize**](CharFiltericuNormalize.md) | [**CharFiltericuNormalize**](CharFiltericuNormalize.md) |  | 
[CharFiltermapping](CharFiltermapping.md) | [**CharFiltermapping**](CharFiltermapping.md) | [**CharFiltermapping**](CharFiltermapping.md) |  | 
[CharFilterpersian](CharFilterpersian.md) | [**CharFilterpersian**](CharFilterpersian.md) | [**CharFilterpersian**](CharFilterpersian.md) |  | 

# tokenFilters

Filter that performs operations such as:  - Stemming, which reduces related words, such as \"talking\", \"talked\", and \"talks\" to their root word \"talk\".  - Redaction, the removal of sensitive information from public documents.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Filter that performs operations such as:  - Stemming, which reduces related words, such as \&quot;talking\&quot;, \&quot;talked\&quot;, and \&quot;talks\&quot; to their root word \&quot;talk\&quot;.  - Redaction, the removal of sensitive information from public documents. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[TokenFilterasciiFolding](TokenFilterasciiFolding.md) | [**TokenFilterasciiFolding**](TokenFilterasciiFolding.md) | [**TokenFilterasciiFolding**](TokenFilterasciiFolding.md) |  | 
[TokenFilterdaitchMokotoffSoundex](TokenFilterdaitchMokotoffSoundex.md) | [**TokenFilterdaitchMokotoffSoundex**](TokenFilterdaitchMokotoffSoundex.md) | [**TokenFilterdaitchMokotoffSoundex**](TokenFilterdaitchMokotoffSoundex.md) |  | 
[TokenFilteredgeGram](TokenFilteredgeGram.md) | [**TokenFilteredgeGram**](TokenFilteredgeGram.md) | [**TokenFilteredgeGram**](TokenFilteredgeGram.md) |  | 
[TokenFiltericuFolding](TokenFiltericuFolding.md) | [**TokenFiltericuFolding**](TokenFiltericuFolding.md) | [**TokenFiltericuFolding**](TokenFiltericuFolding.md) |  | 
[TokenFiltericuNormalizer](TokenFiltericuNormalizer.md) | [**TokenFiltericuNormalizer**](TokenFiltericuNormalizer.md) | [**TokenFiltericuNormalizer**](TokenFiltericuNormalizer.md) |  | 
[TokenFilterlength](TokenFilterlength.md) | [**TokenFilterlength**](TokenFilterlength.md) | [**TokenFilterlength**](TokenFilterlength.md) |  | 
[TokenFilterlowercase](TokenFilterlowercase.md) | [**TokenFilterlowercase**](TokenFilterlowercase.md) | [**TokenFilterlowercase**](TokenFilterlowercase.md) |  | 
[TokenFilternGram](TokenFilternGram.md) | [**TokenFilternGram**](TokenFilternGram.md) | [**TokenFilternGram**](TokenFilternGram.md) |  | 
[TokenFilterregex](TokenFilterregex.md) | [**TokenFilterregex**](TokenFilterregex.md) | [**TokenFilterregex**](TokenFilterregex.md) |  | 
[TokenFilterreverse](TokenFilterreverse.md) | [**TokenFilterreverse**](TokenFilterreverse.md) | [**TokenFilterreverse**](TokenFilterreverse.md) |  | 
[TokenFiltershingle](TokenFiltershingle.md) | [**TokenFiltershingle**](TokenFiltershingle.md) | [**TokenFiltershingle**](TokenFiltershingle.md) |  | 
[TokenFiltersnowballStemming](TokenFiltersnowballStemming.md) | [**TokenFiltersnowballStemming**](TokenFiltersnowballStemming.md) | [**TokenFiltersnowballStemming**](TokenFiltersnowballStemming.md) |  | 
[TokenFilterstopword](TokenFilterstopword.md) | [**TokenFilterstopword**](TokenFilterstopword.md) | [**TokenFilterstopword**](TokenFilterstopword.md) |  | 
[TokenFiltertrim](TokenFiltertrim.md) | [**TokenFiltertrim**](TokenFiltertrim.md) | [**TokenFiltertrim**](TokenFiltertrim.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

