# atlas.model.api_line_item_view.ApiLineItemView

One service included in this invoice.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | One service included in this invoice. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**clusterName** | str,  | str,  | Human-readable label that identifies the cluster that incurred the charge. | [optional] 
**created** | str, datetime,  | str,  | Date and time when MongoDB Cloud created this line item. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**discountCents** | decimal.Decimal, int,  | decimal.Decimal,  | Sum by which MongoDB discounted this line item. MongoDB Cloud expresses this value in cents (100ths of one US Dollar). The resource returns this parameter when a discount applies. | [optional] value must be a 64 bit integer
**endDate** | str, datetime,  | str,  | Date and time when when MongoDB Cloud finished charging for this line item. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**groupId** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the project associated to this line item. | [optional] 
**groupName** | str,  | str,  | Human-readable label that identifies the project. | [optional] 
**note** | str,  | str,  | Comment that applies to this line item. | [optional] 
**percentDiscount** | decimal.Decimal, int, float,  | decimal.Decimal,  | Percentage by which MongoDB discounted this line item. The resource returns this parameter when a discount applies. | [optional] value must be a 32 bit float
**quantity** | decimal.Decimal, int, float,  | decimal.Decimal,  | Number of units included for the line item. These can be expressions of storage (GB), time (hours), or other units. | [optional] value must be a 64 bit float
**sku** | str,  | str,  | Human-readable description of the service that this line item provided. This Stock Keeping Unit (SKU) could be the instance type, a support charge, advanced security, or another service. | [optional] must be one of ["CLASSIC_BACKUP_OPLOG", "CLASSIC_BACKUP_STORAGE", "CLASSIC_BACKUP_SNAPSHOT_CREATE", "CLASSIC_BACKUP_DAILY_MINIMUM", "CLASSIC_BACKUP_FREE_TIER", "CLASSIC_COUPON", "BACKUP_STORAGE_FREE_TIER", "BACKUP_STORAGE", "FLEX_CONSULTING", "CLOUD_MANAGER_CLASSIC", "CLOUD_MANAGER_BASIC_FREE_TIER", "CLOUD_MANAGER_BASIC", "CLOUD_MANAGER_PREMIUM", "CLOUD_MANAGER_FREE_TIER", "CLOUD_MANAGER_STANDARD_FREE_TIER", "CLOUD_MANAGER_STANDARD_ANNUAL", "CLOUD_MANAGER_STANDARD", "CLOUD_MANAGER_FREE_TRIAL", "ATLAS_INSTANCE_M0", "ATLAS_INSTANCE_M2", "ATLAS_INSTANCE_M5", "ATLAS_AWS_INSTANCE_M10", "ATLAS_AWS_INSTANCE_M20", "ATLAS_AWS_INSTANCE_M30", "ATLAS_AWS_INSTANCE_M40", "ATLAS_AWS_INSTANCE_M50", "ATLAS_AWS_INSTANCE_M60", "ATLAS_AWS_INSTANCE_M80", "ATLAS_AWS_INSTANCE_M100", "ATLAS_AWS_INSTANCE_M140", "ATLAS_AWS_INSTANCE_M200", "ATLAS_AWS_INSTANCE_M300", "ATLAS_AWS_INSTANCE_M40_LOW_CPU", "ATLAS_AWS_INSTANCE_M50_LOW_CPU", "ATLAS_AWS_INSTANCE_M60_LOW_CPU", "ATLAS_AWS_INSTANCE_M80_LOW_CPU", "ATLAS_AWS_INSTANCE_M200_LOW_CPU", "ATLAS_AWS_INSTANCE_M300_LOW_CPU", "ATLAS_AWS_INSTANCE_M400_LOW_CPU", "ATLAS_AWS_INSTANCE_M700_LOW_CPU", "ATLAS_AWS_INSTANCE_M40_NVME", "ATLAS_AWS_INSTANCE_M50_NVME", "ATLAS_AWS_INSTANCE_M60_NVME", "ATLAS_AWS_INSTANCE_M80_NVME", "ATLAS_AWS_INSTANCE_M200_NVME", "ATLAS_AWS_INSTANCE_M400_NVME", "ATLAS_AWS_INSTANCE_M10_PAUSED", "ATLAS_AWS_INSTANCE_M20_PAUSED", "ATLAS_AWS_INSTANCE_M30_PAUSED", "ATLAS_AWS_INSTANCE_M40_PAUSED", "ATLAS_AWS_INSTANCE_M50_PAUSED", "ATLAS_AWS_INSTANCE_M60_PAUSED", "ATLAS_AWS_INSTANCE_M80_PAUSED", "ATLAS_AWS_INSTANCE_M100_PAUSED", "ATLAS_AWS_INSTANCE_M140_PAUSED", "ATLAS_AWS_INSTANCE_M200_PAUSED", "ATLAS_AWS_INSTANCE_M300_PAUSED", "ATLAS_AWS_INSTANCE_M40_LOW_CPU_PAUSED", "ATLAS_AWS_INSTANCE_M50_LOW_CPU_PAUSED", "ATLAS_AWS_INSTANCE_M60_LOW_CPU_PAUSED", "ATLAS_AWS_INSTANCE_M80_LOW_CPU_PAUSED", "ATLAS_AWS_INSTANCE_M200_LOW_CPU_PAUSED", "ATLAS_AWS_INSTANCE_M300_LOW_CPU_PAUSED", "ATLAS_AWS_INSTANCE_M400_LOW_CPU_PAUSED", "ATLAS_AWS_INSTANCE_M700_LOW_CPU_PAUSED", "ATLAS_AWS_STORAGE_PROVISIONED", "ATLAS_AWS_STORAGE_STANDARD", "ATLAS_AWS_STORAGE_STANDARD_GP3", "ATLAS_AWS_STORAGE_IOPS", "ATLAS_AWS_DATA_TRANSFER_SAME_REGION", "ATLAS_AWS_DATA_TRANSFER_DIFFERENT_REGION", "ATLAS_AWS_DATA_TRANSFER_INTERNET", "ATLAS_AWS_BACKUP_SNAPSHOT_STORAGE", "ATLAS_AWS_BACKUP_DOWNLOAD_VM", "ATLAS_AWS_BACKUP_DOWNLOAD_VM_STORAGE", "ATLAS_AWS_BACKUP_DOWNLOAD_VM_STORAGE_IOPS", "ATLAS_AWS_PRIVATE_ENDPOINT", "ATLAS_AWS_PRIVATE_ENDPOINT_CAPACITY_UNITS", "ATLAS_GCP_INSTANCE_M10", "ATLAS_GCP_INSTANCE_M20", "ATLAS_GCP_INSTANCE_M30", "ATLAS_GCP_INSTANCE_M40", "ATLAS_GCP_INSTANCE_M50", "ATLAS_GCP_INSTANCE_M60", "ATLAS_GCP_INSTANCE_M80", "ATLAS_GCP_INSTANCE_M140", "ATLAS_GCP_INSTANCE_M200", "ATLAS_GCP_INSTANCE_M250", "ATLAS_GCP_INSTANCE_M300", "ATLAS_GCP_INSTANCE_M400", "ATLAS_GCP_INSTANCE_M40_LOW_CPU", "ATLAS_GCP_INSTANCE_M50_LOW_CPU", "ATLAS_GCP_INSTANCE_M60_LOW_CPU", "ATLAS_GCP_INSTANCE_M80_LOW_CPU", "ATLAS_GCP_INSTANCE_M200_LOW_CPU", "ATLAS_GCP_INSTANCE_M300_LOW_CPU", "ATLAS_GCP_INSTANCE_M400_LOW_CPU", "ATLAS_GCP_INSTANCE_M600_LOW_CPU", "ATLAS_GCP_INSTANCE_M10_PAUSED", "ATLAS_GCP_INSTANCE_M20_PAUSED", "ATLAS_GCP_INSTANCE_M30_PAUSED", "ATLAS_GCP_INSTANCE_M40_PAUSED", "ATLAS_GCP_INSTANCE_M50_PAUSED", "ATLAS_GCP_INSTANCE_M60_PAUSED", "ATLAS_GCP_INSTANCE_M80_PAUSED", "ATLAS_GCP_INSTANCE_M140_PAUSED", "ATLAS_GCP_INSTANCE_M200_PAUSED", "ATLAS_GCP_INSTANCE_M250_PAUSED", "ATLAS_GCP_INSTANCE_M300_PAUSED", "ATLAS_GCP_INSTANCE_M400_PAUSED", "ATLAS_GCP_INSTANCE_M40_LOW_CPU_PAUSED", "ATLAS_GCP_INSTANCE_M50_LOW_CPU_PAUSED", "ATLAS_GCP_INSTANCE_M60_LOW_CPU_PAUSED", "ATLAS_GCP_INSTANCE_M80_LOW_CPU_PAUSED", "ATLAS_GCP_INSTANCE_M200_LOW_CPU_PAUSED", "ATLAS_GCP_INSTANCE_M300_LOW_CPU_PAUSED", "ATLAS_GCP_INSTANCE_M400_LOW_CPU_PAUSED", "ATLAS_GCP_INSTANCE_M600_LOW_CPU_PAUSED", "ATLAS_GCP_STORAGE_SSD", "ATLAS_GCP_DATA_TRANSFER_INTERNET", "ATLAS_GCP_DATA_TRANSFER_INTER_CONNECT", "ATLAS_GCP_DATA_TRANSFER_INTER_ZONE", "ATLAS_GCP_DATA_TRANSFER_INTER_REGION", "ATLAS_GCP_DATA_TRANSFER_GOOGLE", "ATLAS_GCP_BACKUP_SNAPSHOT_STORAGE", "ATLAS_GCP_BACKUP_DOWNLOAD_VM", "ATLAS_GCP_BACKUP_DOWNLOAD_VM_STORAGE", "ATLAS_GCP_PRIVATE_ENDPOINT", "ATLAS_GCP_PRIVATE_ENDPOINT_CAPACITY_UNITS", "ATLAS_AZURE_INSTANCE_M10", "ATLAS_AZURE_INSTANCE_M20", "ATLAS_AZURE_INSTANCE_M30", "ATLAS_AZURE_INSTANCE_M40", "ATLAS_AZURE_INSTANCE_M50", "ATLAS_AZURE_INSTANCE_M60", "ATLAS_AZURE_INSTANCE_M80", "ATLAS_AZURE_INSTANCE_M90", "ATLAS_AZURE_INSTANCE_M200", "ATLAS_AZURE_INSTANCE_R40", "ATLAS_AZURE_INSTANCE_R50", "ATLAS_AZURE_INSTANCE_R60", "ATLAS_AZURE_INSTANCE_R80", "ATLAS_AZURE_INSTANCE_R200", "ATLAS_AZURE_INSTANCE_R300", "ATLAS_AZURE_INSTANCE_R400", "ATLAS_AZURE_INSTANCE_M60_NVME", "ATLAS_AZURE_INSTANCE_M80_NVME", "ATLAS_AZURE_INSTANCE_M200_NVME", "ATLAS_AZURE_INSTANCE_M300_NVME", "ATLAS_AZURE_INSTANCE_M400_NVME", "ATLAS_AZURE_INSTANCE_M600_NVME", "ATLAS_AZURE_INSTANCE_M10_PAUSED", "ATLAS_AZURE_INSTANCE_M20_PAUSED", "ATLAS_AZURE_INSTANCE_M30_PAUSED", "ATLAS_AZURE_INSTANCE_M40_PAUSED", "ATLAS_AZURE_INSTANCE_M50_PAUSED", "ATLAS_AZURE_INSTANCE_M60_PAUSED", "ATLAS_AZURE_INSTANCE_M80_PAUSED", "ATLAS_AZURE_INSTANCE_M90_PAUSED", "ATLAS_AZURE_INSTANCE_M200_PAUSED", "ATLAS_AZURE_INSTANCE_R40_PAUSED", "ATLAS_AZURE_INSTANCE_R50_PAUSED", "ATLAS_AZURE_INSTANCE_R60_PAUSED", "ATLAS_AZURE_INSTANCE_R80_PAUSED", "ATLAS_AZURE_INSTANCE_R200_PAUSED", "ATLAS_AZURE_INSTANCE_R300_PAUSED", "ATLAS_AZURE_INSTANCE_R400_PAUSED", "ATLAS_AZURE_STORAGE_P2", "ATLAS_AZURE_STORAGE_P3", "ATLAS_AZURE_STORAGE_P4", "ATLAS_AZURE_STORAGE_P6", "ATLAS_AZURE_STORAGE_P10", "ATLAS_AZURE_STORAGE_P15", "ATLAS_AZURE_STORAGE_P20", "ATLAS_AZURE_STORAGE_P30", "ATLAS_AZURE_STORAGE_P40", "ATLAS_AZURE_STORAGE_P50", "ATLAS_AZURE_DATA_TRANSFER", "ATLAS_AZURE_DATA_TRANSFER_REGIONAL_VNET_IN", "ATLAS_AZURE_DATA_TRANSFER_REGIONAL_VNET_OUT", "ATLAS_AZURE_DATA_TRANSFER_GLOBAL_VNET_IN", "ATLAS_AZURE_DATA_TRANSFER_GLOBAL_VNET_OUT", "ATLAS_AZURE_DATA_TRANSFER_AVAILABILITY_ZONE_IN", "ATLAS_AZURE_DATA_TRANSFER_AVAILABILITY_ZONE_OUT", "ATLAS_AZURE_BACKUP_SNAPSHOT_STORAGE", "ATLAS_AZURE_BACKUP_DOWNLOAD_VM", "ATLAS_AZURE_BACKUP_DOWNLOAD_VM_STORAGE_P2", "ATLAS_AZURE_BACKUP_DOWNLOAD_VM_STORAGE_P3", "ATLAS_AZURE_BACKUP_DOWNLOAD_VM_STORAGE_P4", "ATLAS_AZURE_BACKUP_DOWNLOAD_VM_STORAGE_P6", "ATLAS_AZURE_BACKUP_DOWNLOAD_VM_STORAGE_P10", "ATLAS_AZURE_BACKUP_DOWNLOAD_VM_STORAGE_P15", "ATLAS_AZURE_BACKUP_DOWNLOAD_VM_STORAGE_P20", "ATLAS_AZURE_BACKUP_DOWNLOAD_VM_STORAGE_P30", "ATLAS_AZURE_BACKUP_DOWNLOAD_VM_STORAGE_P40", "ATLAS_AZURE_BACKUP_DOWNLOAD_VM_STORAGE_P50", "ATLAS_BI_CONNECTOR", "ATLAS_ADVANCED_SECURITY", "ATLAS_ENTERPRISE_AUDITING", "ATLAS_FREE_SUPPORT", "ATLAS_SUPPORT", "STITCH_DATA_DOWNLOADED_FREE_TIER", "STITCH_DATA_DOWNLOADED", "STITCH_COMPUTE_FREE_TIER", "STITCH_COMPUTE", "CREDIT", "MINIMUM_CHARGE", "CHARTS_DATA_DOWNLOADED_FREE_TIER", "CHARTS_DATA_DOWNLOADED", "ATLAS_DATA_LAKE_AWS_DATA_RETURNED_SAME_REGION", "ATLAS_DATA_LAKE_AWS_DATA_RETURNED_DIFFERENT_REGION", "ATLAS_DATA_LAKE_AWS_DATA_RETURNED_INTERNET", "ATLAS_DATA_LAKE_AWS_DATA_SCANNED", "ATLAS_DATA_LAKE_AWS_DATA_TRANSFERRED_FROM_DIFFERENT_REGION", "ATLAS_NDS_AWS_DATA_LAKE_STORAGE_ACCESS", "ATLAS_NDS_AWS_DATA_LAKE_STORAGE", "ATLAS_NDS_AWS_OBJECT_STORAGE_ACCESS", "ATLAS_ARCHIVE_ACCESS_PARTITION_LOCATE", "ATLAS_NDS_AWS_PIT_RESTORE_STORAGE_FREE_TIER", "ATLAS_NDS_AWS_PIT_RESTORE_STORAGE", "ATLAS_NDS_GCP_PIT_RESTORE_STORAGE_FREE_TIER", "ATLAS_NDS_GCP_PIT_RESTORE_STORAGE", "ATLAS_NDS_AZURE_PIT_RESTORE_STORAGE_FREE_TIER", "ATLAS_NDS_AZURE_PIT_RESTORE_STORAGE", "ATLAS_NDS_AZURE_PRIVATE_ENDPOINT_CAPACITY_UNITS", "ATLAS_NDS_AWS_OBJECT_STORAGE", "ATLAS_NDS_AWS_SNAPSHOT_EXPORT_UPLOAD", "ATLAS_NDS_AZURE_SNAPSHOT_EXPORT_VM", "ATLAS_NDS_AZURE_SNAPSHOT_EXPORT_VM_M40", "ATLAS_NDS_AZURE_SNAPSHOT_EXPORT_VM_M50", "ATLAS_NDS_AZURE_SNAPSHOT_EXPORT_VM_M60", "ATLAS_NDS_AZURE_SNAPSHOT_EXPORT_VM_STORAGE_P2", "ATLAS_NDS_AZURE_SNAPSHOT_EXPORT_VM_STORAGE_P3", "ATLAS_NDS_AZURE_SNAPSHOT_EXPORT_VM_STORAGE_P4", "ATLAS_NDS_AZURE_SNAPSHOT_EXPORT_VM_STORAGE_P6", "ATLAS_NDS_AZURE_SNAPSHOT_EXPORT_VM_STORAGE_P10", "ATLAS_NDS_AZURE_SNAPSHOT_EXPORT_VM_STORAGE_P15", "ATLAS_NDS_AZURE_SNAPSHOT_EXPORT_VM_STORAGE_P20", "ATLAS_NDS_AZURE_SNAPSHOT_EXPORT_VM_STORAGE_P30", "ATLAS_NDS_AZURE_SNAPSHOT_EXPORT_VM_STORAGE_P40", "ATLAS_NDS_AZURE_SNAPSHOT_EXPORT_VM_STORAGE_P50", "ATLAS_NDS_AWS_SNAPSHOT_EXPORT_VM", "ATLAS_NDS_AWS_SNAPSHOT_EXPORT_VM_M40", "ATLAS_NDS_AWS_SNAPSHOT_EXPORT_VM_M50", "ATLAS_NDS_AWS_SNAPSHOT_EXPORT_VM_M60", "ATLAS_NDS_AWS_SNAPSHOT_EXPORT_VM_STORAGE", "ATLAS_NDS_AWS_SNAPSHOT_EXPORT_VM_STORAGE_IOPS", "ATLAS_NDS_GCP_SNAPSHOT_EXPORT_VM", "ATLAS_NDS_GCP_SNAPSHOT_EXPORT_VM_M40", "ATLAS_NDS_GCP_SNAPSHOT_EXPORT_VM_M50", "ATLAS_NDS_GCP_SNAPSHOT_EXPORT_VM_M60", "ATLAS_NDS_GCP_SNAPSHOT_EXPORT_VM_STORAGE", "ATLAS_NDS_AWS_SERVERLESS_RPU", "ATLAS_NDS_AWS_SERVERLESS_WPU", "ATLAS_NDS_AWS_SERVERLESS_STORAGE", "ATLAS_NDS_AWS_SERVERLESS_CONTINUOUS_BACKUP", "ATLAS_NDS_AWS_SERVERLESS_BACKUP_RESTORE_VM", "ATLAS_NDS_AWS_SERVERLESS_DATA_TRANSFER_PREVIEW", "ATLAS_NDS_AWS_SERVERLESS_DATA_TRANSFER", "ATLAS_NDS_AWS_SERVERLESS_DATA_TRANSFER_REGIONAL", "ATLAS_NDS_AWS_SERVERLESS_DATA_TRANSFER_CROSS_REGION", "ATLAS_NDS_AWS_SERVERLESS_DATA_TRANSFER_INTERNET", "ATLAS_NDS_GCP_SERVERLESS_RPU", "ATLAS_NDS_GCP_SERVERLESS_WPU", "ATLAS_NDS_GCP_SERVERLESS_STORAGE", "ATLAS_NDS_GCP_SERVERLESS_CONTINUOUS_BACKUP", "ATLAS_NDS_GCP_SERVERLESS_BACKUP_RESTORE_VM", "ATLAS_NDS_GCP_SERVERLESS_DATA_TRANSFER_PREVIEW", "ATLAS_NDS_GCP_SERVERLESS_DATA_TRANSFER", "ATLAS_NDS_GCP_SERVERLESS_DATA_TRANSFER_REGIONAL", "ATLAS_NDS_GCP_SERVERLESS_DATA_TRANSFER_CROSS_REGION", "ATLAS_NDS_GCP_SERVERLESS_DATA_TRANSFER_INTERNET", "ATLAS_NDS_AZURE_SERVERLESS_RPU", "ATLAS_NDS_AZURE_SERVERLESS_WPU", "ATLAS_NDS_AZURE_SERVERLESS_STORAGE", "ATLAS_NDS_AZURE_SERVERLESS_CONTINUOUS_BACKUP", "ATLAS_NDS_AZURE_SERVERLESS_BACKUP_RESTORE_VM", "ATLAS_NDS_AZURE_SERVERLESS_DATA_TRANSFER_PREVIEW", "ATLAS_NDS_AZURE_SERVERLESS_DATA_TRANSFER", "ATLAS_NDS_AZURE_SERVERLESS_DATA_TRANSFER_REGIONAL", "ATLAS_NDS_AZURE_SERVERLESS_DATA_TRANSFER_CROSS_REGION", "ATLAS_NDS_AZURE_SERVERLESS_DATA_TRANSFER_INTERNET", "REALM_APP_REQUESTS_FREE_TIER", "REALM_APP_REQUESTS", "REALM_APP_COMPUTE_FREE_TIER", "REALM_APP_COMPUTE", "REALM_APP_SYNC_FREE_TIER", "REALM_APP_SYNC", "REALM_APP_DATA_TRANSFER_FREE_TIER", "REALM_APP_DATA_TRANSFER", "METERING_E2E_BILLING", "DATA_LAKE_AWS_DATA_SCANNED_TEST_PRICE_CHANGE", "ATLAS_NDS_AWS_INSTANCE_R40_TEST_PRICE_CHANGE", "ATLAS_NDS_AZURE_INSTANCE_M30_TEST_PRICE_CHANGE", "ATLAS_NDS_AWS_PIT_RESTORE_STORAGE_TEST_PRICE_CHANGE", "ATLAS_NDS_GCP_STORAGE_SSD_TEST_PRICE_CHANGE", "ATLAS_NDS_GCP_DATA_TRANSFER_INTERNET_TEST_PRICE_CHANGE", "BACKUP_STORAGE_TEST_PRICE_CHANGE", "GCP_SNAPSHOT_COPY_DISK", ] 
**startDate** | str, datetime,  | str,  | Date and time when MongoDB Cloud began charging for this line item. This parameter expresses its value in the ISO 8601 timestamp format in UTC. | [optional] value must conform to RFC-3339 date-time
**stitchAppName** | str,  | str,  | Human-readable label that identifies the Atlas App Services application associated with this line item. | [optional] 
**tierLowerBound** | decimal.Decimal, int, float,  | decimal.Decimal,  | Lower bound for usage amount range in current SKU tier.   **NOTE**: **lineItems[n].tierLowerBound** appears only if your **lineItems[n].sku** is tiered. | [optional] value must be a 64 bit float
**tierUpperBound** | decimal.Decimal, int, float,  | decimal.Decimal,  | Upper bound for usage amount range in current SKU tier.   **NOTE**: **lineItems[n].tierUpperBound** appears only if your **lineItems[n].sku** is tiered. | [optional] value must be a 64 bit float
**totalPriceCents** | decimal.Decimal, int,  | decimal.Decimal,  | Sum of the cost set for this line item. MongoDB Cloud expresses this value in cents (100ths of one US Dollar) and calculates this value as **unitPriceDollars** × **quantity** × 100. | [optional] value must be a 64 bit integer
**unit** | str,  | str,  | Element used to express what **quantity** this line item measures. This value can be elements of time, storage capacity, and the like. | [optional] 
**unitPriceDollars** | decimal.Decimal, int, float,  | decimal.Decimal,  | Value per **unit** for this line item expressed in US Dollars. | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
