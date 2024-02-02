"""
Create barebones Flask app
Run with: python kickoff_app.py
"""

from flask import Flask, render_template, jsonify

def create_app():
    """
    Create the application instance and define the routes
    """
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/data')
    def get_data():
        data = {"message": "hello world", "status": 200}
        return jsonify(data)
    return app

def launch():
    """
    Launch the Flask app
    """
    return create_app()

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port='8000', host='0.0.0.0')
