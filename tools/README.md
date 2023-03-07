# SDK OpenAPI Tools

Folder contains scripts, generators and other files required to generate Golang client

## Running

### Fetching OpenAPI file

```
make fetch_openapi
```

### Generating Go SDK

```
make generate_client
```

### OpenAPI generator

OpenAPI generator version is set in `openapitools.json` file.

### Transformer

Follow [transformer readme](./transformer/README.md) for more information


#### Contributing

We need to regenerate our SDK if changes in tools will affect the generated clients.
PR based checks will verify if changes are up to date.

```
make clean_and_generate
```
