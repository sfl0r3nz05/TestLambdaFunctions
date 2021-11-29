import os
import json
import boto3 #Amazon base library to use different services

"""
This lybrary constitutes the entrypoint to integrate Amazon Comprehend funtionalities
"""

def listRoles():
    """ Method created to output entities from a raw text as input"""

    client = boto3.Session(
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"), #Recover access key from env variables
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"), #Recover secret access key from env variables
        aws_session_token=os.environ.get("AWS_SESSION_TOKEN"), #Recover session token from env variables
        region_name=os.environ.get("REGION_NAME")).client('iam')

    response = client.list_roles()

    return response