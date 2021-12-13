import io
import zipfile
from os.path import basename

def create_lambda_deployment_package(function_file_name, pathFile):
    """
    Creates a Lambda deployment package in ZIP format in an in-memory buffer. This
    buffer can be passed directly to AWS Lambda when creating the function.

    :param function_file_name: The name of the file that contains the Lambda handler
                               function.
    :return: The deployment package.
    """
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w') as zipped:
        zipped.write(pathFile , basename(pathFile))
    buffer.seek(0)
    return buffer.read()