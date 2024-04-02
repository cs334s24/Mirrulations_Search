class MockDatabase:

    def __init__(self):
        self.data = {}

class MockMongoDatabase(MockDatabase):

    # TODO: Mock out the mongo database connection
    def search_dockets(self, search_term):
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
        return [{
                'attributes': {'lastName': 'pass'},
                'postedDate': 'pass',
                'links': {'self': 'pass'},
                'docketId': 'test'
                }]
    
    def close(self):
        pass

    def get_database(self, database_name):
        return self
    
    def get_collection(self, collection_name):
        return self
    
    def find(self, query):
        return []

    def __init__(self):
        super().__init__()
