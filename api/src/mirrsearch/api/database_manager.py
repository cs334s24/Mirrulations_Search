
"""
Python module that establishes database connections. This class
follows the singleton design pattern to ensure there is never
more than one database connection open. A mock database instance
can also be created using this class.
"""
from pymongo import MongoClient
from mirrsearch.api.mock_database_manager import MockMongoDatabase

class DatabaseManager:
    """
    Class that manages the connection to a database
    """

    def __init__(self):
        pass

    def search_dockets(self, search_term):
        """
        Function that searches the dockets collection in the database
        for a given search term
        """
        raise NotImplementedError("Subclasses must implement search_dockets")

    def search_documents(self, search_term, docket_id):
        """
        Function that searches the documents collection in the database
        for a given search term and docket ID
        """
        raise NotImplementedError("Subclasses must implement search_documents")

    def search_comments(self, search_term, docket_id):
        """
        Function that searches the comments collection in the database
        for a given search term and docket ID
        """
        raise NotImplementedError("Subclasses must implement search_comments")

    @staticmethod
    def get_instance():
        """
        Static method that returns the database client instance.
        """
        raise NotImplementedError("Subclasses must implement get_instance")

    @staticmethod
    def close_instance():
        """
        Static method that closes the database connection if there is currently one open.
        If there is no connection open, the method does nothing.
        """
        raise NotImplementedError("Subclasses must implement close_instance")

class MongoManager(DatabaseManager):
    """
    Class that manages the connection to a Mongo database running locally or
    a mock Mongo database
    """
    __instance = None

    def search_dockets(self, search_term):
        """
        Function that searches the dockets collection in the database
        for a given search term
        """
        client = self.get_instance()
        db = client.get_database('mirrsearch')
        dockets = db.get_collection('docket')

        query = dockets.find({'attributes.title': {'$regex': f'{search_term}'}})

        results = []
        for doc in query:
            results.append(doc) # pragma: no cover

        return results

    def search_documents(self, search_term, docket_id):
        """
        Function that searches the documents collection in the database
        for a given search term and docket ID
        """
        client = self.get_instance()
        db = client.get_database('mirrsearch')
        documents = db.get_collection('documents')

        query = documents.find({'$and': [ {'attributes.docketId': {'$regex': f'{docket_id}'}},
                                        {'attributes.document': {'$regex': f'{search_term}'}}]})

        results = []
        for document in query:
            results.append(document) # pragma: no cover

        return results

    def search_comments(self, search_term, docket_id):
        """
        Function that searches the comments collection in the database
        for a given search term and docket ID
        """
        client = self.get_instance()
        db = client.get_database('mirrsearch')
        comments = db.get_collection('comments')

        query = comments.find({'$and': [ {'attributes.docketId': {'$regex': f'{docket_id}'}},
                                        {'attributes.comment': {'$regex': f'{search_term}'}}]})

        results = []
        for comment in query:
            results.append(comment) # pragma: no cover

        return results

    def get_comment_count(self, search_term, docket_id):
        """ Returns the total number of comments and the number of comments with the search term"""
        client = self.get_instance()
        db = client.get_database('mirrsearch')
        comments = db.get_collection('comments')

        total_comments = comments.count_documents({'attributes.docketId':
                                                   {'$regex': f'{docket_id}'}})
        total_terms = comments.count_documents({'$and': [ {'attributes.docketId':
                                                {'$regex': f'{docket_id}'}},
                                                {'attributes.comment':
                                                 {'$regex': f'{search_term}'}}]})

        return total_comments, total_terms

    def get_document_count(self, search_term, docket_id):
        """
        Function that returns the total number of documents related to a docket ID
        and the number of documents with a search term in them
        """
        client = self.get_instance()
        db = client.get_database('mirrsearch')
        documents = db.get_collection('documents')

        total_documents = documents.count_documents({'attributes.docketId':
                                                   {'$regex': f'{docket_id}'}})
        total_terms = documents.count_documents({'$and': [ {'id': {'$regex': f'{docket_id}'}},
                                                     {'data': {'$regex': f'{search_term}'}}]})

        return total_documents, total_terms

    def comments_date_range(self, docket_id):
        """ Finds earliest and latest comments for a docket """
        client = self.get_instance()
        db = client.get_database('mirrsearch')
        comments = db.get_collection('comments')

        start_date = list(comments.find({ "attributes.docketId" :
                                         {'$regex': f'{docket_id}'}}).sort(
                                            {"attributes.postedDate" : 1 }).limit(1))
        end_date = list(comments.find({ "attributes.docketId" :
                                  {'$regex': f'{docket_id}'} }).sort({ "attributes.postedDate" :
                                                                      -1 }).limit(1))
        if len(start_date) == 0 or len(end_date) == 0:
            return None, None
        start_date = start_date[0]['attributes']['postedDate']
        start_date = start_date.split('T')[0]
        end_date = end_date[0]['attributes']['postedDate']
        end_date = end_date.split('T')[0]
        return start_date.replace('-', '/'), end_date.replace('-', '/')

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

    def __init__(self, hostname='mongo', port=27017):
        """
        Initializer method that ensures there is only ever one database connection open.
        """
        if MongoManager.__instance is not None:
            raise ConnectionException(message='''Error: a database client has already been
                established, another connection cannot be created without
                closing the other first''')

        if hostname == 'mock':
            MongoManager.__instance = MockMongoDatabase()
        else:
            MongoManager.__instance = MongoClient(hostname, port)

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
