from typing import Literal, cast

RawFetchBodyFormat = Literal["html", "markdown"]

RAW_FETCH_BODY_FORMAT_VALUES: set[RawFetchBodyFormat] = {
    "html",
    "markdown",
}


def check_raw_fetch_body_format(value: str) -> RawFetchBodyFormat:
    if value in RAW_FETCH_BODY_FORMAT_VALUES:
        return cast(RawFetchBodyFormat, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RAW_FETCH_BODY_FORMAT_VALUES!r}"
    )
