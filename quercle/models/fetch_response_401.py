from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="FetchResponse401")


@_attrs_define
class FetchResponse401:
    """
    Attributes:
        detail (str): Human-readable error message.
    """

    detail: str

    def to_dict(self) -> dict[str, Any]:
        detail = self.detail

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "detail": detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        detail = d.pop("detail")

        fetch_response_401 = cls(
            detail=detail,
        )

        return fetch_response_401
