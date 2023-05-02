import pytest
import server

@pytest.fixture
def client():
    app = server.app
    
    with app.test_client() as client:
        yield client
