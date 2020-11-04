#!/bin/bash
readonly CONTAINER_NAME="carstore3000_db_1"
readonly IP="docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $CONTAINER_NAME"

docker exec -it "$CONTAINER_NAME" psql -U mpa carstore3000
