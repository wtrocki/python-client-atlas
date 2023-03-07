# coding: utf-8

"""
    MongoDB Atlas Administration API

    The MongoDB Atlas Administration API allows developers to manage all components in MongoDB Atlas. To learn more, review the [Administration API overview](https://www.mongodb.com/docs/atlas/api/atlas-admin-api/). This OpenAPI specification covers all of the collections with the exception of Alerts, Alert Configurations, and Events. Refer to the [legacy documentation](https://www.mongodb.com/docs/atlas/reference/api-resources/) for the specifications of these resources.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""

import unittest

import atlas
from atlas.model.alert_config_audit_type_view import AlertConfigAuditTypeView
from atlas import configuration


class TestAlertConfigAuditTypeView(unittest.TestCase):
    """AlertConfigAuditTypeView unit test stubs"""
    _configuration = configuration.Configuration()


if __name__ == '__main__':
    unittest.main()