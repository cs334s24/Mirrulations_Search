"""Tests for the mongo_manager module"""

import pytest
from mirrsearch.api.database_manager import MongoManager, ConnectionException

def test_manager_returns_mongo_client_instance():
    """
    Tests that the MongoManager class returns an instance that
    is not None when it is first initialized
    """
    client = MongoManager()
    assert client is not None
    client.close_instance()

def test_manager_returns_current_instance():
    """
    Tests that the get_instance function returns the current
    database connection
    """
    client = MongoManager()
    print(client)
    assert client.get_instance() is not None
    client.close_instance()

def test_manager_closes_connection():
    """
    Tests that the close_instance function closes the database
    connection
    """
    client = MongoManager()
    client.close_instance()
    assert client.get_instance() is None

def test_multiple_connections_is_prohibited():
    """
    Tests that there can never be more than one database
    connection open at a time. A ConnectionException is
    thrown if multiple connections try to be created
    """
    client = MongoManager()
    try:
        MongoManager()
        pytest.fail()
    except ConnectionException:
        client.close_instance()

def test_default_connection_exception_message():
    """
    Tests that the ConnectionException default message
    is correct
    """
    exception = ConnectionException()
    assert exception.message == 'Error: the connection to the database could not be established'

def test_custom_connection_exception_message():
    """
    Tests that a custom message can be passed to the
    initializer for the ConnectionException class
    """
    exception = ConnectionException(message='Test exception message')
    assert exception.message == 'Test exception message'
