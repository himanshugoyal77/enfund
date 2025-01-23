import boto3
import json

def lambda_handler(event, context):
    try:
        bucket_name = event['bucket_name']
        file_key = event['file_key']
        file_body = event['file_body'] 

        s3 = boto3.client('s3')

        s3.put_object(
            Bucket=bucket_name,
            Key=file_key,
            Body=file_body
        )

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f'File uploaded successfully to s3://{bucket_name}/{file_key}'
            })
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }