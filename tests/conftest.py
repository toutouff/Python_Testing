import pytest
<<<<<<< HEAD
import server
=======
from Python_Testing import server
>>>>>>> 2-club-should-not-be-able-to-use-more-point-than-allowed

@pytest.fixture
def client():
    app = server.app
    with app.test_client() as client:
        yield client
