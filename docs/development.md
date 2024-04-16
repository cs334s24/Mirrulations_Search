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

## Installing Node Dependencies for Front-End

To run our `front-end` container within docker, you will need to install Node onto your laptop as a pre-requisite:

  ```
  brew install node
  ```

Navigate to the `frontend` folder and run the command:
```
cd frontend
npm install
```

This will generate a folder called `node_modules`, as well as a `package-lock.json` that are necessary for the build process of the front-end container.


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

##### Prerequisite: 
  - Have the system running in by following [Deploy the System in Development]
  - Make sure you have mongosh installed, but your localhost:27017 Mongo instance is not running
    - To check if you have mongosh run `brew list | grep mongosh`
    - If you do not have mongosh installed run `brew install mongosh`
    - Brew installing Mongo will automatcially start a local instance, which we do not want. To stop this, type `mongosh`
    - Inside of the prompt that opens up, type in:
    ```
    db.adminCommand({shutdown:1})
    ```
    - This will ensure your laptop's mongo instance is not running. You can now exit out of the mongosh prompt back to the Mirrulations_Search folder prompt

1. Activate your virtual environment that is currently inside of the `api` folder
```
source ./api/.venv/bin/activate
```
2.  Ensure that you have unzipped our [sample-data](https://drive.google.com/drive/folders/1CsC3CKY0a52ZBI0_2558-No6Ke-UZw_s?usp=drive_link) to your local machine into a singular folder. 
  
3. Make sure you have our dockerized system up and running within a different terminal window. (assuming you have followed the `Deploy the System in Development` steps)
  - This will use the mongo container inside of docker as the mongo instance for ingestion (rather than your local instance, which should not be running)
```
docker-compose up -d
```

4. Run the `mongo_db.py` script to ingest the data:
  - The folder can live anywhere, but you need to pass a path to it as an argument (absolute or relative)
```
python3 ./api/src/mirrsearch/db/mongo_db.py (folder)
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


### Code Formatting with Prettier
This project uses Prettier to ensure consistent code formatting. The Prettier configuration is defined in the `.prettierrc.json` file at the root of the frontend directory. For more details visit the https://prettier.io/ 

## Prettier Configuration
Our Prettier configuration is as follows:
```json
{
  "bracketSpacing": false,
  "singleQuote": false,
  "trailingComma": "all",
  "semi": true,
  "tabWidth": 1,
  "arrowParens": "always",
  "printWidth": 100,
  "jsxBracketSameLine": true
}
```

## Ignored Files
Files or directories that are not formatted by Prettier are listed in the .prettierignore file.
Currently, the node_modules directory and README.md file are ignored.

## Running Prettier
To format your code with Prettier, run the following command from the frontend directory:
npx prettier --write .

## Fixing Linting Errors
If you encounter linting errors, you can automatically fix many of them by running the following command:
npx eslint --fix .

If the linting errors are not automatically fixed, you will need to manually edit the code.