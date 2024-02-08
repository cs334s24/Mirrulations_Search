"""
Create barebones Flask app
Run with: python kickoff_app.py
"""

from flask import Flask, jsonify, request
from flask_cors import CORS


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
       search_term = request.args.get('term')

       if search_term is None or len(search_term) == 0:
           response['error'] = {'code': 400, 'message': 'Error: You must provide a term to be searched'}
           return jsonify(response)
      
       response['data'] = {'search_term': search_term}
       response['data']['dockets'] = []
       # TODO: insert the data with presentation term
       response['data']['dockets'].append({
           'title': 'Designation as a Preexisting Subscription Service',
           'id': "COLC-2006-0014",
           'link': 'https://www.regulations.gov/docket/COLC-2006-0014',
           'number_of_comments': 0,
           'number_of_documents': 1
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
