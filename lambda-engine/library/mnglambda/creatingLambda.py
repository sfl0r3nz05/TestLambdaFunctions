import os
import json
import boto3 #Amazon base library to use different services

"""
This lybrary constitutes the entrypoint to integrate Amazon Comprehend funtionalities
"""

def createLambdaFunc(bucket_name, key, function_name):
    """ Method created to output entities from a raw text as input"""

    lambda_Client = boto3.client('lambda', 
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"), #Recover access key from env variables
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"), #Recover secret access key from env variables
        aws_session_token=os.environ.get("AWS_SESSION_TOKEN"), #Recover session token from env variables
        region_name=os.environ.get("REGION_NAME"))

    response = lambda_Client.create_function(
            Code={
                'S3Bucket': bucket_name,
                'S3Key': key, #how can i create or fetch this S3Key
            },
            Description='Process image objects from Amazon S3.',
            FunctionName= function_name,
            Handler='index.handler',
            Publish=True,
            Role='arn:aws:iam::582548238505:role/lambda',
            Runtime='python3.8',
        )

    return response