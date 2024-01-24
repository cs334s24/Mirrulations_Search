# create barebones flask app
# run with: python kickoff_app.py

from flask import Flask, render_template, jsonify

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')
    return app

def launch():
    return create_app()

def get_data():
    data = {"message": "hello world", "status": 200}
    return jsonify(data)

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port='8000', host='0.0.0.0')