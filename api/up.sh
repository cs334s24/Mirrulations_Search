#!/bin/bash

# start the docker container
docker build -t api .
docker run --name api -d -p 8000:8000 api
echo "API is running on port 8000"
