# TEST LAMBDA FUNCTIONS

## Requirements

1. Install [docker for ubuntu](https://docs.docker.com/engine/install/ubuntu/)
2. [Manage Docker as non-root user](https://docs.docker.com/engine/install/linux-postinstall/)
3. Install [docker-compose for ubuntu](https://docs.docker.com/compose/install/)
4. Install make `sudo apt install make`

## Sources

1. [AWS Lambda Documentation](https://docs.aws.amazon.com/code-samples/latest/catalog/python-lambda-boto_client_examples-lambda_basics.py.html)
2. [AWS developer guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
3. [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
4. [Stackoverflow issue](https://stackoverflow.com/questions/63040090/create-aws-lambda-function-using-boto3-python-code)

## Getting Started

### Environment variables

1. Go into `cd ~/TestLambdaFunctions/network/lambda-engine`.
2. Rename the `.env.example` to `.env`.
3. Complete `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN` and `REGION_NAME` from AWS Account.

### Create lambda functions

1. Go into `cd ~/TestLambdaFunctions/lambda-engine/input`.
2. Modify `lambda_handler_basic.py` with your own lambda function code.

### Build docker images

1. Go into `cd ~/TestLambdaFunctions/lambda-engine`.
2. Build lambda-engine `docker build -t lambda-engine .`

## How to use

1. `cd ~/TestLambdaFunctions/network/lambda-engine`
2. `make start`
3. `make stop`
4. `make destroy`