#!/bin/bash

# Stop and remove the running Docker container
docker stop api
docker rm api
echo "API container stopped and removed"
