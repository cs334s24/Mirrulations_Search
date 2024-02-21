"""
Create barebones Flask app
Run with: python kickoff_app.py
"""

from flask import Flask, jsonify, request
from flask_cors import CORS
from pymongo import MongoClient
  
class MongoManager:
    __instance = None

    @staticmethod 
    def get_instance():
         if MongoManager.__instance == None:
             MongoManager()
         return MongoManager.__instance
    
    @staticmethod
    def close_instance():
        if MongoManager.__instance != None:
            MongoManager.__instance.close()
            MongoManager.__instance = None
        else:
            raise Exception('Error: there is no database connection currently active')
    
    def __init__(self):
        if MongoManager.__instance != None:
            raise Exception('Error: a database client has already been established, another connection cannot be created without closing the other first')
        else:
            MongoManager.__instance = MongoClient('localhost', 27017)

def create_app():
    """
    Create the application instance and define the routes
    """
    app = Flask(__name__)
    CORS(app)
    # In order to restrict access to our specific origin, use origin parameter below.
    # CORS(app, origins='http://your-react-app-domain:your-react-app-port')

    @app.route('/data')
    def get_data():
        data = {"message": "hello world", "status": 200}
        return jsonify(data)

    @app.route('/search_dockets')
    def search_dockets():
        response = {}
        client = get_database_client()
        db = 

        # Obtains the search term
        search_term = request.args.get('term')

        # If a search term is not provided, the server will return this JSON and a 400 status code
        if search_term is None or len(search_term) == 0:
            response['error'] = {'code': 400,
                                 'message': 'Error: You must provide a term to be searched'}
            return (jsonify(response), 400)

        # If the search term is valid, data will be ingested into the JSON response
        response['data'] = {
            'search_term': search_term,
            'dockets': []
        }
        response['data']['dockets'].append({
           'title': 'Designation as a Preexisting Subscription Service',
           'id': "COLC-2006-0014",
           'link': 'https://www.regulations.gov/docket/COLC-2006-0014',
           'number_of_comments': 0,
           'number_of_documents': 1
           })
        return jsonify(response)

    @app.route('/search_comments')
    def search_comments():
        response = {}

        # Obtains the search term and docket id
        search_term = request.args.get('term')
        docket_id = request.args.get('docket_id')

        # If a search term is not provided, the server will return this JSON and a 400 status code
        if search_term is None or len(search_term) == 0:
            response['error'] = {'code': 400,
                                 'message': 'Error: You must provide a term to be searched'}
            return (jsonify(response), 400)

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

def launch():
    """
    Launch the Flask app
    """
    return create_app()

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port='8000', host='0.0.0.0')
