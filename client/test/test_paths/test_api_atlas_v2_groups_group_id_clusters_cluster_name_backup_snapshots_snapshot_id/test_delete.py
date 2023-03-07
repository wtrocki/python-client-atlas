# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import atlas
from atlas.paths.api_atlas_v2_groups_group_id_clusters_cluster_name_backup_snapshots_snapshot_id import delete  # noqa: E501
from atlas import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiAtlasV2GroupsGroupIdClustersClusterNameBackupSnapshotsSnapshotId(ApiTestMixin, unittest.TestCase):
    """
    ApiAtlasV2GroupsGroupIdClustersClusterNameBackupSnapshotsSnapshotId unit test stubs
        Remove One Replica Set Cloud Backup  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 204
    response_body = ''


if __name__ == '__main__':
    unittest.main()
