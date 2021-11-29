import os
import json
import boto3 #Amazon base library to use different services
import logging
from zipfile import ZipFile
from botocore.exceptions import ClientError


def create_bucket(archive, bucket_name, key): 
    client = boto3.Session(
        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"), #Recover access key from env variables
        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"), #Recover secret access key from env variables
        aws_session_token=os.environ.get("AWS_SESSION_TOKEN"), #Recover session token from env variables
        region_name=os.environ.get("REGION_NAME")).client('s3')
    client.create_bucket(Bucket=bucket_name)

    os.chdir('./input')
    #opened_zipfile = ZipFile.open(name='function.zip')
    #print(opened_zipfile)
    with ZipFile('function.zip') as myzip:
        client.put_object(Body=myzip, Bucket=bucket_name, Key=key)
    return bucket_name
