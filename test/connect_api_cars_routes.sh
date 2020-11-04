#!/bin/bash
readonly CONTAINER_NAME="carstore3000_api_1"
readonly IP="$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $CONTAINER_NAME)"
readonly PORT="5000"

curl -i http://$IP:$PORT/api/v1/cars?marker=citroen

curl -i http://$IP:$PORT/api/v1/cars
curl -i -X POST http://$IP:$PORT/api/v1/cars -d '{}'
curl -i -X DELETE http://$IP:$PORT/api/v1/cars
curl -i -X PUT http://$IP:$PORT/api/v1/cars
