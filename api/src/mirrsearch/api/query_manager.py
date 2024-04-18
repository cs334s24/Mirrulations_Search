"""
Module for managing queries to the database
"""
import operator
from mirrsearch.api.database_manager import DatabaseManager

class QueryManager:
    """
    Abstract class for managing queries to the database
    """

    def __init__(self, database_manager: DatabaseManager):
        self._manager = database_manager

    def search_dockets(self, search_term, page):
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

    _dockets_cursor = None

    def search_dockets(self, search_term, page):
        """
        Function that searches the dockets collection in the database
        for a given search term
        """
        dockets = []
        search = self._manager.search_dockets(search_term)
        self._dockets_cursor = search
        for doc in self._dockets_cursor[page*10-10:page*10]:
            doc_id = doc['id']
            number_of_comments, comments_containing = self._manager.get_comment_count(
                search_term, doc_id)
            number_of_documents, documents_containing = self._manager.get_document_count(
                search_term, doc_id)
            start_date, end_date =  self._manager.comments_date_range(doc_id)
            if start_date is None:
                comment_date_range = "No comments"
            else:
                comment_date_range = f"{start_date} - {end_date}"
            dockets.append({
                'title': doc['attributes']['title'],
                'id': doc_id,
                'link': "https://www.regulations.gov/docket/" +  doc_id,
                'total_comments': number_of_comments,
                'total_documents': number_of_documents,
                'documents_containing': documents_containing,
                'comments_containing': comments_containing,
                'docket_type': doc['attributes']['docketType'],
                'docket_agency': doc['attributes']['agencyId'],
                'comment_date_range': comment_date_range,
            })
        dockets.sort(key=operator.itemgetter('documents_containing', 'comments_containing'),
                     reverse=True)
        response = {'data': {'search_term': search_term, 'dockets': dockets}}
        response['meta'] = self.get_meta_data(search_term, page)

        return response

    def get_meta_data(self, search_term, page):
        """
        Function that returns the metadata for the search results
        """
        response = {'links': {}}

        total_results = len(list(self._dockets_cursor))
        response['total_results'] = total_results
        response['links']['current'] = f'api/search_dockets?{search_term}&page={page}'
        if page > 1:
            response['links']['prev'] = f'api/search_dockets?{search_term}&page={page-1}'
        if page <= total_results//10:
            response['links']['next'] = f'api/search_dockets?{search_term}&page={page+1}'
        response['links']['first'] = f'api/search_dockets?{search_term}&page=1'
        last_link = f'api/search_dockets?{search_term}&page={total_results//10+1}'
        response['links']['last'] = last_link

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
