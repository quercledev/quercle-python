from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.post_v1_raw_search_body_format import PostV1RawSearchBodyFormat
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1RawSearchBody")


@_attrs_define
class PostV1RawSearchBody:
    """
    Attributes:
        query (str): The search query to run against the web.
        format_ (PostV1RawSearchBodyFormat | Unset): Output format for search results. Defaults to `markdown`.
        use_safeguard (bool | Unset): Enable prompt-injection detection on search results.
    """

    query: str
    format_: PostV1RawSearchBodyFormat | Unset = UNSET
    use_safeguard: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value

        use_safeguard = self.use_safeguard

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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
        format_: PostV1RawSearchBodyFormat | Unset
        if isinstance(_format_, Unset):
            format_ = UNSET
        else:
            format_ = PostV1RawSearchBodyFormat(_format_)

        use_safeguard = d.pop("use_safeguard", UNSET)

        post_v1_raw_search_body = cls(
            query=query,
            format_=format_,
            use_safeguard=use_safeguard,
        )

        post_v1_raw_search_body.additional_properties = d
        return post_v1_raw_search_body

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
