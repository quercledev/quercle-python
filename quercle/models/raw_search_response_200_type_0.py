from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="RawSearchResponse200Type0")


@_attrs_define
class RawSearchResponse200Type0:
    """
    Attributes:
        result (str): Search results markdown (`format=markdown`).
        unsafe (bool | Unset): True when safeguard marks content as unsafe.
    """

    result: str
    unsafe: bool | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        result = self.result

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
        d = dict(src_dict)
        result = d.pop("result")

        unsafe = d.pop("unsafe", UNSET)

        raw_search_response_200_type_0 = cls(
            result=result,
            unsafe=unsafe,
        )

        return raw_search_response_200_type_0
