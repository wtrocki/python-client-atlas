# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from atlas.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ACCESS_TRACKING = "Access Tracking"
    ALERT_CONFIGURATIONS = "Alert Configurations"
    ALERTS = "Alerts"
    ATLAS_SEARCH = "Atlas Search"
    AUDITING = "Auditing"
    CLOUD_BACKUPS = "Cloud Backups"
    CLOUD_MIGRATION_SERVICE = "Cloud Migration Service"
    CLOUD_PROVIDER_ACCESS = "Cloud Provider Access"
    CLUSTER_OUTAGE_SIMULATION = "Cluster Outage Simulation"
    CLUSTERS = "Clusters"
    AWS_CLUSTERS_DNS = "AWS Clusters DNS"
    CUSTOM_DATABASE_ROLES = "Custom Database Roles"
    DATABASE_USERS = "Database Users"
    DATA_FEDERATION = "Data Federation"
    DATA_LAKE_PIPELINES = "Data Lake Pipelines"
    ENCRYPTION_AT_REST_USING_CUSTOMER_KEY_MANAGEMENT = "Encryption at Rest using Customer Key Management"
    EVENTS = "Events"
    FEDERATED_AUTHENTICATION = "Federated Authentication"
    GLOBAL_CLUSTERS = "Global Clusters"
    INVOICES = "Invoices"
    LDAP_CONFIGURATION = "LDAP Configuration"
    LEGACY_BACKUP = "Legacy Backup"
    MAINTENANCE_WINDOWS = "Maintenance Windows"
    MONGO_DB_CLOUD_USERS = "MongoDB Cloud Users"
    MONITORING_AND_LOGS = "Monitoring and Logs"
    MULTICLOUD_CLUSTERS = "Multi-Cloud Clusters"
    NETWORK_PEERING = "Network Peering"
    ONLINE_ARCHIVE = "Online Archive"
    ORGANIZATIONS = "Organizations"
    PERFORMANCE_ADVISOR = "Performance Advisor"
    PRIVATE_ENDPOINT_SERVICES = "Private Endpoint Services"
    PROGRAMMATIC_API_KEYS = "Programmatic API Keys"
    PROJECT_IP_ACCESS_LIST = "Project IP Access List"
    PROJECTS = "Projects"
    ROLLING_INDEX = "Rolling Index"
    ROOT = "Root"
    SERVERLESS_INSTANCES = "Serverless Instances"
    SERVERLESS_PRIVATE_ENDPOINTS = "Serverless Private Endpoints"
    SHAREDTIER_RESTORE_JOBS = "Shared-Tier Restore Jobs"
    SHAREDTIER_SNAPSHOTS = "Shared-Tier Snapshots"
    TEAMS = "Teams"
    TEST = "Test"
    THIRDPARTY_INTEGRATIONS = "Third-Party Integrations"
    X_509_AUTHENTICATION = "X.509 Authentication"
    LEGACY_BACKUP_RESTORE_JOBS = "Legacy Backup Restore Jobs"