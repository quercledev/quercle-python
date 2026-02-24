from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.search_response_429_errors_item import SearchResponse429ErrorsItem


T = TypeVar("T", bound="SearchResponse429")


@_attrs_define
class SearchResponse429:
    """
    Attributes:
        detail (str): Rate limit error details.
        errors (list[SearchResponse429ErrorsItem] | Unset): Additional validation issue details.
    """

    detail: str
    errors: list[SearchResponse429ErrorsItem] | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        detail = self.detail

        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "detail": detail,
            }
        )
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_response_429_errors_item import SearchResponse429ErrorsItem

        d = dict(src_dict)
        detail = d.pop("detail")

        _errors = d.pop("errors", UNSET)
        errors: list[SearchResponse429ErrorsItem] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = SearchResponse429ErrorsItem.from_dict(errors_item_data)

                errors.append(errors_item)

        search_response_429 = cls(
            detail=detail,
            errors=errors,
        )

        return search_response_429
