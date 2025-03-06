import json
import boto3
import pandas as pd
import os

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('FileMetadata') 

def lambda_handler(event, context):
    try:
        # To Extract bucket name and file name from S3 event
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']
        
        # Downloading the file from S3
        local_file = f'/tmp/{file_key}'
        s3.download_file(bucket_name, file_key, local_file)

        # For Reading CSV file
        df = pd.read_csv(local_file)
        metadata = {
            'filename': file_key,
            'upload_timestamp': event['Records'][0]['eventTime'],
            'row_count': df.shape[0],
            'column_count': df.shape[1],
        }

        # Storing metadata in database
        table.put_item(Item=metadata)
         return {
            'statusCode': 200,
            'body': json.dumps('File processed successfully!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
