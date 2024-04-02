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

class MockMongoDatabase(MockDatabase):
    """
    Class that mocks the MongoDatabase class. It is used for testing purposes
    to simulate the behavior of the MongoDatabase class without actually
    interacting with the database.
    """

    def search_dockets(self, search_term):
        """
        Mocks the search_dockets method of the MongoDatabase class. It returns
        a dictionary with the search term that was passed in.
        """
        return [{
            'attributes': {
                'title': 'pass'
            },
            'id': 'pass',
            'links': {
                'self': 'pass'
            }
        }]

    def search_comments(self, search_term, docket_id):
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

    def close(self):
        """
        Mocks the close method of the MongoDatabase class. It does nothing.
        """
        pass

    def get_database(self, database_name):
        """
        Mocks the get_database method of the MongoDatabase class. It returns
        itself.
        """
        return self

    def get_collection(self, collection_name):
        """
        Mocks the get_collection method of the MongoDatabase class. It returns
        itself.
        """
        return self

    def find(self, query):
        """
        Mocks the find method of the MongoDatabase class. It returns an empty list.
        """
        return []

    def __init__(self):
        super().__init__()
        self.data = {}
        self.client = self
