#!/bin/bash
readonly CONTAINER_NAME="carstore3000_api_1"
readonly IP="$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $CONTAINER_NAME)"
readonly PORT="5000"

curl -i http://$IP:$PORT/ >/dev/null 2>&1
echo -n "$(basename $0) "
[ $? -eq 0 ] && echo "Ok" || echo "Fail"
