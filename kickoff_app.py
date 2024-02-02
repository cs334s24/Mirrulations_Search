# create barebones flask app
# run with: python kickoff_app.py

from flask import Flask, render_template, jsonify
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)
    # In order to restrict access to our specific origin, use origin parameter below.
    # CORS(app, origins='http://your-react-app-domain:your-react-app-port')


    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/data')
    def get_data():
        data = {"message": "hello world", "status": 200}
        return jsonify(data)
    
    return app

def launch():
    return create_app()

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port='8000', host='0.0.0.0')