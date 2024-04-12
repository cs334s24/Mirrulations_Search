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
            doc_id = doc['id']
            number_of_comments, comments_containing = self._manager.get_comment_count(
                search_term, doc_id)
            number_of_documents, documents_containing = self._manager.get_document_count(
                search_term, doc_id)
            date_modified = doc['attributes']['modifyDate']
            date_modified = date_modified.split('T')[0]
            date_modified = date_modified.replace('-', '/')
            start_date, end_date =  self._manager.comments_date_range(doc_id)
            if start_date is None:
                comment_date_range = "No comments"
            else:
                comment_date_range = f"{start_date} - {end_date}"
            response['data']['dockets'].append({
                'title': doc['attributes']['title'],
                'id': doc_id,
                'link': "https://www.regulations.gov/docket/" +  doc_id,
                'total_comments': number_of_comments,
                'total_documents': number_of_documents,
                'documents_containing': documents_containing,
                'comments_containing': comments_containing,
                'docket_type': doc['attributes']['docketType'],
                'docket_agency': doc['attributes']['agencyId'],
                'date_range': date_modified,
                'comment_date_range': comment_date_range,
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
