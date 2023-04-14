from Python_Testing import server
import pytest


@pytest.fixture
def client():
    app = server.app
    with app.test_client() as client:
        yield client
