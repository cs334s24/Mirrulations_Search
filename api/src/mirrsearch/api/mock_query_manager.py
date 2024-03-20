class MockQueryManager:

    def __init__(self):
        self.temp = 'hello'

class MockMongoQueries(MockQueryManager):
    # TODO: Mock out the search_dockets query

    def __init__(self):
        super().__init__()
