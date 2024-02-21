"""Tests for the Flask app."""

# pylint: disable=unused-import

import json
import pytest
from mirrsearch.api.app import create_app
from flask import Flask, jsonify, request

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
    """Test whether the data endpoint returns a 200 OK status code."""
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

def test_search_dockets_endpoint_returns_status(client):
    """Test whether the search_dockets endpoint returns a 200 OK status code."""
    search_term = 'meaningful+use'
    response = client.get(f'/search_dockets?term={search_term}')
    assert response.status_code == 200

def test_search_dockets_endpoint_returns_valid_json(client):
    """Test whether the search_dockets endpoint returns a valid JSON response."""
    search_term = 'meaningful+use'
    response = client.get(f'/search_dockets?term={search_term}')
    assert response.is_json

def test_search_dockets_endpoint_returns_data_key(client):
    """Test whether the search_dockets endpoint returns JSON data containing the key 'data'."""
    search_term = 'meaningful+use'
    response = client.get(f'/search_dockets?term={search_term}')
    data = json.loads(response.data)
    assert 'data' in data

def test_search_dockets_endpoint_returns_status_code_400(client):
    """Test whether the search_dockets endpoint returns a 400
    Bad Request status code when no search term is provided."""
    response = client.get('/search_dockets')
    assert response.status_code == 400

def test_search_documents_success(client):
    """Test whether the search_documents endpoint returns a 200 OK status code
    and the expected JSON response when provided with a search term and document ID."""
    response = client.get('/search_documents?term=test&document_id=123')
    data = response.get_json()
    assert response.status_code == 200
    assert 'data' in data
    assert data['data']['search_term'] == 'test'
    assert isinstance(data['data']['comments'], list)
    assert len(data['data']['comments']) == 1
    comment = data['data']['comments'][0]
    assert comment['author'] == 'Environmental Protection Agency'
    assert comment['document_id'] == '123'

def test_search_documents_missing_term(client):
    """Test whether the search_documents endpoint returns a 400 Bad Request status code
    and the appropriate error message when no search term is provided."""
    response = client.get('/search_documents')
    data = response.get_json()
    assert response.status_code == 400
    assert 'error' in data
    assert data['error']['code'] == 400
    assert data['error']['message'] == 'Error: You must provide a term to be searched'

def test_search_documents_empty_term(client):
    """Test whether the search_documents endpoint returns a 400 Bad Request status code
    and the appropriate error message when an empty search term is provided."""
    response = client.get('/search_documents?term=')
    data = response.get_json()
    assert response.status_code == 400
    assert 'error' in data
    assert data['error']['code'] == 400
    assert data['error']['message'] == 'Error: You must provide a term to be searched'

def test_search_documents_invalid_document_id(client):
    """Test whether the search_documents endpoint handles an invalid document ID
    by returning the appropriate error response."""
    response = client.get('/search_documents?term=test&document_id=invalid_id')
    data = response.get_json()
    assert response.status_code == 200 # Assuming you handle invalid document IDs gracefully
    assert 'data' in data
    assert len(data['data']['comments']) == 1 # Check if any comments are returned
    assert data['data']['comments'][0]['document_id'] == 'invalid_id'
    # Check if the given document ID is returned

def test_search_comments_endpoint_returns_status(client):
    """Test whether the search_comments endpoint returns a 200 OK status code."""
    search_term = 'preexisting'
    docket_id = 'HHS-OS-2010-0014'
    response = client.get(f'/search_comments?term={search_term}&docket_id={docket_id}')
    assert response.status_code == 200

def test_search_comments_endpoint_returns_valid_json(client):
    """Test whether the search_comments endpoint returns a valid JSON response."""
    search_term = 'preexisting'
    docket_id = 'HHS-OS-2010-0014'
    response = client.get(f'/search_comments?term={search_term}&docket_id={docket_id}')
    assert response.is_json

def test_search_comments_endpoint_returns_data_key(client):
    """Test whether the search_comments endpoint returns JSON data containing the key 'data'."""
    search_term = 'preexisting'
    docket_id = 'HHS-OS-2010-0014'
    response = client.get(f'/search_comments?term={search_term}&docket_id={docket_id}')
    data = json.loads(response.data)
    assert 'data' in data

def test_search_comments_endpoint_returns_comments(client):
    """Test whether the search_comments endpoint returns comments in the response."""
    search_term = 'preexisting'
    docket_id = 'HHS-OS-2010-0014'
    response = client.get(f'/search_comments?term={search_term}&docket_id={docket_id}')
    data = json.loads(response.data)
    assert 'comments' in data['data']

def test_search_comments_endpoint_returns_correct_comment_structure(client):
    """Test whether the search_comments endpoint returns comments with correct structure."""
    search_term = 'preexisting'
    docket_id = 'HHS-OS-2010-0014'
    response = client.get(f'/search_comments?term={search_term}&docket_id={docket_id}')
    data = json.loads(response.data)
    comments = data['data']['comments']
    assert all(comment.get('author') for comment in comments)
    assert all(comment.get('date_posted') for comment in comments)
    assert all(comment.get('link') for comment in comments)
    assert all(comment.get('docket_id') for comment in comments)

def test_search_comments_endpoint_returns_status_code_400(client):
    """Test whether the search_comments endpoint returns a 400
    Bad Request status code when no search term is provided."""
    response = client.get('/search_comments')
    assert response.status_code == 400

def test_search_comments_endpoint_returns_status_code_400_missing_docket_id(client):
    """Test whether the search_comments endpoint returns a 400
    Bad Request status code when no docket_id is provided."""
    search_term = 'preexisting'
    response = client.get(f'/search_comments?term={search_term}')
    assert response.status_code == 400
