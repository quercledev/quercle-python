from typing import Literal, cast

RawSearchBodyFormat = Literal["json", "markdown"]

RAW_SEARCH_BODY_FORMAT_VALUES: set[RawSearchBodyFormat] = {
    "json",
    "markdown",
}


def check_raw_search_body_format(value: str) -> RawSearchBodyFormat:
    if value in RAW_SEARCH_BODY_FORMAT_VALUES:
        return cast(RawSearchBodyFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RAW_SEARCH_BODY_FORMAT_VALUES!r}"
    )
