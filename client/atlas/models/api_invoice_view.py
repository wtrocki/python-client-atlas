# coding: utf-8

"""
    MongoDB Atlas Administration API

    The MongoDB Atlas Administration API allows developers to manage all components in MongoDB Atlas. To learn more, review the [Administration API overview](https://www.mongodb.com/docs/atlas/api/atlas-admin-api/). This OpenAPI specification covers all of the collections with the exception of Alerts, Alert Configurations, and Events. Refer to the [legacy documentation](https://www.mongodb.com/docs/atlas/reference/api-resources/) for the specifications of these resources.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, constr, validator
from atlas.models.api_line_item_view import ApiLineItemView
from atlas.models.api_payment_view import ApiPaymentView
from atlas.models.api_refund_view import ApiRefundView
from atlas.models.link import Link

class ApiInvoiceView(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    amount_billed_cents: Optional[StrictInt] = Field(None, alias="amountBilledCents", description="Sum of services that the specified organization consumed in the period covered in this invoice. This parameter expresses its value in cents (100ths of one US Dollar) and calculates its value as **subtotalCents** + **salesTaxCents** - **startingBalanceCents**.")
    amount_paid_cents: Optional[StrictInt] = Field(None, alias="amountPaidCents", description="Sum that the specified organization paid toward this invoice. This parameter expresses its value in cents (100ths of one US Dollar).")
    created: Optional[datetime] = Field(None, description="Date and time when MongoDB Cloud created this invoice. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    credits_cents: Optional[StrictInt] = Field(None, alias="creditsCents", description="Sum that MongoDB credited the specified organization toward this invoice. This parameter expresses its value in cents (100ths of one US Dollar).")
    end_date: Optional[datetime] = Field(None, alias="endDate", description="Date and time when MongoDB Cloud finished the billing period that this invoice covers. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    group_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="groupId", description="Unique 24-hexadecimal digit string that identifies the project associated to this invoice. This identifying string doesn't appear on all invoices.")
    id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, description="Unique 24-hexadecimal digit string that identifies the invoice submitted to the specified organization. Charges typically post the next day.")
    line_items: Optional[List[ApiLineItemView]] = Field(None, alias="lineItems", description="List that contains individual services included in this invoice.")
    linked_invoices: Optional[List[ApiInvoiceView]] = Field(None, alias="linkedInvoices", description="List that contains the invoices for organizations linked to the paying organization.")
    links: Optional[List[Link]] = Field(None, description="List of one or more Uniform Resource Locators (URLs) that point to API sub-resources, related API resources, or both. RFC 5988 outlines these relationships.")
    org_id: Optional[constr(strict=True, max_length=24, min_length=24)] = Field(None, alias="orgId", description="Unique 24-hexadecimal digit string that identifies the organization charged for services consumed from MongoDB Cloud.")
    payments: Optional[List[ApiPaymentView]] = Field(None, description="List that contains funds transferred to MongoDB to cover the specified service noted in this invoice.")
    refunds: Optional[List[ApiRefundView]] = Field(None, description="List that contains payments that MongoDB returned to the organization for this invoice.")
    sales_tax_cents: Optional[StrictInt] = Field(None, alias="salesTaxCents", description="Sum of sales tax applied to this invoice. This parameter expresses its value in cents (100ths of one US Dollar).")
    start_date: Optional[datetime] = Field(None, alias="startDate", description="Date and time when MongoDB Cloud began the billing period that this invoice covers. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    starting_balance_cents: Optional[StrictInt] = Field(None, alias="startingBalanceCents", description="Sum that the specified organization owed to MongoDB when MongoDB issued this invoice. This parameter expresses its value in US Dollars.")
    status_name: Optional[StrictStr] = Field(None, alias="statusName", description="Phase of payment processing in which this invoice exists when you made this request. Accepted phases include:  | Phase Value | Reason | |---|---| | CLOSED | MongoDB finalized all charges in the billing cycle but has yet to charge the customer. | | FAILED | MongoDB attempted to charge the provided credit card but charge for that amount failed. | | FORGIVEN | Customer initiated payment which MongoDB later forgave. | | FREE | All charges totalled zero so the customer won't be charged. | | INVOICED | MongoDB handled these charges using elastic invoicing. | | PAID | MongoDB succeeded in charging the provided credit card. | | PENDING | Invoice includes charges for the current billing cycle. | | PREPAID | Customer has a pre-paid plan so they won't be charged. | ")
    subtotal_cents: Optional[StrictInt] = Field(None, alias="subtotalCents", description="Sum of all positive invoice line items contained in this invoice. This parameter expresses its value in cents (100ths of one US Dollar).")
    updated: Optional[datetime] = Field(None, description="Date and time when MongoDB Cloud last updated the value of this payment. This parameter expresses its value in the ISO 8601 timestamp format in UTC.")
    __properties = ["amountBilledCents", "amountPaidCents", "created", "creditsCents", "endDate", "groupId", "id", "lineItems", "linkedInvoices", "links", "orgId", "payments", "refunds", "salesTaxCents", "startDate", "startingBalanceCents", "statusName", "subtotalCents", "updated"]

    @validator('group_id')
    def group_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('id')
    def id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('org_id')
    def org_id_validate_regular_expression(cls, v):
        if not re.match(r"^([a-f0-9]{24})$", v):
            raise ValueError(r"must validate the regular expression /^([a-f0-9]{24})$/")
        return v

    @validator('status_name')
    def status_name_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('PENDING', 'CLOSED', 'FORGIVEN', 'FAILED', 'PAID', 'FREE', 'PREPAID', 'INVOICED'):
            raise ValueError("must validate the enum values ('PENDING', 'CLOSED', 'FORGIVEN', 'FAILED', 'PAID', 'FREE', 'PREPAID', 'INVOICED')")
        return v

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ApiInvoiceView:
        """Create an instance of ApiInvoiceView from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "amount_billed_cents",
                            "amount_paid_cents",
                            "created",
                            "credits_cents",
                            "end_date",
                            "group_id",
                            "id",
                            "line_items",
                            "linked_invoices",
                            "links",
                            "org_id",
                            "payments",
                            "refunds",
                            "sales_tax_cents",
                            "start_date",
                            "starting_balance_cents",
                            "subtotal_cents",
                            "updated",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in line_items (list)
        _items = []
        if self.line_items:
            for _item in self.line_items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['lineItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in linked_invoices (list)
        _items = []
        if self.linked_invoices:
            for _item in self.linked_invoices:
                if _item:
                    _items.append(_item.to_dict())
            _dict['linkedInvoices'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in payments (list)
        _items = []
        if self.payments:
            for _item in self.payments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['payments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in refunds (list)
        _items = []
        if self.refunds:
            for _item in self.refunds:
                if _item:
                    _items.append(_item.to_dict())
            _dict['refunds'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ApiInvoiceView:
        """Create an instance of ApiInvoiceView from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ApiInvoiceView.parse_obj(obj)

        _obj = ApiInvoiceView.parse_obj({
            "amount_billed_cents": obj.get("amountBilledCents"),
            "amount_paid_cents": obj.get("amountPaidCents"),
            "created": obj.get("created"),
            "credits_cents": obj.get("creditsCents"),
            "end_date": obj.get("endDate"),
            "group_id": obj.get("groupId"),
            "id": obj.get("id"),
            "line_items": [ApiLineItemView.from_dict(_item) for _item in obj.get("lineItems")] if obj.get("lineItems") is not None else None,
            "linked_invoices": [ApiInvoiceView.from_dict(_item) for _item in obj.get("linkedInvoices")] if obj.get("linkedInvoices") is not None else None,
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None,
            "org_id": obj.get("orgId"),
            "payments": [ApiPaymentView.from_dict(_item) for _item in obj.get("payments")] if obj.get("payments") is not None else None,
            "refunds": [ApiRefundView.from_dict(_item) for _item in obj.get("refunds")] if obj.get("refunds") is not None else None,
            "sales_tax_cents": obj.get("salesTaxCents"),
            "start_date": obj.get("startDate"),
            "starting_balance_cents": obj.get("startingBalanceCents"),
            "status_name": obj.get("statusName"),
            "subtotal_cents": obj.get("subtotalCents"),
            "updated": obj.get("updated")
        })
        return _obj

