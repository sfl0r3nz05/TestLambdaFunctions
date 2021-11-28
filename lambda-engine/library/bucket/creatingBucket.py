import os
import json
import boto3 #Amazon base library to use different services
import logging
from botocore.exceptions import ClientError

"""
This lybrary constitutes the entrypoint to integrate Amazon Comprehend funtionalities
"""

#def creatingBucket(archive, bucket, key):
#    """ Method created to output entities from a raw text as input"""
#    lambda_func = boto3.Session(
#        aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"), #Recover access key from env variables
#        aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"), #Recover secret access key from env variables
#        aws_session_token=os.environ.get("AWS_SESSION_TOKEN"), #Recover session token from env variables
#        region_name=os.environ.get("REGION_NAME")).client('s3')  #Recover region name from env variables
#    response = lambda_func.put_object(Body=archive, Bucket=bucket, Key=key) #client.put_object(Body=archive, Bucket='bucket-name', Key='function.zip')
#    return response


def create_bucket(bucket_name):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1).

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """
        # Create bucket
    try:
        lambda_func = boto3.Session(
            aws_access_key_id=os.environ.get("AWS_ACCESS_KEY_ID"), #Recover access key from env variables
            aws_secret_access_key=os.environ.get("AWS_SECRET_ACCESS_KEY"), #Recover secret access key from env variables
            aws_session_token=os.environ.get("AWS_SESSION_TOKEN"), #Recover session token from env variables
            region_name=os.environ.get("REGION_NAME")).client('s3')  #Recover region name from env variables
        location = {'LocationConstraint': os.environ.get("REGION_NAME")}
        lambda_func.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
    
    except ClientError as e:
        logging.error(e)
        return False
    return True