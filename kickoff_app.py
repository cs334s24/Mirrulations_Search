# create barebones flask app
# run with: python kickoff_app.py

from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html')
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)