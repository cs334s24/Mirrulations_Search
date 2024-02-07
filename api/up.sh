#!/bin/bash

# start the docker container
sudo docker run -d -p 80:8000 kickoff_app

echo "App is running on port 80"
