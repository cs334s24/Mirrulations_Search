"""
Python module that establishes database connections. This class
follows the singleton design pattern to ensure there is never
more than one database connection open. A mock database instance
can also be created using this class.
"""
from pymongo import MongoClient

class DatabaseManager:

    # TODO: Change the init function
    def __init__(self):
        pass

class MongoManager(DatabaseManager):
    """
    Class that manages the connection to a Mongo database running locally or
    a mock Mongo database
    """
    __instance = None

    def search_dockets(self, search_term):
        client = self.get_instance()
        db = client['mirrsearch']
        dockets = db.get_collection('docket')

        query = dockets.find({'attributes.title': {'$regex': f'{search_term}'}})

        results = []
        for doc in query:
            results.append(doc)

        return results

    def search_comments(self, search_term, docket_id):
        client = self.get_instance()
        db = client['mongoSample']
        comments = db.get_collection('comments')

        query = comments.find({'$and': [ {'attributes.docketId': {'$regex': f'{docket_id}'}}, {'attributes.comment': {'$regex': f'{search_term}'}}]})

        results = []
        for comment in query:
            results.append(comment)

        return results

    @staticmethod
    def get_instance():
        """
        Static method that returns the MongoDB client. It creates the client
        if it hasn't been created before, otherwise it returns the current
        connection.
        """
        return MongoManager.__instance

    @staticmethod
    def close_instance():
        """
        Static method that closes the database connection if there is currently one open.
        If there is no connection open, the method does nothing.
        """
        if MongoManager.__instance is not None:
            MongoManager.__instance.close()
            MongoManager.__instance = None

    def __init__(self):
        """
        Initializer method that ensures there is only ever one database connection open.
        """
        if MongoManager.__instance is not None:
            raise ConnectionException(message='''Error: a database client has already been
                established, another connection cannot be created without
                closing the other first''')
        else:
            MongoManager.__instance = MongoClient('mongo', 27017)

class ConnectionException(Exception):
    """
    Class that represents the exception that is thrown when there is
    an issue with establishing a connection to the database.
    """

    def __init__(self, message='Error: the connection to the database could not be established'):
        """
        Initializer that uses the message argument to raise the exception
        """
        self.message = message
        super().__init__(self.message)


# from pymongo import MongoClient

# class DatabaseManager:
#     """
#     Base class for managing database connections.
#     """
#     __instance = None

#     @staticmethod
#     def get_instance():
#         """
#         Static method that returns the database client. It creates the client
#         if it hasn't been created before, otherwise it returns the current
#         connection.
#         """
#         return DatabaseManager.__instance

#     @staticmethod
#     def close_instance():
#         """
#         Static method that closes the database connection if there is currently one open.
#         If there is no connection open, the method does nothing.
#         """
#         if DatabaseManager.__instance is not None:
#             DatabaseManager.__instance.close()
#             DatabaseManager.__instance = None
            
# class MongoManager(DatabaseManager):
#     """
#     Class that manages the connection to a Mongo database running locally or
#     a mock Mongo database
#     """
#     def __init__(self, host='localhost', port=27017):
#         """
#         Initializer method that ensures there is only ever one database connection open.
#         """
#         super().__init__()
#         if DatabaseManager.get_instance() is not None:
#             raise ConnectionException(message='''Error: a database client has already been
#                 established, another connection cannot be created without
#                 closing the other first''')
#         else:
#             DatabaseManager.__instance = MongoClient(host, port)

#     def search_dockets(self, search_term):
#         """
#         Method to search dockets in the database based on a search term.
#         """
#         client = self.get_instance()
#         db = client['mirrsearch']
#         dockets = db.get_collection('docket')

#         query = dockets.find({'attributes.title': {'$regex': f'{search_term}'}})
#         return list(query)

#     def search_comments(self, search_term, docket_id):
#         """
#         Method to search comments in the database based on a search term and a docket ID.
#         """
#         client = self.get_instance()
#         db = client['mongoSample']
#         comments = db.get_collection('comments')

#         query = comments.find({'$and': [ {'attributes.docketId': {'$regex': f'{docket_id}'}}, {'attributes.comment': {'$regex': f'{search_term}'}}]})
#         return list(query)

# class ConnectionException(Exception):
#     """
#     Class that represents the exception that is thrown when there is
#     an issue with establishing a connection to the database.
#     """

#     def __init__(self, message='Error: the connection to the database could not be established'):
#         """
#         Initializer that uses the message argument to raise the exception
#         """
#         self.message = message
#         super().__init__(self.message)
