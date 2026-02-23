from enum import Enum


class PostV1ExtractBodyFormat(str, Enum):
    JSON = "json"
    MARKDOWN = "markdown"

    def __str__(self) -> str:
        return str(self.value)
