from boto3 import *

def read_s3_object(s3Client, bucket, key):
    s3_obj = s3Client.get_object(Bucket=bucket, Key=key)

    return s3_obj['Body'].read().decode('utf-8')
