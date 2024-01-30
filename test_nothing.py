import pytest
from kickoff_app import create_app

# Fixture to create a Flask app instance for testing.
@pytest.fixture
def app():
    app = create_app()
    yield app

# Fixture to create a test client for the Flask app.
@pytest.fixture
def client(app):
    return app.test_client()

# Test whether the index route returns a 200 OK status code.
def test_index_response_status(client):
    response = client.get('/')
    assert response.status_code == 200

# Test whether the index route returns a page containing
# the title "Kickoff Webapp".
def test_index_contains_title(client):
    response = client.get('/')
    assert b"Kickoff Webapp" in response.data

# Test whether the index route returns a page containing
# a button with the text "Click Me".
def test_index_contains_button(client):
    response = client.get('/')
    assert b"Click Me" in response.data

# Test whether the index route response contains a specific message.
def test_index_contains_response(client):
    decoded_response_data = client.get('/').data.decode('utf-8')
    expected_message = "This isn't set up to the endpoint yet"
    assert expected_message in decoded_response_data

