# atlas.model.project_setting_item_view.ProjectSettingItemView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**enabled** | bool,  | BoolClass,  | Flag that indicates whether someone enabled the regionalized private endpoint setting for the specified project.  - Set this value to &#x60;true&#x60; to enable regionalized private endpoints. This allows you to create more than one private endpoint in a cloud provider region. You need to enable this setting to connect to multi-region and global MongoDB Cloud sharded clusters. Enabling regionalized private endpoints introduces the following limitations:   - Your applications must use the new connection strings for existing multi-region and global sharded clusters. This might cause downtime.   - Your MongoDB Cloud project can&#x27;t contain replica sets nor can you create new replica sets in this project.    - You can&#x27;t disable this setting if you have:     - more than one private endpoint in more than one region     - more than one private endpoint in one region and one private endpoint in one or more regions.  - Set this value to &#x60;false&#x60; to disable regionalized private endpoints. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

