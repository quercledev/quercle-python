# quercle

Python SDK for Quercle API.

## Installation

```bash
uv add quercle
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
