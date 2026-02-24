from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SearchBody")


@_attrs_define
class SearchBody:
    """
    Attributes:
        query (str): The search query to find information about. Be specific.
        allowed_domains (list[str] | Unset): Only include results from these domains (e.g., ['example.com',
            'docs.example.org']).
        blocked_domains (list[str] | Unset): Exclude results from these domains (e.g., ['example.com',
            'docs.example.org']).
    """

    query: str
    allowed_domains: list[str] | Unset = UNSET
    blocked_domains: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        allowed_domains: list[str] | Unset = UNSET
        if not isinstance(self.allowed_domains, Unset):
            allowed_domains = self.allowed_domains

        blocked_domains: list[str] | Unset = UNSET
        if not isinstance(self.blocked_domains, Unset):
            blocked_domains = self.blocked_domains

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
            }
        )
        if allowed_domains is not UNSET:
            field_dict["allowed_domains"] = allowed_domains
        if blocked_domains is not UNSET:
            field_dict["blocked_domains"] = blocked_domains

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        query = d.pop("query")

        allowed_domains = cast(list[str], d.pop("allowed_domains", UNSET))

        blocked_domains = cast(list[str], d.pop("blocked_domains", UNSET))

        search_body = cls(
            query=query,
            allowed_domains=allowed_domains,
            blocked_domains=blocked_domains,
        )

        search_body.additional_properties = d
        return search_body

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
