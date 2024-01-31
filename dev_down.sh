#!/bin/bash

# Build the Docker image
docker build . --tag "kickoff_app" --file ./Dockerfile

# Stop and remove all existing Docker containers
docker stop $(docker ps -a -q)



echo "Script executed successfully."
