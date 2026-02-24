from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..models.extract_body_format import ExtractBodyFormat, check_extract_body_format
from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtractBody")


@_attrs_define
class ExtractBody:
    """
    Attributes:
        url (str): The URL to fetch and extract relevant chunks from.
        query (str): What information to extract from the page content.
        format_ (ExtractBodyFormat | Unset): Output format for extracted chunks. Defaults to `markdown`.
        use_safeguard (bool | Unset): Enable prompt-injection detection on selected extracted content.
    """

    url: str
    query: str
    format_: ExtractBodyFormat | Unset = UNSET
    use_safeguard: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        query = self.query

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_

        use_safeguard = self.use_safeguard

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
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
        url = d.pop("url")

        query = d.pop("query")

        _format_ = d.pop("format", UNSET)
        format_: ExtractBodyFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = check_extract_body_format(_format_)

        use_safeguard = d.pop("use_safeguard", UNSET)

        extract_body = cls(
            url=url,
            query=query,
            format_=format_,
            use_safeguard=use_safeguard,
        )

        return extract_body
