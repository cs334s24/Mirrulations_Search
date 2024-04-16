"""
Module for mocking the database manager for testing purposes
"""
class MockDatabase:
    """
    Class that mocks the DatabaseManager class. It is used for testing purposes
    to simulate the behavior of the DatabaseManager class without actually
    interacting with the database.
    """

    def __init__(self):
        self.data = {}

class MockCursor:
    """
    Class that mocks the Cursor class. It is used for testing purposes
    to simulate the behavior of the Cursor class without actually
    interacting with the database.
    """

    def __init__(self):
        self.data = {}

    def __iter__(self):
        """
        Mocks the __iter__ method of the Cursor class. It returns
        an empty list.
        """
        return iter(self.data)
    
    def __next__(self):
        """
        Mocks the __next__ method of the Cursor class. It returns
        an empty list.
        """
        return next(self.data)

    def count(self):
        """
        Mocks the count method of the Cursor class. It returns
        0.
        """
        return 0
    
    def sort(self, _query):
        """
        Mocks the sort method of the Cursor class. It returns an empty list.
        """
        return self
    
    def limit(self, _query):
        """
        Mocks the limit method of the Cursor class. It returns an empty list.
        """
        return self.data

class MockMongoDatabase(MockDatabase):
    """
    Class that mocks the MongoDatabase class. It is used for testing purposes
    to simulate the behavior of the MongoDatabase class without actually
    interacting with the database.
    """

    def search_dockets(self, _search_term):
        """
        Mocks the search_dockets method of the MongoDatabase class. It returns
        a dictionary with the search term that was passed in.
        """
        return [{
            'attributes': {
                'title': 'pass',
                'modifyDate': 'pass',
                'docketType': 'pass',
                'agencyId': 'pass'
            },
            'id': 'pass',
            'links': {
                'self': 'pass'
            }
        }]

    def search_comments(self, _search_term, _docket_id):
        """
        Mocks the search_comments method of the MongoDatabase class. It returns
        a list of dictionaries with the search term and docket id that were passed in.
        """
        return [{
                'attributes': {'lastName': 'pass'},
                'postedDate': 'pass',
                'links': {'self': 'pass'},
                'docketId': 'test'
                }]
    
    def comments_date_range(self, _doc_id):
        """
        Mocks the comments_date_range method of the MongoDatabase class. It returns
        None.
        """
        return None, None

    def get_comment_count(self, _search_term, _doc_id):
        """
        Mocks the get_comment_count method of the MongoDatabase class. It returns
        a tuple with the search term and docket id that were passed in.
        """
        return 0, 0

    def get_document_count(self, _search_term, _doc_id):
        """
        Mocks the get_document_count method of the MongoDatabase class. It returns
        a tuple with the search term and docket id that were passed in.
        """
        return 0, 0

    def comments_date_range(self, _doc_id):
        """
        Mocks the comments_date_range method of the MongoDatabase class. It returns
        None.
        """
        return None, None

    def close(self):
        """
        Mocks the close method of the MongoDatabase class. It does nothing.
        """
        return self

    def get_database(self, _database_name):
        """
        Mocks the get_database method of the MongoDatabase class. It returns
        itself.
        """
        return self

    def get_collection(self, _collection_name):
        """
        Mocks the get_collection method of the MongoDatabase class. It returns
        itself.
        """
        return self

    def find(self, _query):
        """
        Mocks the find method of the MongoDatabase class. It returns an empty list.
        """
        return MockCursor()
    
    def sort(self, _query):
        """
        Mocks the sort method of the MongoDatabase class. It returns an empty list.
        """
        return MockCursor()
    
    def limit(self, _query):
        """
        Mocks the limit method of the MongoDatabase class. It returns an empty list.
        """
        return MockCursor()
    
    def count_documents(self, _query):
        """
        Mocks the count_documents method of the MongoDatabase class. It returns
        0.
        """
        return 0

    def __init__(self):
        super().__init__()
        self.data = {}
        self.client = self
