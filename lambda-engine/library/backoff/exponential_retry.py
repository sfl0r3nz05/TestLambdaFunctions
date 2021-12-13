import time
import boto3
import logging
from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)

def exponential_retry(func, error_code, *func_args, **func_kwargs):
    """
    Retries the specified function with a simple exponential backoff algorithm.
    This is necessary when AWS is not yet ready to perform an action because all
    resources have not been fully deployed.

    :param func: The function to retry.
    :param error_code: The error code to retry. Other errors are raised again.
    :param func_args: The positional arguments to pass to the function.
    :param func_kwargs: The keyword arguments to pass to the function.
    :return: The return value of the retried function.
    """
    sleepy_time = 1
    func_return = None
    while sleepy_time < 33 and func_return is None:
        try:
            func_return = func(*func_args, **func_kwargs)
            logger.info("Ran %s, got %s.", func.__name__, func_return)
        except ClientError as error:
            if error.response['Error']['Code'] == error_code:
                print(f"Sleeping for {sleepy_time} to give AWS time to "
                      f"connect resources.")
                time.sleep(sleepy_time)
                sleepy_time = sleepy_time*2
            else:
                raise
    return func_return