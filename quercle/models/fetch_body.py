from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="FetchBody")


@_attrs_define
class FetchBody:
    """
    Attributes:
        url (str): The URL to fetch and analyze.
        prompt (str): Instructions for how to analyze the page content. Be specific about what information you want to
            extract.
    """

    url: str
    prompt: str

    def to_dict(self) -> dict[str, Any]:
        url = self.url

        prompt = self.prompt

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "url": url,
                "prompt": prompt,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        url = d.pop("url")

        prompt = d.pop("prompt")

        fetch_body = cls(
            url=url,
            prompt=prompt,
        )

        return fetch_body
