#!/bin/bash

# Install necessary dependencies
sudo yum install -y git
sudo yum install -y python3
sudo yum install -y docker

# Install Python dependencies
pip install -r requirements.txt

# Start Docker service
sudo service docker start

# Build Docker image
sudo docker build . --tag "kickoff_app" --file ./Dockerfile

echo "Build script executed successfully."