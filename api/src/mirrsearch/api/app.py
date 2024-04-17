
"""
Create barebones Flask app
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from mirrsearch.api.query_manager import MongoQueryManager
from mirrsearch.api.database_manager import MongoManager
from mirrsearch.api.mock_database_manager import MockMongoDatabase
from mirrsearch.api.mock_query_manager import MockMongoQueries
import boto3

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

    @app.route('/zip_data')
    def zip_data():
        data = {"message": "The email to download your data will be sent shortly", "status": 200}
        trigger_lambda()
        return jsonify(data)

    @app.route('/search')
    def search():
        # Obtains the search term
        search_term = request.args.get('term')
        response = {}

        # If a search term is not provided, the server will return this JSON and a 400 status code
        if not search_term:
            response = {}
            response['error'] = {'code': 400,
                                 'message': 'Error: You must provide a term to be searched'}
            return jsonify(response), 400

        response['data'] = {"search_term": search_term, "status": 200}
        return jsonify(response)

    @app.route('/search_dockets')
    def search_dockets():
        # Obtains the search term
        search_term = request.args.get('term')
        page = request.args.get('page')

        try:
            page = int(page)
        except (ValueError, TypeError):
            response = {}
            response['error'] = {'code': 400,
                                    'message': 'Error: Page must be an integer'}

        # If a search term is not provided, the server will return this JSON and a 400 status code
        if not search_term:
            response = {}
            response['error'] = {'code': 400,
                                 'message': 'Error: You must provide a term to be searched'}
            return jsonify(response), 400

        if not page:
            page = 1

        # If the search term is valid, data will be ingested into the JSON response
        response = query_manager.search_dockets(search_term, page)

        return jsonify(response)

    @app.route('/search_documents')
    def search_documents():

        # Obtains the search term and document ID from a prior request
        search_term = request.args.get('term')
        docket_id = request.args.get('docket_id')

        # If a search term is not provided, the server will return this JSON and a 400 status code
        if not search_term:
            response = {}
            response['error'] = {'code': 400,
                                'message': 'Error: You must provide a term to be searched'}
            return jsonify(response), 400

        # This checks if there is a docket ID present
        # If there is no docket ID, the function will return None
        # If there is a docket ID, the function will return the search results
        if docket_id is None:
            return None
        response = query_manager.search_documents(search_term, docket_id)

        return jsonify(response)

    @app.route('/search_comments')
    def search_comments():
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

        response = query_manager.search_comments(search_term, docket_id)

        return jsonify(response)

    return app

def trigger_lambda():
    """
    Trigger the Lambda function to zip the data
    """
    client = boto3.client('lambda', region_name='us-east-1')
    client.invoke(
        FunctionName='ProductionZipSystemLambda',
        InvocationType='Event'
    )

def launch(database):
    """
    Launch the Flask app
    """
    if database == 'mongo': # pragma: no cover
        database_manager = MongoManager()
        query_manager = MongoQueryManager(database_manager)
        return create_app(query_manager)
    if database == 'mockMongo':
        database_manager = MockMongoDatabase()
        query_manager = MockMongoQueries(database_manager)
        return create_app(query_manager)
    raise ValueError('Invalid database type') # pragma: no cover

if __name__ == '__main__':
    flask_app = launch('mongo')
    flask_app.run(debug=True, port=8000, host='0.0.0.0')
