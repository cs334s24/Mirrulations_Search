"""Tests for the Flask app."""

# pylint: disable=unused-import

from unittest.mock import MagicMock, patch
import json
import os
import pytest
import boto3
from mirrsearch.api.app import launch, trigger_lambda
from flask import Flask, jsonify, request

@pytest.fixture
def app():
    """Creates a Flask app instance for testing."""
    app = launch('mockMongo')
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

def test_search_dockets_endpoint_valid_request_returns_200(client):
    """Test whether the search_dockets endpoint returns a 200 OK status code."""
    search_term = 'Governance'
    response = client.get(f'/search_dockets?term={search_term}&page=1')
    print(response)
    assert response.status_code == 200

def test_search_dockets_endpoint_returns_valid_json(client):
    """Test whether the search_dockets endpoint returns a valid JSON response."""
    search_term = 'Governance'
    response = client.get(f'/search_dockets?term={search_term}')
    assert response.is_json

def test_search_dockets_endpoint_returns_data_key(client):
    """Test whether the search_dockets endpoint returns JSON data containing the key 'data'."""
    search_term = 'Governance'
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
    and the expected JSON response when provided with a search term and docket ID."""
    response = client.get('/search_documents?term=test&docket_id=pass')
    data = response.get_json()
    assert response.status_code == 200
    assert 'data' in data
    assert data['data']['search_term'] == 'test'
    assert isinstance(data['data']['documents'], list)
    assert len(data['data']['documents']) == 1
    document = data['data']['documents'][0]
    assert document['author'] == 'pass'
    if document['docket_id'] is None:
        assert document['docket_id'] is None
    else:
        assert document['docket_id'] == 'pass'

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

def test_zip_data_endpoint_returns_200(client, mocker):
    """Test whether the zip_data endpoint returns a 200 OK status code."""
    mocker.patch('mirrsearch.api.app.trigger_lambda')
    response = client.get('/zip_data')
    assert response.status_code == 200

@pytest.fixture
def mock_boto3_client():
    """
    Mocks the boto3.client function using the patch decorator.

    Yields:
        mock_client: The mocked boto3 client object.
    """
    with patch('boto3.client') as mock_client:
        yield mock_client


@pytest.fixture
def mock_env_variables():
    """
    A context manager that mocks the environment variables required for AWS access.

    This context manager sets the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` 
    environment variables
    to the provided values, allowing for mocking AWS access during testing.

    Usage:
        with mock_env_variables():
            # Code that requires AWS access

    """
    with patch.dict(os.environ, {
        "AWS_ACCESS_KEY_ID": "your_access_key_id",
        "AWS_SECRET_ACCESS_KEY": "your_secret_access_key"
    }):
        yield


def test_trigger_lambda(mock_boto3_client, mock_env_variables): # pylint: disable=unused-argument
    """
    Test case for the trigger_lambda function.

    This test case verifies that the trigger_lambda function correctly invokes the
    ZipSystemLambda function with the correct arguments.

    Args:
        mock_boto3_client: A MagicMock object representing the mocked boto3 client.

    Returns:
        None
    """

    # Mocking the client.invoke method
    mock_invoke = MagicMock()
    mock_boto3_client.return_value.invoke = mock_invoke

    # Call the function
    trigger_lambda()

    # Assert that the boto3 client was called with correct arguments
    mock_boto3_client.assert_called_once_with(
        'lambda',
        region_name='us-east-1',
        aws_access_key_id='your_access_key_id',
        aws_secret_access_key='your_secret_access_key'
    )

    # Assert that the invoke method was called with correct arguments
    mock_invoke.assert_called_once_with(
        FunctionName='ZipSystemLambda',
        InvocationType='Event'
    )

def test_launch_returns_flask_app():
    """Test whether the launch function returns a Flask app instance."""
    app = launch('mockMongo')
    assert isinstance(app, Flask)
