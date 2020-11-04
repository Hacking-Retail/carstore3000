#!/bin/bash
# Do some cleanup
docker rm -f $(docker ps -qa) 2>/dev/null
docker volume prune -f 2>/dev/null

# Start application
docker-compose up --force-recreate --build
