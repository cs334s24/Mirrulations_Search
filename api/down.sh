#!/bin/bash

# Stop and remove the running Docker container
docker stop api
docker rm api
echo "API container stopped and removed"

# Stop and remove the running MongoDB container
docker stop mongodb && docker rm mongodb
echo "MongoDB container stopped and removed"
