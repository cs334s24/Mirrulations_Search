import pytest
from kickoff_app import create_app
from flask import Flask, jsonify, request
import json

# Creates a Flask app instance for testing.
@pytest.fixture
def app():
    app = create_app()
    yield app

# Creates a test client for the Flask app.
@pytest.fixture
def client(app):
    return app.test_client()

# Test whether the index route returns a page containing
# the title "Kickoff Webapp".
def test_index_contains_title(client):
    response = client.get('/')
    assert b"Kickoff Webapp" in response.data

# Test whether the index route returns a 200 OK status code.
def test_index_response_status(client):
    response = client.get('/')
    assert response.status_code == 200

# Test whether the data endpoint returns a 200 OK status code.
def test_data_endpoint_response_status(client):
    response = client.get('/data')
    assert response.status_code == 200

# Test whether the data endpoint returns JSON data with status code 200.
def test_data_endpoint_returns_status_code_200(client):
    response = client.get('/data')
    data = json.loads(response.data)
    assert data['status'] == 200

# Test whether the index route returns a page containing
# a button with the text "Click Me".
def test_index_contains_button(client):
    response = client.get('/')
    assert b"Click Me" in response.data

# Test whether the data endpoint returns a valid JSON response.
def test_data_endpoint_returns_valid_json(client):
    response = client.get('/data')
    assert response.is_json

# Test whether the data endpoint returns JSON data containing the key "message".
def test_data_endpoint_returns_message(client):
    response = client.get('/data')
    data = json.loads(response.data)
    assert 'message' in data

# Test whether the data endpoint returns JSON data containing a message with the value "hello world".
def test_data_endpoint_returns_hello_world_message(client):
    response = client.get('/data')
    data = json.loads(response.data)
    assert data['message'] == 'hello world'

# Test whether the data endpoint returns JSON data containing the key "status".
def test_data_endpoint_returns_status(client):
    response = client.get('/data')
    data = json.loads(response.data)
    assert 'status' in data