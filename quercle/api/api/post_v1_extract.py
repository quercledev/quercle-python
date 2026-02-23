from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.post_v1_extract_body import PostV1ExtractBody
from ...models.post_v1_extract_response_200_type_0 import PostV1ExtractResponse200Type0
from ...models.post_v1_extract_response_200_type_1 import PostV1ExtractResponse200Type1
from ...models.post_v1_extract_response_400 import PostV1ExtractResponse400
from ...models.post_v1_extract_response_401 import PostV1ExtractResponse401
from ...models.post_v1_extract_response_402 import PostV1ExtractResponse402
from ...models.post_v1_extract_response_429 import PostV1ExtractResponse429
from ...models.post_v1_extract_response_500 import PostV1ExtractResponse500
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: PostV1ExtractBody | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/extract",
    }

    if not isinstance(body, Unset):
        _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    PostV1ExtractResponse200Type0
    | PostV1ExtractResponse200Type1
    | PostV1ExtractResponse400
    | PostV1ExtractResponse401
    | PostV1ExtractResponse402
    | PostV1ExtractResponse429
    | PostV1ExtractResponse500
    | None
):
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> PostV1ExtractResponse200Type0 | PostV1ExtractResponse200Type1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = PostV1ExtractResponse200Type0.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_1 = PostV1ExtractResponse200Type1.from_dict(data)

            return response_200_type_1

        response_200 = _parse_response_200(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = PostV1ExtractResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = PostV1ExtractResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 402:
        response_402 = PostV1ExtractResponse402.from_dict(response.json())

        return response_402

    if response.status_code == 429:
        response_429 = PostV1ExtractResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = PostV1ExtractResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    PostV1ExtractResponse200Type0
    | PostV1ExtractResponse200Type1
    | PostV1ExtractResponse400
    | PostV1ExtractResponse401
    | PostV1ExtractResponse402
    | PostV1ExtractResponse429
    | PostV1ExtractResponse500
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
    body: PostV1ExtractBody | Unset = UNSET,
) -> Response[
    PostV1ExtractResponse200Type0
    | PostV1ExtractResponse200Type1
    | PostV1ExtractResponse400
    | PostV1ExtractResponse401
    | PostV1ExtractResponse402
    | PostV1ExtractResponse429
    | PostV1ExtractResponse500
]:
    """Fetch a URL and return chunks relevant to a query.

    Args:
        body (PostV1ExtractBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostV1ExtractResponse200Type0 | PostV1ExtractResponse200Type1 | PostV1ExtractResponse400 | PostV1ExtractResponse401 | PostV1ExtractResponse402 | PostV1ExtractResponse429 | PostV1ExtractResponse500]
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
    body: PostV1ExtractBody | Unset = UNSET,
) -> (
    PostV1ExtractResponse200Type0
    | PostV1ExtractResponse200Type1
    | PostV1ExtractResponse400
    | PostV1ExtractResponse401
    | PostV1ExtractResponse402
    | PostV1ExtractResponse429
    | PostV1ExtractResponse500
    | None
):
    """Fetch a URL and return chunks relevant to a query.

    Args:
        body (PostV1ExtractBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostV1ExtractResponse200Type0 | PostV1ExtractResponse200Type1 | PostV1ExtractResponse400 | PostV1ExtractResponse401 | PostV1ExtractResponse402 | PostV1ExtractResponse429 | PostV1ExtractResponse500
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: PostV1ExtractBody | Unset = UNSET,
) -> Response[
    PostV1ExtractResponse200Type0
    | PostV1ExtractResponse200Type1
    | PostV1ExtractResponse400
    | PostV1ExtractResponse401
    | PostV1ExtractResponse402
    | PostV1ExtractResponse429
    | PostV1ExtractResponse500
]:
    """Fetch a URL and return chunks relevant to a query.

    Args:
        body (PostV1ExtractBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PostV1ExtractResponse200Type0 | PostV1ExtractResponse200Type1 | PostV1ExtractResponse400 | PostV1ExtractResponse401 | PostV1ExtractResponse402 | PostV1ExtractResponse429 | PostV1ExtractResponse500]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: PostV1ExtractBody | Unset = UNSET,
) -> (
    PostV1ExtractResponse200Type0
    | PostV1ExtractResponse200Type1
    | PostV1ExtractResponse400
    | PostV1ExtractResponse401
    | PostV1ExtractResponse402
    | PostV1ExtractResponse429
    | PostV1ExtractResponse500
    | None
):
    """Fetch a URL and return chunks relevant to a query.

    Args:
        body (PostV1ExtractBody | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PostV1ExtractResponse200Type0 | PostV1ExtractResponse200Type1 | PostV1ExtractResponse400 | PostV1ExtractResponse401 | PostV1ExtractResponse402 | PostV1ExtractResponse429 | PostV1ExtractResponse500
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
