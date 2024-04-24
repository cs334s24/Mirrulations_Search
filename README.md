## Mirrulations Search

### Contributors: 

* [Thomas Abato](https://www.linkedin.com/in/thomasabato/)
* [Kyle Adams](https://www.linkedin.com/in/kyleadams12/)
* [Marie Addo](https://www.linkedin.com/in/marie-stella-0779a417b/)
* [Jake Clause](https://www.linkedin.com/in/jake-clause-56396a252/)
* [Ben Coleman](https://www.linkedin.com/in/moraviancoleman/)
* [Colin Conway](https://www.linkedin.com/in/colin-conway-ba2b4620a/)
* [Dylan Fodor](https://www.linkedin.com/in/dylan-fodor/)
* [Nate Garay](https://www.linkedin.com/in/nathan-garay-642709252/)
* [Jeremy Goll](https://www.linkedin.com/in/jeremy-goll-85b699253/)
* [Maxwell Houck](www.linkedin.com/in/maxwell-houck-90750a239/)
* [Anna Huang](https://www.linkedin.com/in/anna-huang-73b9b4252/)
* [Vito Leone](https://www.linkedin.com/in/vito-leone/)
* [Devin McCormack](https://www.linkedin.com/in/devin-mccormack-6a8214226/)
* [David Olsakowski](https://www.linkedin.com/in/david-olsakowski-096144257/)
* [Carlton Reyes](https://www.linkedin.com/in/carlton-reyes-9b22b01aa/)
* [Shawn Ryer](https://www.linkedin.com/in/shawn-ryer-914354227/)
* [Jacob Smith](https://www.linkedin.com/in/jacob-smith-a12842205/)
* [Luke Suppa](https://www.linkedin.com/in/luke-suppa-593b0b254/) 


## Project Description:

Characteristics of the Repo:

* Hosted in our Github organization
   * All students have a fork
* Setup process is documented in `README.md`
* CI runs on PR creation/update
  * `pytest` and `jest`
  * linting (both Python and JavaScript)
* CD runs on PR merge
  * deploy script runs on AWS instance
* `setup.cfg` contains the python libraries needed
* database access is encapsulated (pushed to the periphery)
* `src` and `tests` folders, module for app

Application:

We have established a system in which a front-end React-based search utility utilizes a Flask API and gives back results from a Mongo database.

![system](https://i.ibb.co/grvd3Y2/architecture.png)

* Mongo DB as the backend
* Flask server
* Gunicorn
* NGINX
* Dockerized via Docker-Compose
* React frontend for querying API results
* AWS Lambda
* AWS Secrets Manager
* AWS S3
* Amazon Opensearch

## Makefile:
Use the command `make` to run the Makefile. The Makefile will call pytest, pylint, jest, and eslint
to test and lint the system.  

## Launching the System Locally:
Launching the system involves a number of steps to be followed before the utility is usable.

To do this, visit `docs/development.md` for a detailed walkthrough.