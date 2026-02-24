from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="RawSearchResponse200Type1ResultItem")


@_attrs_define
class RawSearchResponse200Type1ResultItem:
    """
    Attributes:
        title (str): Search result title.
        url (str): Search result URL.
        content (str): Search result snippet text.
    """

    title: str
    url: str
    content: str

    def to_dict(self) -> dict[str, Any]:
        title = self.title

        url = self.url

        content = self.content

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "title": title,
                "url": url,
                "content": content,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        url = d.pop("url")

        content = d.pop("content")

        raw_search_response_200_type_1_result_item = cls(
            title=title,
            url=url,
            content=content,
        )

        return raw_search_response_200_type_1_result_item
