# coding: utf-8

"""
    MongoDB Atlas Administration API

    The MongoDB Atlas Administration API allows developers to manage all components in MongoDB Atlas. To learn more, review the [Administration API overview](https://www.mongodb.com/docs/atlas/api/atlas-admin-api/). This OpenAPI specification covers all of the collections with the exception of Alerts, Alert Configurations, and Events. Refer to the [legacy documentation](https://www.mongodb.com/docs/atlas/reference/api-resources/) for the specifications of these resources.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""

from atlas.paths.api_atlas_v2_groups_group_id_maintenance_window_defer.post import DeferMaintenanceWindow
from atlas.paths.api_atlas_v2_groups_group_id_maintenance_window.get import GetMaintenanceWindow
from atlas.paths.api_atlas_v2_groups_group_id_maintenance_window.delete import ResetMaintenanceWindow
from atlas.paths.api_atlas_v2_groups_group_id_maintenance_window_auto_defer.post import ToggleMaintenanceAutoDefer
from atlas.paths.api_atlas_v2_groups_group_id_maintenance_window.patch import UpdateMaintenanceWindow


class MaintenanceWindowsApi(
    DeferMaintenanceWindow,
    GetMaintenanceWindow,
    ResetMaintenanceWindow,
    ToggleMaintenanceAutoDefer,
    UpdateMaintenanceWindow,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
