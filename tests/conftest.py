import pytest
from Python_Testing import server

@pytest.fixture
def client():
    app = server.app
    with app.test_client() as client:
        yield client
