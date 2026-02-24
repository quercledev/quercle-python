from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.raw_fetch_body_format import (
    RawFetchBodyFormat,
    check_raw_fetch_body_format,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RawFetchBody")


@_attrs_define
class RawFetchBody:
    """
    Attributes:
        url (str): The URL to fetch.
        format_ (RawFetchBodyFormat | Unset): Output format for fetched content. Defaults to `markdown`.
        use_safeguard (bool | Unset): Enable prompt-injection detection when `format` is `markdown`.
    """

    url: str
    format_: RawFetchBodyFormat | Unset = UNSET
    use_safeguard: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_

        use_safeguard = self.use_safeguard

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
            }
        )
        if format_ is not UNSET:
            field_dict["format"] = format_
        if use_safeguard is not UNSET:
            field_dict["use_safeguard"] = use_safeguard

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        _format_ = d.pop("format", UNSET)
        format_: RawFetchBodyFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = check_raw_fetch_body_format(_format_)

        use_safeguard = d.pop("use_safeguard", UNSET)

        raw_fetch_body = cls(
            url=url,
            format_=format_,
            use_safeguard=use_safeguard,
        )

        return raw_fetch_body
