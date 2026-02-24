from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

T = TypeVar("T", bound="ExtractResponse200Type1")


@_attrs_define
class ExtractResponse200Type1:
    """
    Attributes:
        result (list[str]): Relevant chunks array (`format=json`).
        unsafe (bool | Unset): True when safeguard marks content as unsafe.
    """

    result: list[str]
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
        result = cast(list[str], d.pop("result"))

        unsafe = d.pop("unsafe", UNSET)

        extract_response_200_type_1 = cls(
            result=result,
            unsafe=unsafe,
        )

        return extract_response_200_type_1
