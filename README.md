# quercle

Generated Python SDK for the Quercle API.

- OpenAPI version: 1.0.0
- This repository is synchronized automatically from Quercle API releases.

## Installation

```bash
pip install quercle
```

## Usage

```python
from quercle import QuercleClient

client = QuercleClient(api_key="your_api_key")
response = client.search("latest bun release notes")

print(response.result)
```

## Async Usage

```python
from quercle import AsyncQuercleClient

client = AsyncQuercleClient(api_key="your_api_key")
response = await client.search("latest bun release notes")
print(response.result)
```

## Tool Metadata

```python
from quercle import tool_metadata

print(tool_metadata["search"]["description"])
print(tool_metadata["search"]["parameters"]["query"])
```
