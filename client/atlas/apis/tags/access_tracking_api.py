# coding: utf-8

"""
    MongoDB Atlas Administration API

    The MongoDB Atlas Administration API allows developers to manage all components in MongoDB Atlas. To learn more, review the [Administration API overview](https://www.mongodb.com/docs/atlas/api/atlas-admin-api/). This OpenAPI specification covers all of the collections with the exception of Alerts, Alert Configurations, and Events. Refer to the [legacy documentation](https://www.mongodb.com/docs/atlas/reference/api-resources/) for the specifications of these resources.  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""

from atlas.paths.api_atlas_v2_groups_group_id_db_access_history_clusters_cluster_name.get import ListAccessLogsByClusterName
from atlas.paths.api_atlas_v2_groups_group_id_db_access_history_processes_hostname.get import ListAccessLogsByHostname


class AccessTrackingApi(
    ListAccessLogsByClusterName,
    ListAccessLogsByHostname,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
