# atlas.model.criteria_view.CriteriaView

Rules by which MongoDB MongoDB Cloud archives data.  Use the **criteria.type** field to choose how MongoDB Cloud selects data to archive. Choose data using the age of the data or a MongoDB query. **\"criteria.type\": \"DATE\"** selects documents to archive based on a date. **\"criteria.type\": \"CUSTOM\"** selects documents to archive based on a custom JSON query. MongoDB Cloud doesn't support **\"criteria.type\": \"CUSTOM\"** when **\"collectionType\": \"TIMESERIES\"**.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Rules by which MongoDB MongoDB Cloud archives data.  Use the **criteria.type** field to choose how MongoDB Cloud selects data to archive. Choose data using the age of the data or a MongoDB query. **\&quot;criteria.type\&quot;: \&quot;DATE\&quot;** selects documents to archive based on a date. **\&quot;criteria.type\&quot;: \&quot;CUSTOM\&quot;** selects documents to archive based on a custom JSON query. MongoDB Cloud doesn&#x27;t support **\&quot;criteria.type\&quot;: \&quot;CUSTOM\&quot;** when **\&quot;collectionType\&quot;: \&quot;TIMESERIES\&quot;**. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### oneOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[CustomCriteriaView](CustomCriteriaView.md) | [**CustomCriteriaView**](CustomCriteriaView.md) | [**CustomCriteriaView**](CustomCriteriaView.md) |  | 
[DateCriteriaView](DateCriteriaView.md) | [**DateCriteriaView**](DateCriteriaView.md) | [**DateCriteriaView**](DateCriteriaView.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

