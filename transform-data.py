import boto3
import os
import json

s3 = boto3.resource("s3")

bucket_source_name = os.environ['BUCKET_SOURCE']
bucket_dest_name = os.environ['BUCKET_DEST']
bucket_dest = s3.Bucket(bucket_dest_name)

def lambda_handler(event, context):
    
    for record in event['Records']:
                
        key = record['s3']['object']['key']

        obj = s3.Object(bucket_source_name, key)
        
        content = obj.get()['Body'].read()
        jsonObject = json.loads(content)
        
        bucket_dest.put_object(Key = os.path.splitext(key)[0] + ".txt", Body=str(jsonObject["nhits"]))

    return True
