# atlas.model.aws_cloud_provider_container.AWSCloudProviderContainer

Collection of settings that configures the network container for a virtual private connection on Amazon Web Services.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Collection of settings that configures the network container for a virtual private connection on Amazon Web Services. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**regionName** | str,  | str,  | Geographic area that Amazon Web Services (AWS) defines to which MongoDB Cloud deployed this network peering container. | must be one of ["US_EAST_1", "US_EAST_2", "US_WEST_1", "US_WEST_2", "CA_CENTRAL_1", "EU_NORTH_1", "EU_WEST_1", "EU_WEST_2", "EU_WEST_3", "EU_CENTRAL_1", "SA_EAST_1", "AP_EAST_1", "AP_SOUTHEAST_2", "AP_SOUTHEAST_3", "AP_NORTHEAST_1", "AP_NORTHEAST_2", "AP_NORTHEAST_3", "AP_SOUTHEAST_1", "AP_SOUTH_1", "CN_NORTH_1", "CN_NORTHWEST_1", "ME_SOUTH_1", "AF_SOUTH_1", "EU_SOUTH_1", "GLOBAL", "US_GOV_WEST_1", "US_GOV_EAST_1", ] 
**atlasCidrBlock** | str,  | str,  | IP addresses expressed in Classless Inter-Domain Routing (CIDR) notation that MongoDB Cloud uses for the network peering containers in your project. MongoDB Cloud assigns all of the project&#x27;s clusters deployed to this cloud provider an IP address from this range. MongoDB Cloud locks this value if an M10 or greater cluster or a network peering connection exists in this project.  These CIDR blocks must fall within the ranges reserved per RFC 1918. AWS and Azure further limit the block to between the &#x60;/24&#x60; and  &#x60;/21&#x60; ranges.  To modify the CIDR block, the target project cannot have:  - Any M10 or greater clusters - Any other VPC peering connections   You can also create a new project and create a network peering connection to set the desired MongoDB Cloud network peering container CIDR block for that project. MongoDB Cloud limits the number of MongoDB nodes per network peering connection based on the CIDR block and the region selected for the project.   **Example:** A project in an Amazon Web Services (AWS) region supporting three availability zones and an MongoDB CIDR network peering container block of limit of &#x60;/24&#x60; equals 27 three-node replica sets. | [optional] 
**vpcId** | str,  | str,  | Unique string that identifies the MongoDB Cloud VPC on AWS. | [optional] 
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the network peering container. | [optional] 
**providerName** | str,  | str,  | Cloud service provider that serves the requested network peering containers. | [optional] must be one of ["AWS", "GCP", "AZURE", "TENANT", "SERVERLESS", ] 
**provisioned** | bool,  | BoolClass,  | Flag that indicates whether MongoDB Cloud clusters exist in the specified network peering container. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

