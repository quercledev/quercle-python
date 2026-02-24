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

## Timeouts

```python
response = client.search("latest bun release notes", timeout=20.0)
```

## Async Usage

```python
import asyncio

from quercle import AsyncQuercleClient

async def main() -> None:
    async with AsyncQuercleClient(api_key="your_api_key") as client:
        response = await client.search("latest bun release notes")
        print(response.result)


if __name__ == "__main__":
    asyncio.run(main())
```

## Tool Metadata

```python
from quercle import tool_metadata

print(tool_metadata["search"]["description"])
print(tool_metadata["search"]["parameters"]["query"])
```
