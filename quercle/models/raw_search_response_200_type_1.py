from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

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

    def to_dict(self) -> dict[str, Any]:
        result = []
        for result_item_data in self.result:
            result_item = result_item_data.to_dict()
            result.append(result_item)

        unsafe = self.unsafe

        field_dict: dict[str, Any] = {}

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

        return raw_search_response_200_type_1
