from pymongo import MongoClient
import mongomock

"""
Class that manages the connection to a Mongo database running locally on port 27017
"""
class MongoManager:
    __instance = None

    """
    Static method that returns the MongoDB client. It creates the client if it hasn't been created before,
    otherwise it returns the current connection.
    """
    @staticmethod 
    def get_instance():
         if MongoManager.__instance == None:
             MongoManager()
         return MongoManager.__instance
    
    """
    Static method that closes the database connection if there is currently one open. If there is no connection
    open, the method does nothing.
    """
    @staticmethod
    def close_instance():
        if MongoManager.__instance != None:
            MongoManager.__instance.close()
            MongoManager.__instance = None
    
    """
    Initializer method that ensures there is only ever one database connection open.
    """
    def __init__(self, test=False):
        if MongoManager.__instance != None:
            raise Exception('Error: a database client has already been established, another connection cannot be created without closing the other first')
        elif test == True:
            MongoManager.__instance = mongomock.MongoClient()
        else:
            MongoManager.__instance = MongoClient('localhost', 27017)