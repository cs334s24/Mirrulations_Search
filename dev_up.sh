#!/bin/bash

docker build . --tag "kickoff_app" --file ./Dockerfile

docker run -d -p 8000:8000 kickoff_app

echo "Up script executed successfully."