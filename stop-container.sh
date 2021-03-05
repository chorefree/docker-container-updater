docker stop $CONTAINER_NAME && docker container rm $CONTAINER_NAME || :
docker image prune -a -f
