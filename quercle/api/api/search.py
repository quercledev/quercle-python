from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.search_body import SearchBody
from ...models.search_response_200 import SearchResponse200
from ...models.search_response_400 import SearchResponse400
from ...models.search_response_401 import SearchResponse401
from ...models.search_response_402 import SearchResponse402
from ...models.search_response_429 import SearchResponse429
from ...models.search_response_500 import SearchResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SearchBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/search",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    SearchResponse200
    | SearchResponse400
    | SearchResponse401
    | SearchResponse402
    | SearchResponse429
    | SearchResponse500
    | None
):
    if response.status_code == 200:
        response_200 = SearchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = SearchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = SearchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = SearchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 429:
        response_429 = SearchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = SearchResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    SearchResponse200
    | SearchResponse400
    | SearchResponse401
    | SearchResponse402
    | SearchResponse429
    | SearchResponse500
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: SearchBody | Unset = UNSET,
) -> Response[
    SearchResponse200
    | SearchResponse400
    | SearchResponse401
    | SearchResponse402
    | SearchResponse429
    | SearchResponse500
]:
    """Search the web and return an AI-synthesized answer from the retrieved results.

    Args:
        body (SearchBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchResponse200 | SearchResponse400 | SearchResponse401 | SearchResponse402 | SearchResponse429 | SearchResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: SearchBody | Unset = UNSET,
) -> (
    SearchResponse200
    | SearchResponse400
    | SearchResponse401
    | SearchResponse402
    | SearchResponse429
    | SearchResponse500
    | None
):
    """Search the web and return an AI-synthesized answer from the retrieved results.

    Args:
        body (SearchBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchResponse200 | SearchResponse400 | SearchResponse401 | SearchResponse402 | SearchResponse429 | SearchResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: SearchBody | Unset = UNSET,
) -> Response[
    SearchResponse200
    | SearchResponse400
    | SearchResponse401
    | SearchResponse402
    | SearchResponse429
    | SearchResponse500
]:
    """Search the web and return an AI-synthesized answer from the retrieved results.

    Args:
        body (SearchBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SearchResponse200 | SearchResponse400 | SearchResponse401 | SearchResponse402 | SearchResponse429 | SearchResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: SearchBody | Unset = UNSET,
) -> (
    SearchResponse200
    | SearchResponse400
    | SearchResponse401
    | SearchResponse402
    | SearchResponse429
    | SearchResponse500
    | None
):
    """Search the web and return an AI-synthesized answer from the retrieved results.

    Args:
        body (SearchBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SearchResponse200 | SearchResponse400 | SearchResponse401 | SearchResponse402 | SearchResponse429 | SearchResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
