# atlas.model.api_prometheus_view.ApiPrometheusView

Details to integrate one Prometheus account with one MongoDB Cloud project.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Details to integrate one Prometheus account with one MongoDB Cloud project. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**scheme** | str,  | str,  | Security Scheme to apply to HyperText Transfer Protocol (HTTP) traffic between Prometheus and MongoDB Cloud. | must be one of ["http", "https", ] 
**serviceDiscovery** | str,  | str,  | Desired method to discover the Prometheus service. | must be one of ["http", "file", ] 
**enabled** | bool,  | BoolClass,  | Flag that indicates whether someone has activated the Prometheus integration. | 
**username** | str,  | str,  | Human-readable label that identifies your Prometheus incoming webhook. | 
**listenAddress** | str,  | str,  | Combination of IPv4 address and Internet Assigned Numbers Authority (IANA) port or the IANA port alone to which Prometheus binds to ingest MongoDB metrics. | [optional] if omitted the server will use the default value of ":9216"
**password** | str,  | str,  |  | [optional] 
**rateLimitInterval** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 32 bit integer
**tlsPemPath** | str,  | str,  | Root-relative path to the Transport Layer Security (TLS) Privacy Enhanced Mail (PEM) key and certificate file on the host. | [optional] 
**type** | str,  | str,  | Human-readable label that identifies the service to which you want to integrate with MongoDB Cloud. The value must match the third-party service integration type. | [optional] must be one of ["PROMETHEUS", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

