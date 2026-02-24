from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.raw_search_response_200_type_1_result_item import (
        RawSearchResponse200Type1ResultItem,
    )


T = TypeVar("T", bound="RawSearchResponse200Type1")


@_attrs_define
class RawSearchResponse200Type1:
    """
    Attributes:
        result (list[RawSearchResponse200Type1ResultItem]): Search results list (`format=json`).
        unsafe (bool | Unset): True when safeguard marks content as unsafe.
    """

    result: list[RawSearchResponse200Type1ResultItem]
    unsafe: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        result = []
        for result_item_data in self.result:
            result_item = result_item_data.to_dict()
            result.append(result_item)

        unsafe = self.unsafe

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "result": result,
            }
        )
        if unsafe is not UNSET:
            field_dict["unsafe"] = unsafe

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.raw_search_response_200_type_1_result_item import (
            RawSearchResponse200Type1ResultItem,
        )

        d = dict(src_dict)
        result = []
        _result = d.pop("result")
        for result_item_data in _result:
            result_item = RawSearchResponse200Type1ResultItem.from_dict(
                result_item_data
            )

            result.append(result_item)

        unsafe = d.pop("unsafe", UNSET)

        raw_search_response_200_type_1 = cls(
            result=result,
            unsafe=unsafe,
        )

        raw_search_response_200_type_1.additional_properties = d
        return raw_search_response_200_type_1

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
