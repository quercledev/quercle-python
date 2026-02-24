from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_

        use_safeguard = self.use_safeguard

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        raw_fetch_body.additional_properties = d
        return raw_fetch_body

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
