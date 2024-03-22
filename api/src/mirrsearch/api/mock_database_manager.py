class MockDatabase:

    def __init__(self):
        self.data = {}

class MockMongoDatabase(MockDatabase):

    # TODO: Mock out the mongo database connection

    def __init__(self):
        super().__init__()
