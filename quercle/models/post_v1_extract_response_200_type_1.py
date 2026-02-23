from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PostV1ExtractResponse200Type1")


@_attrs_define
class PostV1ExtractResponse200Type1:
    """
    Attributes:
        result (list[str]): Relevant chunks array (`format=json`).
        unsafe (bool | Unset): True when safeguard marks content as unsafe.
    """

    result: list[str]
    unsafe: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        result = self.result

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
        d = dict(src_dict)
        result = cast(list[str], d.pop("result"))

        unsafe = d.pop("unsafe", UNSET)

        post_v1_extract_response_200_type_1 = cls(
            result=result,
            unsafe=unsafe,
        )

        post_v1_extract_response_200_type_1.additional_properties = d
        return post_v1_extract_response_200_type_1

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
