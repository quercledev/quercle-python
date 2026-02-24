from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.fetch_body import FetchBody
from ...models.fetch_response_200 import FetchResponse200
from ...models.fetch_response_400 import FetchResponse400
from ...models.fetch_response_401 import FetchResponse401
from ...models.fetch_response_402 import FetchResponse402
from ...models.fetch_response_429 import FetchResponse429
from ...models.fetch_response_500 import FetchResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: FetchBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/fetch",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    FetchResponse200
    | FetchResponse400
    | FetchResponse401
    | FetchResponse402
    | FetchResponse429
    | FetchResponse500
    | None
):
    if response.status_code == 200:
        response_200 = FetchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = FetchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = FetchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = FetchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 429:
        response_429 = FetchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = FetchResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    FetchResponse200
    | FetchResponse400
    | FetchResponse401
    | FetchResponse402
    | FetchResponse429
    | FetchResponse500
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
    body: FetchBody | Unset = UNSET,
) -> Response[
    FetchResponse200
    | FetchResponse400
    | FetchResponse401
    | FetchResponse402
    | FetchResponse429
    | FetchResponse500
]:
    """Fetch a URL and return an AI-synthesized answer based on page content and your prompt.

    Args:
        body (FetchBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FetchResponse200 | FetchResponse400 | FetchResponse401 | FetchResponse402 | FetchResponse429 | FetchResponse500]
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
    body: FetchBody | Unset = UNSET,
) -> (
    FetchResponse200
    | FetchResponse400
    | FetchResponse401
    | FetchResponse402
    | FetchResponse429
    | FetchResponse500
    | None
):
    """Fetch a URL and return an AI-synthesized answer based on page content and your prompt.

    Args:
        body (FetchBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FetchResponse200 | FetchResponse400 | FetchResponse401 | FetchResponse402 | FetchResponse429 | FetchResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: FetchBody | Unset = UNSET,
) -> Response[
    FetchResponse200
    | FetchResponse400
    | FetchResponse401
    | FetchResponse402
    | FetchResponse429
    | FetchResponse500
]:
    """Fetch a URL and return an AI-synthesized answer based on page content and your prompt.

    Args:
        body (FetchBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[FetchResponse200 | FetchResponse400 | FetchResponse401 | FetchResponse402 | FetchResponse429 | FetchResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: FetchBody | Unset = UNSET,
) -> (
    FetchResponse200
    | FetchResponse400
    | FetchResponse401
    | FetchResponse402
    | FetchResponse429
    | FetchResponse500
    | None
):
    """Fetch a URL and return an AI-synthesized answer based on page content and your prompt.

    Args:
        body (FetchBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        FetchResponse200 | FetchResponse400 | FetchResponse401 | FetchResponse402 | FetchResponse429 | FetchResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
