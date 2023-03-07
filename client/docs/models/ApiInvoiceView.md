# atlas.model.api_invoice_view.ApiInvoiceView

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**amountBilledCents** | decimal.Decimal, int,  | decimal.Decimal,  | Sum of services that the specified organization consumed in the period covered in this invoice. This parameter expresses its value in cents (100ths of one US Dollar) and calculates its value as **subtotalCents** + **salesTaxCents** - **startingBalanceCents**. | [optional] value must be a 64 bit integer
**amountPaidCents** | decimal.Decimal, int,  | decimal.Decimal,  | Sum that the specified organization paid toward this invoice. This parameter expresses its value in cents (100ths of one US Dollar). | [optional] value must be a 64 bit integer
**created** | str, datetime,  | str,  | Date and time when MongoDB Cloud created this invoice. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**creditsCents** | decimal.Decimal, int,  | decimal.Decimal,  | Sum that MongoDB credited the specified organization toward this invoice. This parameter expresses its value in cents (100ths of one US Dollar). | [optional] value must be a 64 bit integer
**endDate** | str, datetime,  | str,  | Date and time when MongoDB Cloud finished the billing period that this invoice covers. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**groupId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the project associated to this invoice. This identifying string doesn&#x27;t appear on all invoices. | [optional] 
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the invoice submitted to the specified organization. Charges typically post the next day. | [optional] 
**[lineItems](#lineItems)** | list, tuple,  | tuple,  | List that contains individual services included in this invoice. | [optional] 
**[linkedInvoices](#linkedInvoices)** | list, tuple,  | tuple,  | List that contains the invoices for organizations linked to the paying organization. | [optional] 
**[links](#links)** | list, tuple,  | tuple,  | List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships. | [optional] 
**orgId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the organization charged for services consumed from MongoDB Cloud. | [optional] 
**[payments](#payments)** | list, tuple,  | tuple,  | List that contains funds transferred to MongoDB to cover the specified service noted in this invoice. | [optional] 
**[refunds](#refunds)** | list, tuple,  | tuple,  | List that contains payments that MongoDB returned to the organization for this invoice. | [optional] 
**salesTaxCents** | decimal.Decimal, int,  | decimal.Decimal,  | Sum of sales tax applied to this invoice. This parameter expresses its value in cents (100ths of one US Dollar). | [optional] value must be a 64 bit integer
**startDate** | str, datetime,  | str,  | Date and time when MongoDB Cloud began the billing period that this invoice covers. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**startingBalanceCents** | decimal.Decimal, int,  | decimal.Decimal,  | Sum that the specified organization owed to MongoDB when MongoDB issued this invoice. This parameter expresses its value in US Dollars. | [optional] value must be a 64 bit integer
**statusName** | str,  | str,  | Phase of payment processing in which this invoice exists when you made this request. Accepted phases include:  | Phase Value | Reason | |---|---| | CLOSED | MongoDB finalized all charges in the billing cycle but has yet to charge the customer. | | FAILED | MongoDB attempted to charge the provided credit card but charge for that amount failed. | | FORGIVEN | Customer initiated payment which MongoDB later forgave. | | FREE | All charges totalled zero so the customer won&#x27;t be charged. | | INVOICED | MongoDB handled these charges using elastic invoicing. | | PAID | MongoDB succeeded in charging the provided credit card. | | PENDING | Invoice includes charges for the current billing cycle. | | PREPAID | Customer has a pre-paid plan so they won&#x27;t be charged. |  | [optional] must be one of ["PENDING", "CLOSED", "FORGIVEN", "FAILED", "PAID", "FREE", "PREPAID", "INVOICED", ] 
**subtotalCents** | decimal.Decimal, int,  | decimal.Decimal,  | Sum of all positive invoice line items contained in this invoice. This parameter expresses its value in cents (100ths of one US Dollar). | [optional] value must be a 64 bit integer
**updated** | str, datetime,  | str,  | Date and time when MongoDB Cloud last updated the value of this payment. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# lineItems

List that contains individual services included in this invoice.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains individual services included in this invoice. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiLineItemView**](ApiLineItemView.md) | [**ApiLineItemView**](ApiLineItemView.md) | [**ApiLineItemView**](ApiLineItemView.md) |  | 

# linkedInvoices

List that contains the invoices for organizations linked to the paying organization.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains the invoices for organizations linked to the paying organization. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiInvoiceView**](ApiInvoiceView.md) | [**ApiInvoiceView**](ApiInvoiceView.md) | [**ApiInvoiceView**](ApiInvoiceView.md) |  | 

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

# payments

List that contains funds transferred to MongoDB to cover the specified service noted in this invoice.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains funds transferred to MongoDB to cover the specified service noted in this invoice. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiPaymentView**](ApiPaymentView.md) | [**ApiPaymentView**](ApiPaymentView.md) | [**ApiPaymentView**](ApiPaymentView.md) |  | 

# refunds

List that contains payments that MongoDB returned to the organization for this invoice.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List that contains payments that MongoDB returned to the organization for this invoice. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ApiRefundView**](ApiRefundView.md) | [**ApiRefundView**](ApiRefundView.md) | [**ApiRefundView**](ApiRefundView.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

