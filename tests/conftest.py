import pytest


@pytest.fixture()
def set_up(page) -> None:
    page.goto("/")
    yield page
