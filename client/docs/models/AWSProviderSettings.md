# atlas.model.aws_provider_settings.AWSProviderSettings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**providerName** | str,  | str,  |  | 
**autoScaling** | [**AWSAutoScaling**](AWSAutoScaling.md) | [**AWSAutoScaling**](AWSAutoScaling.md) |  | [optional] 
**diskIOPS** | decimal.Decimal, int,  | decimal.Decimal,  | Maximum Disk Input/Output Operations per Second (IOPS) that the database host can perform. | [optional] value must be a 32 bit integer
**encryptEBSVolume** | bool,  | BoolClass,  | Flag that indicates whether the Amazon Elastic Block Store (EBS) encryption feature encrypts the host&#x27;s root volume for both data at rest within the volume and for data moving between the volume and the cluster. Clusters always have this setting enabled. | [optional] if omitted the server will use the default value of True
**instanceSizeName** | str,  | str,  | Cluster tier, with a default storage and memory capacity, that applies to all the data-bearing hosts in your cluster. | [optional] must be one of ["M10", "M20", "M30", "M40", "M50", "M60", "M80", "M100", "M140", "M200", "M300", "R40", "R50", "R60", "R80", "R200", "R300", "R400", "R700", "M40_NVME", "M50_NVME", "M60_NVME", "M80_NVME", "M200_NVME", "M400_NVME", ] 
**regionName** | str,  | str,  |  Physical location where MongoDB Cloud deploys your AWS-hosted MongoDB cluster nodes. The region you choose can affect network latency for clients accessing your databases. When MongoDB Cloud deploys a dedicated cluster, it checks if a VPC or VPC connection exists for that provider and region. If not, MongoDB Cloud creates them as part of the deployment. MongoDB Cloud assigns the VPC a CIDR block. To limit a new VPC peering connection to one CIDR block and region, create the connection first. Deploy the cluster after the connection starts. | [optional] must be one of ["US_GOV_WEST_1", "US_GOV_EAST_1", "US_EAST_1", "US_EAST_2", "US_WEST_1", "US_WEST_2", "CA_CENTRAL_1", "EU_NORTH_1", "EU_WEST_1", "EU_WEST_2", "EU_WEST_3", "EU_CENTRAL_1", "AP_EAST_1", "AP_NORTHEAST_1", "AP_NORTHEAST_2", "AP_NORTHEAST_3", "AP_SOUTHEAST_1", "AP_SOUTHEAST_2", "AP_SOUTHEAST_3", "AP_SOUTH_1", "SA_EAST_1", "CN_NORTH_1", "CN_NORTHWEST_1", "ME_SOUTH_1", "AF_SOUTH_1", "EU_SOUTH_1", "GLOBAL", ] 
**volumeType** | str,  | str,  | Disk Input/Output Operations per Second (IOPS) setting for Amazon Web Services (AWS) storage that you configure only for abbr title&#x3D;\&quot;Amazon Web Services\&quot;&gt;AWS&lt;/abbr&gt;. Specify whether Disk Input/Output Operations per Second (IOPS) must not exceed the default Input/Output Operations per Second (IOPS) rate for the selected volume size (&#x60;STANDARD&#x60;), or must fall within the allowable Input/Output Operations per Second (IOPS) range for the selected volume size (&#x60;PROVISIONED&#x60;). | [optional] must be one of ["STANDARD", "PROVISIONED", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

