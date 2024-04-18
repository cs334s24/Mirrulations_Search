"""
MockQueryManager is a class that mocks the QueryManager class. It is used
for testing purposes to simulate the behavior of the QueryManager class
without actually interacting with the database. It is used in conjunction
with the MockMongoQueries class to simulate
the behavior of the MongoQueries class.
"""
from mirrsearch.api.mock_database_manager import MockMongoDatabase

class MockQueryManager:
    """
    Class that mocks the QueryManager class. It is used for testing purposes
    to simulate the behavior of the QueryManager class without actually
    interacting with the database. It is used in conjunction with the
    MockMongoQueries class to simulate
    the behavior of the MongoQueries class.
    """

    manager = None

    def __init__(self) -> None:
        pass

class MockMongoQueries(MockQueryManager):
    """
    Class that mocks the MongoQueries class. It is used for testing purposes
    to simulate the behavior of the MongoQueries class without actually
    interacting with the database.
    """

    def search_dockets(self, search_term, page):
        """
        Mocks the search_dockets method of the MongoQueries class. It returns
        a dictionary with the search term that was passed in.
        """
        return {'data': search_term, 'page': page}

    def search_documents(self, search_term, docket_id):
        """
        Mocks the search_documents method of the MongoQueries class. It returns
        a dictionary with the search term and docket id that were passed in.
        """
        return {
                'data': 
                {'search_term': search_term,
                 'docket_id': docket_id,
                 'documents': [
                        {
                         'author': 'pass', 
                         'date_posted': 'pass', 
                         'link': 'pass',
                         'docket_id': docket_id
                        }
                    ]
                }
                }

    def search_comments(self, search_term, docket_id):
        """
        Mocks the search_comments method of the MongoQueries class. It returns
        a dictionary with the search term and docket id that were passed in.
        """
        return {
                'data': 
                {'search_term': search_term,
                 'docket_id': docket_id,
                 'comments': [
                        {
                         'author': 'pass', 
                         'date_posted': 'pass', 
                         'link': 'pass',
                         'docket_id': docket_id
                        }
                    ]
                }
                }

    def __init__(self, manager: MockMongoDatabase):
        super().__init__()
        self.manager = manager
