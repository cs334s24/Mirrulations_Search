from mirrsearch.api.mock_database_manager import MockMongoDatabase

class MockQueryManager:

    __manager = None

    def __init__(self) -> None:
        pass

class MockMongoQueries(MockQueryManager):
    # TODO: Mock out the search_dockets query

    def search_dockets(self, search_term):
        return {'data': search_term}
    
    def search_comments(self, search_term, docket_id):
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
        self.__manager = manager
        