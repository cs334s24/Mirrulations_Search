from mirrsearch.api.mock_database_manager import MockMongoDatabase

class MockQueryManager:

    __manager = None

    def __init__(self) -> None:
        pass

class MockMongoQueries(MockQueryManager):
    # TODO: Mock out the search_dockets query

    def search_dockets(self, search_term):
        return {'data': search_term}

    def __init__(self, manager: MockMongoDatabase):
        self.__manager = manager
        
