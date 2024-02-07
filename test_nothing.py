""" Set up the testing environment for the Flask app. """

import json
import pytest
from kickoff_app import create_app

@pytest.fixture
def app():
    """Creates a Flask app instance for testing."""
    app = create_app()
    yield app

@pytest.fixture
def client(app):
    """Creates a test client for the Flask app."""
    return app.test_client()

def test_data_endpoint_response_status(client):
    """Test whether the data endpoint returns a 200 OK status code."""
    response = client.get('/data')
    assert response.status_code == 200

def test_data_endpoint_returns_status_code_200(client):
    """Test whether the data endpoint returns JSON data with status code 200."""
    response = client.get('/data')
    data = json.loads(response.data)
    assert data['status'] == 200

def test_data_endpoint_returns_valid_json(client):
    """Test whether the data endpoint returns a valid JSON response."""
    response = client.get('/data')
    assert response.is_json

def test_data_endpoint_returns_message(client):
    """Test whether the data endpoint returns JSON data containing the key 'message'."""
    response = client.get('/data')
    data = json.loads(response.data)
    assert 'message' in data

def test_data_endpoint_returns_hello_world_message(client):
    """Test whether the data endpoint returns JSON data
    containing a message with the value 'hello world'."""
    response = client.get('/data')
    data = json.loads(response.data)
    assert data['message'] == 'hello world'

def test_data_endpoint_returns_status(client):
    """Test whether the data endpoint returns JSON data containing the key 'status'."""
    response = client.get('/data')
    data = json.loads(response.data)
    assert 'status' in data
