aws ecr get-login-password \
    --region eu-west-1 \
| docker login \
    --username AWS \
    --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.eu-west-1.amazonaws.com 
docker pull $AWS_ACCOUNT_ID.dkr.ecr.eu-west-1.amazonaws.com/cryptobot-$BRANCH_NAME
docker run -ditp $PORT:8000 \
    --name cryptobot_$BRANCH_NAME \
    --restart unless-stopped \
    $AWS_ACCOUNT_ID.dkr.ecr.eu-west-1.amazonaws.com/cryptobot-$BRANCH_NAME:latest
