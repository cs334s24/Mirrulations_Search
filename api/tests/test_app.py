import pytest
from mirrsearch.api.app import create_app
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


# Test whether the data endpoint returns a 200 OK status code.
def test_data_endpoint_response_status(client):
    response = client.get('/data')
    assert response.status_code == 200


# Test whether the data endpoint returns JSON data with status code 200.
def test_data_endpoint_returns_status_code_200(client):
    response = client.get('/data')
    data = json.loads(response.data)
    assert data['status'] == 200


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

# Test whether the search_dockets endpoint returns a 200 status code.
def test_search_dockets_endpoint_returns_status(client):
    search_term = 'meaningful+use'
    response = client.get(f'/search_dockets?term={search_term}')
    assert response.status_code == 200


def test_search_dockets_endpoint_returns_valid_json(client):
    search_term = 'meaningful+use'
    response = client.get(f'/search_dockets?term={search_term}')
    assert response.is_json

def test_search_dockets_endpoint_returns_data_key(client):
    search_term = 'meaningful+use'
    response = client.get(f'/search_dockets?term={search_term}')
    assert 'data' in response.data

def test_search_dockets_endpoint_returns_status_code_400(client):
    response = client.get('/search_dockets')
    assert response.status_code == 400