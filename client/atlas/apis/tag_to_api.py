import typing_extensions

from atlas.apis.tags import TagValues
from atlas.apis.tags.access_tracking_api import AccessTrackingApi
from atlas.apis.tags.alert_configurations_api import AlertConfigurationsApi
from atlas.apis.tags.alerts_api import AlertsApi
from atlas.apis.tags.atlas_search_api import AtlasSearchApi
from atlas.apis.tags.auditing_api import AuditingApi
from atlas.apis.tags.cloud_backups_api import CloudBackupsApi
from atlas.apis.tags.cloud_migration_service_api import CloudMigrationServiceApi
from atlas.apis.tags.cloud_provider_access_api import CloudProviderAccessApi
from atlas.apis.tags.cluster_outage_simulation_api import ClusterOutageSimulationApi
from atlas.apis.tags.clusters_api import ClustersApi
from atlas.apis.tags.aws_clusters_dns_api import AWSClustersDNSApi
from atlas.apis.tags.custom_database_roles_api import CustomDatabaseRolesApi
from atlas.apis.tags.database_users_api import DatabaseUsersApi
from atlas.apis.tags.data_federation_api import DataFederationApi
from atlas.apis.tags.data_lake_pipelines_api import DataLakePipelinesApi
from atlas.apis.tags.encryption_at_rest_using_customer_key_management_api import EncryptionAtRestUsingCustomerKeyManagementApi
from atlas.apis.tags.events_api import EventsApi
from atlas.apis.tags.federated_authentication_api import FederatedAuthenticationApi
from atlas.apis.tags.global_clusters_api import GlobalClustersApi
from atlas.apis.tags.invoices_api import InvoicesApi
from atlas.apis.tags.ldap_configuration_api import LDAPConfigurationApi
from atlas.apis.tags.legacy_backup_api import LegacyBackupApi
from atlas.apis.tags.maintenance_windows_api import MaintenanceWindowsApi
from atlas.apis.tags.mongo_db_cloud_users_api import MongoDBCloudUsersApi
from atlas.apis.tags.monitoring_and_logs_api import MonitoringAndLogsApi
from atlas.apis.tags.multi_cloud_clusters_api import MultiCloudClustersApi
from atlas.apis.tags.network_peering_api import NetworkPeeringApi
from atlas.apis.tags.online_archive_api import OnlineArchiveApi
from atlas.apis.tags.organizations_api import OrganizationsApi
from atlas.apis.tags.performance_advisor_api import PerformanceAdvisorApi
from atlas.apis.tags.private_endpoint_services_api import PrivateEndpointServicesApi
from atlas.apis.tags.programmatic_api_keys_api import ProgrammaticAPIKeysApi
from atlas.apis.tags.project_ip_access_list_api import ProjectIPAccessListApi
from atlas.apis.tags.projects_api import ProjectsApi
from atlas.apis.tags.rolling_index_api import RollingIndexApi
from atlas.apis.tags.root_api import RootApi
from atlas.apis.tags.serverless_instances_api import ServerlessInstancesApi
from atlas.apis.tags.serverless_private_endpoints_api import ServerlessPrivateEndpointsApi
from atlas.apis.tags.shared_tier_restore_jobs_api import SharedTierRestoreJobsApi
from atlas.apis.tags.shared_tier_snapshots_api import SharedTierSnapshotsApi
from atlas.apis.tags.teams_api import TeamsApi
from atlas.apis.tags.test_api import TestApi
from atlas.apis.tags.third_party_integrations_api import ThirdPartyIntegrationsApi
from atlas.apis.tags.x509_authentication_api import X509AuthenticationApi
from atlas.apis.tags.legacy_backup_restore_jobs_api import LegacyBackupRestoreJobsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ACCESS_TRACKING: AccessTrackingApi,
        TagValues.ALERT_CONFIGURATIONS: AlertConfigurationsApi,
        TagValues.ALERTS: AlertsApi,
        TagValues.ATLAS_SEARCH: AtlasSearchApi,
        TagValues.AUDITING: AuditingApi,
        TagValues.CLOUD_BACKUPS: CloudBackupsApi,
        TagValues.CLOUD_MIGRATION_SERVICE: CloudMigrationServiceApi,
        TagValues.CLOUD_PROVIDER_ACCESS: CloudProviderAccessApi,
        TagValues.CLUSTER_OUTAGE_SIMULATION: ClusterOutageSimulationApi,
        TagValues.CLUSTERS: ClustersApi,
        TagValues.AWS_CLUSTERS_DNS: AWSClustersDNSApi,
        TagValues.CUSTOM_DATABASE_ROLES: CustomDatabaseRolesApi,
        TagValues.DATABASE_USERS: DatabaseUsersApi,
        TagValues.DATA_FEDERATION: DataFederationApi,
        TagValues.DATA_LAKE_PIPELINES: DataLakePipelinesApi,
        TagValues.ENCRYPTION_AT_REST_USING_CUSTOMER_KEY_MANAGEMENT: EncryptionAtRestUsingCustomerKeyManagementApi,
        TagValues.EVENTS: EventsApi,
        TagValues.FEDERATED_AUTHENTICATION: FederatedAuthenticationApi,
        TagValues.GLOBAL_CLUSTERS: GlobalClustersApi,
        TagValues.INVOICES: InvoicesApi,
        TagValues.LDAP_CONFIGURATION: LDAPConfigurationApi,
        TagValues.LEGACY_BACKUP: LegacyBackupApi,
        TagValues.MAINTENANCE_WINDOWS: MaintenanceWindowsApi,
        TagValues.MONGO_DB_CLOUD_USERS: MongoDBCloudUsersApi,
        TagValues.MONITORING_AND_LOGS: MonitoringAndLogsApi,
        TagValues.MULTICLOUD_CLUSTERS: MultiCloudClustersApi,
        TagValues.NETWORK_PEERING: NetworkPeeringApi,
        TagValues.ONLINE_ARCHIVE: OnlineArchiveApi,
        TagValues.ORGANIZATIONS: OrganizationsApi,
        TagValues.PERFORMANCE_ADVISOR: PerformanceAdvisorApi,
        TagValues.PRIVATE_ENDPOINT_SERVICES: PrivateEndpointServicesApi,
        TagValues.PROGRAMMATIC_API_KEYS: ProgrammaticAPIKeysApi,
        TagValues.PROJECT_IP_ACCESS_LIST: ProjectIPAccessListApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.ROLLING_INDEX: RollingIndexApi,
        TagValues.ROOT: RootApi,
        TagValues.SERVERLESS_INSTANCES: ServerlessInstancesApi,
        TagValues.SERVERLESS_PRIVATE_ENDPOINTS: ServerlessPrivateEndpointsApi,
        TagValues.SHAREDTIER_RESTORE_JOBS: SharedTierRestoreJobsApi,
        TagValues.SHAREDTIER_SNAPSHOTS: SharedTierSnapshotsApi,
        TagValues.TEAMS: TeamsApi,
        TagValues.TEST: TestApi,
        TagValues.THIRDPARTY_INTEGRATIONS: ThirdPartyIntegrationsApi,
        TagValues.X_509_AUTHENTICATION: X509AuthenticationApi,
        TagValues.LEGACY_BACKUP_RESTORE_JOBS: LegacyBackupRestoreJobsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ACCESS_TRACKING: AccessTrackingApi,
        TagValues.ALERT_CONFIGURATIONS: AlertConfigurationsApi,
        TagValues.ALERTS: AlertsApi,
        TagValues.ATLAS_SEARCH: AtlasSearchApi,
        TagValues.AUDITING: AuditingApi,
        TagValues.CLOUD_BACKUPS: CloudBackupsApi,
        TagValues.CLOUD_MIGRATION_SERVICE: CloudMigrationServiceApi,
        TagValues.CLOUD_PROVIDER_ACCESS: CloudProviderAccessApi,
        TagValues.CLUSTER_OUTAGE_SIMULATION: ClusterOutageSimulationApi,
        TagValues.CLUSTERS: ClustersApi,
        TagValues.AWS_CLUSTERS_DNS: AWSClustersDNSApi,
        TagValues.CUSTOM_DATABASE_ROLES: CustomDatabaseRolesApi,
        TagValues.DATABASE_USERS: DatabaseUsersApi,
        TagValues.DATA_FEDERATION: DataFederationApi,
        TagValues.DATA_LAKE_PIPELINES: DataLakePipelinesApi,
        TagValues.ENCRYPTION_AT_REST_USING_CUSTOMER_KEY_MANAGEMENT: EncryptionAtRestUsingCustomerKeyManagementApi,
        TagValues.EVENTS: EventsApi,
        TagValues.FEDERATED_AUTHENTICATION: FederatedAuthenticationApi,
        TagValues.GLOBAL_CLUSTERS: GlobalClustersApi,
        TagValues.INVOICES: InvoicesApi,
        TagValues.LDAP_CONFIGURATION: LDAPConfigurationApi,
        TagValues.LEGACY_BACKUP: LegacyBackupApi,
        TagValues.MAINTENANCE_WINDOWS: MaintenanceWindowsApi,
        TagValues.MONGO_DB_CLOUD_USERS: MongoDBCloudUsersApi,
        TagValues.MONITORING_AND_LOGS: MonitoringAndLogsApi,
        TagValues.MULTICLOUD_CLUSTERS: MultiCloudClustersApi,
        TagValues.NETWORK_PEERING: NetworkPeeringApi,
        TagValues.ONLINE_ARCHIVE: OnlineArchiveApi,
        TagValues.ORGANIZATIONS: OrganizationsApi,
        TagValues.PERFORMANCE_ADVISOR: PerformanceAdvisorApi,
        TagValues.PRIVATE_ENDPOINT_SERVICES: PrivateEndpointServicesApi,
        TagValues.PROGRAMMATIC_API_KEYS: ProgrammaticAPIKeysApi,
        TagValues.PROJECT_IP_ACCESS_LIST: ProjectIPAccessListApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.ROLLING_INDEX: RollingIndexApi,
        TagValues.ROOT: RootApi,
        TagValues.SERVERLESS_INSTANCES: ServerlessInstancesApi,
        TagValues.SERVERLESS_PRIVATE_ENDPOINTS: ServerlessPrivateEndpointsApi,
        TagValues.SHAREDTIER_RESTORE_JOBS: SharedTierRestoreJobsApi,
        TagValues.SHAREDTIER_SNAPSHOTS: SharedTierSnapshotsApi,
        TagValues.TEAMS: TeamsApi,
        TagValues.TEST: TestApi,
        TagValues.THIRDPARTY_INTEGRATIONS: ThirdPartyIntegrationsApi,
        TagValues.X_509_AUTHENTICATION: X509AuthenticationApi,
        TagValues.LEGACY_BACKUP_RESTORE_JOBS: LegacyBackupRestoreJobsApi,
    }
)
