# atlas.model.api_payment_view.ApiPaymentView

Funds transferred to MongoDB to cover the specified service in this invoice.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Funds transferred to MongoDB to cover the specified service in this invoice. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amountBilledCents** | decimal.Decimal, int,  | decimal.Decimal,  | Sum of services that the specified organization consumed in the period covered in this invoice. This parameter expresses its value in cents (100ths of one US Dollar) and calculates its value as **subtotalCents** + **salesTaxCents** - **startingBalanceCents**. | [optional] value must be a 64 bit integer
**amountPaidCents** | decimal.Decimal, int,  | decimal.Decimal,  | Sum that the specified organization paid toward the associated invoice. This parameter expresses its value in cents (100ths of one US Dollar). | [optional] value must be a 64 bit integer
**created** | str, datetime,  | str,  | Date and time when the customer made this payment attempt. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies this payment toward the associated invoice. | [optional] 
**salesTaxCents** | decimal.Decimal, int,  | decimal.Decimal,  | Sum of sales tax applied to this invoice. This parameter expresses its value in cents (100ths of one US Dollar). | [optional] value must be a 64 bit integer
**statusName** | str,  | str,  | Phase of payment processing for the associated invoice when you made this request.  These phases include:  | Phase Value | Reason | |---|---| | &#x60;CANCELLED&#x60; | Customer or MongoDB cancelled the payment. | | &#x60;ERROR&#x60; | Issue arose when attempting to complete payment. | | &#x60;FAILED&#x60; | MongoDB tried to charge the credit card without success. | | &#x60;FAILED_AUTHENTICATION&#x60; | Strong Customer Authentication has failed. Confirm that your payment method is authenticated. | | &#x60;FORGIVEN&#x60; | Customer initiated payment which MongoDB later forgave. | | &#x60;INVOICED&#x60; | MongoDB issued an invoice that included this line item. | | &#x60;NEW&#x60; | Customer provided a method of payment, but MongoDB hasn&#x27;t tried to charge the credit card. | | &#x60;PAID&#x60; | Customer submitted a successful payment. | | &#x60;PARTIAL_PAID&#x60; | Customer paid for part of this line item. |  | [optional] must be one of ["NEW", "FORGIVEN", "FAILED", "PAID", "PARTIAL_PAID", "CANCELLED", "INVOICED", "ERROR", "FAILED_AUTHENTICATION", "PROCESSING", "PENDING_REVERSAL", ] 
**subtotalCents** | decimal.Decimal, int,  | decimal.Decimal,  | Sum of all positive invoice line items contained in this invoice. This parameter expresses its value in cents (100ths of one US Dollar). | [optional] value must be a 64 bit integer
**updated** | str, datetime,  | str,  | Date and time when the customer made an update to this payment attempt. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

