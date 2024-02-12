#!/bin/bash

# start the docker container
docker build -t api .
docker run --name api -d -p 8000:8000 api
echo "API is running on port 8000"

# start the mongodb container
export MONGODB_VERSION=6.0-ubi8     # the version of mongodb to use
export MONGODB_PORT=27017           # the port to run mongodb on
docker run --name mongodb -d -p $MONGODB_PORT:$MONGODB_PORT mongodb/mongodb-community-server:$MONGODB_VERSION
echo "MongoDB is running on port " $MONGODB_PORT
