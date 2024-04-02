"""
Module for managing queries to the database
"""
from mirrsearch.api.database_manager import DatabaseManager

class QueryManager:
    """
    Abstract class for managing queries to the database
    """

    __manager = None

    def __init__(self, database_manager):
        self.__manager = database_manager


class MongoQueryManager(QueryManager):
    """
    Class for managing queries to a MongoDB database
    """

    __manager = None

    def search_dockets(self, search_term):
        """
        Function that searches the dockets collection in the database
        for a given search term
        """
        response = {}

        # Uses the database manager to query the dockets
        search = self.__manager.search_dockets(search_term)

        # If the search term is valid, data will be ingested into the JSON response
        response['data'] = {
            'search_term': search_term,
                'dockets': []
            }

        for doc in search:
            title = doc['attributes']['title']
            doc_id = doc['id']
            link = doc['links']['self']
            # TODO: Query comments and documents collections to get count of each using docket ID
            number_of_comments = 0
            number_of_documents = 0
            response['data']['dockets'].append({
                'title': title,
                'id': doc_id,
                'link': link,
                'number_of_comments': number_of_comments,
                'number_of_documents': number_of_documents
            })

        return response

    def search_comments(self, search_term, docket_id):
        """
        Function that searches the comments collection in the database
        for a given search term and docket ID
        """
        response = {}

        # Uses the database manager to query the comments
        search = self.__manager.search_comments(search_term, docket_id)

        # If the search term is valid, data will be ingested into the JSON response
        response['data'] = {
            'search_term': search_term,
            'docket_id': docket_id,
            'comments': []
        }

        for comment in search:
            author = comment['attributes']['lastName']
            date_posted = comment['postedDate']
            link = comment['links']['self']
            docket_id = comment['docketId']
            response['data']['comments'].append({
                'author': author,
                'date_posted': date_posted,
                'link': link,
                'docket_id': docket_id,
                })

        return response

    def __init__(self, database_manager: DatabaseManager):
        super().__init__(database_manager)
        self.__manager = database_manager
