from __future__ import annotations

import os
from http import HTTPStatus
from types import TracebackType
from typing import TypeVar

from .api.api.extract import asyncio_detailed as extract_async_detailed
from .api.api.extract import sync_detailed as extract_sync_detailed
from .api.api.fetch import asyncio_detailed as fetch_async_detailed
from .api.api.fetch import sync_detailed as fetch_sync_detailed
from .api.api.raw_fetch import asyncio_detailed as raw_fetch_async_detailed
from .api.api.raw_fetch import sync_detailed as raw_fetch_sync_detailed
from .api.api.raw_search import asyncio_detailed as raw_search_async_detailed
from .api.api.raw_search import sync_detailed as raw_search_sync_detailed
from .api.api.search import asyncio_detailed as search_async_detailed
from .api.api.search import sync_detailed as search_sync_detailed
from .client import AuthenticatedClient
from .models.extract_body import ExtractBody
from .models.extract_body_format import ExtractBodyFormat
from .models.extract_response_200_type_0 import ExtractResponse200Type0
from .models.extract_response_200_type_1 import ExtractResponse200Type1
from .models.fetch_body import FetchBody
from .models.fetch_response_200 import FetchResponse200
from .models.raw_fetch_body import RawFetchBody
from .models.raw_fetch_body_format import RawFetchBodyFormat
from .models.raw_fetch_response_200 import RawFetchResponse200
from .models.raw_search_body import RawSearchBody
from .models.raw_search_body_format import RawSearchBodyFormat
from .models.raw_search_response_200_type_0 import RawSearchResponse200Type0
from .models.raw_search_response_200_type_1 import RawSearchResponse200Type1
from .models.search_body import SearchBody
from .models.search_response_200 import SearchResponse200
from .types import Response

DEFAULT_BASE_URL = "https://api.quercle.dev"
API_KEY_ENV = "QUERCLE_API_KEY"
BASE_URL_ENV = "QUERCLE_BASE_URL"

ExtractResponse = ExtractResponse200Type0 | ExtractResponse200Type1
RawSearchResponse = RawSearchResponse200Type0 | RawSearchResponse200Type1


class QuercleApiError(RuntimeError):
    def __init__(
        self,
        operation: str,
        status_code: int,
        detail: str,
        payload: object | None = None,
    ) -> None:
        super().__init__(f"Quercle API {operation} failed with status {status_code}: {detail}")
        self.operation = operation
        self.status_code = status_code
        self.detail = detail
        self.payload = payload


def _resolve_api_key(api_key: str | None) -> str:
    resolved = api_key or os.getenv(API_KEY_ENV)
    if not resolved:
        raise ValueError("Missing API key. Pass api_key or set QUERCLE_API_KEY.")
    return resolved


def _resolve_base_url(base_url: str | None) -> str:
    return base_url or os.getenv(BASE_URL_ENV) or DEFAULT_BASE_URL


def _build_client(
    api_key: str | None,
    base_url: str | None,
) -> AuthenticatedClient:
    return AuthenticatedClient(
        base_url=_resolve_base_url(base_url),  # ty: ignore[unknown-argument]
        token=_resolve_api_key(api_key),  # ty: ignore[unknown-argument]
    )


def _extract_detail(parsed: object | None, content: bytes) -> str:
    if parsed is not None:
        detail_attr = getattr(parsed, "detail", None)
        if isinstance(detail_attr, str) and detail_attr:
            return detail_attr

    decoded = content.decode("utf-8", errors="replace").strip()
    return decoded or "Request failed"


TParsed = TypeVar("TParsed")


def _ensure_ok(operation: str, response: Response[TParsed]) -> TParsed:
    if response.status_code != HTTPStatus.OK:
        detail = _extract_detail(response.parsed, response.content)
        raise QuercleApiError(operation, int(response.status_code), detail, response.parsed)

    if response.parsed is None:
        raise QuercleApiError(operation, int(response.status_code), "Empty response payload", None)

    return response.parsed


