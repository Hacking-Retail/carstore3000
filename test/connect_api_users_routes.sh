#!/bin/bash
readonly CONTAINER_NAME="carstore3000_api_1"
readonly IP="$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $CONTAINER_NAME)"
readonly PORT="5000"

curl -i http://$IP:$PORT/api/v1/users
curl -i -X POST http://$IP:$PORT/api/v1/users -d '{"username": "user1", "password": "password1"}'
curl -i -X POST http://$IP:$PORT/api/v1/users -d '{"username": "user1", "password": "password1"}'
curl -i -X DELETE http://$IP:$PORT/api/v1/users -d '{"username": "user1", "password": "password1"}'
