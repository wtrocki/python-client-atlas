# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import atlas
from atlas.paths.api_atlas_v2_groups_group_id_clusters_cluster_name_snapshots_snapshot_id import get  # noqa: E501
from atlas import configuration, schemas, api_client

from .. import ApiTestMixin


class TestApiAtlasV2GroupsGroupIdClustersClusterNameSnapshotsSnapshotId(ApiTestMixin, unittest.TestCase):
    """
    ApiAtlasV2GroupsGroupIdClustersClusterNameSnapshotsSnapshotId unit test stubs
        Return One Legacy Backup Snapshot  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
