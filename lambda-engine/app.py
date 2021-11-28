import os
from flask import Flask
from pathlib import Path
from dotenv import load_dotenv
from library.file.zipfile import computeZip
from library.bucket.creatingBucket import create_bucket
from library.mnglambda.creatingLambda import createLambdaFunc
app = Flask(__name__)
dotenv_path = Path('~/TestLambdaFunctions/network/lambda-engine/.env')
load_dotenv(dotenv_path=dotenv_path)
filePath = os.getenv("PATH_INPUT")

archive = computeZip(filePath)
bucket = 'bucket-lambda-1'
key = 'function.zip'
response = create_bucket(archive, bucket, key)

print(response)
print(a)
@app.route('/')
def server():
    return