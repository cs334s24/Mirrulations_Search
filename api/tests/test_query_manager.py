"""
Module to test the query manager
"""

from mirrsearch.api.mock_database_manager import MockMongoDatabase
from mirrsearch.api.query_manager import MongoQueryManager, QueryManager

def test_search_dockets_mongo_queries():
    """
    Function to test the search_dockets function in the MongoQueryManager class
    """
    manager = MockMongoDatabase()
    query_manager = MongoQueryManager(manager)
    response = query_manager.search_dockets('test', 1)
    assert response['data']['search_term'] == 'test'

def test_search_documents_mongo_queries():
    """
    Function to test the search_documents function in the MongoQueryManager class
    """
    manager = MockMongoDatabase()
    query_manager = MongoQueryManager(manager)
    response = query_manager.search_documents('test', 'test')
    assert response['data']['search_term'] == 'test'
    assert response['data']['docket_id'] == 'test'
    assert response['data']['documents'][0]['author'] == 'pass'
    assert response['data']['documents'][0]['date_posted'] == 'pass'
    assert response['data']['documents'][0]['link'] == 'pass'
    if 'docket_id' in response['data']['documents']:
        assert response['data']['documents'][0]['docket_id'] == 'test'

def test_search_comments_mongo_queries():
    """
    Function to test the search_comments function in the MongoQueryManager class
    """
    manager = MockMongoDatabase()
    query_manager = MongoQueryManager(manager)
    response = query_manager.search_comments('test', 'test')
    assert response['data']['search_term'] == 'test'
    assert response['data']['docket_id'] == 'test'
    assert response['data']['comments'][0]['author'] == 'pass'
    assert response['data']['comments'][0]['date_posted'] == 'pass'
    assert response['data']['comments'][0]['link'] == 'pass'
    assert response['data']['comments'][0]['docket_id'] == 'test'

def test_query_manager_search_dockets_raises_error():
    """
    Function to test that the QueryManager class raises an error
    when the search_dockets function is called
    """
    manager = MockMongoDatabase()
    try:
        query_manager = QueryManager(manager)
        query_manager.search_dockets('test', 1)
    except NotImplementedError as error:
        assert str(error) == "Subclasses must implement search_dockets"

def test_query_manager_search_documents_raises_error():
    """
    Function to test that the QueryManager class raises an error
    when the search_documents function is called
    """
    manager = MockMongoDatabase()
    try:
        query_manager = QueryManager(manager)
        query_manager.search_documents('test', 'test')
    except NotImplementedError as error:
        assert str(error) == "Subclasses must implement search_documents"

def test_query_manager_search_comments_raises_error():
    """
    Function to test that the QueryManager class raises an error
    when the search_comments function is called
    """
    manager = MockMongoDatabase()
    try:
        query_manager = QueryManager(manager)
        query_manager.search_comments('test', 'test')
    except NotImplementedError as error:
        assert str(error) == "Subclasses must implement search_comments"
