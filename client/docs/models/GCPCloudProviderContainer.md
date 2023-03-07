# atlas.model.gcp_cloud_provider_container.GCPCloudProviderContainer

Collection of settings that configures the network container for a virtual private connection on Amazon Web Services.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Collection of settings that configures the network container for a virtual private connection on Amazon Web Services. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**atlasCidrBlock** | str,  | str,  | IP addresses expressed in Classless Inter-Domain Routing (CIDR) notation that MongoDB Cloud uses for the network peering containers in your project. MongoDB Cloud assigns all of the project&#x27;s clusters deployed to this cloud provider an IP address from this range. MongoDB Cloud locks this value if an M10 or greater cluster or a network peering connection exists in this project.  These CIDR blocks must fall within the ranges reserved per RFC 1918. GCP further limits the block to a lower bound of the &#x60;/18&#x60; range.  To modify the CIDR block, the target project cannot have:  - Any M10 or greater clusters - Any other VPC peering connections   You can also create a new project and create a network peering connection to set the desired MongoDB Cloud network peering container CIDR block for that project. MongoDB Cloud limits the number of MongoDB nodes per network peering connection based on the CIDR block and the region selected for the project.   **Example:** A project in an Google Cloud (GCP) region supporting three availability zones and an MongoDB CIDR network peering container block of limit of &#x60;/24&#x60; equals 27 three-node replica sets. | 
**gcpProjectId** | str,  | str,  | Unique string that identifies the GCP project in which MongoDB Cloud clusters in this network peering container exist. The response returns **null** if no clusters exist in this network peering container. | [optional] 
**networkName** | str,  | str,  | Human-readable label that identifies the network in which MongoDB Cloud clusters in this network peering container exist. MongoDB Cloud returns **null** if no clusters exist in this network peering container. | [optional] 
**[regions](#regions)** | list, tuple,  | tuple,  | List of GCP regions to which you want to deploy this MongoDB Cloud network peering container.  In this MongoDB Cloud project, you can deploy clusters only to the GCP regions in this list. To deploy MongoDB Cloud clusters to other GCP regions, create additional projects. | [optional] 
**id** | str,  | str,  | Unique 24-hexadecimal digit string that identifies the network peering container. | [optional] 
**providerName** | str,  | str,  | Cloud service provider that serves the requested network peering containers. | [optional] must be one of ["AWS", "GCP", "AZURE", "TENANT", "SERVERLESS", ] 
**provisioned** | bool,  | BoolClass,  | Flag that indicates whether MongoDB Cloud clusters exist in the specified network peering container. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# regions

List of GCP regions to which you want to deploy this MongoDB Cloud network peering container.  In this MongoDB Cloud project, you can deploy clusters only to the GCP regions in this list. To deploy MongoDB Cloud clusters to other GCP regions, create additional projects.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of GCP regions to which you want to deploy this MongoDB Cloud network peering container.  In this MongoDB Cloud project, you can deploy clusters only to the GCP regions in this list. To deploy MongoDB Cloud clusters to other GCP regions, create additional projects. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  | List of GCP regions to which you want to deploy this MongoDB Cloud network peering container.  In this MongoDB Cloud project, you can deploy clusters only to the GCP regions in this list. To deploy MongoDB Cloud clusters to other GCP regions, create additional projects. | must be one of ["ASIA_EAST_2", "ASIA_NORTHEAST_2", "ASIA_NORTHEAST_3", "ASIA_SOUTH_1", "ASIA_SOUTH_2", "ASIA_SOUTHEAST_2", "AUSTRALIA_SOUTHEAST_1", "AUSTRALIA_SOUTHEAST_2", "CENTRAL_US", "EASTERN_ASIA_PACIFIC", "EASTERN_US", "EUROPE_CENTRAL_2", "EUROPE_NORTH_1", "EUROPE_WEST_2", "EUROPE_WEST_3", "EUROPE_WEST_4", "EUROPE_WEST_6", "NORTH_AMERICA_NORTHEAST_1", "NORTH_AMERICA_NORTHEAST_2", "NORTHEASTERN_ASIA_PACIFIC", "SOUTH_AMERICA_EAST_1", "SOUTH_AMERICA_WEST_1", "SOUTHEASTERN_ASIA_PACIFIC", "US_EAST_4", "US_WEST_2", "US_WEST_3", "US_WEST_4", "WESTERN_EUROPE", "WESTERN_US", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

