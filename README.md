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
import os

from quercle import AuthenticatedClient
from quercle.api.api.post_v1_search import sync as post_v1_search
from quercle.models.post_v1_search_body import PostV1SearchBody

client = AuthenticatedClient(base_url="https://api.quercle.dev", token=os.environ["QUERCLE_API_KEY"])
response = post_v1_search(client=client, body=PostV1SearchBody(query="latest bun release notes"))

if response is not None:
    print(response.result)
```
