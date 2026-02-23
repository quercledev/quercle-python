from quercle import AuthenticatedClient, Client


def test_imports() -> None:
    assert Client is not None
    assert AuthenticatedClient is not None
