"""Tests for the database manager module"""

import pytest
from mirrsearch.api.database_manager import MongoManager, ConnectionException, DatabaseManager

def test_manager_returns_mongo_client_instance():
    """
    Tests that the MongoManager class returns an instance that
    is not None when it is first initialized
    """
    client = MongoManager(hostname='mock')
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

def test_search_comments_returns_results():
    """
    Tests that the search_comments function returns the
    expected results
    """
    client = MongoManager(hostname='mock')
    results = client.search_comments('test', 'test')
    assert results is not None
    client.close_instance()

def test_search_dockets_returns_results():
    """
    Tests that the search_dockets function returns the
    expected results
    """
    client = MongoManager(hostname='mock')
    results = client.search_dockets('test')
    assert results is not None
    client.close_instance()

def test_database_manager_search_dockets_raises_error():
    """
    Tests that the MongoManager class raises an error
    when the search_dockets function is called
    """
    client = DatabaseManager()
    try:
        client.search_dockets('test')
    except NotImplementedError as error:
        assert str(error) == "Subclasses must implement search_dockets"

def test_database_manager_search_comments_raises_error():
    """
    Tests that the MongoManager class raises an error
    when the search_comments function is called
    """
    client = DatabaseManager()
    try:
        client.search_comments('test', 'test')
    except NotImplementedError as error:
        assert str(error) == "Subclasses must implement search_comments"

def test_database_manager_get_instance_raises_error():
    """
    Tests that the MongoManager class raises an error
    when the get_instance function is called
    """
    try:
        MongoManager.get_instance()
    except NotImplementedError as error:
        assert str(error) == "Subclasses must implement get_instance"

def test_database_manager_close_instance_raises_error():
    """
    Tests that the MongoManager class raises an error
    when the close_instance function is called
    """
    try:
        MongoManager.close_instance()
    except NotImplementedError as error:
        assert str(error) == "Subclasses must implement close_instance"

def test_get_instance_before_connection():
    """
    Tests that get_instance raises a NotImplementedError
    when called before establishing a connection
    """
    try:
        DatabaseManager.get_instance()
    except NotImplementedError as error:
        assert str(error) == "Subclasses must implement get_instance"

def test_close_instance_before_connection():
    """
    Tests that close_instance raises a NotImplementedError
    when called before establishing a connection
    """
    try:
        DatabaseManager.close_instance()
    except NotImplementedError as error:
        assert str(error) == "Subclasses must implement close_instance"

def test_close_instance_multiple_times():
    """
    Tests that close_instance can be called multiple times
    without raising any errors
    """
    try:
        MongoManager.close_instance()
        MongoManager.close_instance()
    except NotImplementedError:
        pytest.fail("close_instance raised NotImplementedError unexpectedly")

def test_get_instance_after_connection_closed():
    """
    Tests that get_instance raises a NotImplementedError
    when called after closing the connection
    """
    client = MongoManager(hostname='mock')
    client.close_instance()
    try:
        client.get_instance()
    except NotImplementedError as error:
        assert str(error) == "Subclasses must implement get_instance"
