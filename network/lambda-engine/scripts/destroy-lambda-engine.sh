#!/bin/bash

echo "Stopping nlp engine container"

#docker rm -f $(docker ps -aq)
sudo rm -rf ~/TestLambdaFunctions/lambda-engine/input/function.zip            
docker-compose down