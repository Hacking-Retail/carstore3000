#!/bin/bash
readonly CONTAINER_NAME="carstore3000_db_1"

docker exec -it "$CONTAINER_NAME" psql -U mpa carstore3000
