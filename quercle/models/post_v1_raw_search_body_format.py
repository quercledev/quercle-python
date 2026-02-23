from enum import Enum


class PostV1RawSearchBodyFormat(str, Enum):
    JSON = "json"
    MARKDOWN = "markdown"

    def __str__(self) -> str:
        return str(self.value)
