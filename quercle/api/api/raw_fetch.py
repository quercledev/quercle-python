from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.raw_fetch_body import RawFetchBody
from ...models.raw_fetch_response_200 import RawFetchResponse200
from ...models.raw_fetch_response_400 import RawFetchResponse400
from ...models.raw_fetch_response_401 import RawFetchResponse401
from ...models.raw_fetch_response_402 import RawFetchResponse402
from ...models.raw_fetch_response_429 import RawFetchResponse429
from ...models.raw_fetch_response_500 import RawFetchResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RawFetchBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/raw_fetch",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RawFetchResponse200
    | RawFetchResponse400
    | RawFetchResponse401
    | RawFetchResponse402
    | RawFetchResponse429
    | RawFetchResponse500
    | None
):
    if response.status_code == 200:
        response_200 = RawFetchResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RawFetchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RawFetchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = RawFetchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 429:
        response_429 = RawFetchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RawFetchResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RawFetchResponse200
    | RawFetchResponse400
    | RawFetchResponse401
    | RawFetchResponse402
    | RawFetchResponse429
    | RawFetchResponse500
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
    body: RawFetchBody | Unset = UNSET,
) -> Response[
    RawFetchResponse200
    | RawFetchResponse400
    | RawFetchResponse401
    | RawFetchResponse402
    | RawFetchResponse429
    | RawFetchResponse500
]:
    """Fetch a URL and return raw markdown or HTML.

    Args:
        body (RawFetchBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RawFetchResponse200 | RawFetchResponse400 | RawFetchResponse401 | RawFetchResponse402 | RawFetchResponse429 | RawFetchResponse500]
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
    body: RawFetchBody | Unset = UNSET,
) -> (
    RawFetchResponse200
    | RawFetchResponse400
    | RawFetchResponse401
    | RawFetchResponse402
    | RawFetchResponse429
    | RawFetchResponse500
    | None
):
    """Fetch a URL and return raw markdown or HTML.

    Args:
        body (RawFetchBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RawFetchResponse200 | RawFetchResponse400 | RawFetchResponse401 | RawFetchResponse402 | RawFetchResponse429 | RawFetchResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RawFetchBody | Unset = UNSET,
) -> Response[
    RawFetchResponse200
    | RawFetchResponse400
    | RawFetchResponse401
    | RawFetchResponse402
    | RawFetchResponse429
    | RawFetchResponse500
]:
    """Fetch a URL and return raw markdown or HTML.

    Args:
        body (RawFetchBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RawFetchResponse200 | RawFetchResponse400 | RawFetchResponse401 | RawFetchResponse402 | RawFetchResponse429 | RawFetchResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RawFetchBody | Unset = UNSET,
) -> (
    RawFetchResponse200
    | RawFetchResponse400
    | RawFetchResponse401
    | RawFetchResponse402
    | RawFetchResponse429
    | RawFetchResponse500
    | None
):
    """Fetch a URL and return raw markdown or HTML.

    Args:
        body (RawFetchBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RawFetchResponse200 | RawFetchResponse400 | RawFetchResponse401 | RawFetchResponse402 | RawFetchResponse429 | RawFetchResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
