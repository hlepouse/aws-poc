from botocore.vendored import requests
import boto3
import os

dataset = 'velib-disponibilite-en-temps-reel'
row = -1
url = 'https://opendata.paris.fr/api/records/1.0/search/?dataset=' + dataset + '&rows=' + str(row)
apiKey = 'eyJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiNWNjZThmNDE2MzRmNDEzMjk2NDQ3Y2NhIiwidGltZSI6MTU1NzA0MjI1Mi4wMjI0NX0.iZEqmWAT_z0S5-wTwXPtvtWT4IjYPOIjhUPKpsGV77E'

bucket_name = os.environ['BUCKET']
s3 = boto3.resource("s3")
bucket = s3.Bucket(bucket_name)

def lambda_handler(event, context):
    
    response = requests.get(url, headers={'X-API-KEY': 'apiKey' })
    
    s3_path = "velib-disponibilite-en-temps-reel_" + '-'.join(event['time'].split(':')) + ".json"

    bucket.put_object(Key=s3_path, Body=response.content)

    return True
