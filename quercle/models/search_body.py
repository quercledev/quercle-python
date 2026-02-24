from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

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

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        allowed_domains: list[str] | Unset = UNSET
        if not isinstance(self.allowed_domains, Unset):
            allowed_domains = self.allowed_domains

        blocked_domains: list[str] | Unset = UNSET
        if not isinstance(self.blocked_domains, Unset):
            blocked_domains = self.blocked_domains

        field_dict: dict[str, Any] = {}

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

        return search_body
