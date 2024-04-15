"""
Module for managing queries to the database
"""
from mirrsearch.api.database_manager import DatabaseManager

class QueryManager:
    """
    Abstract class for managing queries to the database
    """

    def __init__(self, database_manager: DatabaseManager):
        self._manager = database_manager

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

class MongoQueryManager(QueryManager):
    """
    Class for managing queries to a MongoDB database
    """

    def search_dockets(self, search_term):
        """
        Function that searches the dockets collection in the database
        for a given search term
        """
        response = {'data': {'search_term': search_term, 'dockets': []}}
        search = self._manager.search_dockets(search_term)
        for doc in search:
            title = doc['attributes']['title']
            doc_id = doc['id']
            link = "https://www.regulations.gov/docket/" + doc_id
            number_of_comments = 0  # Placeholder for counting comments
            number_of_documents = 0  # Placeholder for counting documents
            response['data']['dockets'].append({
                'title': title,
                'id': doc_id,
                'link': link,
                'total_comments': number_of_comments,
                'total_documents': number_of_documents,
                'documents_containing': 54,
                'comments_containing': 20,
                'docket_type': 'Notice',
                'date_range': '2008/03/31-2023/12/28',
                'comment_date_range': '2008/03/31-2023/12/28'
            })
        return response

    def search_documents(self, search_term, docket_id):
        """
        Function that searches the documents collection in the database
        for a given search term and docket ID
        """
        response = {'data': {'search_term': search_term, 'docket_id': docket_id, 'documents': []}}
        search = self._manager.search_documents(search_term, docket_id)
        for document in search:
            author = document['attributes']['lastName']
            date_posted = document['postedDate']
            link = document['links']['self']
            docket_id = document['docketId']
            response['data']['documents'].append({
                'author': author,
                'date_posted': date_posted,
                'link': link,
                'docket_id': docket_id,
            })
        return response

    def search_comments(self, search_term, docket_id):
        """
        Function that searches the comments collection in the database
        for a given search term and docket ID
        """
        response = {'data': {'search_term': search_term, 'docket_id': docket_id, 'comments': []}}
        search = self._manager.search_comments(search_term, docket_id)
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
