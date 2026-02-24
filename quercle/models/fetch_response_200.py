from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="FetchResponse200")


@_attrs_define
class FetchResponse200:
    """
    Attributes:
        result (str): AI-synthesized answer based on the fetched page and your prompt.
    """

    result: str

    def to_dict(self) -> dict[str, Any]:
        result = self.result

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "result": result,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        result = d.pop("result")

        fetch_response_200 = cls(
            result=result,
        )

        return fetch_response_200
