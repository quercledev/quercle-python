from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.raw_search_body import RawSearchBody
from ...models.raw_search_response_200_type_0 import RawSearchResponse200Type0
from ...models.raw_search_response_200_type_1 import RawSearchResponse200Type1
from ...models.raw_search_response_400 import RawSearchResponse400
from ...models.raw_search_response_401 import RawSearchResponse401
from ...models.raw_search_response_402 import RawSearchResponse402
from ...models.raw_search_response_429 import RawSearchResponse429
from ...models.raw_search_response_500 import RawSearchResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: RawSearchBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/raw_search",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    RawSearchResponse200Type0
    | RawSearchResponse200Type1
    | RawSearchResponse400
    | RawSearchResponse401
    | RawSearchResponse402
    | RawSearchResponse429
    | RawSearchResponse500
    | None
):
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> RawSearchResponse200Type0 | RawSearchResponse200Type1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = RawSearchResponse200Type0.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = RawSearchResponse200Type1.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = RawSearchResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = RawSearchResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = RawSearchResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 429:
        response_429 = RawSearchResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = RawSearchResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    RawSearchResponse200Type0
    | RawSearchResponse200Type1
    | RawSearchResponse400
    | RawSearchResponse401
    | RawSearchResponse402
    | RawSearchResponse429
    | RawSearchResponse500
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
    body: RawSearchBody | Unset = UNSET,
) -> Response[
    RawSearchResponse200Type0
    | RawSearchResponse200Type1
    | RawSearchResponse400
    | RawSearchResponse401
    | RawSearchResponse402
    | RawSearchResponse429
    | RawSearchResponse500
]:
    """Run web search and return raw results.

    Args:
        body (RawSearchBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RawSearchResponse200Type0 | RawSearchResponse200Type1 | RawSearchResponse400 | RawSearchResponse401 | RawSearchResponse402 | RawSearchResponse429 | RawSearchResponse500]
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
    body: RawSearchBody | Unset = UNSET,
) -> (
    RawSearchResponse200Type0
    | RawSearchResponse200Type1
    | RawSearchResponse400
    | RawSearchResponse401
    | RawSearchResponse402
    | RawSearchResponse429
    | RawSearchResponse500
    | None
):
    """Run web search and return raw results.

    Args:
        body (RawSearchBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RawSearchResponse200Type0 | RawSearchResponse200Type1 | RawSearchResponse400 | RawSearchResponse401 | RawSearchResponse402 | RawSearchResponse429 | RawSearchResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: RawSearchBody | Unset = UNSET,
) -> Response[
    RawSearchResponse200Type0
    | RawSearchResponse200Type1
    | RawSearchResponse400
    | RawSearchResponse401
    | RawSearchResponse402
    | RawSearchResponse429
    | RawSearchResponse500
]:
    """Run web search and return raw results.

    Args:
        body (RawSearchBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RawSearchResponse200Type0 | RawSearchResponse200Type1 | RawSearchResponse400 | RawSearchResponse401 | RawSearchResponse402 | RawSearchResponse429 | RawSearchResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: RawSearchBody | Unset = UNSET,
) -> (
    RawSearchResponse200Type0
    | RawSearchResponse200Type1
    | RawSearchResponse400
    | RawSearchResponse401
    | RawSearchResponse402
    | RawSearchResponse429
    | RawSearchResponse500
    | None
):
    """Run web search and return raw results.

    Args:
        body (RawSearchBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RawSearchResponse200Type0 | RawSearchResponse200Type1 | RawSearchResponse400 | RawSearchResponse401 | RawSearchResponse402 | RawSearchResponse429 | RawSearchResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