class QuercleClient:
    def __init__(
        self,
        api_key: str | None = None,
        *,
        base_url: str | None = None,
        client: AuthenticatedClient | None = None,
    ) -> None:
        self._client = client or _build_client(api_key, base_url)

    @property
    def client(self) -> AuthenticatedClient:
        return self._client

    def close(self) -> None:
        self._client.get_httpx_client().close()

    def __enter__(self) -> QuercleClient:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        self.close()

    def fetch(self, url: str, prompt: str) -> FetchResponse200:
        body = FetchBody.from_dict({"url": url, "prompt": prompt})
        response = fetch_sync_detailed(client=self._client, body=body)
        parsed = _ensure_ok("fetch", response)
        if isinstance(parsed, FetchResponse200):
            return parsed
        raise QuercleApiError("fetch", int(response.status_code), "Unexpected response payload", parsed)

    def search(
        self,
        query: str,
        *,
        allowed_domains: list[str] | None = None,
        blocked_domains: list[str] | None = None,
    ) -> SearchResponse200:
        body_payload: dict[str, object] = {"query": query}
        if allowed_domains is not None:
            body_payload["allowed_domains"] = allowed_domains
        if blocked_domains is not None:
            body_payload["blocked_domains"] = blocked_domains

        response = search_sync_detailed(client=self._client, body=SearchBody.from_dict(body_payload))
        parsed = _ensure_ok("search", response)
        if isinstance(parsed, SearchResponse200):
            return parsed
        raise QuercleApiError("search", int(response.status_code), "Unexpected response payload", parsed)

    def raw_fetch(
        self,
        url: str,
        *,
        format: RawFetchBodyFormat | None = None,
        use_safeguard: bool | None = None,
    ) -> RawFetchResponse200:
        body_payload: dict[str, object] = {"url": url}
        if format is not None:
            body_payload["format"] = format
        if use_safeguard is not None:
            body_payload["use_safeguard"] = use_safeguard

        response = raw_fetch_sync_detailed(client=self._client, body=RawFetchBody.from_dict(body_payload))
        parsed = _ensure_ok("raw_fetch", response)
        if isinstance(parsed, RawFetchResponse200):
            return parsed
        raise QuercleApiError("raw_fetch", int(response.status_code), "Unexpected response payload", parsed)

    def raw_search(
        self,
        query: str,
        *,
        format: RawSearchBodyFormat | None = None,
        use_safeguard: bool | None = None,
    ) -> RawSearchResponse:
        body_payload: dict[str, object] = {"query": query}
        if format is not None:
            body_payload["format"] = format
        if use_safeguard is not None:
            body_payload["use_safeguard"] = use_safeguard

        response = raw_search_sync_detailed(client=self._client, body=RawSearchBody.from_dict(body_payload))
        parsed = _ensure_ok("raw_search", response)
        if isinstance(parsed, (RawSearchResponse200Type0, RawSearchResponse200Type1)):
            return parsed
        raise QuercleApiError("raw_search", int(response.status_code), "Unexpected response payload", parsed)

    def extract(
        self,
        url: str,
        query: str,
        *,
        format: ExtractBodyFormat | None = None,
        use_safeguard: bool | None = None,
    ) -> ExtractResponse:
        body_payload: dict[str, object] = {"url": url, "query": query}
        if format is not None:
            body_payload["format"] = format
        if use_safeguard is not None:
            body_payload["use_safeguard"] = use_safeguard

        response = extract_sync_detailed(client=self._client, body=ExtractBody.from_dict(body_payload))
        parsed = _ensure_ok("extract", response)
        if isinstance(parsed, (ExtractResponse200Type0, ExtractResponse200Type1)):
            return parsed
        raise QuercleApiError("extract", int(response.status_code), "Unexpected response payload", parsed)


class AsyncQuercleClient:
    def __init__(
        self,
        api_key: str | None = None,
        *,
        base_url: str | None = None,
        client: AuthenticatedClient | None = None,
    ) -> None:
        self._client = client or _build_client(api_key, base_url)

    @property
    def client(self) -> AuthenticatedClient:
        return self._client

    async def aclose(self) -> None:
        await self._client.get_async_httpx_client().aclose()

    async def __aenter__(self) -> AsyncQuercleClient:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.aclose()

    async def fetch(self, url: str, prompt: str) -> FetchResponse200:
        body = FetchBody.from_dict({"url": url, "prompt": prompt})
        response = await fetch_async_detailed(client=self._client, body=body)
        parsed = _ensure_ok("fetch", response)
        if isinstance(parsed, FetchResponse200):
            return parsed
        raise QuercleApiError("fetch", int(response.status_code), "Unexpected response payload", parsed)

    async def search(
        self,
        query: str,
        *,
        allowed_domains: list[str] | None = None,
        blocked_domains: list[str] | None = None,
    ) -> SearchResponse200:
        body_payload: dict[str, object] = {"query": query}
        if allowed_domains is not None:
            body_payload["allowed_domains"] = allowed_domains
        if blocked_domains is not None:
            body_payload["blocked_domains"] = blocked_domains

        response = await search_async_detailed(client=self._client, body=SearchBody.from_dict(body_payload))
        parsed = _ensure_ok("search", response)
        if isinstance(parsed, SearchResponse200):
            return parsed
        raise QuercleApiError("search", int(response.status_code), "Unexpected response payload", parsed)

    async def raw_fetch(
        self,
        url: str,
        *,
        format: RawFetchBodyFormat | None = None,
        use_safeguard: bool | None = None,
    ) -> RawFetchResponse200:
        body_payload: dict[str, object] = {"url": url}
        if format is not None:
            body_payload["format"] = format
        if use_safeguard is not None:
            body_payload["use_safeguard"] = use_safeguard

        response = await raw_fetch_async_detailed(client=self._client, body=RawFetchBody.from_dict(body_payload))
        parsed = _ensure_ok("raw_fetch", response)
        if isinstance(parsed, RawFetchResponse200):
            return parsed
        raise QuercleApiError("raw_fetch", int(response.status_code), "Unexpected response payload", parsed)

    async def raw_search(
        self,
        query: str,
        *,
        format: RawSearchBodyFormat | None = None,
        use_safeguard: bool | None = None,
    ) -> RawSearchResponse:
        body_payload: dict[str, object] = {"query": query}
        if format is not None:
            body_payload["format"] = format
        if use_safeguard is not None:
            body_payload["use_safeguard"] = use_safeguard

        response = await raw_search_async_detailed(client=self._client, body=RawSearchBody.from_dict(body_payload))
        parsed = _ensure_ok("raw_search", response)
        if isinstance(parsed, (RawSearchResponse200Type0, RawSearchResponse200Type1)):
            return parsed
        raise QuercleApiError("raw_search", int(response.status_code), "Unexpected response payload", parsed)

    async def extract(
        self,
        url: str,
        query: str,
        *,
        format: ExtractBodyFormat | None = None,
        use_safeguard: bool | None = None,
    ) -> ExtractResponse:
        body_payload: dict[str, object] = {"url": url, "query": query}
        if format is not None:
            body_payload["format"] = format
        if use_safeguard is not None:
            body_payload["use_safeguard"] = use_safeguard

        response = await extract_async_detailed(client=self._client, body=ExtractBody.from_dict(body_payload))
        parsed = _ensure_ok("extract", response)
        if isinstance(parsed, (ExtractResponse200Type0, ExtractResponse200Type1)):
            return parsed
        raise QuercleApiError("extract", int(response.status_code), "Unexpected response payload", parsed)
