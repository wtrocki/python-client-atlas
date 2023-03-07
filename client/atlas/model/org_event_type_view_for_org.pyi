# coding: utf-8

"""
    MongoDB Atlas Administration API

    The MongoDB Atlas Administration API allows developers to manage all components in MongoDB Atlas. To learn more, review the [Administration API overview](https://www.mongodb.com/docs/atlas/api/atlas-admin-api/). This OpenAPI specification covers all of the collections with the exception of Alerts, Alert Configurations, and Events. Refer to the [legacy documentation](https://www.mongodb.com/docs/atlas/reference/api-resources/) for the specifications of these resources.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from atlas import schemas  # noqa: F401


class OrgEventTypeViewForOrg(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Unique identifier of event type.
    """
    
    @schemas.classproperty
    def ORG_CREATED(cls):
        return cls("ORG_CREATED")
    
    @schemas.classproperty
    def ORG_CREDIT_CARD_ADDED(cls):
        return cls("ORG_CREDIT_CARD_ADDED")
    
    @schemas.classproperty
    def ORG_CREDIT_CARD_UPDATED(cls):
        return cls("ORG_CREDIT_CARD_UPDATED")
    
    @schemas.classproperty
    def ORG_CREDIT_CARD_CURRENT(cls):
        return cls("ORG_CREDIT_CARD_CURRENT")
    
    @schemas.classproperty
    def ORG_CREDIT_CARD_ABOUT_TO_EXPIRE(cls):
        return cls("ORG_CREDIT_CARD_ABOUT_TO_EXPIRE")
    
    @schemas.classproperty
    def ORG_PAYPAL_LINKED(cls):
        return cls("ORG_PAYPAL_LINKED")
    
    @schemas.classproperty
    def ORG_PAYPAL_UPDATED(cls):
        return cls("ORG_PAYPAL_UPDATED")
    
    @schemas.classproperty
    def ORG_PAYPAL_CANCELLED(cls):
        return cls("ORG_PAYPAL_CANCELLED")
    
    @schemas.classproperty
    def ORG_OVERRIDE_PAYMENT_METHOD_ADDED(cls):
        return cls("ORG_OVERRIDE_PAYMENT_METHOD_ADDED")
    
    @schemas.classproperty
    def ORG_ACTIVATED(cls):
        return cls("ORG_ACTIVATED")
    
    @schemas.classproperty
    def ORG_TEMPORARILY_ACTIVATED(cls):
        return cls("ORG_TEMPORARILY_ACTIVATED")
    
    @schemas.classproperty
    def ORG_SUSPENDED(cls):
        return cls("ORG_SUSPENDED")
    
    @schemas.classproperty
    def ORG_ADMIN_SUSPENDED(cls):
        return cls("ORG_ADMIN_SUSPENDED")
    
    @schemas.classproperty
    def ORG_ADMIN_LOCKED(cls):
        return cls("ORG_ADMIN_LOCKED")
    
    @schemas.classproperty
    def ORG_CLUSTERS_DELETED(cls):
        return cls("ORG_CLUSTERS_DELETED")
    
    @schemas.classproperty
    def ORG_CLUSTERS_PAUSED(cls):
        return cls("ORG_CLUSTERS_PAUSED")
    
    @schemas.classproperty
    def ORG_LOCKED(cls):
        return cls("ORG_LOCKED")
    
    @schemas.classproperty
    def ORG_RENAMED(cls):
        return cls("ORG_RENAMED")
    
    @schemas.classproperty
    def ALL_ORG_USERS_HAVE_MFA(cls):
        return cls("ALL_ORG_USERS_HAVE_MFA")
    
    @schemas.classproperty
    def ORG_USERS_WITHOUT_MFA(cls):
        return cls("ORG_USERS_WITHOUT_MFA")
    
    @schemas.classproperty
    def ORG_INVOICE_UNDER_THRESHOLD(cls):
        return cls("ORG_INVOICE_UNDER_THRESHOLD")
    
    @schemas.classproperty
    def ORG_INVOICE_OVER_THRESHOLD(cls):
        return cls("ORG_INVOICE_OVER_THRESHOLD")
    
    @schemas.classproperty
    def ORG_DAILY_BILL_UNDER_THRESHOLD(cls):
        return cls("ORG_DAILY_BILL_UNDER_THRESHOLD")
    
    @schemas.classproperty
    def ORG_DAILY_BILL_OVER_THRESHOLD(cls):
        return cls("ORG_DAILY_BILL_OVER_THRESHOLD")
    
    @schemas.classproperty
    def ORG_GROUP_CHARGES_UNDER_THRESHOLD(cls):
        return cls("ORG_GROUP_CHARGES_UNDER_THRESHOLD")
    
    @schemas.classproperty
    def ORG_GROUP_CHARGES_OVER_THRESHOLD(cls):
        return cls("ORG_GROUP_CHARGES_OVER_THRESHOLD")
    
    @schemas.classproperty
    def ORG_TWO_FACTOR_AUTH_REQUIRED(cls):
        return cls("ORG_TWO_FACTOR_AUTH_REQUIRED")
    
    @schemas.classproperty
    def ORG_TWO_FACTOR_AUTH_OPTIONAL(cls):
        return cls("ORG_TWO_FACTOR_AUTH_OPTIONAL")
    
    @schemas.classproperty
    def ORG_PUBLIC_API_ACCESS_LIST_REQUIRED(cls):
        return cls("ORG_PUBLIC_API_ACCESS_LIST_REQUIRED")
    
    @schemas.classproperty
    def ORG_PUBLIC_API_ACCESS_LIST_NOT_REQUIRED(cls):
        return cls("ORG_PUBLIC_API_ACCESS_LIST_NOT_REQUIRED")
    
    @schemas.classproperty
    def ORG_EMPLOYEE_ACCESS_RESTRICTED(cls):
        return cls("ORG_EMPLOYEE_ACCESS_RESTRICTED")
    
    @schemas.classproperty
    def ORG_EMPLOYEE_ACCESS_UNRESTRICTED(cls):
        return cls("ORG_EMPLOYEE_ACCESS_UNRESTRICTED")
    
    @schemas.classproperty
    def ORG_SFDC_ACCOUNT_ID_CHANGED(cls):
        return cls("ORG_SFDC_ACCOUNT_ID_CHANGED")
    
    @schemas.classproperty
    def ORG_CONNECTED_TO_MLAB(cls):
        return cls("ORG_CONNECTED_TO_MLAB")
    
    @schemas.classproperty
    def ORG_DISCONNECTED_FROM_MLAB(cls):
        return cls("ORG_DISCONNECTED_FROM_MLAB")
    
    @schemas.classproperty
    def ORG_IDP_CERTIFICATE_CURRENT(cls):
        return cls("ORG_IDP_CERTIFICATE_CURRENT")
    
    @schemas.classproperty
    def ORG_IDP_CERTIFICATE_ABOUT_TO_EXPIRE(cls):
        return cls("ORG_IDP_CERTIFICATE_ABOUT_TO_EXPIRE")
    
    @schemas.classproperty
    def ORG_CONNECTED_TO_VERCEL(cls):
        return cls("ORG_CONNECTED_TO_VERCEL")
    
    @schemas.classproperty
    def ORG_DISCONNECTED_FROM_VERCEL(cls):
        return cls("ORG_DISCONNECTED_FROM_VERCEL")
    
    @schemas.classproperty
    def ORG_DISCONNECTED_TO_VERCEL(cls):
        return cls("ORG_DISCONNECTED_TO_VERCEL")
    
    @schemas.classproperty
    def ORG_CONNECTION_UNINSTALLED_FROM_VERCEL(cls):
        return cls("ORG_CONNECTION_UNINSTALLED_FROM_VERCEL")
    
    @schemas.classproperty
    def ORG_UI_IP_ACCESS_LIST_ENABLED(cls):
        return cls("ORG_UI_IP_ACCESS_LIST_ENABLED")
    
    @schemas.classproperty
    def ORG_UI_IP_ACCESS_LIST_DISABLED(cls):
        return cls("ORG_UI_IP_ACCESS_LIST_DISABLED")
    
    @schemas.classproperty
    def ORG_EDITED_UI_IP_ACCESS_LIST_ENTRIES(cls):
        return cls("ORG_EDITED_UI_IP_ACCESS_LIST_ENTRIES")