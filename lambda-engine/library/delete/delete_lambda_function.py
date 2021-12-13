import boto3
import logging
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

def delete_lambda_function(lambda_client, function_name):
    """
    Deletes an AWS Lambda function.

    :param lambda_client: The Boto3 AWS Lambda client object.
    :param function_name: The name of the function to delete.
    """
    try:
        lambda_client.delete_function(FunctionName=function_name)
    except ClientError:
        logger.exception("Couldn't delete function %s.", function_name)
        raise