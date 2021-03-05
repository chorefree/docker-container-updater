docker stop cryptobot_$BRANCH_NAME && docker container rm cryptobot_$BRANCH_NAME || :
docker image prune -a -f
