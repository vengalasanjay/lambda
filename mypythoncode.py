import json

def lambda_handler(event, context):
    print('This code is pushed from GitHub')
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
