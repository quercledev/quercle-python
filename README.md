# Quercle Python SDK

Official Python SDK for the [Quercle API](https://quercle.dev) - AI-powered web search and fetching.

## Installation

```bash
pip install quercle
```

## Quick Start

```python
from quercle import QuercleClient

# Initialize with API key (or set QUERCLE_API_KEY env var)
client = QuercleClient(api_key="qk_...")

# Fetch and analyze a URL
result = client.fetch(
    url="https://example.com/article",
    prompt="Summarize the main points in bullet points"
)
print(result)

# Search the web
result = client.search("What is TypeScript?")
print(result)
```

## Authentication

Get your API key at [quercle.dev](https://quercle.dev).

```python
# Option 1: Pass API key directly
client = QuercleClient(api_key="qk_...")

# Option 2: Set environment variable
# export QUERCLE_API_KEY=qk_...
client = QuercleClient()
```

## Usage

### Synchronous Client

```python
from quercle import QuercleClient

# Using context manager (recommended)
with QuercleClient() as client:
    # Fetch a URL and analyze content
    result = client.fetch(
        url="https://example.com",
        prompt="Extract the main heading and first paragraph"
    )
    print(result)

    # Search the web
    result = client.search("Python best practices 2024")
    print(result)

    # Search with domain filtering
    result = client.search(
        "machine learning tutorials",
        allowed_domains=["*.edu", "arxiv.org"],
        blocked_domains=["spam.com"]
    )
    print(result)
```

### Asynchronous Client

```python
import asyncio
from quercle import AsyncQuercleClient

async def main():
    async with AsyncQuercleClient() as client:
        # Fetch
        result = await client.fetch(
            url="https://example.com",
            prompt="Summarize this page"
        )
        print(result)

        # Search
        result = await client.search("Latest AI news")
        print(result)

        # Parallel requests
        results = await asyncio.gather(
            client.search("Python tutorials"),
            client.search("TypeScript tutorials"),
        )
        for r in results:
            print(r)

asyncio.run(main())
```

## API Reference

### `QuercleClient` / `AsyncQuercleClient`

#### Constructor

```python
QuercleClient(
    api_key: str | None = None,      # API key (or use QUERCLE_API_KEY env var)
    base_url: str | None = None,     # Custom API base URL
    timeout: float | None = None,    # Request timeout in seconds (default: 120)
)
```

#### Methods

**`fetch(url: str, prompt: str) -> str`**

Fetch a URL and analyze its content with AI.

- `url`: The URL to fetch and analyze
- `prompt`: Instructions for how to analyze the page content
- Returns: AI-processed analysis of the page content

**`search(query: str, *, allowed_domains: list[str] | None = None, blocked_domains: list[str] | None = None) -> str`**

Search the web and get AI-synthesized answers with citations.

- `query`: The search query
- `allowed_domains`: Only include results from these domains (e.g., `["*.edu", "example.com"]`)
- `blocked_domains`: Exclude results from these domains
- Returns: AI-synthesized answer with source citations

## Error Handling

```python
from quercle import QuercleClient, QuercleError
from quercle.exceptions import (
    AuthenticationError,
    InsufficientCreditsError,
    RateLimitError,
    TimeoutError,
)

try:
    client = QuercleClient()
    result = client.search("test query")
except AuthenticationError:
    print("Invalid API key")
except InsufficientCreditsError:
    print("Not enough credits")
except RateLimitError:
    print("Too many requests")
except TimeoutError:
    print("Request timed out")
except QuercleError as e:
    print(f"API error: {e.status_code} - {e.detail}")
```

## Requirements

- Python 3.10+
- httpx

## License

MIT
