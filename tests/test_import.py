from quercle import AsyncQuercleClient, QuercleApiError, QuercleClient, tool_metadata


def test_imports() -> None:
    assert QuercleClient is not None
    assert AsyncQuercleClient is not None
    assert QuercleApiError is not None
    assert "search" in tool_metadata
