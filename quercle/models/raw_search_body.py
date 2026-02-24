from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.raw_search_body_format import (
    RawSearchBodyFormat,
    check_raw_search_body_format,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RawSearchBody")


@_attrs_define
class RawSearchBody:
    """
    Attributes:
        query (str): The search query to run against the web.
        format_ (RawSearchBodyFormat | Unset): Output format for search results. Defaults to `markdown`.
        use_safeguard (bool | Unset): Enable prompt-injection detection on search results.
    """

    query: str
    format_: RawSearchBodyFormat | Unset = UNSET
    use_safeguard: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_

        use_safeguard = self.use_safeguard

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "query": query,
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
        query = d.pop("query")

        _format_ = d.pop("format", UNSET)
        format_: RawSearchBodyFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = check_raw_search_body_format(_format_)

        use_safeguard = d.pop("use_safeguard", UNSET)

        raw_search_body = cls(
            query=query,
            format_=format_,
            use_safeguard=use_safeguard,
        )

        return raw_search_body
