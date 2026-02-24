from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="RawFetchResponse401")


@_attrs_define
class RawFetchResponse401:
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

        raw_fetch_response_401 = cls(
            detail=detail,
        )

        return raw_fetch_response_401
