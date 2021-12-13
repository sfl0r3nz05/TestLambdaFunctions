import os
import json
import boto3
import random
import logging
from flask import Flask
from pathlib import Path
from dotenv import load_dotenv

from library.backoff.exponential_retry import exponential_retry
from library.invoke.invoke_lambda_function import invoke_lambda_function
from library.delete.delete_lambda_function import delete_lambda_function
from library.deploy.deploy_lambda_function import deploy_lambda_function
from library.roles.create_iam_role_for_lambda import create_iam_role_for_lambda
from library.file.create_lambda_deployment_package import create_lambda_deployment_package

dotenv_path = Path('~/TestLambdaFunctions/network/lambda-engine/.env')
load_dotenv(dotenv_path=dotenv_path)
filePath = os.getenv("PATH_INPUT")

def usage_demo():

    logger = logging.getLogger(__name__)

    """
    Shows how to create, invoke, and delete an AWS Lambda function.
    """
    logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
    print('-'*88)
    print("Welcome to the AWS Lambda basics demo.")
    print('-'*88)

    lambda_function_filename = 'lambda_handler_basic.py'
    lambda_handler_name = 'lambda_handler_basic.lambda_handler'
    lambda_role_name = 'demo-lambda-role'
    lambda_function_name = 'demo-lambda-function'

    base = boto3.Session(
            aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"), #Recover access key from env variables
            aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"), #Recover secret access key from env variables
            aws_session_token=os.environ.get("AWS_SESSION_TOKEN"), #Recover session token from env variables
            region_name=os.environ.get("REGION_NAME"))
    iam_resource = base.resource('iam')
    lambda_client = base.client('lambda')

    ### TO CREATE LAMBDA FUNCTION ###

    print(f"Creating AWS Lambda function {lambda_function_name} from the "
          f"{lambda_handler_name} function in {lambda_function_filename}...")
    deployment_package = create_lambda_deployment_package(lambda_function_filename, filePath)
    iam_role = create_iam_role_for_lambda(iam_resource, lambda_role_name)
    
    exponential_retry(
        deploy_lambda_function, 'InvalidParameterValueException',
        lambda_client, lambda_function_name, lambda_handler_name, iam_role,
        deployment_package)

    ### TO USE LAMBDA FUNCTION ###

    print(f"Directly invoking function {lambda_function_name} a few times...")
    actions = ['square', 'square root', 'increment', 'decrement']
    for _ in range(5):
        lambda_parms = {
            'number': random.randint(1, 100), 'action': random.choice(actions)
        }
        response = invoke_lambda_function(
            lambda_client, lambda_function_name, lambda_parms)
        print(f"The {lambda_parms['action']} of {lambda_parms['number']} resulted in "
              f"{json.load(response['Payload'])}")

    ### TO USE DELETE LAMBDA FUNCTION ###

    delete_lambda_function(lambda_client, lambda_function_name)
    print(f"Deleted function {lambda_function_name}.")

if __name__ == '__main__':
    usage_demo()