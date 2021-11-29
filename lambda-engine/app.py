import os
from flask import Flask
from pathlib import Path
from dotenv import load_dotenv
from library.file.zipfile import computeZip
from library.roles.getRoles import listRoles
from library.bucket.creatingBucket import create_bucket
from library.mnglambda.creatingLambda import createLambdaFunc
app = Flask(__name__)
dotenv_path = Path('~/TestLambdaFunctions/network/lambda-engine/.env')
load_dotenv(dotenv_path=dotenv_path)
filePath = os.getenv("PATH_INPUT")

archive = computeZip(filePath)

bucket = 'bucket-lambda-1'
key = 'function.zip'
bucket_name = create_bucket(archive, bucket, key)

response1 = listRoles()
print(response1)

function_name = 'lambdahandler'
response2 = createLambdaFunc(bucket_name, key, function_name)
print(response2)

print(a)
@app.route('/')
def server():
    return