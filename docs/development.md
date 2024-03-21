## Developer Setup

As a developer, you need to configure a local python environment and a local
node environment.  The following sections discuss the steps.

This document also describes how to launch a local instance of the complete system using `docker-compose`.


## Python (API)

### Setup

* Go into `api` and create a virtual environment

  ```
  cd api
  python3 -m venv .venv
  ```

* Install the `mirrsearch` module (in `api/src`)  

  ```
  source .venv/bin/activate
  pip install -e .
  ```

  The `-e` switch makes the module editable (otherwise it save the current version
  of the source, and any changes will not be used).  The `.` parameter indicates
  that `setup.py` and `setup.cfg` are in the current directory.

  The `setup.cfg` file contains all the libraries for the package (Flask, gunicorn, pytest, etc.).


At this point, you should be able to run `pytest` in the `api` folder or `api/tests` folder.

### Launch API Locally

The `up.sh` script will

* Build the Docker container as `api`
* Launch an instance of the `api` container and bind port 8000 to the `localhost`

The `down.sh` script will

* Stop the `api` container
* Remove the `api` container

### Run Testing and Linting

In order to use any of these commands, you must be in the root of the project.

* Type `make` to run both
* Type `make lint` to only lint. Only `pylint` is used for this project
* Type `make test` to only test. `pytest` is used for this project. 
  * You can also run `pytest` to test the project
  * `pytest` uses a 95% coverage metric
  * Run `open htmlcov/index.html` in order to see the coverage report

## House-cleaning for Front-end

* Navigate to the frontend directory

```
cd frontend
```

* Make a `.env` file

```
nano .env
```

* Add the line `WDS_SOCKET_PORT=0` and save

## Setup HTTPS for Development

* Starting from the root directory make your way to the nginx folder

```
cd nginx
```

* create a folder named certs in the nginx folder

```
mkdir certs
```

* enter the certs folder

```
cd certs
```

* Run this on the command line to creat the necessary cert and priv key
* It is IMPERITAVE you are in the certs folder at this time

  After running this command you will be prompted with questions regarding
  the certificates. The first question will be like:
  Country Name 2 Letter Code AU: 
  You can answer this with 'US' and then you will be prompted with
  more questions which you can just skip by hitting return through them

```
openssl req -x509 -newkey rsa:4096 -nodes -out fullchain.pem -keyout privkey.pem -days 365
```

* Return to the root directory

```
cd ../..
```

* Create a .env file
* inside the .env file paste

```
CERT=./nginx/certs/fullchain.pem:/etc/nginx/certs/fullchain.pem
KEY=./nginx/certs/privkey.pem:/etc/nginx/certs/privkey.pem
```

Because we are using self signed certs for development when you go to 
`https://localhost` you will have to hit the advanced settings to continue
because your browser will pick up that it is not 3rd party authenticated.
Chrome is a little more strict about this so you may be better off using
safari or another browser. 

## Deploy the System in Development

To launch the entire system:

* Open docker
  
  First you will need to have the docker app open on your system
  
* Build the system:

  ```
  docker-compose build
  ```

  This will build each of the containers and report any errors.  If it is successful, you will be able to launch the system.

* Launch the system

  ```
  docker-compose up -d
  ```

  At this point you will have access to:

  * `https://localhost` - Interact through the NGINX server.  Requests will be routed to the Node (React) server or the Flask (API) server, as appropriate.
  * `http://localhost:8000` - direct access to the Flask (API) server.
  * `http://localhost:3000` - diredt access to the React server.

* Bring the system down

  ```
  docker-compose down
  ```


### Ingesting Data into mongoDB

Prerequisite: Have the system running in by following [Deploy the System in Development]

1. Navigate to the api folder and activate your virtual environment
```
cd api
source .venv/bin/activate
```

2. Navigate to MongoDB script directory
```
cd src/mirrsearch/db
```

3.  Ensure that you have unzipped our [sample-data](https://drive.google.com/drive/folders/1CsC3CKY0a52ZBI0_2558-No6Ke-UZw_s?usp=drive_link) to this directory, into a folder called `sample-data` that contains the names of various organizations such as "IHS" and "CRB" as parent folders.
  
  - To check if you have mongosh run 'brew list | grep mongosh'
  - If you do not have mongosh installed run 'brew install mongosh'

4. Run the `mongo_db.py` script to ingest the data:
```
python3 mongo_db.py
```
5. The data is now ingested within the `mirrsearch` database inside of `Mongo`. To access the data, follow these steps:

  - Launch the MongoDB shell:
```
mongosh
```

  - List available dbs and switch to the `mirrsearch` database:
```
show dbs
use mirrsearch
```

  - You can list all collections within the `mirrsearch`. You can then view the contents of a collection type:
```
show collections
db.collectionName.find()
```
