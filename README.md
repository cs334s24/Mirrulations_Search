## Mirrulations_Search 

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
  * `pytest`
  * linting
* CD runs on PR merge
  * deploy script runs on AWS instance
* `requirements.txt` contains the python libraries needed
* database access is encapsulated (pushed to the periphery)
* `src` and `tests` folders, module for app

Application:

We are going to make a basic system to query a document database
and give back results

![system](https://i.ibb.co/ccmj6YK/52c0e1d0a08f.png)  

* Web interface: search bar that queries server and displays results
* Document DB as the backend
* Flask server
* Gunicorn
* NGINX
* Dockerized

![detailed system](https://i.ibb.co/X5svbqF/28e27cd1280e.png)

## Makefile:
Use the command `make` to run the Makefile. The Makefile will call pytest and pylint
to test and lint the system.  

## Docker Commands:
To run the dockerized version of the system utilizing Node.js:

* Run `docker-compose build`
* Run `docker-compose up`