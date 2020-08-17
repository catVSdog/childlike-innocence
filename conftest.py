import pytest

from applications import create_app


@pytest.fixture
def app():
    return create_app()
