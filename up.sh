#!/bin/bash

# start the docker container
sudo docker run -d -p 80:8000 kickoff_app

echo "App is running on port 80"


# start a mongodb container
# the version of mongodb to use
export MONGODB_VERSION=6.0-ubi8
export MONGODB_PORT=27017
# start the mongodb container with the specified version
sudo docker run --name mongodb -d -p $MONGODB_PORT:$MONGODB_PORT mongodb/mongodb-community-server:$MONGODB_VERSION

echo "MongoDB is running on port " $MONGODB_PORT