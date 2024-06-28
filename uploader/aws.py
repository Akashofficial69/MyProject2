import os
import boto3
from botocore.exceptions import NoCredentialsError


def upload_to_s3(file_name, bucket, object_name=None):
    s3_client = boto3.client('s3')
    if object_name is None:
        object_name = os.path.basename(file_name)

    try:
        s3_client.upload_file(file_name, bucket, object_name)
        print(f"Upload Successful: {file_name} to bucket: {bucket}")
    except FileNotFoundError:
        print(f"The file was not found: {file_name}")
    except NoCredentialsError:
        print("Credentials not available")
