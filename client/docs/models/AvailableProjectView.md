# atlas.model.available_project_view.AvailableProjectView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Human-readable label that identifies this project. | 
**projectId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the project to be migrated. | 
**[deployments](#deployments)** | list, tuple,  | tuple,  | List of clusters that can be migrated to MongoDB Cloud. | [optional] 
**[migrationHosts](#migrationHosts)** | list, tuple,  | tuple,  | Hostname of MongoDB Agent list that you configured to perform a migration. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# deployments

List of clusters that can be migrated to MongoDB Cloud.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of clusters that can be migrated to MongoDB Cloud. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AvailableDeploymentView**](AvailableDeploymentView.md) | [**AvailableDeploymentView**](AvailableDeploymentView.md) | [**AvailableDeploymentView**](AvailableDeploymentView.md) |  | 

# migrationHosts

Hostname of MongoDB Agent list that you configured to perform a migration.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Hostname of MongoDB Agent list that you configured to perform a migration. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | Hostname of MongoDB Agent that you configured to perform a migration. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

