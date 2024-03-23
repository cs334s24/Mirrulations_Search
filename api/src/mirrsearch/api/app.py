"""
Create barebones Flask app
Run with: python kickoff_app.py
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from mirrsearch.api.query_manager import MongoQueryManager
from mirrsearch.api.database_manager import MongoManager
from mirrsearch.api.mock_database_manager import MockMongoDatabase
from mirrsearch.api.mock_query_manager import MockMongoQueries

def create_app(query_manager):
    """
    Create the application instance and define the routes
    """
    app = Flask(__name__)
    CORS(app)

    @app.route('/data')
    def get_data():
        data = {"message": "hello world", "status": 200}
        return jsonify(data)

    @app.route('/search_dockets')
    def search_dockets():
        # Obtains the search term
        search_term = request.args.get('term')

        # If a search term is not provided, the server will return this JSON and a 400 status code
        if not search_term:
            response = {}
            response['error'] = {'code': 400,
                                 'message': 'Error: You must provide a term to be searched'}
            return jsonify(response), 400
        
        response = query_manager.search_dockets(search_term)

        return jsonify(response)

    @app.route('/search_documents')
    def search_documents():
        response = {}

        # Obtains the search term and document id from a prior request
        search_term = request.args.get('term')
        document_id = request.args.get('document_id')

        # If a search term is not provided, the server will return this JSON and a 400 status code
        if not search_term:
            response['error'] = {'code': 400,
                                 'message': 'Error: You must provide a term to be searched'}
            return jsonify(response), 400

        # If the search term is valid, data will be ingested into the JSON response
        response['data'] = {
            'search_term': search_term,
            'comments': []
        }
        response['data']['comments'].append({
            "author": "Environmental Protection Agency",
            "date_posted": "Dec 22, 2003",
            "link": "https://www.regulations.gov/document/EPA-HQ-OAR-2003-0083-0794",
            "document_id": document_id
           })
        return jsonify(response)

    @app.route('/search_comments')
    def search_comments():
        response = {}

        # Obtains the search term and docket id from a prior request
        search_term = request.args.get('term')
        docket_id = request.args.get('docket_id')

        # If a search term is not provided, the server will return this JSON and a 400 status code
        if not search_term:
            response = {}
            response['error'] = {'code': 400,
                                 'message': 'Error: You must provide a term to be searched'}
            return jsonify(response), 400
        if not docket_id:
            response = {}
            response['error'] = {'code': 400,
                                 'message': 'Error: You must provide a docket_id to be searched'}
            return jsonify(response), 400

        # If the search term is valid, data will be ingested into the JSON response
        response['data'] = {
            'search_term': search_term,
            'comments': []
        }

        response['data']['comments'].append({
            "author": "Department of Health and Human Services",
            "date_posted": "Apr 14, 2011",
            "link": "https://www.regulations.gov/comment/HHS-OS-2010-0014-0032",
            "docket_id": docket_id
           })
        return jsonify(response)

    return app

def launch(database):
    """
    Launch the Flask app
    """
    if database == 'mongo':
        database_manager = MongoManager(host='mongo', port=27017)
        query_manager = MongoQueryManager(database_manager)
        return create_app(query_manager)
    elif database == 'mockMongo':
        database_manager = MockMongoDatabase()
        query_manager = MockMongoQueries(database_manager)
        return create_app(query_manager)
    
    # TODO: Handle case where they do not provide which database they want to use

if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run(debug=True, port=8000, host='0.0.0.0')
