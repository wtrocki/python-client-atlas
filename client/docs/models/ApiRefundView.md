# atlas.model.api_refund_view.ApiRefundView

One payment that MongoDB returned to the organization for this invoice.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | One payment that MongoDB returned to the organization for this invoice. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amountCents** | decimal.Decimal, int,  | decimal.Decimal,  | Sum of the funds returned to the specified organization expressed in cents (100th of US Dollar). | [optional] value must be a 64 bit integer
**created** | str, datetime,  | str,  | Date and time when MongoDB Cloud created this refund. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**paymentId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the payment that the organization had made. | [optional] 
**reason** | str,  | str,  | Justification that MongoDB accepted to return funds to the organization. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

