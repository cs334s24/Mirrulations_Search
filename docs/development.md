## Developer Setup

## Launch Locally
* Create a virtual environment
'''
python3 -m venv .venv
'''

* Activate virtual environment
'''
source .venv/bin/activate
'''

* Install requirements
'''
pip install -r requirements.txt
'''

* Build Docker Container
'''
docker build . --tag "kickoff_app" --file ./Dockerfile
'''

* Run Docker Container
'''
docker run -p "8000:8000" kickoff_app
'''

## Pytest

* run pytest
'''
pytest
'''

## Pylint
'''
pylint [ filename ]
'''
