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

    def __init__(self):
        super().__init__()
