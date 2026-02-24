from typing import Literal, cast

ExtractBodyFormat = Literal["json", "markdown"]

EXTRACT_BODY_FORMAT_VALUES: set[ExtractBodyFormat] = {
    "json",
    "markdown",
}


def check_extract_body_format(value: str) -> ExtractBodyFormat:
    if value in EXTRACT_BODY_FORMAT_VALUES:
        return cast(ExtractBodyFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EXTRACT_BODY_FORMAT_VALUES!r}"
    )
