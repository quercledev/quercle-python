from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define

T = TypeVar("T", bound="FetchResponse429ErrorsItem")


@_attrs_define
class FetchResponse429ErrorsItem:
    """
    Attributes:
        code (str): Validation issue code.
        path (list[float | str]): Path to the invalid field.
        message (str): Validation issue message.
    """

    code: str
    path: list[float | str]
    message: str

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        path = []
        for path_item_data in self.path:
            path_item: float | str
            path_item = path_item_data
            path.append(path_item)

        message = self.message

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "code": code,
                "path": path,
                "message": message,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code")

        path = []
        _path = d.pop("path")
        for path_item_data in _path:

            def _parse_path_item(data: object) -> float | str:
                return cast(float | str, data)

            path_item = _parse_path_item(path_item_data)

            path.append(path_item)

        message = d.pop("message")

        fetch_response_429_errors_item = cls(
            code=code,
            path=path,
            message=message,
        )

        return fetch_response_429_errors_item
