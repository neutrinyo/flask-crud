import pytest
from ..app import app  # Import your Flask application

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client  # Make the client available to your tests